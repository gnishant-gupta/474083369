
# Attivo

Efficiently derail attacker discovery, lateral movement, privilege escalation, & collection activities early in the attack cycle with Attivo.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|String|https:/{{ip address}}|
|Username||True|String||
|Password||True|Password|*****|
|Verify SSL||False|Boolean|True|


#### Dependencies
| |
|-|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### List Critical ThreatPath
List available critical ThreatPaths in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter critical paths.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|



##### JSON Results
```json
[{"destIp": "172.30.xxx.xxx", "permissionId": -1, "reason": null, "srcHostName": "Unmanaged host", "acmId": -1, "source": null, "type": "Paths", "permScore": "Medium", "cancellable": false, "targetScore": "Medium", "crRuleName": "System Default: Domain Admin Pilferage", "credOuPath": "CN=Users,DC=exlab,DC=local", "submissionId": -1, "credAcctStatus": "Enabled", "credential": "exlab.local\\administrator", "srcId": "dummy-endpoint-1SUB1", "destHostName": "HOST02SMIME", "cid2": "rdp1", "id": "Unmanaged host172.16.30.5HOST02SMIME172.30.201.198RDP Memory Credentialexlab.local\\administratorPaths", "srcIp": "172.16.xxx.xxx", "firstSeen": 1636667535105, "credDept": null, "subscriberId": 1, "remediable": false, "credLastPswResetTime": 1620201383000, "credLastLogonTime": 1636729127000, "moretarget": false, "destId": "27f018b6-47c8-4b20-ab62-545c672ddf7cHOST02SMIME:S-1-5-21-2143737273-3756110848-2070699859-500", "shareName": null, "desc": "rdp Active logon session for exlab.local\\administrator at Unmanaged OU/172.16.30.5 (unmanaged host). Potential movement to Computers/HOST02SMIME.", "cid": "rdp0", "permissionName": "", "destOu": "Computers", "critical": true, "isgrouppath": false, "credUpn": "Administrator@exlab.local", "credCreatedTime": 1610374114000, "memberList": null, "memberOf": null, "remediateStatus": null, "severity": "High", "srcOu": "Unmanaged", "target": "HOST02SMIME(172.30.201.198)", "loggedOn": false, "credSamAcctName": "Administrator", "service": "RDP Memory Credential", "credDisplayName": null, "ukey": null, "category": "Saved credential"}]
```



