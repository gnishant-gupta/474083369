
# AWSSecurityHub

AWS Security Hub gives you a comprehensive view of your high-priority security alerts and security posture across your AWS accounts. There are a range of powerful security tools at your disposal, from firewalls and endpoint protection to vulnerability and compliance scanners. But oftentimes this leaves your team switching back-and-forth between these tools to deal with hundreds, and sometimes thousands, of security alerts every day.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|AWS Access Key ID|None|True|String||
|AWS Secret Key|None|True|Password|*****|
|AWS Default Region|None|True|String||


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|jmespath-1.0.1-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|botocore-1.35.4-py3-none-any.whl|
|boto3-1.35.4-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|


## Actions
#### Get Insight Details
Return detailed information about an insight in AWS Security Hub.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Insight ARN|Specify the ARN of the insight.|True|String||
|Max Results to Return|Specify how many results to return.|False|String|50|



##### JSON Results
```json
[{"InsightResults":{"InsightArn":"arn:aws:securityhub:::insight/securityhub/default/1","GroupByAttribute":"ResourceId","ResultValues":[{"GroupByAttributeValue":"arn:aws:s3:::int-arcsight-v-27-0-getreportstatus","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-arcsight-v-27-0-searchactionbug","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-arcsight-v-27-0-unicodeandlogs","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-automation-v-1-0","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-awss3-v-1-0","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-azureactivedirectory-v-4-0","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-bootcamp-v-1-0","Count":5},{"GroupByAttributeValue":"arn:aws:s3:::int-categories","Count":5}]}}]
```



#### Update Insight
Update an insight in AWS Security Hub.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Insight ARN|Specify the ARN of the insight.|True|String||
|Insight Name|Specify the new name of the insight.|False|String||
|Group By Attribute|Specify a new name of the attribute by which findings should be grouped under one insight.|False|List|Select One|
|Filter JSON Object|Specify a new filter for the findings. Filter is represented as a JSON object, where you can specify different attributes and values. Please refer to action documentation for more details.|False|String||



#### Create Insight
Create an insight in AWS Security Hub.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Insight Name|Specify the name of the insight.|True|String||
|Group By Attribute|Specify the name of the attribute by which findings should be grouped under one insight.|True|List|AWS Account ID|
|Filter JSON Object|Specify a filter for the findings. Filter is represented as a JSON object, where you can specify different attributes and values. Please refer to action documentation for more details.|True|String||



##### JSON Results
```json
[{"InsightArn":"arn:aws:securityhub:us-east-2:962970284126:insight/962970284126/custom/da74bc5f-b024-4d6f-8077-3f8161c1f41d"}]
```



#### Ping
Test connectivity to AWS Security Hub with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Update Finding
Update findings in AWS Security Hub.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ID|Specify ID of the finding that you want to update.|True|String||
|Product ARN|Specify the product ARN of the finding that you want to update.|True|String||
|Note|Specify new text for the note on the finding. Note: If the “Note” parameter has a value, you should also fill out the “Note Author” parameter. This is an AWS Security Hub limitation.|False|String||
|Note Author|Specify the author of the note. Note: If the “Note Author” parameter has a value, you should also fill out the “Note” parameter. This is an AWS Security Hub limitation.|False|String||
|Severity|Specify new severity for the finding.|False|List|Select One|
|Verification State|Specify a new verification state for the finding.|False|List|Select One|
|Confidence|Specify new confidence for the finding.|False|String||
|Criticality|Specify new criticality for the finding.|False|String||
|Types|Specify a comma-separated list of types for the finding. Example: type1,type2|False|String||
|Workflow Status|Specify new workflow status for the finding.|False|List|Select One|
|Custom Fields|Specify custom fields that should be updated in the finding. Format Custom_field_1:value,Custom_field_2:value|False|String||









## Connectors
#### AWS Security Hub - Findings Connector
Pull findings from AWS Security Hub.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|ProductFields_aws/securityhub/ProductName|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|Title|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|AWS Access Key ID|AWS Access Key ID to use in integration.|True|String||
|AWS Secret Key|AWS Secret Key to use in integration.|True|Password|*****|
|AWS Default Region|AWS default region to use in integration, for example us-west-2.|True|String||
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Findings To Fetch|How many findings to process per one connector iteration.|True|Integer|50|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch findings. Possible values: Informational, Low, Medium, High, Critical|True|String|Medium|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the AWS Security Hub is valid.|False|Boolean|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.