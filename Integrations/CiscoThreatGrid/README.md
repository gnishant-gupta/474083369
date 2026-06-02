
# CiscoThreatGrid

Threat Grid combines advanced sandboxing with threat intelligence into one unified solution to protect organizations from malware.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root||True|None|https://x.x.x.x|
|Api Key||True|Password|*****|
|Use SSL||False|Boolean||


#### Dependencies
| |
|-|
|pycparser-3.0-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|paramiko-3.4.0-py3-none-any.whl|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|bcrypt-5.0.0-cp39-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|idna-3.13-py3-none-any.whl|
|tzdata-2026.2-py2.py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|cryptography-47.0.0-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|six-1.17.0-py2.py3-none-any.whl|
|pynacl-1.6.2-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|arrow-1.4.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Get Submissions
Get submissions by entity
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark as suspicious if max threat score pass the threshold|True|String|50|
|Max Submissions To Return|Specify how many submissions to return per entitiy. Default: 10. Maximum: 100|False|String|10|



##### JSON Results
```json
[{"EntityResult": [{"Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe", "Submitted": "2018-06-13T09:16:12Z", "Score": 95, "Indicators": 20, "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894", "MD5": "5fa6b79842cec6d8d172fb16e56b7247"}, {"Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe", "Submitted": "2018-06-13T09:15:51Z", "Score": 95, "Indicators": 21, "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894", "MD5": "5fa6b79842cec6d8d172fb16e56b7247"}, {"Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe", "Submitted": "2018-06-13T09:14:38Z", "Score": 95, "Indicators": 20, "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894", "MD5": "5fa6b79842cec6d8d172fb16e56b7247"}, {"Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe", "Submitted": "2018-06-13T09:13:12Z", "Score": 95, "Indicators": 19, "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894", "MD5": "5fa6b79842cec6d8d172fb16e56b7247"}, {"Name": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894.exe", "Submitted": "2018-06-13T09:12:27Z", "Score": 95, "Indicators": 19, "SHA256": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894", "MD5": "5fa6b79842cec6d8d172fb16e56b7247"}], "Entity": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Get Hash Associated IPs
Get IPs associated to a given hash
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": ["95.128.128.129", "192.168.1.255", "192.168.1.1"], "Entity": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"}]
```



#### Get Hash Associated Domains
Get domains associated to a given hash
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": ["migsel.com"], "Entity": "dfdca325e9a23bb0131d1f887480481f961f3df919a0609d6472381e76a53894"}]
```



#### Upload Sample
Upload and analyze a sample. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vm|The vm to run the analysis on. e.g. win7-x64|False|String|None|
|File Path|The sample file path|True|String|None|
|Playbook|Name of a playbook to apply to this sample run. e.g. default|False|String|None|
|Network Exit|Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location.|False|String|None|
|Private|if checked, the sample will be marked private|False|Boolean|true|
|Linux Server Address|Specify the IP address of the remote linux server, where the file is located.|False|String||
|Linux Username|Specify the username of the remote linux server, where the file is located.|False|String||
|Linux Password|Specify the password of the remote linux server, where the file is located.|False|Password|*****|



##### JSON Results
```json
{"count": 0, "max-confidence": 0, "sample": "99ca73a47996cc3069e39a672728a49c", "score": 0, "bis": [], "max-severity": 0}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.