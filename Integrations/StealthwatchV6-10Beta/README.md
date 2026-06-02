
# StealthwatchV6-10Beta

Cisco Stealthwatch provides pervasive network visibility and sophisticated security analytics for advanced protection across the extended network and cloud.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|None|https://x.x.x.x|
|Username|None|True|String||
|Password|None|True|Password|*****|



## Actions
#### Search Flows
Get flows by IP address for a given time frame
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Timeframe|Time frame in hours(e.g: 3).|True|String||
|Limit|The limit of the recieved flow.|True|String||
|Tenant ID|Tenant in which the search should be performed.|False|String||
|IP Address|Comma-separated list of IPs that need to be searched. Note: this parameter will be used together with IP entities.|False|String||
|Start Time|Timestamp that will be used together with "Timeframe" parameter to generate the time for the search. If nothing is provided, action will use current time. Format: ISO8601|False|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds









