
# Arcsight

Real-time threat detection and automated response backed by a powerful, open, and intelligent SIEM (Security Information and Event Management).

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{IP_ADDR}:{PORT}|
|User name|None|True|String||
|Password|None|True|Password|*****|
|CA Certificate File|None|False|String||
|Verify SSL|None|False|Boolean|false|


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|TIPCommon-1.0.16-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|netaddr-1.3.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|simplejson-3.19.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Get Report
Get details about report in ArcSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report Full Path (URI)|Specify the URI to the report. Example: /All Reports/ArcSight Foundation/MITRE ATT&CK/Mitre ATT&CK Summary|True|String|None|
|Field 2|The dynamic fields for the query to generate the report|False|String|None|
|Field 3|The dynamic fields for the query to generate the report|False|String|None|
|Field 4|The dynamic fields for the query to generate the report|False|String|None|
|Field 5|The dynamic fields for the query to generate the report|False|String|None|
|Field 6|The dynamic fields for the query to generate the report|False|String|None|
|Field 7|The dynamic fields for the query to generate the report|False|String|None|
|Field 8|The dynamic fields for the query to generate the report|False|String|None|
|Field 9|The dynamic fields for the query to generate the report|False|String|None|
|Field 10|The dynamic fields for the query to generate the report|False|String|None|



##### JSON Results
```json
[{"Target_Zone_URI": "", "Target_Address": "", "SumAggregated_Event_Count": "734"}, {"Target_Zone_URI": "/All Zones/ArcSight System/Private Address Space Zones/RFC1918: 172.16.x.x-172.31.x.x", "Target_Address": "172.30.x.x", "SumAggregated_Event_Count": "93946"}]
```



#### Add Entries To Activelist
Add new entry to active list in ArcSight. Column values are separated by delimiter ‘|' and entries are separated by ‘;’ in parameter ‘Entries’. Column names are separated by delimiter ‘;’ in parameter ‘Columns’. You can also use Entries JSON instead of ‘Columns’ + 'Entries’“.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Columns|Specify the name of the columns, where you want to put values for the entries. Format: Column_name1;Column_name2|False|String||
|Entries|Specify the entries. Format entry1_value1|entry1_value2;entry2_value1|entry2_value2|False|String||
|Active List UUID|Specify the UUID of the active list, where you want to add new entries. Note: parameter “Active list UUID“ takes priority over “Active list name“. Example: HLZRc9yYBABC-lHtlf3-f0Q==|False|String||
|Active list name|Specify the name of the active list, where you want to add new entries. Note: parameter “Active list UUID“ takes priority over “Active list name“.|False|String||
|Entries JSON|Specify a list of JSON objects that contain information about the entry. Note: Combination of ‘Columns' and ‘Entries’ parameters have priority over 'Entries JSON’. Format: [{"Column_1": "Value_1", "Column_2": "Value_2"}, {"Column_1": "Value_3", "Column_2": "Value_4"}]|False|String||



#### Add Entities To Active List
Add entities to the active list in ArcSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Active List Name|Specify the name of the active list to which you want to add entities.|True|String||
|Entity Column|Specify the name of the column, where entity value should be put.|True|String||
|Additional Fields|Specify additional fields that should be added alongside the entity in the active list. Format is a JSON object. Example: {"Column_1": "Value_1","Column_2": "Value_2"}|False|String||



#### Get Query Results
Get results for the provided query in ArcSight
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query ID|Specify the ID of the query for which you want to return results. Note: parameter “Query ID“ takes priority over “Query Name“. Example: cyUJKRz4BABCFwS9iFPq+aA==|False|String||
|Max Items To Return|Specify how many items to return in the response.|False|String|100|
|Query Name|Specify the name of the query for which you want to return results. Note: parameter “Query ID“ takes priority over “Query Name“.|False|String||



