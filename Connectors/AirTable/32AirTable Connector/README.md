# 32AirTable Connector
The Connector ingests records from a given table in Airtable


Integration: AirTable

Integration Version: 16.0

Device Product Field: <none>

Event Name Field: <none>
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|30|
|Table name|Each Base can include multiple tables. The parameter indicates the name of the table within the base.|True|<table_name>|
|Alert name field|Determines the Alert name based on the airtable column name defined in the parameter|False|<alert_name_field>|
|Alert name prefix|The alert name prefix|False|<alert_name_prefix>|
|Alert type|Determines the Alert type based on the airtable column name defined in the parameter|True|<alert_type>|
|Api key|Your API Key can be found in your account overview under API|True|*****|
|Base id|Base is a database in Airtable in which you store data. The base ID can be found in the URL of the API page of the base.|True|<base_id>|
|Field name|The field name that you would like to search the value by|False|<field_name>|
|Field value|The value that you would like to search for under the relevant field name|False|<field_value>|
|Max records|The maximum rows in the table that will be affected by the action|True|300|

