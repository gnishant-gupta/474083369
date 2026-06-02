# 31AWS IAM Access Analyzer - Findings Connector
Pull findings from AWS IAM Access Analyzer. Note: Whitelist works on resource types.Example: AWS::S3::Bucket.


Integration: AWSIAMAccessAnalyzer

Integration Version: 9.0

Device Product Field: Product Name

Event Name Field: resourceType
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|AWS Access Key ID|AWS Access Key ID to use in integration.|True|hgfd|
|AWS Secret Key|AWS Secret Key to use in integration.|True|*****|
|AWS Default Region|AWS default region to use in integration, for example us-west-2.|True|hgfd|
|Analyzer Name|Name of the analyzer that should be used in the integration.|True|jhgfd|
|Alert Severity|Severity of the Siemplify Alerts created from this connector. Possible values: Critical, High, Medium , Low, Informational.|False|Medium|
|Max Findings To Fetch|How many findings to process per one connector iteration.|False|50|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the AWS IAM Access Analyzer server is valid.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

