# 24SentinelOne - Threats Connector
Pull threats from SentinelOne.


Integration: SentinelOneV2

Integration Version: 50.0

Device Product Field: siemplify_event

Event Name Field: threatinfo_classification
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|API Root|Address of SentinelOne API root.|True|https://usea1-partners.sentinelone.net/|
|API Token|SentinelOne API token.|True|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Sentinel public cloud server is valid.|False|true|
|Fetch Max Days Backwards|Number of days before the first connector iteration to retrieve threats from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|25|
|Event Object Type Filter|A comma-separated list of event objects that need to be returned alongside threat info. This parameter is used as a filter to only return certain objects. Examples: process,ip,indicators. If nothing is provided, the connector will ingest all event object types.|False||
|Event Type Filter|A comma-separated list of event types that need to be returned alongside threat info. This parameter is used as a filter to only return certain event types. Examples: Process Creation, Behavioral Indicators.|False||
|Max Events To Return|How many events to return per threat. Maximum: 199.|False|199|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|API Version|Specify what version of api to use in the connector. If nothing is provided connector will use version 2.1. Note: Siemplify Event structure is different between API versions. It is recommended to use the latest one. Possible values: 2.0, 2.1.|False|2.0|