##### JSON Results
```json
[{"Target User Name": "user", "Attacker Address": "1.1.1.1", "External ID": "127", "Name": "A Kerberos authentication ticket (TGT) was requested.", "Target Address": "1.1.1.1", "Connector Information": "172.30.xx.xx|Manager Internal Agent|RFC1918: 172.16.0.0-172.xx.xx.xx", "Priority": "3", "Total": "7"}, {"Target User Name": "user", "Attacker Address": "1.1.1.1", "External ID": "127", "Name": "A Kerberos authentication ticket (TGT) was requested.", "Target Address": "1.1.1.1", "Connector Information": "172.30.xx.xx|Manager Internal Agent|RFC1918: 172.16.0.0-172.xx.xx.xx", "Priority": "3", "Total": "7"}]
```



#### Change Case Stage
Update the stage of the case in ArcSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Case Name|Specify the name of the case for which you want to update the stage.|True|String||
|Stage|Specify a new stage for the case. Possible values: INITIAL, QUEUED, CLOSED, FINAL, and FOLLOW_UP.|True|String||



#### Get Activelist Entries
Retrieve active list entries in ArcSight
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Active list UUID|Specify the UUID of the active list for which you want to retrieve entries. Note: parameter “Active list UUID“ takes priority over “Active list name“. Example: HLZRc9yYBABC-lHtlf3-f0Q==|False|String||
|Active list name|Specify the name of the active list for which you want to retrieve entries. Note: parameter “Active list UUID“ takes priority over “Active list name“.|False|String||
|Map Columns|If enabled, action will map columns to the values in the JSON result.|False|Boolean|false|
|Max Entries To Return|Specify how many entries to return.|False|String||



##### JSON Results
```json
[{"Name":"hash","ResourceType":"ad","Path":"dsa","StartTime":"asd","EventClassID":"dsa","Status":"sasd","Duration":"sad"}]
```



#### List Resources
List available queries in ArcSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Return Active Lists|If enabled, action will return available active lists.|False|Boolean|true|
|Return Queries|If enabled, action will return available queries|False|Boolean|true|
|Return Cases|If enabled, action will return available cases.|False|Boolean|false|
|Return Reports|If enabled, action will return available reports.|False|Boolean|false|
|Max Resources To Return|Specify how many resources to return per type.|False|String|50|



