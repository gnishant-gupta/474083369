
# Devo

Devo is the cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API URL||True|String|https://apiv2-us.devo.com|
|API Token||False|Password|*****|
|API Key||False|Password|*****|
|API Secret||False|Password|*****|
|Verify SSL||False|Boolean|true|


#### Dependencies
| |
|-|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|six-1.17.0-py2.py3-none-any.whl|
|TIPCommon-1.0.11.1-py2.py3-none-any.whl|
|python_dateutil-2.8.2-py2.py3-none-any.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Ping
Test connectivity to the Devo instance with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Advanced Query
Execute an advanced query based on the provided parameters. Note that action is not working on Siemplify entities. If its planned to query table other than siem.logtrust.alert.info, please create an additional token for that table following the documentation at https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens and specify it on the integration configuration page.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify a query to execute against Devo instance. Example format: 'from siem.logtrust.alert.info'.|True|String||
|Time Frame|Specify a time frame for the results. If 'Custom' is selected, you also need to provide 'Start Time'.|False|List|Last Hour|
|Start Time|Specify a time frame for the results. If 'Custom' is selected, you also need to provide 'Start Time'.|False|String||
|End Time|Specify the start time for the query. This parameter is mandatory, if 'Custom' is selected for the 'Time Frame' parameter. Format: ISO 8601. Example: 2021-08-05T05:18:42Z|False|String||
|Max rows to return|Specify max number of rows the action should return.|False|String|50|



##### JSON Results
```json
{"msg": "", "timestamp": 1632291351284, "cid": "9eXXXXXXXc0", "status": 0, "object": [{"eventdate": 1619452643049, "alertHost": "backoffice", "domain": "siemplify", "priority": 7.0, "context": "my.XXXXX.XXXXX.500", "category": "my.context", "status": 0, "alertId": "123456", "srcIp": null, "srcPort": null, "srcHost": "", "dstIp": null, "dstPort": null, "dstHost": "", "protocol": "", "username": "XXXXX@XXXXX.XXXX", "application": "", "engine": "XXXX-pro-XXXX-XXXX-aws", "extraData": "{\"count\":\"13\",\"eventdate\":\"2021-04-26+15%3A56%3A30.0\"}"}]}
```



#### Simple Query
Execute a simple query based on the provided parameters. Note that action is not working on Siemplify entities. If its planned to query table other than siem.logtrust.alert.info, please create an additional token for that table following the documentation at https://docs.devo.com/confluence/ndt/latest/domain-administration/security-credentials/authentication-tokens and specify it on the integration configuration page.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify what table should be queried.|True|String|siem.logtrust.alert.info|
|Fields To Return|Specify what fields to return. If nothing is provided, action will return all fields.|False|String||
|Where Filter|Specify the WHERE filter for the query  that needs to be executed.|False|String||
|Time Frame|Specify a time frame for the results. If 'Custom' is selected, you also need to provide 'Start Time'.|False|List|Last Hour|
|Start Time|Specify a time frame for the results. If 'Custom' is selected, you also need to provide 'Start Time'.|False|String||
|End Time|Specify the start time for the query. This parameter is mandatory, if 'Custom' is selected for the 'Time Frame' parameter. Format: ISO 8601. Example: 2021-08-05T05:18:42Z|False|String||
|Max rows to return|Specify max number of rows the action should return.|False|String|50|



##### JSON Results
```json
{"msg": "", "timestamp": 1632309545362, "cid": "123456789", "status": 0, "object": [{"eventdate": 1619452643049, "alertHost": "backoffice", "domain": "XXXXXX", "priority": 7.0, "context": "my.XXXX.XXXX.XXXX", "category": "my.context", "status": 0, "alertId": "123456789", "srcIp": null, "srcPort": null, "srcHost": "", "dstIp": null, "dstPort": null, "dstHost": "", "protocol": "", "username": "XXXX@XXXXX.XXX", "application": "", "engine": "XXX-XXX-XXX-XXX-aws", "extraData": "{\"count\":\"13\",\"eventdate\":\"2021-04-26+15%3A56%3A30.0\"}"}]}
```









## Connectors
#### Devo Alerts Connector
Connector can be used to fetch alert records from Devo siem.logtrust.alert.info table. Connector whitelist can be used to ingest only specific types of alerts based on alert context value.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Describes the name of the field where the product name is stored.|True|String|Product Name|
|EventClassId|Describes the name of the field where the event name is stored|False|String|context|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.|False|String|.*|
|API Root|Specify API URL for the target Devo instance.|True|String|https://apiv2-us.devo.com|
|API Token|If token-based authentication is used, sSpecify API token for the target Devo instance.|False|Password|*****|
|API Key|If access keys authentication is used, specify API key for the target Devo instance.|False|Password|*****|
|API Secret|If access keys authentication is used, specify API secret for the target Devo instance.|False|Password|*****|
|Verify SSL|If enabled, Siemplify server will check the certificate configured for API root.|False|Boolean|false|
|Offset time in hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|24|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|Integer|30|
|Minimum Priority to Fetch|Minimum priority of the alert to be ingested to Siemplify, for example, Low or Medium. Possible values: Very low, Low, Normal, High, Very high.|False|String|Normal|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|300|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.