
# AWSGuardDuty

Amazon GuardDuty informs you of the status of your AWS environment by producing security findings. GuardDuty helps to detect and manage threats to your AWS system.

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
|pyasn1_modules-0.4.1-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.151.0-py2.py3-none-any.whl|
|jmespath-1.0.1-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|rsa-4.9-py3-none-any.whl|
|boto3-1.35.10-py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|proto_plus-1.25.0-py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|urllib3-2.2.2-py3-none-any.whl|
|google_api_core-2.22.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|TIPCommon-2.0.3-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|botocore-1.35.10-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|httpcore-1.0.6-py3-none-any.whl|


## Actions
#### Archive Findings
Archive GuardDuty findings that are specified by finding IDs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector.|True|String||
|Finding IDs|The IDs of the findings that you want to archive. Comma separated ids.|True|String||
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



#### Delete a Trusted IP list
Delete the IPSet specified by the Id.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to delete an IP set. This parameter can be found in the “Settings” tab.|True|String||
|Trusted IP List IDs|Specify the comma-separated list of ids of ips sets. Example: id_1,id_2|True|String||



#### Delete Threat Intelligence Set
Delete a threat intelligence set in AWS GuardDuty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to get threat intelligence sets details. This parameter can be found in the “Settings” tab.|True|String||
|Threat Intelligence Set IDs|Specify the comma-separated list of ids of threat intelligence sets. Example: id_1,id_2|True|String||



#### Delete a Detector
Delete an Amazon GuardDuty detector that is specified by the detector ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector that you want to delete.|True|String||



#### Get a Trusted IP List
Get details about a trusted IP list in AWS GuardDuty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to get an IP set. This parameter can be found in the "Settings" tab.|True|String||
|Trusted IP List IDs|Specify the comma-separated list of ids of ips sets. Example: id_1,id_2.|True|String||



##### JSON Results
```json
[{"EntityResult": {"Format": "TXT", "Name": "Test", "Location": "https://testsiemplify.s3.amazonaws.com/ips.txt", "Status": "INACTIVE"}, "Entity": "f6ba9dcaf89d16cd959921737f038cf7"}]
```



#### Create Threat Intelligence Set
Create a threat intelligence set in AWS GuardDuty. Note: iam:PutRolePolicy permission. Maximum number of Threat Intel sets is 6.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to create a Threat Intelligence Set. This parameter can be found in the "Settings" tab.|True|String||
|Name|Specify the name of the Threat Intelligence Set.|True|String||
|File Format|Select the format of the file that should be used to create a threat intelligence set.|True|List|Plaintext|
|File Location|Specify the URI location, where the file is located.|True|String|https://s3.amazonaws.com/{bucket-name}/file.txt|
|Active|If enabled, the newly created Threat Intelligence Set will be activated.|False|Boolean|true|
|Tags|Specify additional tags that should be added to the Threat Intelligence Set. Format: key_1:value_1,key_2:value_1.|False|String||



##### JSON Results
```json
{"ThreatIntelSetId": ["b6f0c884a54449cc8e29eed3094e9c31"]}
```



#### Create Sample Findings
Generates example findings of types specified by the list of findings.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector to create sample findings for.|True|String||
|Finding Types|The types of sample findings to generate. Comma separated values. If empty, example findings of all supported finding types will be generated. Types can be found in the UI at ‘Findings’ section under ‘Finding Type’ column|False|String||



#### Create a Trusted IP List
Creates a new list of trusted IP addresses (IPSet) that were white listed for secure communication with AWS infrastructure and applications. Note: Only 1 Trusted IP set can be created and activated. GuardDuty doesn't generate findings for IP addresses that are included in IPSets. Only users from the master account can use this operation.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to create a Trusted IP List. This parameter can be found in the "Settings" tab.|True|String||
|Name|Specify the name of the Trusted IP List.|True|String||
|File Format|Select the format of the file that should be used to create a Trusted IP List.|True|List|Plaintext|
|File Location|Specify the URI location, where the file is located.|True|String|https://s3.amazonaws.com/{bucket-name}/file.txt|
|Activate|If enabled, the newly created Trusted IP List will be activated.|False|Boolean|true|
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
{"TrustedIPID": ["f6ba9dcaf89d16cd959921737f038cf7"]}
```



#### Create a Detector
Creates a single Amazon GuardDuty detector. A detector is a resource that represents the GuardDuty service.You can have only one detector per account per Region.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enable|Specifies whether the detector is to be enabled|False|Boolean|false|



##### JSON Results
```json
{"detectorId": "123456abcd"}
```



#### Get all Trusted IP lists
Get all trusted IP lists (IPSets) of the GuardDuty service specified by the detector ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to list IP sets. This parameter can be found in the "Settings" tab.|True|String||
|Max Trusted IP Lists To Return|Specify how many Trusted IPs lists to return. Default is 50.|False|String|50|
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
{"IpSetIds": ["f6ba9dcaf89d16cd959921737f038cf7"]}
```



#### Get Detector Details
Retrieve an Amazon GuardDuty detector specified by the detector ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector that you want to retrieve. Comma separated values|True|String||



##### JSON Results
```json
[{"Entity": "abcdefg", "EntityResult": {"DetectorId": "abcdefg", "CreatedAt": "2020-11-01T11:57:32.958Z", "ServiceRole": "arn:aws:iam::123456:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty", "Status": "ENABLED", "UpdatedAt": "2020-11-01T11:57:32.958Z"}}]
```



#### Get Threat Intelligence Set Details
Get details about a threat intelligence set in AWS GuardDuty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to get threat intelligence sets details. This parameter can be found in the "Settings" tab.|True|String||
|Threat Intelligence Set IDs|Specify the comma-separated list of ids of threat intelligence sets. Example: id_1,id_2.|True|String||
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
[{"EntityResult": {"ResponseMetadata": {"RequestId": "34c2992c-4bce-412b-ae6d-6cc2b7aa3ce5", "HTTPStatusCode": 200, "HTTPHeaders": {"date": "Tue, 20 Oct 2020 11:12:03 GMT", "content-type": "application/json", "content-length": "195", "connection": "keep-alive", "x-amzn-requestid": "34c2992c-4bce-412b-ae6d-6cc2b7aa3ce5", "x-amz-apigw-id": "UtPgdESBIAMF67g=", "x-amzn-trace-id": "Root=1-5f8ec602-00fe46b9722778852039359a;Sampled=0"}, "RetryAttempts": 0}, "Name": "Test4", "Format": "PROOF_POINT", "Location": "https://s3.amazonaws.com/siemplifytest/file.txt", "Status": "INACTIVE", "Tags": {"tt": "22", "test": "tag"}}, "Entity": "96b15ef2cb93412897b2b9dadbe429cf"}]
```



#### List Detectors
Lists detectorIds of all the existing Amazon GuardDuty detector resources.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Detectors To Return|Specify how many detectors to return. Default is 50.|False|String|50|



##### JSON Results
```json
{"detectorIds": ["123456abcde"]}
```



#### List Findings for a Detector
Lists all Amazon GuardDuty findings for the specified detector ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector that you want to retrieve.|True|String||
|Max Findings To Return|Specify how many detectors to return. Default is 50.|False|String|50|
|Sort By|Represents the finding attribute (for example, accountId) to sort findings by.|False|String||
|Order By|The order by which the sorted findings are to be displayed.|False|List||
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
{"FindingIds": ["10ba96ae50733ae38b9cae95431b7558"]}
```



#### Ping
Test connectivity to AWS GuardDuty with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Update a Detector
Update the Amazon GuardDuty detector specified by the detector ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector that you want to update.|True|String||
|Enable|Specifies whether the detector should be enabled|False|Boolean|false|



#### Update Findings Feedback
Mark the specified Amazon GuardDuty findings as useful or not useful.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector associated with the findings to update feedback for.|True|String||
|Useful?|The feedback for the finding.|False|Boolean||
|Findings IDs|The IDs of the findings that you want to mark as useful or not useful. Comma separated values.|True|String||
|Comment|Additional feedback about the GuardDuty findings.|False|String||
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



#### Update Threat Intelligence Set
Update a threat intelligence set in AWS GuardDuty. Note: iam:PutRolePolicy permission.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to update a Threat Intelligence Set. This parameter can be found in the "Settings" tab.|True|String||
|ID|Specify the ID of the Threat Intelligence set that should be updated.|True|String||
|Name|Specify the new name of the Threat Intelligence Set.|False|String||
|File Location|Specify a new URI location, where the file is located.|False|String|https://s3.amazonaws.com/{bucket-name}/file.txt|
|Active|If enabled, the Threat Intelligence Set will be activated.|False|Boolean|true|



