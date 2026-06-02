
# CSV

Integration designed around working with CSV files. CSV is a simple file format used to store tabular data, such as a spreadsheet or database.

Python Version - 3


#### Dependencies
| |
|-|
|protobuf-6.32.1-cp39-abi3-manylinux2014_x86_64.whl|
|cachetools-6.2.0-py3-none-any.whl|
|googleapis_common_protos-1.70.0-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|google_api_python_client-2.184.0-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|google_auth-2.41.1-py2.py3-none-any.whl|
|charset_normalizer-3.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|chardet-5.2.0-py3-none-any.whl|
|pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|anyio-4.11.0-py3-none-any.whl|
|tzdata-2024.1-py2.py3-none-any.whl|
|TIPCommon-2.2.14-py2.py3-none-any.whl|
|pytz-2024.1-py2.py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|httplib2-0.31.0-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|google_api_core-2.26.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|certifi-2025.10.5-py3-none-any.whl|
|pyparsing-3.2.5-py3-none-any.whl|


## Actions
#### CSV Search by String
Search for strings in CSV files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|CSV Path|Specify the file path to the CSV file or a folder path that contains all of the CSV files. If folder is provide, action will iterate over all CSV files in the folder.|True|String||
|CSV Column|Specify a comma-separated list of columns that can contain entity information. If nothing is provided, action will search in all of the columns.|False|String||
|Days Back|Specify how many days backwards to process the CSV files.|False|String||
|Search Value|Specify a string that needs to be searched. If 'Search Multiple Strings' is enabled, this parameter is treated as a comma-separated list of strings that need to be searched.|True|String||
|Return the first row only|If enabled, action will only return 1 row in the first file that matched the entity.|False|Boolean||
|File Encoding Types|A comma separated list CSV encoding types used for decoding your CSV files, e.g. utf-8, latin-1, iso-8859-1, utf-16... Order in which the encoding types are given sets the order in which they are used for decoding files, e.g.(from example above) the utf-8 has the highest priority and will be used primarily for decoding all the files, if there is a CSV file that uses some other encoding then the next in the order: latin-1 encoding will be used, and so on, until the last encoding is used.|True|String|utf-8, latin-1, iso-8859-1|
|Fields To Return|Specify a comma-separated list of values that need to be returned.|False|String||
|Search Multiple Strings|If enabled, 'Search Value' will work as a comma-separated list of values, instead of a single string.|False|Boolean|false|



##### JSON Results
```json
[{"EntityResult": {"Field2": "Value2", "Field3": "Value3", "Field1": "Value1", "Field4": "Value4", "Field5": "Value5"}, "Entity": "host"}, {"EntityResult": {"Field2": "Value2", "Field3": "Value3", "Field1": "Value1", "Field4": "Value4", "Field5": "Value5"}, "Entity": "1.1.1.1"}]
```



#### CSV Search by Entity
Search for entities in CSV files and enrich them.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|CSV Path|Specify the file path to the CSV file or a folder path that contains all of the CSV files. If folder is provide, action will iterate over all CSV files in the folder.|True|String||
|CSV Column|Specify a comma-separated list of columns that can contain entity information. If nothing is provided, action will search in all of the columns.|False|String||
|Days Back|Specify how many days backwards to process the CSV files.|False|String||
|Mark As Suspicious|If enabled, action will mark entity as suspicious, if it was found in file.|False|Boolean||
|Return the first row only|If enabled, action will only return 1 row in the first file that matched the entity.|False|Boolean||
|File Encoding Types|A comma separated list CSV encoding types used for decoding your CSV files, e.g. utf-8, latin-1, iso-8859-1, utf-16... Order in which the encoding types are given sets the order in which they are used for decoding files, e.g.(from example above) the utf-8 has the highest priority and will be used primarily for decoding all the files, if there is a CSV file that uses some other encoding then the next in the order: latin-1 encoding will be used, and so on, until the last encoding is used.|True|String|utf-8, latin-1, iso-8859-1|
|Enrich Entities|If enabled, action will add information from CSV file and add it to the enrichment table of entity.|False|Boolean|true|
|Create Insight|If enabled, action will create an insight, if entity was found in the file.|False|Boolean|true|
|Fields To Return|Specify a comma-separated list of values that need to be returned.|False|String||



##### JSON Results
```json
[{"EntityResult": [{"domain": "SmartCompany.dom", "fileHash": "cbbc5aea3d4c7ec193aa2ff3b52df36ebb12338b18c9bb53fc4896115efaf78d", "reporter": "Symantec Antivirus", "app": "Arcsight", "id": "1011", "eventTime": "9/4/2017 10:00", "antivirusAction": "blocked", "virusName": "ECAT", "rule": "malicious", "eventName": "Virus detected", "User": "Ziv", "eventHostName": "WS-ZivDevComp", "File Source Path": "C:\\Users\\Default\\Desktop\\stringTimeRaw.csv", "machineAddress": "192.168.11.11"}, {"domain": "SmartCompany.dom", "fileHash": "cbbc5aea3d4c7ec193aa2ff3b52df36ebb12338b18c9bb53fc4896115efaf78d", "reporter": "Symantec Antivirus", "app": "ESM", "id": "1012", "eventTime": "9/4/2017 10:00", "antivirusAction": "allowed", "virusName": "ECAT", "rule": "malicious", "eventName": "Virus detected", "User": "GG", "eventHostName": "WS-GGDevComp", "File Source Path": "C:\\Users\\Default\\Desktop\\stringTimeRaw.csv", "machineAddress": "192.168.11.11"}], "Entity": "192.168.11.11"}]
```



#### Save Json To CSV
Save JSON object  to CSV.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|Specify the JSON object that needs to be saved as CSV.|True|String||
|Overwrite|If enabled, action will overwrite existing file.|False|Boolean|False|
|File Path|Specify the absolute file path for the newly created CSV file. If only the file name is provided, action will store the file in /tmp/ folder.|True|String||
|Advanced Nested JSON Handling|If enabled, action will create a CSV, where nested JSONs keys will be in separate columns and lists of JSON objects will be converted into rows. Data in CSV will be filled.|False|Boolean|False|



##### JSON Results
```json
{"filepath":"/tmp/sample.csv"}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds









## Connectors
#### CSV Connector
Fetch data from csv files located in a specific folder, convert this data to alerts in siemplify system

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Csv Folder Path|Folder path that contains all of the csv files that need to be ingested.|True|String||
|CSV Limit|How many CSV files to process per one iteration.|False|Integer||
|Time Field Name|Name of the field that contains information about the event time.|False|String||
|Time Field Timezone|Timezone of the column stated in the 'Time Field Name' param.|False|String|UTC|
|Rule Generator Field Name|Name of the field that contains information about the rule generator.|False|String||
|CSV Has Header|Indicates whether the csv file has header|False|Boolean|true|
|File Encoding Types|A comma separated list CSV encoding types used for decoding your CSV files, e.g. utf-8, latin-1, iso-8859-1, utf-16... Order in which the encoding types are given sets the order in which they are used for decoding files, e.g.(from example above) the utf-8 has the highest priority and will be used primarily for decoding all the files, if there is a CSV file that uses some other encoding then the next in the order: latin-1 encoding will be used, and so on, until the last encoding is used.|True|String|utf-8, latin-1, iso-8859-1|
|Alert Field Name|Name of the field that contains information about alert name.|False|String||
|Severity Field Name|Name of the field that contains information about severity. Note: you can map severity based on the values in the response. For that you need to go to the connector execution folder and modify severity_mapping_config.json. Check documentation for reference.|False|String||





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.