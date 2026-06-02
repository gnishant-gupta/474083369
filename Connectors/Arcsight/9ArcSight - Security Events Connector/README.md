# 9ArcSight - Security Events Connector
Pull correlations from ArcSight. Note: dynamic list works with "name" parameter. Please refer to the doc portal for the configuration setup. This connector is suitable for Saas deployment of Chronicle SOAR and is the recommended one for production use.


Integration: Arcsight

Integration Version: 45.0

Device Product Field: type

Event Name Field: name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|360|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of the ArcSight instance.|True|https://{ip}|
|Username|Username of the ArcSight account.|True|rty|
|Password|Password of the ArcSight account.|True|*****|
|Report Name|Name of the report that will be used to fetch events.|True|rtyui|
|Fetch Base Events|If enabled, connector will also fetch base events.|False|true|
|Lowest Priority To Fetch|Lowest priority that will be used to fetch events. Possible values are in range 1 to 10. If nothing is provided, all events will be ingested.|False||
|Max Events To Fetch|How many alerts to process per one connector iteration. Maximum is 1000.|False|100|
|Use dynamic list as a blocklist|If enabled, dynamic lists will be used as a blocklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ArcSight server is valid.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

