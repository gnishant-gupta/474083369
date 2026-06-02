
# Cuckoo

Cuckoo Sandbox is an advanced, extremely modular, and 100% open source automated malware analysis system with infinite application opportunities. Cuckoo provides you all the requirements to easily integrate the sandbox into your existing framework and backend in the way you want, with the format you want, and all of that without licensing requirements.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root||True|None|http://x.x.x.x:8090|
|Web Interface Address||True|None|http://x.x.x.x:8000|
|Warning Threshold||True|Integer|5.0|
|CA Certificate File||False|String||
|API Token||False|Password|*****|
|Verify SSL||False|Boolean|False|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Detonate File
Submit a file for analysis and get a report (async)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|The path of the file to submit|True|String||



##### JSON Results
```json
{"powershell8693919272434274241.ps1": {"info": {"category": "file", "added": 1547640117.991152, "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09", "package": "ps1", "started": 1547640190.471362, "route": "internet", "custom": null, "machine": {"status": "stopped", "shutdown_on": "2019-01-16 12:28:55", "started_on": "2019-01-16 12:03:16", "manager": "VirtualBox", "label": "win7x6427", "name": "win7x6427"}, "ended": 1547641736.394026, "score": 6.6, "platform": "windows", "version": "2.0.6", "owner": null, "git": {"head": "03731c4c136532389e93239ac6c3ad38441f81a7", "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"}, "options": "procmemdump=yes,route=internet", "id": 889621, "duration": 1545}, "signatures": [{"families": [], "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic", "name": "network_cnc_http", "markcount": 1, "references": [], "marks": [{"suspicious_features": "Connection to IP address", "type": "generic", "suspicious_request": "GET http://1.1.1.1:8080/"}], "severity": 2}, {"families": [], "description": "Connects to smtp.live.com, possibly for spamming or data exfiltration", "name": "smtp_live", "markcount": 1, "references": [], "marks": [{"category": "domain", "type": "ioc", "ioc": "smtp.live.com", "description": null}], "severity": 2}, {"families": [], "description": "Connects to smtp.mail.yahoo.com, possibly for spamming or data exfiltration", "name": "smtp_yahoo", "markcount": 1, "references": [], "marks": [{"category": "domain", "type": "ioc", "ioc": "smtp.mail.yahoo.com", "description": null}], "severity": 2}]}}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Detonate Url
Send a URL for analysis and get a report (async)
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"info": {"category": "url", "git": {"head": "03731c4c136532389e93239ac6c3ad38441f81a7", "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"}, "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09", "package": "ie", "started": null, "route": "internet", "custom": null, "machine": {"status": "stopped", "shutdown_on": "2019-01-16 13:14:26", "label": "win7x6412", "manager": "VirtualBox", "started_on": "2019-01-16 12:48:54", "name": "win7x6412"}, "ended": 1547644467.207864, "added": null, "id": 889669, "platform": null, "version": "2.0.6", "owner": null, "score": 4.4, "options": "procmemdump=yes,route=internet", "duration": null}, "signatures": [{"families": [], "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic", "name": "network_cnc_http", "markcount": 1, "references": [], "marks": [{"suspicious_features": "Connection to IP address", "type": "generic", "suspicious_request": "GET http://1.1.1.1:8080/"}], "severity": 2}, {"families": [], "description": "Performs some HTTP requests", "name": "network_http", "markcount": 9, "references": [], "marks": [{"category": "request", "ioc": "GET http://crl.microsoft.com/pki/crl/products/WinPCA.crl", "type": "ioc", "description": null}, {"category": "request", "ioc": "GET http://www.microsoft.com/pki/crl/products/WinPCA.crl", "type": "ioc", "description": null}, {"category": "request", "ioc": "GET http://crl.microsoft.com/pki/crl/products/MicrosoftTimeStampPCA.crl", "type": "ioc", "description": null}], "severity": 2}, {"families": [], "description": "Communicates with host for which no DNS query was performed", "name": "nolookup_communication", "markcount": 11, "references": [], "marks": [{"host": "1.1.1.1", "type": "generic"}, {"host": "1.1.1.1", "type": "generic"}, {"host": "1.1.1.1", "type": "generic"}], "severity": 3}]}, "Entity": "http://digi.ba/eng/#pgc-56-0-0"}]
```



#### Get Report
Get report of a particular task by id (async)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task ID|The task's id. e.g. 10|True|String||



##### JSON Results
```json
{"info": {"category": "file", "added": 1547640117.991152, "monitor": "22c39cbb35f4d916477b47453673bc50bcd0df09", "package": "ps1", "started": 1547640190.471362, "route": "internet", "custom": null, "machine": {"status": "stopped", "shutdown_on": "2019-01-16 12:28:55", "started_on": "2019-01-16 12:03:16", "manager": "VirtualBox", "label": "win7x6427", "name": "win7x6427"}, "ended": 1547641736.394026, "score": 6.6, "platform": "windows", "version": "2.0.6", "owner": null, "git": {"head": "03731c4c136532389e93239ac6c3ad38441f81a7", "fetch_head": "03731c4c136532389e93239ac6c3ad38441f81a7"}, "options": "procmemdump=yes,route=internet", "id": 889621, "duration": 1545}, "signatures": [{"families": [], "description": "HTTP traffic contains suspicious features which may be indicative of malware related traffic", "name": "network_cnc_http", "markcount": 1, "references": [], "marks": [{"suspicious_features": "Connection to IP address", "type": "generic", "suspicious_request": "GET http://1.1.1.1:8080/"}], "severity": 2}, {"families": [], "description": "Connects to smtp.live.com, possibly for spamming or data exfiltration", "name": "smtp_live", "markcount": 1, "references": [], "marks": [{"category": "domain", "type": "ioc", "ioc": "smtp.live.com", "description": null}], "severity": 2}, {"families": [], "description": "Connects to smtp.mail.yahoo.com, possibly for spamming or data exfiltration", "name": "smtp_yahoo", "markcount": 1, "references": [], "marks": [{"category": "domain", "type": "ioc", "ioc": "smtp.mail.yahoo.com", "description": null}], "severity": 2}]}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.