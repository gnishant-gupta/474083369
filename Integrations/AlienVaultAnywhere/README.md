
# AlienVaultAnywhere

AlienVault USM Anywhere delivers powerful threat detection, incident response, and compliance management for cloud, on-premises, and hybrid environments.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|None||
|ClientID|None|True|String||
|Secret|None|True|Password|*****|
|Product Version|None|True|String|V2|
|Use SSL|None|False|Boolean|True|


#### Dependencies
| |
|-|
|TIPCommon-1.1.9.0-py2.py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|protobuf-5.28.0-cp38-abi3-manylinux2014_x86_64.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.144.0-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|google_api_core-2.19.2-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|anyio-4.4.0-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|google_auth-2.34.0-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|httpcore-1.0.5-py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240906-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|pyparsing-3.1.4-py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|


## Actions
#### Get Alarm Details
Retrieve details for an alarm by ID
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alarm ID|The alarm ID. Can be obtained by running connector.|True|String||



##### JSON Results
```json
{"uuid": "9cefe1e7-3bfd-5ebf-2f55-d5df0fd157dd", "has_alarm": false, "needs_enrichment": true, "packet_data": ["20f816ba-7e02-edf4-a409-3dac045b6060"], "priority": 20, "suppressed": false, "status": "open", "_links": {"self": {"href": "https://siemplify.alienvault.cloud/api/2.0/alarms/9cefe1e7-3bfd-5ebf-2f55-d5df0fd157dd"}}, "rule_intent": "Environmental Awareness", "alarm_events_count": 1, "source_username": "HW-HOST-13$", "rule_dictionary": "WindowsRules-Dict", "destination_name": "00000000-cd1e-4780-baf8-4527d5e49ad8", "timestamp_occured": "1591639519000", "event_type": "Alarm", "rule_method": "Windows Scheduled Job Created", "priority_label": "low", "rule_attack_tactic": ["Execution", "Persistence", "Privilege Escalation"], "source_name": "00000000-cd1e-4780-baf8-4527d5e49ad8", "timestamp_received": "1591639577405", "destination_canonical": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "source_asset_id": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "rule_strategy": "Security Critical Event", "timestamp_received_iso8601": "2020-06-08T18:06:17.405Z", "alarm_destination_assset_ids": ["8c5029e3-9bc5-eee1-9953-8f5bb550c58f"], "alarm_sources": ["8c5029e3-9bc5-eee1-9953-8f5bb550c58f"], "rule_attack_id": "T1053", "alarm_destinations": ["8c5029e3-9bc5-eee1-9953-8f5bb550c58f"], "highlight_fields": ["source_username", "source_ntdomain", "destination_canonical", "rule_attack_id", "rule_attack_tactic", "rule_attack_technique"], "destination_asset_id": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "rule_id": "Windows scheduled job created", "sensor_uuid": "72fb15aa-51a8-4960-8b10-ff8dc9a6427e", "timestamp_occured_iso8601": "2020-06-08T18:05:19.000Z", "transient": false, "alarm_source_asset_ids": ["8c5029e3-9bc5-eee1-9953-8f5bb550c58f"], "rule_attack_technique": "Scheduled Task", "source_canonical": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "source_ntdomain": "WORKGROUP", "packet_type": "alarm"}
```



#### List Events
Search for AlienVault events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Account Name|The account name.|False|String||
|Event Name|The name of the event.|False|String||
|Source Name|The source name.|False|String||
|Start Time|Filtered results will include events that occurred after this timestamp. format: DD/MM/YYYY|False|String||
|End Time|Filtered results will include events that occurred before this timestamp. format: DD/MM/YYYY|False|String||
|Suppressed|Whether to filter events by the suppressed flag.|False|Boolean|False|
|Events Limit|Maximum number of events to return.|False|String|100|



