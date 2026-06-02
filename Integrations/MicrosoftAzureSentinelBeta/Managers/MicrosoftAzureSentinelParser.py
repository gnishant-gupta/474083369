from __future__ import annotations

from datamodels import *


DEFAULT_ALERT_NAME = "No alert name found"
DEFAULT_RULE_GENERATOR_NAME = "No rule generator found"
DEFAULT_PRODUCT = "Azure Sentinel"
DEFAULT_VENDOR = "Microsoft"


class MicrosoftAzureSentinelParser:
    def __init__(self, siemplify_logger=None):
        self.siemplify_logger = siemplify_logger

    def build_results(self, raw_json, method, data_key="value", limit=None, *kwargs):
        """Build result object from json data."""
        return [
            getattr(self, method)(item_json, *kwargs)
            for item_json in (raw_json.get(data_key, []) if data_key else raw_json)[
                :limit
            ]
        ]

    @staticmethod
    def build_siemplify_incident_obj(raw_json):
        properties = raw_json.get("properties", {})
        return Incident(
            raw_data=raw_json,
            id_=raw_json.get("id"),
            type_=raw_json.get("type"),
            **raw_json,
            incident_properties=(
                IncidentProperties(**properties, **properties.get("additionalData", {}))
                if properties
                else None
            ),
        )

    @staticmethod
    def build_scheduled_alert_objs(raw_json: list[dict]):
        """Build ScheduledAlert data models out of raw JSON data."""
        return [
            ScheduledAlert(
                raw_data=sa_json,
                system_alert_id=sa_json.get("SystemAlertId"),
                product_component_name=sa_json.get("ProductComponentName"),
                vendor_name=sa_json.get("VendorName"),
            )
            for sa_json in raw_json
        ]

    @staticmethod
    def build_siemplify_incident_statistic_obj(incident_statistic_data):
        return IncidentStatistic(
            raw_data=incident_statistic_data, **incident_statistic_data
        )

    @staticmethod
    def build_siemplify_incident_alert_obj(incident_alert_data):
        return IncidentAlert(raw_data=incident_alert_data, **incident_alert_data)

    @staticmethod
    def build_siemplify_alert_entity_obj(alert_entity_data, alert_edge_data):
        return AlertEntity(
            raw_data=alert_entity_data,
            additional_data=alert_edge_data,
            **alert_entity_data,
        )

    @staticmethod
    def build_siemplify_alert_rule_obj(alert_rule_data):
        return AlertRule(raw_data=alert_rule_data, **alert_rule_data)

    @staticmethod
    def build_siemplify_custom_hunting_rule_obj(raw_json):
        return CustomHuntingRule(raw_data=raw_json, **raw_json)

    @staticmethod
    def build_siemplify_custom_hunting_rule_req_obj(raw_json):
        return CustomHuntingRuleRequest(raw_data=raw_json, **raw_json)

    @staticmethod
    def build_siemplify_primary_result_obj(raw_json):
        return PrimaryResult(**raw_json)

    @staticmethod
    def get_next_page_link(raw_json):
        return raw_json.get("nextLink")

    @staticmethod
    def calculate_priority(alert_severity):
        """
        The function calculates case priority by the Priority Map.
        :param alert_severity: severity value as it came from Sentinel {string}
        :return: calculated Siemplify alarm priority {integer}
        """

        # Draft
        if alert_severity == SentinelPriorityEnum.DRAFT.value:
            return SiemplifyPriorityEnum.DRAFT.value
        # Low.
        elif alert_severity == SentinelPriorityEnum.LOW.value:
            return SiemplifyPriorityEnum.LOW.value
        # Medium
        elif alert_severity == SentinelPriorityEnum.MEDIUM.value:
            return SiemplifyPriorityEnum.MEDIUM.value
        # High
        elif alert_severity == SentinelPriorityEnum.HIGH.value:
            return SiemplifyPriorityEnum.HIGH.value
        # Critical
        elif alert_severity == SentinelPriorityEnum.CRITICAL.value:
            return SiemplifyPriorityEnum.CRITICAL.value

        # Informative
        return SiemplifyPriorityEnum.INFO.value
