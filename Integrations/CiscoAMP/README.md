
# CiscoAMP

Get global threat intelligence, advanced sandboxing, and real-time malware blocking to prevent breaches with Cisco Advanced Malware Protection (AMP). But because you can’t rely on prevention alone, AMP also continuously analyzes file activity across your extended network, so you can quickly detect, contain, and remove advanced malware.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|None|https://api.amp.cisco.com|
|Client ID|None|True|String||
|Api Key|None|True|Password|*****|
|Use SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|


## Actions
#### Get Computers By Network Activity (URL)
Fetch a list of computers that have connected to the given hostname or URL
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"0": {"connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2", "links": {"trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory", "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2", "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"}, "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4", "active": "True", "operating_system": "Windows Server 2012 R2, SP 0.0", "network_addresses": [{"ip": "10.0.0.4", "mac": "00:0d:3a:4e:fc:6e"}, {"ip": "10.212.134.201", "mac": "00:09:0f:aa:00:01"}], "faults": [], "external_ip": "13.72.107.194", "hostname": "poc-JuanV", "install_date": "2019-04-29T19:37:06Z", "connector_version": "6.2.9.10881", "internal_ips": ["10.0.0.4", " 10.212.134.201"], "policy": {"guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c", "name": "Server"}, "last_seen": "2019-05-28T11:46:32Z"}}, "Entity": "entityIdentifier"}]
```



#### Get Computers By Network Activity (Ip)
Fetch a list of computers that have connected to the given IP address
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"0": {"connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2", "links": {"trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory", "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2", "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"}, "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4", "active": "True", "operating_system": "Windows Server 2012 R2, SP 0.0", "network_addresses": [{"ip": "10.0.0.4", "mac": "00:0d:3a:4e:fc:6e"}, {"ip": "10.212.134.201", "mac": "00:09:0f:aa:00:01"}], "faults": [], "external_ip": "13.72.107.194", "hostname": "poc-JuanV", "install_date": "2019-04-29T19:37:06Z", "connector_version": "6.2.9.10881", "internal_ips": ["10.0.0.4", " 10.212.134.201"], "policy": {"guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c", "name": "Server"}, "last_seen": "2019-05-28T11:46:32Z"}}, "Entity": "entityIdentifier"}]
```



#### Get File List Items
Get the items listed in a given file list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File List Name|e.g. File Blacklist|True|String||



##### JSON Results
```json
{"items": [{"source": "Created by uploading 1_Credit Card Magnetic Tracks - Notepad (2).TXT via Web from 1.1.1.1.", "sha256": "640e9583763fa553069a4984f8df5e81d6890897a6eb0f5de881218e3ed409c8", "description": ""}, {"source": "Created by entering SHA-256 via Public api.", "sha256": "5fd924625f6ab16a19cc9807c7c506ae1813490e4ba675f843d5a10e0baacdb8", "description": "Added by Siemplify"}, {"source": "Created by entering SHA-256 via Public api.", "sha256": "1248712441dbbf43bb37f91d626a020e7e0f4486f050142034b8a267b06a2f0c", "description": "Added by Siemplify"}], "guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5", "name": "File Blacklist"}
```



#### Get Computer Info
Get details about a computer
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"orbital": {"status": "not_enabled"}, "operating_system": "Windows 10, SP 0.0", "connector_guid": "f719857b-5474-467f-803c-00393616cdcf", "policy": {"guid": "d04fbbc0-fc5d-45d9-94f6-9e53f5079c2f", "name": "Triage"}, "external_ip": "1.1.1.1", "group_guid": "bcaafdfb-bf15-4f65-81e0-58b14624ff26", "hostname": "Demo_AMP", "install_date": "2019-12-19T16:00:07Z", "network_addresses": [{"ip": "1.1.1.1", "mac": "18:ac:08:1f:49:13"}], "connector_version": "7.1.5.11523", "windows_processor_id": "96b4ea231f570d8", "internal_ips": ["1.1.1.1"], "faults": [], "isolation": {"available": false, "status": "not_isolated"}, "active": true, "last_seen": "2019-12-21T17:07:39Z"}, "Entity": "Demo_AMP"}]
```



#### Create Group
Create a new group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|The name of the new group|True|String||
|Group Description|The description of the new group|True|String||



##### JSON Results
```json
{"source": "CreatedviaAPI", "guid": "c5e2099d-3aeb-4dc2-add4-42fb01d05c51", "name": "test", "policies": [{"product": "windows", "description": "ThispolicyputstheAMPforEndpointsConnectorinamodethatwillonlydetectmaliciousfilesbutnotquarantinethem.Maliciousnetworktrafficisalsodetectedbutnotblocked.", "links": {"policy": "https: //api.amp.cisco.com/v1/policies/a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2", "policy_xml": "https: //api.amp.cisco.com/v1/policies/a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2.xml"}, "default": true, "file_lists": [{"guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5", "type": "simple_custom_detections", "name": "FileBlacklist"}, {"guid": "38c1a9eb-0389-4f12-8084-96f5ee62d72e", "type": "application_blocking", "name": "ExecutionBlacklist"}, {"guid": "3133128e-5455-4e74-82c5-1ff3c816c414", "type": "application_whitelist", "name": "FileWhitelist"}], "ip_lists": [], "used_in_groups": [{"guid": "d3f8be3c-e53b-4b31-a8b7-a78a69b74ea1", "name": "Audit", "description": "AuditGroupforPartner-Siemplify"}], "inherited": false, "serial_number": 28, "guid": "a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2", "exclusion_sets": [{"guid": "43fc08b5-c603-4c24-9b4d-501d342f443c", "name": "WorkstationExclusions"}], "name": "Audit"}], "description": "added by siemplify!"}
```



#### Get File Lists By Policy
Get the file lists that are assigned in a policy
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Name|The name of the policy e.g. Triage|True|String||



##### JSON Results
```json
{"1": {"guid": "38c1a9eb-0389-4f12-8084-96f5ee62d72e", "type": "application_blocking", "name": "Execution Blacklist"}, "0": {"guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5", "type": "simple_custom_detections", "name": "File Blacklist"}, "2": {"guid": "3133128e-5455-4e74-82c5-1ff3c816c414", "type": "application_whitelist", "name": "File Whitelist"}}
```



#### Isolate Machine
Isolate Machine by connector guid.
Timeout - 600 Seconds



##### JSON Results
```json
{ "EntityResult": { "available": true, "status": "not_isolated", "unlock_code": "unlock_code", "isolated_by": "Name Surname", "comment": "Some comment"}, "Entity": "1.1.1.1"}
```



#### Get Computers By File Name
Fetch a list of computers that have observed files with the given file name
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"0": {"connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2", "links": {"trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory", "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2", "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"}, "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4", "active": "True", "operating_system": "Windows Server 2012 R2, SP 0.0", "network_addresses": [{"ip": "10.0.0.4", "mac": "00:0d:3a:4e:fc:6e"}, {"ip": "10.212.134.201", "mac": "00:09:0f:aa:00:01"}], "faults": [], "external_ip": "13.72.107.194", "hostname": "poc-JuanV", "install_date": "2019-04-29T19:37:06Z", "connector_version": "6.2.9.10881", "internal_ips": ["10.0.0.4", " 10.212.134.201"], "policy": {"guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c", "name": "Server"}, "last_seen": "2019-05-28T11:46:32Z"}}, "Entity": "entityIdentifier"}]
```



