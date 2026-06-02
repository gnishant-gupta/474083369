# 22Microsoft Sentinel Incident Tracking Connector
Connector works with Microsoft Azure Sentinel incidents and fetches updates to the Sentinel incidents as the new SecOps alerts. Connector's Dynamic List can be used to specify the incidents names that needs to be fetched. It is recommended to configure SecOps Alerts grouping based on SourceGroupIdentifier for this connector. See connector documentation for more information.


Integration: MicrosoftAzureSentinel

Integration Version: 62.0

Device Product Field: product_type

Event Name Field: event_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Use dynamic list as a blocklist|If enabled, dynamic list will be used as a blocklist.|False|false|
|Incidents Tags To Ingest|Specify a comma separated list of tags Sentinel incident should have to be ingested. Incidents that will not have tags from this list will be ignored. Example of how Sentinel tags can be provided: tag1, tag2|False||
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|480|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|.*|
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|nhgfds|
|Entra ID Directory ID|Azure Entra ID Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|gfds|
|Api Root|Management.azure.com Api root url to use with integration.|True|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|https://login.microsoftonline.com|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|gfd|
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|gfdsah|
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|gfds|
|Client Secret|Secret that was entered for Azure AD app registration.|True|*****|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|true|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.|True|New,  Active, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the SecOps server. Parameter can take multiple values as a comma separated string.|True|Informational, Low, Medium, High|
|Max Incidents per Cycle|How many incidents should be processed during one connector run.|True|10|
|Use the same approach with event creation for all alert types?|By default connector uses a different approach with Scheduled Alert or NRT types of alerts - it tries to fetch events that caused the alert by running the query specified in alert details. Specify whether to change this behavior and use the same approach for the scheduled and NRT alerts as for other alert types.|False|false|
|Backlog Expiration Timer|Time frame in minutes for connector to keep incidents in backlog for.|True|60|
|StartTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Start Time" alert field in descending order. Additionally, new "SecOps_Start_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.|True|properties_firstActivityTimeGenerated,properties_startTimeUtc,properties_createdTimeUtc,properties_firstAlertTimeGenerated|
|EndTimeFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "End Time" alert field in descending order. Additionally, new "SecOps_End_Time" attribute will be added to created events. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on. If none of the fallback fields are found, connector will use createdTimeUTC, and if that's also non existent - alert ingestion time to SecOps.|True|properties_lastActivityTimeGenerated,properties_endTimeUtc,properties_createdTimeUtc,properties_lastAlertTimeGenerated|
|Enable Fallback Logic Debug?|Specify if connector should add to the created events a "debug" fields that will contain the values it used for fallback.|False|false|
|VendorFieldFallback|Specify a comma separated list of incident attributes that should be used as a fallback for the "DeviceVendor" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|vendorName|
|ProductFieldFallback|Specify a comma separated list of incident or alert attributes that should be used as a fallback for the "Product Field Name" parameter and "DeviceProduct" field in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|ProductName|
|EventFieldFallback|Specify a comma separated list of alert attributes that should be used as a fallback for the "Event Field Name" parameter in descending order. First attribute will have the highest priority, next if its not present or empty in the event - fallback to the next value from the list and so on.|True|kind|
|Max Backlog Incidents per cycle|How many incidents  connector should try to fetch from the backlog during one connector run.|True|10|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|false|
|Total number of Scheduled Alerts Events Limit to Ingest|Specify the total number of events the connector should ingest for a Microsoft Sentinel incident that is based on a Scheduled or NRT alert. Connector ‘counts’ events in all corresponding SecOps alerts created for the Microsoft Sentinel Incident and no new events will be ingested once this limit is reached.|False|100|
|Create Chronicle SOAR Alerts for Sentinel incidents that do not have entities?|If enabled, connector will create SecOps alerts from Microsoft Sentinel incidents that dont have entities. Otherwise, such incidents will be skipped for all Sentinel incidents types except Sentinel Scheduled and NRT alerts.|False|false|
|Incidents Padding Period (minutes)|If specified, to get incidents returned not in chronological order, connector will fetch Sentinel incidents from this value backwards in time.|False|60|
|Alert Name Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Alert Name. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [title]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Rule Generator Template|If specified, connector will use this value from the Microsoft Azure Sentinel API response for incident data for Chronicle SOAR Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: Sentinel incident - [severity]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False||
|How many hours to track ingested incident for updates|Specify how long connector should track already ingested Sentinel incident for updates - either addition of new events or entities and incident details.|True|24|
|Proxy Server Address|Proxy server to use for connection.|False||
|Proxy Username|Proxy server username.|False||
|Proxy Password|Proxy server password.|False|*****|
|Create extra events for all entities|If enabled, when creating entities from the Sentinel API, connector will create extra SecOps events for all Sentinel incident's entities, not only Account, Mailbox, Host or Ip.|False|false|
|Wait For Scheduled/NRT Alert Object|If enabled, the connector will wait until a Scheduled/NRT alert object will be available.|False|false|

