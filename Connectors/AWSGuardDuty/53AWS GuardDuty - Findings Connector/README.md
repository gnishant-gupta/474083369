# 53AWS GuardDuty - Findings Connector
Pull findings from AWS GuardDuty. Note: Whitelist works with Finding types, for example, UnauthorizedAccess:EC2/RDPBruteForce.


Integration: AWSGuardDuty

Integration Version: 12.0

Device Product Field: Product Name

Event Name Field: Type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|180|
|AWS Access Key ID|AWS Access Key ID to use in integration.|True|dfghjk|
|AWS Secret Key|AWS Secret Key to use in integration.|True|*****|
|AWS Default Region|AWS default region to use in integration, for example us-west-2.|True|fghjk|
|Detector ID|ID of the detector. It can be found in the "Settings" tab.|True|iuytre|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Findings To Fetch|How many findings to process per one connector iteration. Maximum is 50. This is a GuardDuty limitation.|True|50|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch findings. Possible values are in range from 1 to 8. Note: AWS GuardDuty maps the integer value in the following order: 1,2,3 - Low; 4,5,6 - Medium; 7,8 - High.|True|1|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