#### Enrich Entities
Enrich entities using information from Attivo. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Include ThreatPaths|If enabled, action will return information about ThreatPaths related to the entity.|False|Boolean|true|
|Include Vulnerabilities|If enabled, action will return information about vulnerabilities related to the entity.|False|Boolean|true|
|Include Credential Info|If enabled, action will return information about credential information related to the entity.|False|Boolean|true|
|Create Insights|If enabled, action will create an insight containing all of the retrieved information about the entity.|False|Boolean|true|
|Max ThreatPaths To Return|Specify how many ThreatPaths to return per entity. Default: 50.|False|String|50|
|Max Vulnerabilities To Return|Specify how many vulnerabilities to return per entity. Default: 50.|False|String|50|
|Max Credentials To Return|Specify how many credentials to return per entity. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Entity": "HOSTxxxxxx", "EntityResult": {"upgradeToVersion": null, "quarantineStatus": 0, "acmId": -1, "tostatus": 0, "systemtype": "VM", "adsErrorMessage": "", "accessprotection": false, "functionalId": {"templateName": null, "usersid": null, "errorCode": 0, "debugInfo": "", "userName": "exlab.local\\Administrator", "status": null, "timestamp": 1636558715000}, "ondAssigned": false, "usersInfo": [{"templateName": "Default_ThreatStrike_Profile:2", "usersid": "S-1-5-21-2143737273-3756110848-xxxxxxxxx", "errorCode": 0, "debugInfo": "Error:0 lsass UnInstallation\\nError:0 webftp UnInstallation\\nError:0 cookies UnInstallation\\nError:0 mstsc UnInstallation\\nError:0 SMB UnInstallation\\nError:0 Web Credential UnInstallation\\nError:0 outlook UnInstallation\\nError:0 iexplorer UnInstallation\\nError:0 Putty UnInstallation\\nError:0 Mozilla UnInstallation\\nError:0 Chrome UnInstallation\\nError:0 FileZilla UnInstallation\\nError:0 lsass UnInstallation\\nError:0 AWS UnInstallation\\nError:0 Telnet UnInstallation\\nError:0 OracleDBClient UnInstallation\\nError:0 IEFavorite UnInstallation\\nError:0 WindowsDNS UnInstallation\\nError:0 RasVPN UnInstallation", "userName": "exlab.local\\Administrator", "status": "INSTALLED", "timestamp": 1636558727000}], "id": 101, "epVersion": "5.0.1.25", "activeDirectory": {"groups": ["Domain Computers"], "organizationalUnit": "Computers"}, "installMode": 2, "processor_arch": " 64-bit", "tdDeflectMessage": "", "clientGroupId": "ThreatStrike-Default-Client", "deployMode": 0, "latestExecutableStatus": "INSTALLED", "subscriberId": 1, "botsinkDocumentId": 0, "executableStatus": [{"timestamp": 1636558715000, "status": "INSTALLED"}], "processor_cpuSpeed": "2300 MHz", "guid": "27f018b6-47c8-4b20-ab62-xxxxxxxxxx", "ondMessage": "", "debugCollect": false, "ondInActive": false, "adsstatus": 1, "upgradeRequired": false, "ondstatus": 0, "hostName": "HOSTxxxxxxx", "memory": "8190 MB", "lastModifiedTime": "2021-11-11T15:41:16.254Z", "arstatus": 1, "dnsName": "exlab.local", "botsinkDeviceId": 0, "endpoint_os_type": 1, "disabledInClientGroup": false, "tddstatus": 1, "adsenabled": false, "tdDeflectStatus": 0, "osType": "Non-Server", "featuresstatusforusers": [{"tddstatus": 1, "tsstatus": 1, "tostatus": 0, "usersid": "S-1-5-21-2143737273-3756110848-xxxxxxxxx", "adsstatus": 1, "logIn": 1636558717, "ondstatus": 0, "logOut": 0, "tpstatus": 1, "live": true, "username": "exlab.local\\Administrator"}], "interfaces": [{"subnet": "172.30.xx.xxxx", "score": 1400.133919820602, "macAddress": "00:50:56:xx:xx:xxx", "ipAddress": "172.30.xx.xxx", "name": "Intel(R) 82574L Gigabit Network Connection", "type": "Wired", "timestamp": 1636645218000}], "migrateCL": false, "debugStatus": false, "osName": "Windows 10 64-bit", "uptime": "134836", "tsstatus": 1, "processor_numOfCpu": 4, "newClientGroup": null, "tpstatus": 1, "threatPaths": [{"destIp": "172.30.xx.xx", "permissionId": -1, "reason": null, "srcHostName": "Unmanaged host", "acmId": -1, "source": null, "type": "Paths", "permScore": "Medium", "cancellable": false, "targetScore": "Medium", "crRuleName": "System Default: Domain Admin Pilferage", "credOuPath": "CN=Users,DC=exlab,DC=local", "submissionId": -1, "credAcctStatus": "Enabled", "credential": "exlab.local\\administrator", "srcId": "dummy-endpoint-1SUB1"}], "vulnerabilities": ["More than two Administrators were found on this computer", "Presence of local administrative privileges for domain user account"], "credentials": [{"isDeceptive": true, "service": "putty", "domain": "EXLAB-W10H66.exlab.local\\accessDBuser", "serverIp": "EXLAB-W10H66.exlab.local", "isShortcut": false}, {"isDeceptive": true, "service": "putty", "domain": "EXLAB-W10H77.exlab.local\\accessDBadm", "serverIp": "EXLAB-W10H77.exlab.local", "isShortcut": false}]}}]
```



#### Ping
Test connectivity to the Attivo with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Vulnerability Hosts
List hosts related to the vulnerability in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vulnerabilities|Specify a comma-separated list of vulnerabilities for which action needs to return hostnames.|True|String||
|Max Hosts To Return|Specify how many hosts to return. If nothing is provided, action will return 50 hosts.|False|String|50|



##### JSON Results
```json
[{"vulnerability": "Vulnerability Name", "hostNames": ["host_1", "host_2"]}]
```



#### Update Event
Update event in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID of the event, which needs to be updated.|True|String||
|Status|Specify the status for the event.|False|List|Select One|
|Comment|Specify a comment that needs to be added to the event.|False|String||



#### List Service ThreatPaths
List ThreatPaths related to services in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Services|Specify a comma-separated list of services for which action needs to return ThreatPaths.|True|String||
|Max ThreatPaths To Return|Specify how many ThreatPaths to return. If nothing is provided, action will return 50 ThreatPaths.|False|String|50|



##### JSON Results
```json
[{"service": "Web", "paths": [{"destIp": "172.30.xxx.xxx", "permissionId": -1, "reason": null, "srcHostName": "Unmanaged host", "acmId": -1, "source": null, "type": "Paths", "permScore": "Medium", "cancellable": false, "targetScore": "Medium", "crRuleName": "System Default: Domain Admin Pilferage", "credOuPath": "CN=Users,DC=exlab,DC=local", "submissionId": -1, "credAcctStatus": "Enabled", "credential": "exlab.local\\administrator", "srcId": "dummy-endpoint-1SUB1", "destHostName": "HOST02SMIME", "cid2": "rdp1", "id": "Unmanaged host172.16.30.5HOST02SMIME172.30.201.198RDP Memory Credentialexlab.local\\administratorPaths", "srcIp": "172.16.xxx.xxx", "firstSeen": 1636667535105, "credDept": null, "subscriberId": 1, "remediable": false, "credLastPswResetTime": 1620201383000, "credLastLogonTime": 1636729127000, "moretarget": false, "destId": "27f018b6-47c8-4b20-ab62-545c672ddf7cHOST02SMIME:S-1-5-21-2143737273-3756110848-2070699859-500", "shareName": null, "desc": "rdp Active logon session for exlab.local\\administrator at Unmanaged OU/172.16.30.5 (unmanaged host). Potential movement to Computers/HOST02SMIME.", "cid": "rdp0", "permissionName": "", "destOu": "Computers", "critical": true, "isgrouppath": false, "credUpn": "Administrator@exlab.local", "credCreatedTime": 1610374114000, "memberList": null, "memberOf": null, "remediateStatus": null, "severity": "High", "srcOu": "Unmanaged", "target": "HOST02SMIME(172.30.201.198)", "loggedOn": false, "credSamAcctName": "Administrator", "service": "RDP Memory Credential", "credDisplayName": null, "ukey": null, "category": "Saved credential"}]}]
```









## Connectors
#### Attivo - Events Connector
Pull events from Attivo into Siemplify. Note: whitelist works with attackName parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|attackName|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Attivo instance.|True|String|https:/{{ip address}}|
|Username|Attivo API Username.|True|String||
|Password|Attivo API Password.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Attivo server is valid.|False|Boolean|true|
|Lowest Severity To Fetch|Severity that will be used to fetch events. If nothing is specified, action will ingest all events. Possible values: System Activity, Very Low, Low, Medium, High, Very High.|False|String|Medium|
|Status Filter|Status filter for the connector. Possible values: unacknowledged, acknowledged, all.|True|String|All|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve events from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.|False|Integer|1|
|Max Events To Fetch|How many events to process per one connector iteration. Maximum is 1000. Default: 100.|False|Integer|100|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.