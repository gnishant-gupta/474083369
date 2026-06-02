# 48VMware Carbon Black Cloud Alerts and Events Tracking Connector
Fetch Carbon Black Cloud Alerts and Events as Events are added to Carbon Black Cloud Alerts. Connector can create multiple Siemplify alerts for single Carbon Black Cloud Alert, if Cloud Alert was updated with new events after initial ingestion by Siemplify.


Integration: CBCloud

Integration Version: 38.0

Device Product Field: ProductName

Event Name Field: event_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|sdfghj|
|Organization Key|Vmware Carbon Black Cloud Organization Key, Eg. 7DDDD9DD|True|dfghjk|
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|*****|
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|*****|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|100|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify, for example, 4 or 7|False||
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|type|
|Alert Reputation to Ingest|What Carbon Black Cloud alert reputation alert can have to be ingested. Parameter accepts multiple values as a comma separated string. If "N/A" is provided, connector will ingest alerts without reputation.|False||
|Events Padding Period (hours)|Specify how many hours connector should track new events for already ingested alert.|True|24|
|Events Limit to Ingest per Alert|Specify how many events can be ingested per single CB Cloud alert per Connector iteration.|True|25|
|Total Limit of Events per Alert|Specify a total number of events connector should get per single CB Cloud alert. If this limit is reached, no new events will be fetched for alert. In order to not limit the total number of events, please leave this parameter empty.|False|100|
|Max Backlog Alerts per Cycle|How many alerts connector should try to fetch from the backlog during one connector run.|True|10|
|Alerts Backlog Timer|Time frame in minutes for which connector should try to fetch again the alerts from backlog it previously failed to process.|True|60|
|Proxy Server Address|Proxy server to use for connection.|False||
|Proxy Server Username|Proxy server username|False||
|Proxy Server Password|Proxy server password|False|*****|
|Watchlist Name Filter|If provided, for CB Cloud alerts with the type “Watchlist“ ingest only that were triggered by the respective whatchlist. Parameter accepts multiple values as a comma separated string. If nothing is specified - ingest everything regardless of watchlist name.|False||
|Alert Name Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Alert Name. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD Alert - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Rule Generator Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False||

