
# AWSCloudWatch

Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing you with a unified view of AWS resources, applications, and services that run on AWS and on-premises servers. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.

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
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|jmespath-1.0.1-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|botocore-1.35.4-py3-none-any.whl|
|boto3-1.35.4-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|


## Actions
#### List Log Streams
List available log streams in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Groups|Specify a comma-separated list of group names for which you want to retrieve log streams.|True|String||
|Order By|Specify how the log streams should be ordered.|False|List|Log Stream Name|
|Sort Order|Specify how the log streams should be sorted.|False|List|Ascending|
|Max Streams To Return|Specify how many streams to return per log group. Default: 50.|False|String|50|



##### JSON Results
```json
[[{"group": "Siemplify", "logStreams": [{"arn": "arn:aws:logs:x-x-x:123456789:log-group:Siemplify:log-stream:XXXX", "creationTime": "2020-12-03T11:15:02Z", "firstEventTimestamp": "2020-12-03T11:16:37Z", "lastEventTimestamp": "2020-12-03T11:17:29Z", "lastIngestionTime": 1606994249760, "logStreamName": "XXXX", "storedBytes": "", "uploadSequenceToken": "123456789XXXXX"}]}]]
```



#### Create Log Group
Create a log group in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group Name|Specify the name for the new log group.|True|String||



##### JSON Results
```json
{"group_name": "Amit2Test"}
```



#### Delete Log Group
Delete a log group in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group Name|Specify the name of the log group that needs to be deleted.|True|String||



#### Delete Log Stream
Delete a log stream in a log group in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group Name|Specify the name of the log group that contains the log stream.|True|String||
|Log Stream Name|Specify the name of the log stream that needs to be deleted.|True|String||



#### Remove Retention Policy
Remove the retention policy from the log group in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group|Specify the name of the log group from which you want to remove the retention policy.|True|String||



#### Search Log Events
Search log events in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group|Specify the name of the log group, where you want to search for events.|True|String||
|Log Streams|Specify a comma-separated list of log streams, where you want to search for events.|False|String||
|Time Frame|Specify a time frame for the search. If “Custom” is selected, you also need to provide “Start Time”.|False|List|Last Hour|
|Start Time|Specify the start time for the search. This parameter is mandatory, if “Custom” is selected for the “Time Frame” parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the search. Format: ISO 8601. If nothing is provided and “Custom” is selected for the “Time Frame” parameter then this parameter will use current time.|False|String||
|Custom Filter|Specify the custom filter for the search. For additional information please refer to the documentation portal.|False|String||
|Max Events To Return|Specify how many events to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"eventId": "1213456789", "ingestionTime": "2021-03-07T09:37:46Z", "logStreamName": "Amit2Test", "message": "Amit1", "timestamp": "2021-03-07T09:37:50Z"}]
```



#### Set Retention Policy
Set the retention policy for log groups in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group|Specify the name of the log group for which you want to set the retention policy.|True|String||
|Retention Days|Specify for how many days the data should be retained in the log group.|True|List|1|



#### List Log Groups
List available log groups in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Groups To Return|Specify how many groups to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"arn": "arn:aws:logs:XX-XXX-X:123456789:log-group:CloudTrail/DefaultLogGroup:*", "creationTime": "2021-01-25T13:36:35Z", "logGroupName": "CloudTrail/DefaultLogGroup", "metricFilterCount": 0, "storedBytes": 123456789}]
```



#### Create Log Stream
Create a log stream for the log group in AWS CloudWatch.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log Group|Specify the name of the log group, where you want to create a log stream.|True|String||
|Log Stream Name|Specify the name for the new log stream.|True|String||



##### JSON Results
```json
{"log_stream": "Amit2Test3"}
```



#### Ping
Test connectivity to AWS CloudWatch with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.