# 12Crowdstrike Falcon Streaming Events Connector
Crowdstrike Falcon Streaming Events Connector


Integration: CrowdStrikeFalcon

Integration Version: 76.0

Device Product Field: device_product

Event Name Field: Name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Proxy Username|Proxy username.|False||
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|600|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.|False||
|API Root|API root of the Crowdstrike instance|False|https://api.crowdstrike.com|
|Client ID|Client ID for Crowdstrike API|True|rtyjhkl|
|Client Secret|Client Secret for Crowdstrike API|True|*****|
|Event types|Specify a comma-separated list of event types. Examples of the event types: DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent. For more information visit documentation portal.|False|DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent|
|Max Events per Cycle|Max events to process per connector run.|True|100|
|Max Day Backwards|Number of days before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|3|
|Min Severity|Specify the events that should be ingested based on the events severity (detections events). The value ranges from 0-5. If other event types besides detections are ingested by the connector, connector sets a severity for them as -1 and this filter is not applied to those types of events|False|0|
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Rule Generator Template|	

If provided, the connector will use this value for Siemplify Rule Generator. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use the first Siemplify event for placeholders. Only keys that have string value will be handled. If nothing is provided or the user provides an invalid template, the connector will use the default rule generator.|False||
|Proxy Server Address|Proxy server address.|False||
|Proxy Password|Proxy password.|False|*****|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|false|
|Verify SSL|Indicate whether to use SSL in the session or not|False|false|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False||