##### JSON Results
```json
{"active_lists":[{"attributeInitializationInProgress":false,"contentVersionID":"AAAXXXX-kXXXT2e","createdTime":{"day":8,"hour":16,"milliSecond":375,"minute":32,"month":6,"second":54,"timezoneID":"Europe/Sofia","year":2020},"createdTimestamp":1594215174375,"creatorName":"admin","deprecated":false,"description":"Description......","disabled":false,"inCache":true,"inactive":false,"initialized":true,"isAdditionalLoaded":false,"localID":254844649434,"modificationCount":1,"modifiedTime":{"day":8,"hour":16,"milliSecond":754,"minute":33,"month":6,"second":10,"timezoneID":"Europe/Sofia","year":2020},"modifiedTimestamp":1594215190754,"modifierName":"admin","name":"Name XXXXXXX","reference":{"id":"H5wtzXXXXXXXRe9YMg==","isModifiable":true,"managerID":"TneiLnMBXXXXXXV4PFAXg==","referenceName":"ActiveList","referenceString":"<Resource URI=\"/XXXXXXXX\" ID=\"H5wtztCoXXXXXXXfXRe9YMg==\"/>","referenceType":24,"uri":"/XXXXXXX"},"resourceid":"H5wtztXXXXXXXfXRe9YMg==","state":2,"type":24,"typeName":"ActiveList","URI":"/XXXXXXX","versionID":"AAAXXXX-kXXXT2e","activeListType":"FIELD_BASED","capacity":10000,"caseSensitiveType":"CASE_SENSITIVE","entryTimeToLive":604800000,"fieldNames":["ConnectorName","AverageEPS"],"fieldSubTypes":[{"@xsi.nil":"true"},{"@xsi.nil":"true"}],"fieldTypes":["String","Double"],"keyFields":[true,false],"multiMap":false,"optimizeData":false,"partialCache":false,"timePartitioned":false}],"queries":[{"attributeInitializationInProgress":false,"createdTime":{"day":8,"hour":16,"milliSecond":191,"minute":32,"month":6,"second":55,"timezoneID":"Europe/Sofia","year":2020},"createdTimestamp":1594215175191,"creatorName":"admin","deprecated":false,"description":"This query viewer displays data on connectors that have filled their caches to the point that they are dropping events. This query viewer queries on an active list that is maintained by the Connector Monitoring content (rules), so it can update every minute.","disabled":false,"inCache":true,"inactive":false,"initialized":true,"isAdditionalLoaded":false,"localID":515148412151,"modificationCount":1,"modifiedTime":{"day":8,"hour":16,"milliSecond":775,"minute":33,"month":6,"second":20,"timezoneID":"Europe/Sofia","year":2020},"modifiedTimestamp":1594215200775,"modifierName":"admin","name":"XXXXXXXXXXXXXXX","reference":{"id":"c05DPpy4XXXXXXXml6MSoA==","isModifiable":true,"managerID":"TneiLnMBXXXXXXXXXPFAXg==","referenceName":"QueryViewer","referenceString":"<Resource URI=\"/All XXXXXXXXXXXts\" ID=\"c05DPpy4XXXXXXXml6MSoA==\"/>","referenceType":51,"uri":"/All XXXXXXXXXXXts"},"resourceid":"c05DPpy4XXXXXXXml6MSoA==","state":2,"type":51,"typeName":"QueryViewer","URI":"/All XXXXXXXXXXXts","versionID":"AAAXXXX-kXXXT2e","enabled":true,"supportsToggle":false,"columnAliasMap":{"entry":[{"key":"CacheSize","value":"Cache Size"},{"key":"ConnectorType","value":"Connector Type"},{"key":"CurrentDroppedCount","value":"Current Dropped Count"},{"key":"ConnectorName","value":"Connector Name"},{"key":"ConnectorURI","value":"ConnectorURI"},{"key":"ConnectorHostName","value":"Connector Host Name"},{"key":"DroppedCount","value":"Dropped Count"}]},"data":{"endTimestamp":1607427783684,"startTimestamp":1607427783684,"timestamp":1607427942720,"colHeaderTS":1607427942720,"columnHeaders":["Connector Name","Connector Type","Connector Host Name","Cache Size","Dropped Count","Current Dropped Count","ConnectorURI"],"maxColumns":0,"properties":""},"queryViewerId":"c05DPpyXXXXXXml6MSoA==","refreshInterval":60000}],"cases":[{"attributeInitializationInProgress":false,"createdTime":{"day":23,"hour":12,"milliSecond":536,"minute":39,"month":11,"second":17,"timezoneID":"Europe/Sofia","year":2020},"createdTimestamp":1608719957536,"creatorName":"admin","deprecated":false,"disabled":false,"inCache":true,"inactive":false,"initialized":true,"isAdditionalLoaded":false,"localID":548484515164,"modificationCount":0,"modifiedTime":{"day":23,"hour":12,"milliSecond":536,"minute":39,"month":11,"second":17,"timezoneID":"Europe/Sofia","year":2020},"modifiedTimestamp":1608719957536,"modifierName":"admin","name":"Case1","reference":{"id":"7+Eouj3YXXXXXXXXpxa5bNQ==","isModifiable":true,"managerID":"TneiLnMBXXXXXXXXXPFAXg==","referenceName":"Case","referenceString":"<Resource URI=\\\"XXXXXXXXXXX\" ID=\\\"7+Eouj3YXXXXXXXXpxa5bNQ==\\\"/>","referenceType":7,"uri":"/XXXXXCasesXXXX"},"resourceid":"7+Eouj3YXXXXXXXXpxa5bNQ==","state":2,"type":7,"typeName":"Case","URI":"/XXXXXCasesXXXX","action":"BLOCK_OR_SHUTDOWN","actionsTaken":"","affectedElements":"D","affectedServices":"A","affectedSites":"B","associatedImpact":"AVAILABILITY","attackAddress":"","attackAgent":"INSIDER","attackImpact":"","attackLocationID":"","attackMechanism":"PHYSICAL","attackNode":"","attackOS":"","attackProgram":"","attackProtocol":"","attackService":"","attackTarget":"","conclusions":"","consequenceSeverity":"NONE","displayID":2,"estimatedImpact":"C","finalReportAction":"","followupContact":"","frequency":"NEVER_OR_ONCE","history":"KNOWN_OCCURENCE","incidentSource1":"","incidentSource2":"","inspectionResults":"","numberOfOccurences":0,"operationalImpact":"NO_IMPACT","plannedActions":"","recommendedActions":"","recordedData":"","reportingLevel":0,"resistance":"HIGH","securityClassification":"UNCLASSIFIED","securityClassificationCode":"P I D U A B ","sensitivity":"UNCLASSIFIED","sourceAddress":"","stage":"QUEUED","ticketType":"INTERNAL","vulnerability":"DESIGN","vulnerabilityData":"","vulnerabilityEvidence":"","vulnerabilitySource":"","vulnerabilityType1":"ACCIDENTAL","vulnerabilityType2":"EMI_RFI"}],"reports":[{"attributeInitializationInProgress":false,"createdTime":{"day":8,"hour":16,"milliSecond":316,"minute":32,"month":6,"second":53,"timezoneID":"Europe/Sofia","year":2020},"createdTimestamp":1594215173316,"creatorName":"admin","deprecated":false,"description":"This report shows nXXXXXXXX within the last 24 hours.","disabled":false,"inCache":true,"inactive":false,"initialized":true,"isAdditionalLoaded":false,"localID":1515152164163,"modificationCount":1,"modifiedTime":{"day":8,"hour":16,"milliSecond":181,"minute":33,"month":6,"second":9,"timezoneID":"Europe/Sofia","year":2020},"modifiedTimestamp":1594215189181,"modifierName":"admin","name":"New DXXXXXXXX - Last 24 Hours","reference":{"id":"9025mTEXXXXXXXg1s3ZG3-w==","isModifiable":true,"managerID":"TneiLnMBXXXXXXXXXPFAXg==","referenceName":"Report","referenceString":"<Resource URI=\\\"/XXXXXXXXXXXXXXXXX\" ID=\\\"9025mTEXXXXXXXg1s3ZG3-w==\\\"/>","referenceType":9,"uri":"/XXXXXXXXXX"},"resourceid":"9025mTEXXXXXXXg1s3ZG3-w==","state":2,"type":9,"typeName":"Report","URI":"/XXXXXXXXXXXXXXXXXX","versionID":"AAXXXXXXXOX","canRunDeltaReport":false,"commonParameters":[{"displayName":"Report Name","name":"Report Name","parameterType":0,"type":{"javaTypeName":"int","name":"ReportOutXXXEnumeration","type":7},"value":4},{"displayName":"Page Size","name":"Page Size","parameterType":0,"type":{"javaTypeName":"int","name":"ReportXXXXEnumeration","type":7},"value":0},{"displayName":"Run as User","name":"Run as User","parameterType":0,"type":{"javaTypeName":"com.arcsiXXXXXXXourceReference","name":"com.arcXXXXXXurceReference","type":8}},{"displayName":"Email to","name":"Email to","parameterType":0,"type":{"javaTypeName":"com.arcsiXXXXXXXXourceReference[]","name":"com.arcsiXXXXXXXXourceReference[]","type":9}},{"displayName":"Email Addresses","name":"Email addresses","parameterType":0,"type":{"javaTypeName":"String","name":"String","type":0}},{"displayName":"Email Format","name":"Email Format","parameterType":0,"type":{"javaTypeName":"int","name":"ReportMailXXXXXnumeration","type":7},"value":0},{"displayName":"Email Subject","name":"Email Subject","parameterType":0,"type":{"javaTypeName":"String","name":"String","type":0},"value":"$ReportName"}],"componentIDs":["Table","Subtitle","TableTitle"],"componentParameters":[{"displayName":"Time Zone","name":"Time Zone","parameterType":0,"type":{"javaTypeName":"int","name":"ReportTXXXXXXXEnumeration","type":7},"value":0,"id":"Table"},{"displayName":"RXXXXX","name":"RXXXXX","parameterType":0,"type":{"javaTypeName":"int","name":"Integer","type":4},"value":10000,"id":"Table"}],"customReport":false,"hasPermissionToArchive":true,"reportXML":"<Report> XXXXXXXXXXX </Report>","saveOutputParameters":[{"displayName":"Archive Report Folder","name":"Archive Report Folder","parameterType":0,"type":{"javaTypeName":"com.arcsiXXXXXXXXourceReference","name":"com.arcsiXXXXXXXXourceReference","type":8}},{"displayName":"ArXXXXXme","name":"ArXXXXXme","parameterType":0,"type":{"javaTypeName":"String","name":"String","type":0},"value":"${Today}/${ReportName}_${Now}"},{"displayName":"ArXXXXXXTime","name":"ArXXXXXXTime","parameterType":0,"type":{"javaTypeName":"long","name":"DateTime","type":1},"value":"$NoXXXXX6M"}]}]}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Is Value In Activelist Column
Action checks, if entities were found in ArcSight Activelist
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Active list UUID|Specify the UUID of the active list, where you want to search for entities. Note: parameter “Active list UUID“ takes priority over “Active list name“. Example: HLZRc9yYBABC-lHtlf3-f0Q==|False|String||
|Column name|Specify the name of the column, where you want to search for the entity.|True|String||
|Active list name|Specify the name of the active list, where you want to search for entities. Note: parameter “Active list UUID“ takes priority over “Active list name“.|False|String||



##### JSON Results
```json
[{"Name":"hash","ResourceType":"ad","Path":"dsa","StartTime":"asd","EventClassID":"dsa","Status":"sasd","Duration":"sad"}]
```



#### Search
Search for available resources in ArcSight
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search Query|Specify the search query.|True|String|None|
|Max Items To Return|Specify how many items to return in the response.|False|String|100|



##### JSON Results
```json
[{"score": 1.2440307, "uuid": "TyJnM2jwBABCMzP5h6xxxx==", "uri": "/All_Fields/ArcSight_Foundation/Variables_Library/IPv6/Attacker_IPv6_Address", "name": "Attacker IPv6 Address"}, {"score": 1.2440307, "uuid": "TyJnM2jwBABCMzP5h6xxxx==", "uri": "/All_Fields/ArcSight_Foundation/Variables_Library/IPv6/Attacker_IPv6_Address", "name": "Attacker IPv6 Address"}]
```









## Connectors
#### Arcsight ESM Connector
Arcsight ESM Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|500|
|Server Address|Server address of the ArcSight instance|True|String||
|Username|Username of the ArcSight account|True|String||
|Password|Password of the ArcSight account|True|Password|*****|
|Events Count Limit|How many events to process per one alert|True|Integer|15|
|Cases Folder Path|Absolute path to cases. Example: /opt/Correlations|True|String|/opt/Correlations|
|Alerts Count Limit|How many alerts to process per one iteration|True|Integer|10|
|Environment Field Name|The name of the environment's field. e.g. event.CustomerURI|True|String|event.CustomerURI|
|Secondary Device Product Field|Secondary field for Device Product|False|String||
|Alert Custom Fields Names|Additional fields that should be added to Siemplify Alert. Example: source_address|False|String||
|Done files retention days|For how many days to leave files in the “Done” folder |True|Integer|3|
|Error files retention days|For how many days to leave files in the “Error” folder|True|Integer|14|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ArcSight ESM server is valid.|False|Boolean|false|
|CA Certificate File|Base 64 encoded CA certificate file.|False|String||


#### ArcSight - Security Events Connector
Pull correlations from ArcSight. Note: dynamic list works with "name" parameter. Please refer to the doc portal for the configuration setup. This connector is suitable for Saas deployment of Chronicle SOAR and is the recommended one for production use.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|type|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|name|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|360|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the ArcSight instance.|True|String|https://{ip}|
|Username|Username of the ArcSight account.|True|String||
|Password|Password of the ArcSight account.|True|Password|*****|
|Report Name|Name of the report that will be used to fetch events.|True|String||
|Fetch Base Events|If enabled, connector will also fetch base events.|False|Boolean|true|
|Lowest Priority To Fetch|Lowest priority that will be used to fetch events. Possible values are in range 1 to 10. If nothing is provided, all events will be ingested.|False|String||
|Max Events To Fetch|How many alerts to process per one connector iteration. Maximum is 1000.|False|Integer|100|
|Use dynamic list as a blocklist|If enabled, dynamic lists will be used as a blocklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ArcSight server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.