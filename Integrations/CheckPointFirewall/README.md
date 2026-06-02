
# CheckPointFirewall

VPN-1 is a firewall and VPN product developed by Check Point Software Technologies Ltd. VPN-1 is a stateful firewall which also filters traffic by inspecting the application layer.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server Address||True|IP|xx.xx.xx.xx:443|
|Username||True|String||
|Domain||False|String||
|Password||True|Password|*****|
|Policy Name||True|String|standard|
|Verify SSL||False|Boolean||


#### Dependencies
| |
|-|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Add Ip To Group
Add IP to the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Blacklist Group Name|Specify the name of the group to which you want to add IP address.|True|String||



#### List Policies On Site
Retrieve all existing policies
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Policies To Return|Specify how many policies to return in the response. Default: 50.|False|String|50|



##### JSON Results
```json
[{"uid": "fa0844a2-6a63-48d1-92f5-xxxx", "name": "Standard", "type": "package", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "installation-targets-revision": [{"target-name": "gaia80.10", "target-uid": "8f36a0de-e0d5-6347-ae51-xxxx", "revision": {"uid": "2c7e13c7-1e83-47d8-beb5-xxxx", "type": "session", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "state": "published", "user-name": "admin", "description": "", "last-login-time": {"posix": 1603722754891, "iso-xxx": "2020-10-26T16:32+0200"}, "publish-time": {"posix": 1603722758612, "iso-xxx": "2020-10-26T16:32+0200"}, "expired-session": false, "application": "WEB_API", "changes": 0, "in-work": false, "ip-address": "127.0.0.1", "locks": 1, "connection-mode": "read write", "session-timeout": 600, "comments": "", "color": "black", "icon": "Objects/worksession", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1603722754896, "iso-xxx": "2020-10-26T16:32+0200"}, "last-modifier": "admin", "creation-time": {"posix": 1603722754896, "iso-xxx": "2020-10-26T16:32+0200"}, "creator": "admin"}, "read-only": false}}], "access": true, "access-layers": [{"uid": "50c71672-c7da-40cb-92ae-xxxx", "name": "Network", "type": "access-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "shared": false, "applications-and-url-filtering": false, "content-awareness": false, "mobile-access": false, "firewall": true, "implicit-cleanup-action": "drop", "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "locked by other session", "validation-state": "ok", "last-modify-time": {"posix": 1539092983392, "iso-xxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092983344, "iso-xxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}], "threat-layers": [{"uid": "364b9452-d032-4d02-8358-xxxx", "name": "IPS", "type": "threat-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "ips-layer": true, "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1539092985626, "iso-xxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092985538, "iso-xxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}, {"uid": "a199e513-a565-4851-b23d-xxxx", "name": "Standard Threat Prevention", "type": "threat-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "ips-layer": false, "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1539092985651, "iso-xxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092984703, "iso-xxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}], "vpn-traditional-mode": false, "nat-policy": true, "qos": false, "qos-policy-type": "recommended", "desktop-security": false, "threat-prevention": true, "installation-targets": "all", "https-inspection-policy": true, "https-inspection-layer": {"uid": "da74622e-6afc-4c32-976e-xxxx", "name": "Default Layer", "type": "https-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "shared": true, "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "locked by other session", "validation-state": "ok", "last-modify-time": {"posix": 1602698385402, "iso-xxx": "2020-10-14T20:59+0300"}, "last-modifier": "System", "creation-time": {"posix": 1602698384431, "iso-xxx": "2020-10-14T20:59+0300"}, "creator": "System"}, "read-only": false}, "comments": "", "color": "black", "icon": "Blades/Access", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1602698390129, "iso-xxx": "2020-10-14T20:59+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092983314, "iso-xxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Remove IP From Group
Remove IP from the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Blacklist Group Name|Specify the name of the group from which you want to remove IP address.|True|String||



#### Remove SAM Rule
Remove a SAM (suspicious activity monitoring) rule from Checkpoint Firewall. Note: you need to match the current rule in order to remove it. Please refer to the Checkpoint fw_sam command criteria section documentation for available ip, netmask, port and protocol combinations - https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_CLI_ReferenceGuide/Topics-CLIG/MDSG/fw-sam.htm
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Security Gateway|Specify the name of Security Gateway from where to remove SAM Rule|True|String||
|Source IP|Specify the source IP to be added to the rule.|False|String||
|Source Netmask|Specify the source netmask to be added to the rule.|False|String||
|Destination IP|Specify the destination IP to be added to the rule.|False|String||
|Destination Netmask|Specify the destination netmask to be added to the rule.|False|String||
|Port|Specify the port number to be added to the rule for example, 5005|False|String||
|Protocol|Specify the protocol name to be added to the rule for example, TCP|False|String||
|Action for the Matching Connections|Specify the action that should be executed for the matching connections.|True|List|Drop|
|How to Track Matching Connections|Specify how to track matching connections.|True|List|Log|
|Close Connections|Specify if the existing matching connections should be closed.|False|Boolean|false|



##### JSON Results
```json
{"tasks": [{"uid": "68f580e0-914f-4eef-8e46-436dfbxxxxfd", "name": "xxxx - Siemplify-generated-script-remove-sam-rule", "type": "CdmTaskNotification", "domain": {"uid": "41e821a0-3720-11e3-aa6e-0800200c9xxx", "name": "User1", "domain-type": "domain"}, "task-id": "e2531d26-dfcc-46d3-a9b0-560b4e1aaxxx", "task-name": "xxx1.1 - Siemplify-generated-script-remove-sam-rule", "status": "succeeded", "progress-percentage": "100", "start-time": {"posix": "1612258xx53865", "iso-8601": "2021-02-02T11:27+0200"}, "last-update-time": {"posix": "16122580558xx", "iso-8601": "2021-02-02T11:27+0200"}, "suppressed": "false", "task-details": [{"uid": "de29c086-db7f-47d8-8e96-38e4bc9b5cxx", "name": "null", "domain": {"uid": "41e821a0-3720-11e3-aa6e-0800200c9xxx", "name": "User1", "domain-type": "domain"}, "color": "black", "statusCode": "succeeded", "statusDescription": "asd", "taskNotification": "68f580e0-914f-4eef-8e46-436dfb3403fd", "gatewayId": "8f36axxx-e0d5-6347-ae51-6fb22d573f04", "gatewayName": "asd", "transactionId": "683682800", "responseMessage": "asd", "responseError": "asd", "meta-info": {"validation-state": "ok", "last-modify-time": {"posix": "1612258055858", "iso-8601": "2021-02-02T11:27+0200"}, "last-modifier": "admin", "creation-time": {"posix": "1612258053923", "iso-8601": "2021-02-02T11:27+0200"}, "creator": "admin"}, "tags": [], "icon": "GeneralglobalsNa", "comments": "ads", "display-name": "asd", "customFields": "null"}], "comments": "Completed", "color": "black", "icon": "GeneralglobalsNa", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": "1612258055834", "iso-8601": "2021-02-02T11:27+0200"}, "last-modifier": "admin", "creation-time": {"posix": "1612258053905", "iso-8601": "2021-02-02T11:27+0200"}, "creator": "admin"}, "read-only": "false"}]}
```



#### Remove Url From Group
Remove URL from the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs Group Name|Specify the name of the group from which you want to remove URL.|True|String||



#### Run Script
Run arbitrary script with CheckPoint run-script API call. Note: action is not using Siemplify entities to operate.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Script text|Script to execute. For example, fw sam command: fw sam -t 600 -I src 8.9.10.12|True|String||
|Target|Specify CheckPoint device to execute script on, for example: gaia80.10. Parameter accepts multiple values as a comma separated list.|True|String||



##### JSON Results
```json
{"tasks": [{"task-id": "867fef24-647e-40ea-91ef-9b5f8ae83d07", "status": "succeeded", "domain": {"domain-type": "domain", "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde", "name": "SMC User"}, "start-time": {"posix": 1597737649683, "iso-8601": "2020-08-18T11:00+0300"}, "uid": "bb5c4640-9774-45cd-8631-8e80518f4e18", "tags": [], "last-update-time": {"posix": 1597737651783, "iso-8601": "2020-08-18T11:00+0300"}, "suppressed": false, "progress-percentage": 100, "comments": "Completed", "task-name": "gaia80.10 - Siemplify-generated-script", "color": "black", "meta-info": {"creation-time": {"posix": 1597737649720, "iso-8601": "2020-08-18T11:00+0300"}, "validation-state": "ok", "creator": "admin", "lock": "unlocked", "last-modifier": "admin", "last-modify-time": {"posix": 1597737651810, "iso-8601": "2020-08-18T11:00+0300"}}, "task-details": [{"display-name": "", "domain": {"domain-type": "domain", "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde", "name": "SMC User"}, "gatewayName": "", "uid": "b4a71da3-60fc-4785-a379-3bb9f7a0ff2f", "icon": "General/globalsNa", "tags": [], "color": "black", "comments": "", "name": null, "responseError": "", "taskNotification": "bb5c4640-9774-45cd-8631-8e80518f4e18", "responseMessage": "", "gatewayId": "8f36a0de-e0d5-6347-ae51-6fb22d573f04", "transactionId": 931053033, "meta-info": {"creation-time": {"posix": 1597737649735, "iso-8601": "2020-08-18T11:00+0300"}, "last-modify-time": {"posix": 1597737651840, "iso-8601": "2020-08-18T11:00+0300"}, "creator": "admin", "validation-state": "ok", "last-modifier": "admin"}, "customFields": null, "statusDescription": "", "statusCode": "succeeded"}], "icon": "General/globalsNa", "type": "CdmTaskNotification", "read-only": false, "name": "gaia80.10 - Siemplify-generated-script"}]}
```



#### Show Logs
Retrieve logs from CheckPoint FireWall based on the filter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query Filter|Specify the query filter that will be used to return logs.|False|String||
|Time Frame|Specify what time frame should be used for log retrieval.|True|List|Last Hour|
|Log Type|Specify what type of logs should be returned.|True|List|Log|
|Max Logs To Return|Specify how many logs to return. Maximum is 100. This is Checkpoint FireWall limitation.|False|String|50|



##### JSON Results
```json
[{"subject": "Status Report", "confidence_level": "N/A", "description": "Properly secure network devices with special mechanisms and tools (e.g., authentication for device management, secure communications, strong authentication mechanisms). Implement active monitoring and pattern recognition to protect devices from attack. [Original CobiT 4.1 Reference: Deliver and Support / Ensure Systems Security / Network Security : DS.5.10.1.3]", "type": "Control", "orig_log_server_attr": [{"isCHKPObject": "true", "uuid": "8f36a0de-e0d5-6347-ae51-xxxx", "resolved": "gaia80.10"}], "cb_log_type": "Regulatory Requirement", "user_field": "admin", "administrator": "admin", "index_time": "2020-11-01T21:36:05Z", "d_name": "Check that each Gateway's Anti-Bot configuration is activated according to the policy", "violation_date": "3/6/2020 15:03", "id": "ac1eca60-81b3-d219-5f9f-xxxx", "rounded_received_bytes": "0", "cb_title": "Regulatory Requirement  150042 Status: Good", "cb_old_status": "Secure", "lastUpdateSeqNum": "1479", "severity": "Informational", "product_family": "Network", "product": "Compliance Blade", "sequencenum": "1479xx", "rounded_sent_bytes": "0", "cb_scan_id": "Sun Nov  1 23:35:48 2020", "orig_log_server": "172.30.202.xx", "cb_changed_objects": "ABSettings_8F36A0DE-E0D5-6347-AE51-xxxx", "additional_info": "Regulatory Requirement status", "cb_status": "Good", "orig": "gaia80.10", "marker": "@A@@B@1604181600@C@62734", "rounded_bytes": "0", "orig_log_server_ip": "172.30.202.xx", "stored": "true", "calc_desc": "Regulatory Requirement  150042 Status: Good", "logid": "1342832xxx", "time": "2020-11-01T21:36:05Z", "cb_recommendation": "Each Gateway should be configured to work according to the profiles defined in the Anti-Bot policy. The Activation Mode should be set to 'According to Policy' and not 'Detect Only'.", "best_practice_id": "AB104xxx", "lastUpdateTime": "1604266565000"}]
```



#### Add Url To Group
Add Url to the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs Group Name|Specify the name of the group to which you want to add URL.|True|String||



#### Download Log Attachment
Download log attachments from CheckPoint FireWall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log IDs|Specify the comma-separated list of log IDs from which you want to download attachments.|True|String||
|Download Folder Path|Specify the absolute path for the folder where the action should store the attachments.|True|String||
|Create Case Wall Attachment|If enabled, action will create a case wall attachment for each successfully downloaded file. Note: that attachment will only be created if it’s size is less than 3 MB.|False|Boolean||



##### JSON Results
```json
[{"tasks": [{"task-id": "012asd-89ab-cdef-xxxx", "task-name": "Packet Capture operation", "status": "succeeded", "progress-percentage": 100, "suppressed": false, "absolute_path": "home/test", "task-details": [{"attachments": [{"base64-data": "1MOyoQIABAD///xxxx//APBqlv//AAAnB0DlUBEEAaDBAAA=\n", "file-name": "Anti-Virus-blob-file.cap"}]}]}]}]
```



#### List Layers On Site
Retrieve all of the available Access Control and Threat Prevention layers
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Layers To Return|Specify how many layers to return in the response. Default: 50.|False|String|50|



##### JSON Results
```json
[[{"uid": "50c71672-c7da-40cb-92ae-xxxx", "name": "Network", "type": "access-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "shared": false, "applications-and-url-filtering": false, "content-awareness": false, "mobile-access": false, "firewall": true, "implicit-cleanup-action": "drop", "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "locked by other session", "validation-state": "ok", "last-modify-time": {"posix": 1539092983392, "iso-xxxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092983344, "iso-xxxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}], [{"uid": "364b9452-d032-4d02-8358-xxxx", "name": "IPS", "type": "threat-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "ips-layer": true, "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1539092985626, "iso-xxxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092985538, "iso-xxxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}, {"uid": "a199e513-a565-4851-b23d-6cbf57b023c3", "name": "Standard Threat Prevention", "type": "threat-layer", "domain": {"uid": "41e821a0-3720-11e3-aa6e-xxxx", "name": "SMC User", "domain-type": "domain"}, "ips-layer": false, "comments": "", "color": "black", "icon": "ApplicationFirewall/rulebase", "tags": [], "meta-info": {"lock": "unlocked", "validation-state": "ok", "last-modify-time": {"posix": 1539092985651, "iso-xxxx": "2018-10-09T16:49+0300"}, "last-modifier": "System", "creation-time": {"posix": 1539092984703, "iso-xxxx": "2018-10-09T16:49+0300"}, "creator": "System"}, "read-only": false}]]
```



#### Add a SAM Rule
Add a SAM (suspicious activity monitoring) rule for Checkpoint Firewall. Please refer to the Checkpoint fw_sam command criteria section documentation for available ip, netmask, port and protocol combinations - https://sc1.checkpoint.com/documents/R80.40/WebAdminGuides/EN/CP_R80.40_CLI_ReferenceGuide/Content/Topics-CLIG/MDSG/fw-sam.htm
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Security Gateway to Create SAM Rule on|Specify the name of Security Gateway to create a rule for.|True|String||
|Source IP|Specify the source IP to be added to the rule.|False|String||
|Source Netmask|Specify the source netmask to be added to the rule.|False|String||
|Destination IP|Specify the destination IP to be added to the rule.|False|String||
|Destination Netmask|Specify the destination netmask to be added to the rule.|False|String||
|Port|Specify the port number to be added to the rule for example, 5005|False|String||
|Protocol|Specify the protocol name to be added to the rule for example, TCP|False|String||
|Expiration|Specify how long in seconds the newly added SAM rule should be active for example, 4. If nothing is specified - then the rule never expires.|False|String||
|Action for the Matching Connections|Specify the action that should be executed for the matching connections.|True|List|Drop|
|How to Track Matching Connections|Specify how to track matching connections.|True|List|Log|
|Close Connections|Specify if the existing matching connections should be closed.|False|Boolean|false|



##### JSON Results
```json
{"tasks": [{"task-id": "867fef24-647e-40ea-91ef-9b5f8ae83d07", "status": "succeeded", "domain": {"domain-type": "domain", "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde", "name": "SMC User"}, "start-time": {"posix": 1597737649683, "iso-8601": "2020-08-18T11:00+0300"}, "uid": "bb5c4640-9774-45cd-8631-8e80518f4e18", "tags": [], "last-update-time": {"posix": 1597737651783, "iso-8601": "2020-08-18T11:00+0300"}, "suppressed": false, "progress-percentage": 100, "comments": "Completed", "task-name": "gaia80.10 - Siemplify-generated-script", "color": "black", "meta-info": {"creation-time": {"posix": 1597737649720, "iso-8601": "2020-08-18T11:00+0300"}, "validation-state": "ok", "creator": "admin", "lock": "unlocked", "last-modifier": "admin", "last-modify-time": {"posix": 1597737651810, "iso-8601": "2020-08-18T11:00+0300"}}, "task-details": [{"display-name": "", "domain": {"domain-type": "domain", "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde", "name": "SMC User"}, "gatewayName": "", "uid": "b4a71da3-60fc-4785-a379-3bb9f7a0ff2f", "icon": "General/globalsNa", "tags": [], "color": "black", "comments": "", "name": null, "responseError": "", "taskNotification": "bb5c4640-9774-45cd-8631-8e80518f4e18", "responseMessage": "", "gatewayId": "8f36a0de-e0d5-6347-ae51-6fb22d573f04", "transactionId": 931053033, "meta-info": {"creation-time": {"posix": 1597737649735, "iso-8601": "2020-08-18T11:00+0300"}, "last-modify-time": {"posix": 1597737651840, "iso-8601": "2020-08-18T11:00+0300"}, "creator": "admin", "validation-state": "ok", "last-modifier": "admin"}, "customFields": null, "statusDescription": "", "statusCode": "succeeded"}], "icon": "General/globalsNa", "type": "CdmTaskNotification", "read-only": false, "name": "gaia80.10 - Siemplify-generated-script"}]}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.