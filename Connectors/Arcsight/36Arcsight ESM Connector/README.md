# 36Arcsight ESM Connector
Arcsight ESM Connector


Integration: Arcsight

Integration Version: 45.0

Device Product Field: device_product

Event Name Field: name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|500|
|Server Address|Server address of the ArcSight instance|True|jhgfd|
|Username|Username of the ArcSight account|True|jhgfd|
|Password|Password of the ArcSight account|True|*****|
|Events Count Limit|How many events to process per one alert|True|15|
|Cases Folder Path|Absolute path to cases. Example: /opt/Correlations|True|/opt/Correlations|
|Alerts Count Limit|How many alerts to process per one iteration|True|10|
|Environment Field Name|The name of the environment's field. e.g. event.CustomerURI|True|event.CustomerURI|
|Secondary Device Product Field|Secondary field for Device Product|False||
|Alert Custom Fields Names|Additional fields that should be added to Siemplify Alert. Example: source_address|False||
|Done files retention days|For how many days to leave files in the “Done” folder |True|3|
|Error files retention days|For how many days to leave files in the “Error” folder|True|14|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ArcSight ESM server is valid.|False|false|
|CA Certificate File|Base 64 encoded CA certificate file.|False||