##### JSON Results
```json
[{"uuid": "13f20da5-1b97-4a4d-1bfe-68f27eb7688d", "event_name": "Service Control Manager: EventID 7040", "timestamp_occured": "1597585711000", "has_alarm": false, "needs_enrichment": true, "suppressed": false, "source_asset_id": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "source_canonical": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "source_name": "00000000-cd1e-4780-baf8-4527d5e49ad8", "destination_asset_id": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "destination_canonical": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "destination_name": "00000000-cd1e-4780-baf8-4527d5e49ad8", "_links": {"self": {"href": "https://siemplify.alienvault.cloud/api/2.0/events/13f20da5-1b97-4a4d-1bfe-68f27eb7688d"}}, "was_fuzzied": false, "device_external_id": "{555908d1-a6d7-4695-8e1e-26931d2012f4}", "plugin_version": "0.43", "control_id": "fd037cc5-20d8-4d81-a4a3-78113ae3f4a9", "log": "{\"hostIdentifier\":\"00000000-cd1e-4780-baf8-4527d5e49ad8\",\"param1\":\"Background Intelligent Transfer Service\",\"param2\":\"auto start\",\"param3\":\"demand start\",\"param4\":\"BITS\",\"datetime\":\"2020-08-16T13:48:30.319281400Z\",\"eventid\":\"7040\",\"keywords\":\"-1\",\"level\":\"4\",\"provider_guid\":\"{555908d1-a6d7-4695-8e1e-26931d2012f4}\",\"provider_name\":\"Service Control Manager\",\"source\":\"System\",\"task\":\"0\",\"time\":\"1597585711\"}", "customfield_13": "Background Intelligent Transfer Service", "event_severity": "INFORMATION", "customfield_14": "auto start", "customheader_13": "Event Parameter 1", "customheader_14": "Event Parameter 2", "rep_device_hostname": "00000000-cd1e-4780-baf8-4527d5e49ad8", "rep_device_asset_id": "8c5029e3-9bc5-eee1-9953-8f5bb550c58f", "used_hint": false, "plugin_device_type": "Endpoint Security", "was_guessed": false, "timestamp_received": "1597585778946", "time_offset": "Z", "rep_dev_canonical": "00000000-cd1e-4780-baf8-4527d5e49ad8", "timestamp_received_iso8601": "2020-08-16T13:49:38.946Z", "plugin_device": "AlienVault Agent", "highlight_fields": ["file_name", "event_severity", "event_category", "event_subcategory", "file_hash", "file_hash_sha1", "file_hash_sha256", "file_hash_md5", "source_process", "destination_process", "source_process_parent", "source_process_parent_commandline", "source_process_commandline", "source_username", "destination_username", "source_ntdomain", "malware_family", "event_outcome", "destination_port_label", "source_port_label", "customfield_13", "customfield_14", "pefile_fileversion", "pefile_description", "pefile_product", "pefile_company", "relative_distinguished_name", "event_attack_id", "event_attack_technique", "event_attack_tactic"], "event_category": "System", "event_subcategory": "Service Control Manager", "timestamp_occured_iso8601": "2020-08-16T13:48:31.000Z", "plugin": "AlienVault Agent - Windows EventLog", "transient": false, "rep_device_rule_id": "7040", "packet_type": "log"}]
```



#### Ping
Test connectivity
Timeout - 600 Seconds









## Connectors
#### AlienVault USM Anywhere Connector
AlienVault USM Anywhere Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|message_plugin|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Api Root|e.g. https://<instance>.alienvault.com|True|String||
|ClientID|ClientID|True|String||
|Secret|Secret|True|Password|*****|
|Product Version|AlienVault Anywhere version - V1, V2|True|String|V2|
|Verify SSL|Indicate whether to use SSL in the session or not|False|Boolean|FALSE|
|Max Alerts Per Cycle|Limit the number of alerts in every cycle. e.g. 10|True|Integer|10|
|Max Days Backwards|This field is used in the connector first running cycle and determine the start time. e.g. 3|True|Integer|1|
|Padding Period|Padding period (hours) for the connector execution.|False|Integer|0|
|Show Suppressed|Whether to include suppressed alarms in the search|False|Boolean||
|Use Suppressed Filter|This parameter will be used to determine whether to filter the incoming alerts using the "Show Suppressed" filter or not.|False|Boolean|True|
|Priority|Filter by alarm priority, comma separated. Valid value: high/medium/low.|False|String||
|Rule Intent|Filter alarms by the purpose of the alarm. The intent describes the context of the behavior that is being observed. These are the threat categories: System Compromise, Exploitation & Installation, Delivery & Attack, Reconnaissance & Probing, Environmental Awareness|False|String||
|Rule Strategy|The strategy of the rule that triggered the alarm. For example, use Client-Side Attack - Known Vulnerability when trying to exploit a known vulnerability in a web browser the attacker|False|String||
|Rule Method|Filter alarms by rule method. The method would provide additional detail on the target of the attack and the particular vulnerability. e.g. Firefox - CVE-2008-4064|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.