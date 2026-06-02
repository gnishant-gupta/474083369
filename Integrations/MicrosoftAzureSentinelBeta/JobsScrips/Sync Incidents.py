from __future__ import annotations

import re
from typing import TYPE_CHECKING

from SiemplifyUtils import (
    convert_datetime_to_unix_time,
    utc_now,
)
from TIPCommon.base.job import Job
from TIPCommon.base.action.data_models import (
    CloseCaseOrAlertInconclusiveRootCauses,
    CloseCaseOrAlertMaliciousRootCauses,
    CloseCaseOrAlertNotMaliciousRootCauses,
)
from TIPCommon.smp_io import read_content, write_content
from TIPCommon.smp_time import validate_timestamp

import constants
from exceptions import MicrosoftAzureSentinelManagerError
from MicrosoftAzureSentinelManager import MicrosoftAzureSentinelManager
import utils

if TYPE_CHECKING:
    from typing import NoReturn

    from TIPCommon.types import SingleJson


def strip_html_tags(text: str) -> str:
    """Removes HTML tags from a string."""
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)

class SyncIncidents(Job):
    def __init__(self) -> None:
        super().__init__(constants.SYNC_INCIDENTS_JOB_NAME)
        self.manager: MicrosoftAzureSentinelManager | None = None
        self.last_successful_execution_time = None
        self.updated_processed_incidents: dict[str, list[str]] = {}

    def _init_api_clients(self) -> None:
        pass

    def _initialize_manager(self) -> None:
        """Initializes manager based on job parameters."""
        azure_active_directory_id: str = self.params.azure_active_directory_id
        oauth2_login_endpoint_url: str = self.params.oauth2_login_endpoint_url
        api_root: str = self.params.api_root
        client_id: str = self.params.client_id
        client_secret: str = self.params.client_secret
        verify_ssl: bool = self.params.verify_ssl

        self.manager = MicrosoftAzureSentinelManager(
            api_root=api_root,
            login_url=oauth2_login_endpoint_url,
            tenant_id=azure_active_directory_id,
            client_id=client_id,
            client_secret=client_secret,
            verify_ssl=verify_ssl,
            siemplify=self.soar_job,
        )

    def _perform_job(self) -> None:
        """
        Executes the main synchronization logic.
        """
        self._initialize_manager()
        last_run_timestamp = self.soar_job.fetch_timestamp(datetime_format=True)
        max_hours_backwards: int = self.params.max_hours_backwards

        self.last_successful_execution_time = validate_timestamp(
            last_run_timestamp, max_hours_backwards
        )
        self.logger.info(
            f"Last successful execution time: {self.last_successful_execution_time}"
        )

        self.updated_processed_incidents = self._read_incident_ids().copy()

        self._sync_to_sentinel()
        self._sync_from_sentinel()
        self._write_incident_ids(self.updated_processed_incidents)
        self.soar_job.save_timestamp(new_timestamp=utc_now())

    def _get_cases(self) -> list[str]:
        """Fetches new and modified cases from Google SecOps."""
        environment_name = self.params.environment_name

        start_time_ms = convert_datetime_to_unix_time(
            self.last_successful_execution_time
        )
        created_case_ids = self.soar_job.get_cases_ids_by_filter(
            tags=[constants.SECOPS_CASE_TAG],
            status=constants.CASE_STATUS_BOTH,
            start_time_from_unix_time_in_ms=start_time_ms,
            environments=[str(environment_name)],
        )
        modified_case_ids = self.soar_job.get_cases_ids_by_filter(
            tags=[constants.SECOPS_CASE_TAG],
            status=constants.CASE_STATUS_BOTH,
            update_time_from_unix_time_in_ms=start_time_ms,
            environments=[str(environment_name)],
        )

        all_relevant_case_ids = list(set(created_case_ids + modified_case_ids))
        self.logger.info(f"Found new/modified case IDs: {all_relevant_case_ids}")
        return all_relevant_case_ids

    def _sync_to_sentinel(self) -> None:
        """Synchronizes changes from Google SecOps to Microsoft Sentinel."""
        self.logger.info(
            "--- Starting synchronization from Google SecOps to Microsoft Sentinel ---"
        )
        case_ids = self._get_cases()

        for case_id in case_ids:
            self._process_secops_case(case_id)

    def _process_secops_case(self, case_id: str) -> None:
        """
        Synchronization of a single Google SecOps case to Microsoft Sentinel.
        """
        try:
            case = self.soar_job._get_case_by_id(case_id)
            incident_ids = self._extract_incident_ids_from_secops_case(case)
            if not incident_ids:
                self.logger.info(
                    f"No Sentinel incident IDs found for Google SecOps case {case_id}."
                    " Skipping."
                )
                return

            self.updated_processed_incidents[str(case_id)] = incident_ids
            for incident_id in incident_ids:
                self._sync_case_status_to_sentinel(case, case_id, incident_id)
                self._sync_case_comments_to_sentinel(case_id, incident_id)
                self._sync_case_tags_to_sentinel(case, case_id, incident_id)
        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to process Google SecOps case {case_id}. Error: {e}"
            )

    def _sync_case_status_to_sentinel(
        self,
        case: SingleJson,
        case_id: str,
        incident_id: str,
    ) -> None:
        """
        Syncs the status from a Google SecOps case to a Microsoft Sentinel incident.
        """
        if case.get("status") != constants.CLOSED_STATUS_CODE:
            return

        try:
            case_closure_reason = self.soar_job.get_case_closure_details(
                [str(case_id)]
            )[0].get("reason", "")
            classification, determination = self._set_sentinel_closure_details(
                case_closure_reason
            )

            self.manager.update_incident_status(
                incident_id=incident_id,
                status=constants.RESOLVED_STATUS,
                classification=classification,
                determination=determination,
            )
            self.logger.info(
                f"Successfully closed Microsoft Sentinel incident {incident_id} "
                f"for Google SecOps case {case_id}."
            )
            self._remove_synced_entries(
                self.updated_processed_incidents, [(str(case_id), incident_id)]
            )
        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to update Microsoft Sentinel incident {incident_id}. "
                f"Error: {e}"
            )

    def _set_sentinel_closure_details(
        self,
        case_closure_reason: str,
    ) -> tuple[str, str]:
        """
        Maps Google SecOps closure reason to Sentinel classification and determination.
        """
        mapping: dict[str, tuple[str, str]] = {
            "Malicious": ("truePositive", "maliciousUserActivity"),
            "NotMalicious": ("falsePositive", "other"),
        }

        return mapping.get(case_closure_reason, ("unknown", "unknown"))

    def _sync_case_comments_to_sentinel(self, case_id: str, incident_id: str) -> None:
        """
        Syncs comments from a Google SecOps case to a Microsoft Sentinel incident.
        """
        try:
            secops_comments = self.soar_job.fetch_case_comments(
                case_id=case_id,
                from_timestamp=convert_datetime_to_unix_time(
                    self.last_successful_execution_time
                ),
            )

            if not secops_comments:
                return

            def is_valid_comment(comment: SingleJson) -> bool:
                content = comment.get("comment", "").strip()
                return bool(content) and not content.startswith(
                    constants.SENTINEL_COMMENT_PREFIX
                )

            valid_comments = [
                f"{constants.SECOPS_COMMENT_PREFIX}{c['comment']}"
                for c in secops_comments
                if is_valid_comment(c)
            ]

            for comment in valid_comments:
                self.manager.add_comment_to_graph_incident(incident_id, comment)

            if valid_comments:
                self.logger.info(
                    "Successfully synced comments from SecOps to Sentinel incident "
                    f"{incident_id}."
                )

        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to sync comments from Google SecOps for case {case_id}. "
                f"Error: {e}"
            )

    def _get_new_tags(
        self,
        source_tags: list[str],
        existing_tags: list[str],
        prefix_to_add: str,
        prefix_to_exclude: str,
        tag_to_exclude: str | None = None,
        min_len: int = 0,
        max_len: int = float("inf"),
    ) -> list[str]:
        """
        Identifies tags from source_tags that should be added
        to the destination system.
        """
        new_tags = []
        for tag in source_tags:
            stripped_tag = tag.strip()
            if not stripped_tag:
                continue
            if tag_to_exclude and stripped_tag == tag_to_exclude:
                continue
            if stripped_tag.startswith(prefix_to_exclude):
                continue
            if not min_len <= len(stripped_tag) <= max_len:
                continue

            prefixed_tag = f"{prefix_to_add}{stripped_tag}"
            if prefixed_tag not in existing_tags:
                new_tags.append(prefixed_tag)
        return new_tags

    def _sync_case_tags_to_sentinel(
        self,
        case: SingleJson,
        case_id: str,
        incident_id: str,
    ) -> None:
        """Syncs tags from a Google SecOps case to a Microsoft Sentinel incident."""
        try:
            secops_tags_string = case.get("additional_properties", {}).get("Tags", "")
            secops_tags = self.manager.convert_comma_separated_to_list(
                secops_tags_string
            )

            ms_tags = self.manager.get_incident_tags(incident_id)

            new_tags = self._get_new_tags(
                source_tags=secops_tags,
                existing_tags=ms_tags,
                prefix_to_add=constants.SECOPS_TAG_PREFIX,
                prefix_to_exclude=constants.SENTINEL_TAG_PREFIX,
                tag_to_exclude=constants.SECOPS_CASE_TAG,
            )

            if new_tags:
                combined_tags = list(set(ms_tags + new_tags))
                self.manager.add_tags_to_incident(incident_id, combined_tags)
                self.logger.info(
                    f"Successfully synced tags from Google SecOps for case {case_id}."
                )

        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to sync tags from Google SecOps for case {case_id}. Error: {e}"
            )

    def _sync_from_sentinel(self) -> None:
        """Synchronizes changes from Microsoft Sentinel to Google SecOps."""
        self.logger.info(
            "--- Starting synchronization from Microsoft Sentinel to Google SecOps ---"
        )
        all_incident_ids = [
            incident_id
            for ids in self.updated_processed_incidents.values()
            for incident_id in ids
        ]

        if not all_incident_ids:
            self.logger.info("No Microsoft Sentinel incidents to check for updates.")
            return

        try:
            incidents = self.manager.get_incidents_by_ids(all_incident_ids)
            for incident in incidents:
                self._process_sentinel_incident(incident)
        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to fetch incidents from Microsoft Sentinel. Error: {e}"
            )

    def _process_sentinel_incident(self, incident: SingleJson) -> None:
        """
        Synchronization of Microsoft Sentinel incident to Google SecOps.
        """
        incident_id = incident.get("id")
        case_id = self._find_case_id_by_incident_id(
            incident_id, self.updated_processed_incidents
        )

        if not case_id:
            return

        try:
            case = self.soar_job._get_case_by_id(case_id)
            closed = self._sync_incident_status_to_secops(incident, case, case_id)
            if closed:
                self._remove_synced_entries(
                    self.updated_processed_incidents, [(case_id, incident_id)]
                )
            self._sync_incident_comments_to_secops(incident_id, case, case_id)
            self._sync_incident_tags_to_secops(incident_id, case, case_id)

        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                f"Failed to sync from Microsoft Sentinel for incident {incident_id} "
                f"to case {case_id}. Error: {e}"
            )

    def _sync_incident_status_to_secops(
        self,
        incident: SingleJson,
        case: SingleJson,
        case_id: str,
    ) -> bool:
        """
        Syncs the status from a Sentinel incident to a Google SecOps case or alert.
        """
        incident_status = incident.get("status")

        if (
            incident_status == constants.RESOLVED_STATUS
            and case.get("status") == constants.OPEN_STATUS_CODE
        ):
            reason, root_cause = self._set_secops_closure_details(incident)

            alerts_in_case = list(case.get("cyber_alerts", []))
            alert_identifier = self._find_alert_identifier(case, incident.get("id"))

            try:
                if len(alerts_in_case) <= 1:
                    self._close_case(case_id, reason, root_cause, alert_identifier)
                else:
                    self._close_alert(case_id, alert_identifier, reason, root_cause)

                return True
            except MicrosoftAzureSentinelManagerError as e:
                self.logger.error(
                    f"Failed to check case details for {case_id}. Error: {e}"
                )
        return False

    def _set_secops_closure_details(self, incident: SingleJson) -> tuple[str, str]:
        """
        Maps Sentinel classification to Google SecOps closure reason and root cause.
        """
        mapping: dict[str, tuple[str, str]] = {
            "truePositive": (
                "Malicious",
                CloseCaseOrAlertMaliciousRootCauses.OTHER.value,
            ),
            "falsePositive": (
                "NotMalicious",
                CloseCaseOrAlertNotMaliciousRootCauses.OTHER.value,
            ),
        }

        return mapping.get(
            incident.get("classification"),
            (
                "Inconclusive",
                CloseCaseOrAlertInconclusiveRootCauses.NO_CLEAR_CONCLUSION.value,
            ),
        )

    def _sync_incident_comments_to_secops(
        self,
        incident_id: str,
        case: SingleJson,
        case_id: str,
    ) -> None:
        """
        Syncs comments from a Microsoft Sentinel incident to Google SecOps.
        """
        try:
            ms_comments = self.manager.get_incident_comments(
                incident_id,
                start_time=self.last_successful_execution_time,
            )
            alert_identifier = self._find_alert_identifier(case, incident_id)

            if not alert_identifier:
                self.logger.info(
                    f"No alert identifier found for incident {incident_id}. "
                    "Skipping comment sync."
                )
                return

            if not ms_comments:
                return

            valid_comments = [
                f"{constants.SENTINEL_COMMENT_PREFIX}{strip_html_tags(c)}"
                for c in ms_comments
                if self._is_valid_ms_comment(c)
            ]

            for comment in valid_comments:
                self.soar_job.add_comment(
                    case_id=case_id,
                    comment=comment,
                    alert_identifier=alert_identifier,
                )

            if valid_comments:
                self.logger.info(
                    f"Successfully synced comments from Sentinel to SecOps case "
                    f"{case_id}."
                )

        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                "Failed to sync comments from Microsoft Sentinel for incident "
                f"{incident_id}. Error: {e}"
            )

    def _is_valid_ms_comment(self, comment: str) -> bool:
        """
        Checks if a Microsoft Sentinel comment should be synced to SecOps.
        """
        clean_comment = strip_html_tags(comment)
        return not clean_comment.startswith(constants.SECOPS_COMMENT_PREFIX)

    def _sync_incident_tags_to_secops(
        self,
        incident_id: str,
        case: SingleJson,
        case_id: str,
    ) -> None:
        """Syncs tags from a Microsoft Sentinel incident to Google SecOps."""
        try:
            alert_identifier = self._find_alert_identifier(case, incident_id)
            if not alert_identifier:
                self.logger.info(
                    f"No alert identifier found for incident {incident_id}. "
                    "Skipping tag sync."
                )
                return

            ms_tags = self.manager.get_incident_tags(incident_id)
            secops_tags_string = case.get("additional_properties", {}).get("Tags", "")
            secops_tags = self.manager.convert_comma_separated_to_list(
                secops_tags_string
            )

            new_tags = self._get_new_tags(
                source_tags=ms_tags,
                existing_tags=secops_tags,
                prefix_to_add=constants.SENTINEL_TAG_PREFIX,
                prefix_to_exclude=constants.SECOPS_TAG_PREFIX,
                min_len=constants.MIN_TAG_LEN,
                max_len=constants.MAX_TAG_LEN,
            )

            if new_tags:
                for tag in new_tags:
                    self.soar_job.add_tag(
                        case_id=case_id, tag=tag, alert_identifier=alert_identifier
                    )
                self.logger.info(
                    f"Successfully synced tags from Sentinel to secops case {case_id}."
                )

        except MicrosoftAzureSentinelManagerError as e:
            self.logger.error(
                "Failed to sync tags from Microsoft Sentinel for incident "
                f"{incident_id}. Error: {e}"
            )

    def _read_incident_ids(self) -> dict[str, list[str]]:
        """Reads processed incident IDs from a file or database."""
        return read_content(
            siemplify=self.soar_job,
            file_name=constants.IDS_FILE_NAME,
            db_key=constants.IDS_DB_KEY,
            default_value_to_return={},
            identifier=constants.SYNC_INCIDENTS_IDENTIFIER,
        )

    def _write_incident_ids(self, updated_incidents: dict[str, list[str]]) -> None:
        """Writes processed incident IDs to a file or database."""
        write_content(
            siemplify=self.soar_job,
            content_to_write=updated_incidents,
            file_name=constants.IDS_FILE_NAME,
            db_key=constants.IDS_DB_KEY,
            identifier=constants.SYNC_INCIDENTS_IDENTIFIER,
        )

    def _extract_incident_ids_from_secops_case(self, case: SingleJson) -> list[str]:
        """Extracts Sentinel incident IDs from a Google SecOps case."""
        incident_ids = []
        for alert in case.get("cyber_alerts", []):
            ticket_id = utils.get_incident_id_from_alert(self.soar_job, alert)
            if ticket_id:
                incident_ids.append(ticket_id)
        return incident_ids

    def _find_case_id_by_incident_id(
        self,
        incident_id: str,
        id_map: dict[str, list[str]],
    ) -> str | None:
        """Finds the corresponding case ID for a given incident ID."""
        for case_id, incident_ids in id_map.items():
            if incident_id in incident_ids:
                return case_id
        return None

    def _remove_synced_entries(
        self,
        id_map: dict[str, list[str]],
        synced_list: list[tuple[str, str]],
    ) -> None:
        """Removes entries from the ID map after successful synchronization."""
        for case_id, incident_id in synced_list:
            if case_id in id_map and incident_id in id_map[case_id]:
                id_map[case_id].remove(incident_id)
                if not id_map[case_id]:
                    del id_map[case_id]

    def _find_alert_identifier(self, case: SingleJson, incident_id: str) -> str | None:
        """Finds the alert identifier associated with a Sentinel incident ID."""
        for alert in case.get("cyber_alerts", []):
            extracted_incident_id = utils.get_incident_id_from_alert(
                self.soar_job, alert
            )
            if extracted_incident_id == incident_id:
                domain_entities = alert.get("domain_entities", [])
                if domain_entities:
                    return domain_entities[0].get("alert_identifier")
        return None

    def _close_case(
        self,
        case_id: str,
        reason: str,
        root_cause: str,
        alert_identifier: str,
    ) -> None:
        """Closes a Google SecOps case with a specified reason."""
        close_comment = (
            "Closed automatically due to Microsoft Sentinel incident status change. "
            f" Reason: {reason}"
        )
        self.soar_job.close_case(
            root_cause=root_cause,
            comment=close_comment,
            reason=reason,
            case_id=case_id,
            alert_identifier=alert_identifier,
        )
        self.logger.info(f"Successfully closed Google SecOps case {case_id}.")

    def _close_alert(
        self,
        case_id: str,
        alert_identifier: str,
        reason: str,
        root_cause: str,
    ) -> None:
        """Closes a specific alert within a Google SecOps case."""
        close_comment = (
            "Closed automatically due to Microsoft Sentinel incident status change. "
            f"Reason: {reason}"
        )
        self.soar_job.close_alert(
            root_cause=root_cause,
            comment=close_comment,
            reason=reason,
            case_id=case_id,
            alert_id=alert_identifier,
        )
        self.logger.info(
            f"Successfully closed Google SecOps alert {alert_identifier} "
            f"in case {case_id}."
        )


def main() -> NoReturn:
    SyncIncidents().start()


if __name__ == "__main__":
    main()