#### Get Policies
Get policy details
Timeout - 600 Seconds



##### JSON Results
```json
{"1": {"product": "ios", "name": "Audit", "default": true, "serial_number": 38, "guid": "1111111111111111", "description": "ThispolicyputsClarityinamodethatwilllogandalertonconvictionsbutnotblocktraffic."}, "0": {"product": "android", "name": "Protect", "default": true, "serial_number": 11, "guid": "1111111111111111", "description": "ThisisthestandardpolicyfortheAMPforEndpointsConnectorthatwillquarantinemaliciousfilesandblockmaliciousnetworkconnections."}}
```



#### Ping
Test connectivity to Cisco AMP.
Timeout - 600 Seconds



#### Get Groups
Get group details
Timeout - 600 Seconds



##### JSON Results
```json
{"1": {"source": "CreatedviaAPI", "guid": "1111111111111111111111", "name": "TestGroup", "description": "GroupcreatedbySiemplify"}, "0": {"source": null, "guid": "1111111111111111111111", "name": "Audit", "description": "AuditGroupforPartner-Siemplify"}}
```



#### Unisolate Machine
Stop isolation of Machine by connector guid.
Timeout - 600 Seconds



##### JSON Results
```json
{ "EntityResult": { "available": true, "status": "isolated", "unlock_code": "unlock_code", "isolated_by": "Name Surname", "comment": "Some comment"}, "Entity": "1.1.1.1"}
```



#### Get Computers By File Hash
Fetch a list of computers that have observed files with the given SHA-256 value
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"0": {"connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2", "links": {"trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory", "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2", "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"}, "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4", "active": "True", "operating_system": "Windows Server 2012 R2, SP 0.0", "network_addresses": [{"ip": "10.0.0.4", "mac": "00:0d:3a:4e:fc:6e"}, {"ip": "10.212.134.201", "mac": "00:09:0f:aa:00:01"}], "faults": [], "external_ip": "13.72.107.194", "hostname": "poc-JuanV", "install_date": "2019-04-29T19:37:06Z", "connector_version": "6.2.9.10881", "internal_ips": ["10.0.0.4", " 10.212.134.201"], "policy": {"guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c", "name": "Server"}, "last_seen": "2019-05-28T11:46:32Z"}}, "Entity": "entityIdentifier"}]
```



#### Add File To File List
Add a SHA-256 for a specific file list
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File List Name|File Blacklist|True|String||
|Description|Description of the file|True|String||









## Connectors
#### Cisco AMP - Security Events Connector
Pull security events from Cisco AMP into Siemplify. Note: whitelist works with eventType parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|event_type|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic.|False|String|.*|
|API Root|API root of the Cisco AMP instance.|False|String|https://{{ip address}}|
|Client ID|Client AMP Client ID.|True|String||
|API Key|Cisco AMP API Key.|True|Password|*****|
|Lowest Severity To Fetch|Severity that will be used to fetch events. If nothing is specified, connector will ingest all events. Possible values: Low, Medium, High, Critical.|False|String||
|Fetch Events Without Severity|If enabled, the connector will fetch events that don't have severity. Those events will be assigned "Informational" severity.|False|Boolean|true|
|Max Events To Fetch|How many alerts to process per one connector iteration. Maximum is 1000. Default: 100.|True|Integer|100|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Proxy Server Address|Proxy server address.|False|String||
|Proxy Username|Proxy username.|False|String||
|Proxy Password|Proxy password.|False|Password|*****|
|Verify SSL|If enabled,, verify the SSL certificate for the connection to the Cisco AMP server is valid.|False|Boolean|true|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.