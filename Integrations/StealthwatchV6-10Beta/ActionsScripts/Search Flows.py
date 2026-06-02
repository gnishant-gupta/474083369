from SiemplifyUtils import output_handler
from SiemplifyDataModel import EntityTypes
from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import utc_now, construct_csv, dict_to_flat
from Stealthwatch610Manager import StealthwatchManager, StealthwatchManagerError
import datetime
from dateutil.parser import parse
import json


@output_handler
def main():
    siemplify = SiemplifyAction()
    configurations = siemplify.get_configuration("StealthwatchV6-10")
    server_address = configurations["Api Root"]
    username = configurations["Username"]
    password = configurations["Password"]

    time_delta = int(siemplify.parameters["Timeframe"])
    limit = int(siemplify.parameters["Limit"])
    tenant_id = siemplify.parameters.get("Tenant ID")
    ip_addresses_str = siemplify.parameters.get("IP Address")
    start_time_str = siemplify.parameters.get("Start Time")

    end_time_dt = utc_now()
    if start_time_str:
        start_time_dt = parse(start_time_str).replace(tzinfo=datetime.timezone.utc)
        end_time_dt = start_time_dt + datetime.timedelta(hours=time_delta)
    else:
        start_time_dt = end_time_dt - datetime.timedelta(hours=time_delta)

    end_time = end_time_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    start_time = start_time_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]

    stealthwatch_manager = StealthwatchManager(server_address, username, password)

    enriched_entities = []
    results = []
    if tenant_id:
        siemplify.LOGGER.info(
            f"Tenant ID {tenant_id} provided. Searching for top flows in this tenant."
        )
        results = []
        search_id = stealthwatch_manager.search_flows(
            domain_id=tenant_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        if search_id:
            results = stealthwatch_manager.get_flows_search_results(
                tenant_id, search_id, limit
            )

    else:
        ip_addresses_param = (
            [ip.strip() for ip in ip_addresses_str.split(",")]
            if ip_addresses_str
            else []
        )
        ip_entities = [
            entity.identifier
            for entity in siemplify.target_entities
            if entity.entity_type == EntityTypes.ADDRESS
        ]
        target_ips = ip_addresses_param + ip_entities
        target_ips = sorted(list(set(target_ips)))
        entity_map = {entity.identifier: entity for entity in siemplify.target_entities}
        siemplify.LOGGER.info(target_ips)

        for ip_address in target_ips:
            siemplify.LOGGER.info(f"Searching flows for {ip_address}")
            try:
                domain_id = stealthwatch_manager.get_domain_id_by_ip(ip_address)
            except StealthwatchManagerError as e:
                siemplify.LOGGER.info(f"Skipping IP {ip_address}: {e}")
                continue

            if domain_id:
                results = []

                search_id = stealthwatch_manager.search_flows(
                    domain_id=domain_id,
                    start_time=start_time,
                    end_time=end_time,
                    limit=limit,
                    source_ips=[ip_address],
                )

                if search_id:
                    results = stealthwatch_manager.get_flows_search_results(
                        domain_id, search_id, limit
                    )

                search_id = stealthwatch_manager.search_flows(
                    domain_id=domain_id,
                    start_time=start_time,
                    end_time=end_time,
                    limit=limit,
                    destination_ips=[ip_address],
                )

                if search_id:
                    results.extend(
                        stealthwatch_manager.get_flows_search_results(
                            domain_id, search_id, limit
                        )
                    )

                if results:
                    # Attach all data as JSON
                    siemplify.result.add_json(ip_address, json.dumps(results))

                    csv_output = construct_csv(list(map(dict_to_flat, results)))
                    siemplify.result.add_entity_table(ip_address, csv_output)

                    if ip_address in entity_map:
                        enriched_entities.append(entity_map[ip_address])

    if results:
        if tenant_id:
            output_message = f"Successfully found flows for tenant {tenant_id}."
            siemplify.result.add_json("Flows", json.dumps(results))
        else:
            entities_names = [entity.identifier for entity in enriched_entities]
            output_message = (
                "Flows were found for the following entities:\n"
                + "\n".join(entities_names)
            )

        result_value = "true"

    else:
        output_message = "No flows were found."
        result_value = "true"

    siemplify.end(output_message, result_value)


if __name__ == "__main__":
    main()
