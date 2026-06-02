# 55VMware Carbon Black Cloud Alerts Connector
Siemplify VMware Carbon Black Cloud Alerts Connector should be used to ingest alerts from Carbon Black Cloud (Platform) instances. Note that this connector is deprecated and not recommended to use. Consider switching to "VMware Carbon Black Cloud Alerts and Events Baseline Connector" or "VMware Carbon Black Cloud Alerts and Events Tracking Connector"


Integration: CBCloud

Integration Version: 38.0

Device Product Field: ProductName

Event Name Field: type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|300|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|dfj|
|Organization Key|Vmware Carbon Black Cloud Organization Key|True|sdfghj|
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|*****|
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|*****|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify|False||
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|type|
|Proxy Server Address|Proxy server to use for connection.|False||
|Proxy Server Username|Proxy server username|False||
|Proxy Server Password|Proxy server password|False|*****|

