# 29AWS Cloud Trail - Insights Connector
Pull insights from AWS Cloud Trail.


Integration: AWSCloudTrail

Integration Version: 6.0

Device Product Field: Product Name

Event Name Field: CloudTrailEvent_insightDetails_insightType
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|AWS Access Key ID|AWS Access Key ID to use in integration.|True|jhgfds|
|AWS Secret Key|AWS Secret Key to use in integration.|True|*****|
|AWS Default Region|AWS default region to use in integration, for example us-west-2.|True|hgfd|
|Alert Severity|Severity of the Siemplify Alerts created based on the insights. Possible values: Informational, Low, Medium, High, Critical|True|Medium|
|Max Insights To Fetch|How many insights to process per one connector iteration. Maximum is 50.|False|50|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve insights from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the AWS Cloud Trail server is valid.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

