
# Armis

Agentless and passive security that sees, identifies, and classifies every device, tracks behavior, identifies threats, and takes action automatically to protect critical information and systems.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|String|https://{root}|
|API Secret||True|Password|*****|
|Verify SSL||False|Boolean|true|


#### Dependencies
| |
|-|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|tzdata-2026.2-py2.py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|six-1.17.0-py2.py3-none-any.whl|
|arrow-1.4.0-py3-none-any.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Enrich Entities
Enrich entities using information from Armis. Supported entities: IP, Mac Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Endpoint Insight|If enabled, action will create an insight containing information about the endpoints.|False|Boolean|True|



##### JSON Results
```json
[{"Entity": "XX.XXX.XXX.XX", "EntityResult": {"accessSwitch": "XXXX", "category": "XXXXXXX", "dataSources": [], "firstSeen": "XXXX-XX-XXTXX:XX:XX.XXXXXX+XX:XX", "id": "XXXX", "ipAddress": "XX.XXX.XXX.XX", "ipv6": "XXXX", "lastSeen": "XXXX-XX-XXTXX:XX:XX.XXXXXX+XX:XX", "macAddress": "XX:XX:XX:XX:XX:XX", "manufacturer": "XXXXXX", "model": "XXXXXXXXXX", "name": "XXXXXXXXXXX", "operatingSystem": "XXXX", "operatingSystemVersion": "XXXX", "purdueLevel": "X", "riskLevel": "X", "sensor": {"name": "XXXXXXXX", "type": "XXXXXXXXXXX"}, "site": {"location": "XXXXXXXX", "name": "XXXXXXXXXXXXXXX"}, "tags": ["XXX"], "type": "XXXX", "user": "", "visibility": "XXXX"}}]
```



#### List Alert Connections
List connections related to the alert in Armis.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the id of the alert for which you want to pull connections data.|True|String||
|Lowest Severity To Fetch|Specify the lowest severity of the connections that should be used when fetching them.|False|List|Medium|
|Max Connections To Return|Specify how many connections to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"band": null, "channel": null, "dhcpAuthenticationDuration": null, "duration": 12339, "endTimestamp": "2021-04-01T20:19:31.718097+00:00", "id": 1234, "inboundTraffic": 1234, "outboundTraffic": 1234, "protocol": "Bluetooth", "radiusAuthenticationDuration": null, "risk": "Medium", "rssi": null, "sensor": {"name": "AAA", "type": "Switch"}, "site": {"location": "XXXXX", "name": "XXXX HQ"}, "snr": null, "sourceId": 1234, "startTimestamp": "2021-04-01T16:53:52.718097+00:00", "targetId": 1234, "title": "Connection between XXXXX XXXX and XXXX XXX iPhone", "totalAssociationDuration": null, "traffic": 1234, "wlanAssociationDuration": null}]
```



#### Update Alert Status
Update status of the alert in Armis.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the id of the alert for which you want to update status.|True|String||
|Status|Specify what status should be set for the alert.|False|List|Unhandled|



#### Ping
Test connectivity to the Armis with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds









## Connectors
#### Armis - Alerts Connector
Pull alerts with related activities from Armis.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|alert_type|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Armis instance.|True|String|https://{root}|
|API Secret|API Secret of the Armis account.|True|Password|*****|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch alerts. Possible values: Low, Medium, High.|True|String|Low|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Maximum is 1000.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Armis server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.