#### Get Finding Details
Return detailed information about a finding in AWS Guard Duty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Finding IDs|The IDs of the findings that you want to retrieve. Comma separated ids.|True|String||
|Detector ID|The unique ID of the detector that you want to retrieve.|True|String||
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
{"Findings": [{"AccountId": "582302349248", "Arn": "arn:aws:guardduty:us-east-1:582302349248:detector/26b8d318c596f5eb942b4c146870944f/finding/02ba7e2d000521f35033ed64488b8e1b", "CreatedAt": "2020-10-06T05:19:50.794Z", "Description": "213.108.133.9 is performing RDP brute force attacks against i-053d1520f53584149. Brute force attacks are used to gain unauthorized access to your instance by guessing the RDP password.", "Id": "02ba7e2d000521f35033ed64488b8e1b", "Partition": "aws", "Region": "us-east-1", "Resource": {"InstanceDetails": {"AvailabilityZone": "us-east-1e", "ImageId": "ami-01b670d1a5b2c1da7", "InstanceId": "i-053d1520f53584149", "InstanceState": "running", "InstanceType": "t2.micro", "LaunchTime": "2020-05-27T08:54:03Z", "NetworkInterfaces": [{"Ipv6Addresses": [], "NetworkInterfaceId": "eni-012d9b8a1a3b4e40a", "PrivateDnsName": "ip-1.1.1.1.ec2.internal", "PrivateIpAddress": "1.1.1.1", "PrivateIpAddresses": [{"PrivateDnsName": "ip-1.1.1.1.ec2.internal", "PrivateIpAddress": "1.1.1.1"}], "PublicDnsName": "ec2-54-234-69-236.compute-1.amazonaws.com", "PublicIp": "54.234.69.236", "SecurityGroups": [{"GroupId": "sg-0fa42e04e9cd15407", "GroupName": "Windows Server 2016"}], "SubnetId": "subnet-2edddf10", "VpcId": "vpc-48a7ac32"}], "Platform": "windows", "ProductCodes": [], "Tags": [{"Key": "Name", "Value": "CiscoAMP-win2012"}]}, "ResourceType": "Instance"}, "SchemaVersion": "2.0", "Service": {"Action": {"ActionType": "NETWORK_CONNECTION", "NetworkConnectionAction": {"Blocked": false, "ConnectionDirection": "INBOUND", "LocalPortDetails": {"Port": 3389, "PortName": "RDP"}, "Protocol": "TCP", "LocalIpDetails": {"IpAddressV4": "1.1.1.1"}, "RemoteIpDetails": {"City": {"CityName": "Moscow"}, "Country": {"CountryName": "Russia"}, "GeoLocation": {"Lat": 55.7522, "Lon": 37.6156}, "IpAddressV4": "213.108.133.9", "Organization": {"Asn": "24875", "AsnOrg": "NovoServe B.V.", "Isp": "NovoServe B.V.", "Org": "NovoServe B.V."}}, "RemotePortDetails": {"Port": 1549, "PortName": "Unknown"}}}, "Archived": false, "Count": 5, "DetectorId": "26b8d318c596f5eb942b4c146870944f", "EventFirstSeen": "2020-10-06T05:10:58Z", "EventLastSeen": "2020-10-06T05:46:59Z", "ResourceRole": "TARGET", "ServiceName": "guardduty"}, "Severity": 2, "Title": "213.108.133.9 is performing RDP brute force attacks against i-053d1520f53584149.", "Type": "UnauthorizedAccess:EC2/RDPBruteForce", "UpdatedAt": "2020-10-06T06:01:46.380Z"}]}
```



#### Unarchive Findings
Unarchive GuardDuty findings that are specified by finding IDs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|The unique ID of the detector.|True|String||
|Finding IDs|The IDs of the findings that you want to unarchive. Comma separated ids.|True|String||



#### Update a Trusted IP List
Update a trusted IP list in AWS GuardDuty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to update a Trusted IP List. This parameter can be found in the "Settings" tab.|True|String||
|Trusted IP List ID|Specify the ID of the Trusted IP List that should be updated.|True|String||
|Name|Specify the new name of the Trusted IP List.|False|String||
|File Location|Specify a new URI location, where the file is located.|False|String|https://s3.amazonaws.com/{bucket-name}/file.txt|
|Activate|If enabled, the Trusted IP List will be activated.|False|Boolean|true|
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



#### List Threat Intelligence Sets
List available threat intelligence sets in AWS GuardDuty.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector ID|Specify the detector ID that should be used to list threat intelligence sets. This parameter can be found in the "Settings" tab.|True|String||
|Max Threat Intelligence Sets To Return|Specify how many threat intelligence sets to return. Default is 50.|False|String|50|
|AWS Region|Optionally specify the AWS Region to be used in the action that can be different from the default region specified in the integration configuration page.|False|String||



##### JSON Results
```json
{"ThreatIntelSetIds": ["14ba8b942b76c1be6d985715eb7443eb"]}
```









## Connectors
#### AWS GuardDuty - Findings Connector
Pull findings from AWS GuardDuty. Note: Whitelist works with Finding types, for example, UnauthorizedAccess:EC2/RDPBruteForce.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|Type|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|AWS Access Key ID|AWS Access Key ID to use in integration.|True|String||
|AWS Secret Key|AWS Secret Key to use in integration.|True|Password|*****|
|AWS Default Region|AWS default region to use in integration, for example us-west-2.|True|String||
|Detector ID|ID of the detector. It can be found in the "Settings" tab.|True|String||
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Findings To Fetch|How many findings to process per one connector iteration. Maximum is 50. This is a GuardDuty limitation.|True|Integer|50|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch findings. Possible values are in range from 1 to 8. Note: AWS GuardDuty maps the integer value in the following order: 1,2,3 - Low; 4,5,6 - Medium; 7,8 - High.|True|String|1|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.