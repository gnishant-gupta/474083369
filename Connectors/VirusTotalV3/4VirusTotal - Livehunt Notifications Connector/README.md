# 4VirusTotal - Livehunt Notifications Connector
Pull information about Livehunt notifications and related files from VirusTotal. Note: this connector requires a premium API token. Dynamic list works with "rule_name" parameter.


Integration: VirusTotalV3

Integration Version: 40.0

Device Product Field: Product Name

Event Name Field: type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|API Key|VirusTotal API Key.|True|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the VirusTotal server is valid.|False|true|
|Engine Whitelist|Specify a comma-separated list of engines that should be used, when counting the \'Engine Percentage Threshold To Fetch\' parameter. Example: AlienVault,Kaspersky. Note: if nothing is provided, all engines from the response are counted.|False||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve notifications from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Notifications To Fetch|How many notifications to process per one connector iteration. Default: 40.|False|40|
|Use dynamic list as a blacklist|If enabled, dynamic lists will be used as a blacklist.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False|http://host.containers.internal:8866|
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Engine Percentage Threshold To Fetch|The percentage of engines that need to mark the file as suspicious/malicious before it's being ingested. Maximum value: 100. Minimum: 0.|True|0|

