# 33AlienVault USM Anywhere Connector
AlienVault USM Anywhere Connector


Integration: AlienVaultAnywhere

Integration Version: 35.0

Device Product Field: device_product

Event Name Field: message_plugin
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Server Address|The address of the proxy server to use.|False||
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|60|
|Api Root|e.g. https://<instance>.alienvault.com|True|hgfd|
|ClientID|ClientID|True|hgfd|
|Secret|Secret|True|*****|
|Product Version|AlienVault Anywhere version - V1, V2|True|V2|
|Verify SSL|Indicate whether to use SSL in the session or not|False|false|
|Max Alerts Per Cycle|Limit the number of alerts in every cycle. e.g. 10|True|10|
|Max Days Backwards|This field is used in the connector first running cycle and determine the start time. e.g. 3|True|1|
|Padding Period|Padding period (hours) for the connector execution.|False|0|
|Show Suppressed|Whether to include suppressed alarms in the search|False|true|
|Use Suppressed Filter|This parameter will be used to determine whether to filter the incoming alerts using the "Show Suppressed" filter or not.|False|true|
|Priority|Filter by alarm priority, comma separated. Valid value: high/medium/low.|False||
|Rule Intent|Filter alarms by the purpose of the alarm. The intent describes the context of the behavior that is being observed. These are the threat categories: System Compromise, Exploitation & Installation, Delivery & Attack, Reconnaissance & Probing, Environmental Awareness|False||
|Rule Strategy|The strategy of the rule that triggered the alarm. For example, use Client-Side Attack - Known Vulnerability when trying to exploit a known vulnerability in a web browser the attacker|False||
|Rule Method|Filter alarms by rule method. The method would provide additional detail on the target of the attack and the particular vulnerability. e.g. Firefox - CVE-2008-4064|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

