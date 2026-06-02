# 23SentinelOne - Alerts Connector
Pull alerts from SentinelOne. Dynamic List works with the “ruleInfo.name” parameter.


Integration: SentinelOneV2

Integration Version: 50.0

Device Product Field: Product Name

Event Name Field: ruleInfo_name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Max Hours Backwards|Amount of hours from where to fetch alerts.|True|24|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Script Timeout (Seconds)|The timeout limit in seconds for the python process running the current script.|True|180|
|API Root|Address of SentinelOne API root.|True|eertyui|
|API Token|SentinelOne API token.|True|*****|
|Status Filter|Comma-separated list of status that should be ingested. Possible values: Unresolved, In Progress, Resolved. If nothing is provided, the connector will fetch alerts with statuses Unresolved and InProgress.|False|Unresolved, In Progress|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False||
|Alert Name Template|If provided, connector will use this value for Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Lowest Severity To Fetch|Lowest severity of the alerts to fetch. If nothing is provided, the connector will ingest alerts with all severities. Possible Values: Info, Low, Medium, High, Critical.|False||
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Maximum: 100.|True|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|true|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the SentinelOne server is valid.|False|true|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

