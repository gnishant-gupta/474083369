
# Darktrace

Darktrace empowers defenders to reduce risk and minimize cyber disruption. Its Self-Learning AI technology develops a deep and evolving understanding on your bespoke organization, allowing it to prevent, detect, and respond to unpredictable cyber-attacks across the entire digital environment – from cloud and email to endpoints and OT networks.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|String|https://{{api root}}|
|API Token||True|String||
|API Private Token||True|Password|*****|
|Verify SSL||False|Boolean|true|


#### Dependencies
| |
|-|
|rsa-4.9.1-py3-none-any.whl|
|TIPCommon-1.1.0.1-py2.py3-none-any.whl|
|certifi-2025.11.12-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|cachetools-6.2.2-py3-none-any.whl|
|google_auth-2.43.0-py2.py3-none-any.whl|


## Actions
#### List Endpoint Events
List latest events related to the endpoint in Darktrace. Supported entities: IP, Hostname, MacAddress. Note: events will be returned in UTC timezone.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Type|Specify a comma-separated list of event types that they want to return. Possible values: connection, unusualconnection, newconnection, notice, devicehistory, modelbreach.|True|String|connection,unusualconnection,notice|
|Time Frame|Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".|True|List|Last Hour|
|Start Time|Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Events To Return|Specify how many events to return per event type. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Entity": "172.30.xxx.xxx", "EntityResult": {"connection": [{"time": "2021-04-11 23:59:24", "timems": 1618185564100, "action": "connection", "eventType": "connection", "uid": "CRtoOy3YrHw8xxxxxx", "sdid": "9xx", "ddid": "3xx", "port": 53, "sourcePort": 51318, "destinationPort": 53, "direction": "out", "applicationprotocol": "DNS", "protocol": "UDP", "sourceDevice": {"id": "9xx", "did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host", "time": "1614184533000", "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}, "destinationDevice": {"id": "3xx", "did": "3xx", "ip": "172.30.2xx.xx", "ips": [{"ip": "172.30.2xx.xx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "1x"}], "sid": "1x", "hostname": "example.local", "time": "1614091446000", "os": "Windows 7, 8 or 10", "typename": "dnsserver", "typelabel": "DNS Server"}, "source": "host", "destination": "example.local"}], "unusualconnection": [{"time": "2021-04-11 23:58:59", "timems": 1618185539419, "action": "connection", "eventType": "connection", "uid": "CZbWNp3CcmuFzxxxxx", "sdid": "9xx", "port": 21801, "sourcePort": 48663, "destinationPort": 21801, "info": "11 connections at 56 minute intervals.", "direction": "out", "applicationprotocol": "Unknown", "protocol": "UDP", "sourceDevice": {"id": "9xx", "did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host", "time": "1614184533000", "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}, "destinationDevice": {"longitude": 57.181, "latitude": 50.298, "city": "Aktobe", "country": "Kazakhstan", "countrycode": "KZ", "asn": "AS59443 Baynur and P Ltd.", "region": "Asia", "ip": "95.182.x.xx", "ippopularity": "0", "connectionippopularity": "0"}, "source": "host", "destination": "95.182.x.xx"}], "newconnection": [{"time": "2021-04-11 23:45:27", "timems": 1618184727716, "action": "connection", "eventType": "connection", "uid": "CZVz2M1jrGhVOxxxxx", "sdid": "9xx", "port": 2059, "sourcePort": 48663, "destinationPort": 2059, "info": "A new connection externally on port 2059", "direction": "out", "applicationprotocol": "Unknown", "protocol": "UDP", "sourceDevice": {"id": "9xx", "did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host", "time": "1614184533000", "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}, "destinationDevice": {"longitude": 46.718, "latitude": 24.657, "city": "Riyadh", "country": "Saudi Arabia", "countrycode": "SA", "asn": "AS39891 Saudi Telecom Company JSC", "region": "Asia", "ip": "37.224.1xx.xxx", "ippopularity": "100", "connectionippopularity": "67"}, "source": "host", "destination": "37.224.1xx.xxx"}], "notice": [{"time": "2021-04-11 23:58:25", "timems": 1618185505000, "action": "notice", "nuid": "Nmcggxvgovgxxxxx", "eventType": "notice", "nid": "121xxx", "uid": "", "mlid": "2xx", "type": "DT::ModelBreach", "msg": "Device / Activity Identifier / BitTorrent Ports", "size": 45, "detail": {"pid": "8xx"}, "sourceDevice": {"id": "9xx", "did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host", "time": "1614184533000", "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}, "source": "host"}], "devicehistory": [{"time": "2021-04-06 11:25:24", "timems": 1617708324000, "eventType": "deviceHistory", "name": "removetag", "value": "External DNS", "reason": "Expired", "device": {"id": "9xx", "did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618768800000, "time": "2021-04-18 18:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host", "time": "1614184534000", "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}}], "modelbreach": [{"time": "2021-04-11 20:40:19", "timems": 1618173619000, "pbid": "1xx", "pid": "8xx", "phid": "11xx", "action": "policybreach", "eventType": "policybreach", "creationTime": 1618173682000, "creationTimestamp": "2021-04-11 20:41:22", "name": "Compromise::Beacon for 4 Days", "components": ["23xx", "23xx"], "didRestrictions": [], "didExclusions": [], "throttle": 86400, "sharedEndpoints": false, "interval": 3600, "sequenced": false, "active": true, "retired": false, "instanceID": "19xxx", "acknowledged": false, "state": "New", "score": 0.415498, "commentCount": 0, "componentBreaches": ["23xx"], "componentBreachTimes": [1618173618000], "devices": ["9xx"], "deviceLabels": ["host"]}]}}]
```



#### List Similar Devices
List similar devices to the endpoint in Darktrace. Supported entities: IP, Hostname, Mac Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Devices To Return|Specify how many devices to return per entity. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Entity": "00:50:xx:xx:xx:xx", "EntityResult": [{"did": 179, "score": 100, "macaddress": "00:50:xx:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648713600000, "time": "2022-03-31 08:00:00", "sid": 5}], "sid": 5, "hostname": "EPO-xxx", "firstSeen": 1646732712000, "lastSeen": 1648716815000, "typename": "server", "typelabel": "Server"}, {"did": 171, "score": 100, "macaddress": "00:50:xx:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648720800000, "time": "2022-03-31 10:00:00", "sid": 5}], "sid": 5, "hostname": "RSA-xxx", "firstSeen": 1646129271000, "lastSeen": 1648721308000, "typename": "server", "typelabel": "Server"}]}, {"Entity": "WH01-xxx", "EntityResult": [{"did": 179, "score": 100, "macaddress": "00:50:xx:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648713600000, "time": "2022-03-31 08:00:00", "sid": 5}], "sid": 5, "hostname": "EPO-xxx", "firstSeen": 1646732712000, "lastSeen": 1648716815000, "typename": "server", "typelabel": "Server"}, {"did": 171, "score": 100, "macaddress": "00:50:xx:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648720800000, "time": "2022-03-31 10:00:00", "sid": 5}], "sid": 5, "hostname": "RSA-xxx", "firstSeen": 1646129271000, "lastSeen": 1648721308000, "typename": "server", "typelabel": "Server"}]}, {"Entity": "172.30.xxx.xx", "EntityResult": [{"did": 90, "score": 99, "macaddress": "00:50:xx:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1647860400000, "time": "2022-03-21 11:00:00", "sid": 5}], "sid": 5, "hostname": "DESKTOP-xxx", "firstSeen": 1614183620000, "lastSeen": 1647861513000, "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}, {"did": 130, "score": 100, "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648735200000, "time": "2022-03-31 14:00:00", "sid": 1}], "sid": 1, "firstSeen": 1640176281000, "lastSeen": 1648737829000, "os": "Linux 3.11 and newer", "typename": "desktop", "typelabel": "Desktop"}]}]
```



#### Execute Custom Search
Execute custom search in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed.|True|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time". If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened. Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time"|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
{"hits": [{"_index": "logstash-vmprobe-2022.03.30", "_type": "doc", "_id": "AX_aKYBlovxxxxxxxxxx", "_score": null, "_source": {"@fields": {"certificate_not_valid_before": 1635062830, "source_port": "10xxx", "certificate_issuer": "CN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE", "certificate_sig_alg": "sha256WithRSAEncryption", "certificate_not_valid_after": 1669362596, "fid": "FwLteK2Hi3xxxxxxxxxx", "certificate_key_length": 2048, "certificate_key_type": "rsa", "san_dns": ["*.checkpoint.com", "checkpoint.com"], "epochdate": 1648632620.401279, "certificate_key_alg": "rsaEncryption", "certificate_subject": "CN=*.checkpoint.com", "source_ip": "172.30.xxx.xxx", "certificate_exponent": "65xxx", "dest_port": "44xx", "dest_ip": "194.29.xx.xx", "uid": "CCTCpp3JLgxxxxxxxxxx", "certificate_version": 3, "certificate_serial": "7796FB90CCBDAxxxxxxxxxxx", "basic_constraints_ca": false}, "@type": "x509", "@timestamp": "2022-03-30T09:30:20", "@message": "1648632620.4013\\tCCTCpp3JLgxxxxxxxxxx\\t172.30.xxx.xxx\\t10001\\t194.29.xx.xx\\t443\\t-\\t-\\t1635062830\\tCN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE\\tsha256WithRSAEncryption\\t1669362596\\tFwLteK2Hi3xxxxxxxxxx\\t2048\\trsa\\t[*.checkpoint.com,checkpoint.com]\\trsaEncryption\\tCN=*.checkpoint.com\\t65537\\t3\\t7796FB90CCBDAxxxxxxxxxxx\\tfalse", "@darktrace_probe": "1"}, "sort": [1648632620000]}, {"_index": "logstash-vmprobe-2022.03.30", "_type": "doc", "_id": "AX_aJO_jovxxxxxxxxxx", "_score": null, "_source": {"@fields": {"certificate_not_valid_before": 1635062830, "source_port": "10xxx", "certificate_issuer": "CN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE", "certificate_sig_alg": "sha256WithRSAEncryption", "certificate_not_valid_after": 1669362596, "fid": "FfUP05126pxxxxxxxxxx", "certificate_key_length": 2048, "certificate_key_type": "rsa", "san_dns": ["*.checkpoint.com", "checkpoint.com"], "epochdate": 1648632319.884309, "certificate_key_alg": "rsaEncryption", "certificate_subject": "CN=*.checkpoint.com", "source_ip": "172.30.xxx.xxx", "certificate_exponent": "65xxx", "dest_port": "44xx", "dest_ip": "194.29.xx.xx", "uid": "CduWm1xoxxxxxxxxxxx", "certificate_version": 3, "certificate_serial": "7796FB90CCBDAxxxxxxxxxxx", "basic_constraints_ca": false}, "@type": "x509", "@timestamp": "2022-03-30T09:25:19", "@message": "1648632319.8843\\tCduWm1xoxxxxxxxxxxx\\t172.30.xxx.xxx\\t10000\\t194.29.xx.xx\\t443\\t-\\t-\\t1635062830\\tCN=GlobalSign GCC R3 DV TLS CA 2020,O=GlobalSign nv-sa,C=BE\\tsha256WithRSAEncryption\\t1669362596\\tFfUP05126pxxxxxxxxxx\\t2048\\trsa\\t[*.checkpoint.com,checkpoint.com]\\trsaEncryption\\tCN=*.checkpoint.com\\t65537\\t3\\t7796FB90CCBDAxxxxxxxxxxx\\tfalse", "@darktrace_probe": "1"}, "sort": [1648632319000]}]}
```



#### Add Comment To Model Breach
Add a comment to model breach in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Model Breach ID|Specify the ID of the model breach to which you want to add a comment.|True|String||
|Comment|Specify the comment for the model breach.|True|String||



##### JSON Results
```json
{"response": "SUCCESS"}
```



#### Ping
Test connectivity to the Darktrace with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Update Model Breach Status
Update model breach status in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Status|Specify what status to set for the model breach.|True|List|Acknowledged|
|Model Breach ID|Specify the id of the model breach, for which you want to update status.|True|String||



#### Enrich Entities
Enrich entities using information from Darktrace. Supported entities: IP, Hostname, MacAddress, URL. Note: action will extract the domain part out of URL entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fetch Connection Data|If enabled, action will return additional information about connections related to the internal endpoints of Darktrace.|False|Boolean|true|
|Max Hours Backwards|Specify how many hours backwards, action needs to fetch connection data. Default: 24.|False|String|24|
|Create Endpoint Insight|If enabled, action will create an insight containing information about the internal endpoints of Darktrace.|False|Boolean|true|



##### JSON Results
```json
[{"Entity": "https://www.google.com", "EntityResult": {"connection_data": {"deviceInfo": [{"did": "1xx", "similarityScore": 100, "info": {"totalUsed": 0, "totalServed": 0, "totalDevicesAndPorts": 0, "devicesAndPorts": [], "portsUsed": [], "portsServed": [], "devicesUsed": [{"did": "0xx", "size": 100}], "devicesServed": []}}], "devices": [{"did": "1xx", "macaddress": "00:50:56:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648411200000, "time": "2022-03-27 20:00:00", "sid": "0xx"}], "sid": "0xx", "hostname": "EPO-HWxxxx", "firstSeen": 1646732712000, "lastSeen": 1648412675000, "typename": "unknown", "typelabel": "Unknown", "tags": [{"tid": "8xx", "expiry": 0, "thid": "8xx", "name": "Virtual Machine", "restricted": false, "data": {"auto": false, "color": 200, "description": ""}, "isReferenced": true}]}]}, "hostname": "www.google.com", "firsttime": 1614091840000, "devices": [{"did": "1xx", "macaddress": "00:50:56:a2:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.201.xxx", "ips": [{"ip": "172.30.201.xxx", "timems": 1617760800000, "time": "2021-04-07 02:00:00", "sid": "5x"}], "sid": "5x", "hostname": "DESKTOP-CV0RM4M", "firstSeen": 1616749011000, "lastSeen": 1617763005000, "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}], "ips": [{"ip": "142.250.xxx.x", "firsttime": 1615895887000, "lasttime": 1617508137000}, {"ip": "142.250.xxx.xxx", "firsttime": 1617506696000, "lasttime": 1617508377000}], "locations": [{"latitude": 37, "longitude": -122, "country": "United States", "city": "Mountain View"}, {"latitude": 37, "longitude": -97, "country": "United States", "city": ""}]}}, {"Entity": "00:50:56:a2:xx:xx", "EntityResult": {"connection_data": {"deviceInfo": [{"did": "1xx", "similarityScore": 100, "info": {"totalUsed": 0, "totalServed": 0, "totalDevicesAndPorts": 0, "devicesAndPorts": [], "portsUsed": [], "portsServed": [], "devicesUsed": [{"did": "0xx", "size": 100}], "devicesServed": []}}], "devices": [{"did": "1xx", "macaddress": "00:50:56:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1648411200000, "time": "2022-03-27 20:00:00", "sid": "0xx"}], "sid": "0xx", "hostname": "EPO-HWxxxx", "firstSeen": 1646732712000, "lastSeen": 1648412675000, "typename": "unknown", "typelabel": "Unknown", "tags": [{"tid": "8xx", "expiry": 0, "thid": "8xx", "name": "Virtual Machine", "restricted": false, "data": {"auto": false, "color": 200, "description": ""}, "isReferenced": true}]}]}, "id": "9xx", "macaddress": "00:50:56:a2:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618477200000, "time": "2021-04-15 09:00:00", "sid": "5x"}], "did": "9xx", "sid": "5x", "hostname": "host1", "time": 1614183727000, "endtime": 1618478881000, "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}}, {"Entity": "78.60.xxx.x", "EntityResult": {"connection_data": {"deviceInfo": [{"did": "1xx", "similarityScore": 100, "info": {"totalUsed": 133958, "totalServed": 0, "totalDevicesAndPorts": 133958, "devicesAndPorts": [{"deviceAndPort": {"direction": "out", "device": 0, "port": "5xx"}, "size": 32}, {"deviceAndPort": "others", "size": 61}], "externalDomains": [{"domain": "Unknown", "size": 67}, {"domain": "microsoft.com", "size": 7}], "portsUsed": [{"port": "5xx", "size": 64, "firstTime": 1640176079000}], "portsServed": [], "devicesUsed": [{"did": "0xx", "size": 40, "firstTime": 1640176078000}], "devicesServed": []}}], "devices": [{"did": "1xx", "macaddress": "00:50:56:xx:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1647957600000, "time": "2022-03-22 14:00:00", "sid": "1xx"}], "sid": "1xx", "hostname": "SEP-Wxxxxx", "firstSeen": 1640176095000, "lastSeen": 1647958950000, "os": "Windows NT kernel", "typename": "server", "typelabel": "Server"}]}, "ip": "78.60.xxx.x", "firsttime": 1617810778000, "country": "Lithuania", "asn": "AS8764 Telia Lietuva, AB", "city": "Vilnius", "region": "Europe", "name": "", "longitude": 25.298, "latitude": 54.678, "ipage": "1209xxx", "iptime": "2021-04-01 09:54:17", "devices": [{"did": "9xx", "macaddress": "00:50:56:a2:xx:xx", "vendor": "VMware, Inc.", "ip": "172.30.xxx.xxx", "ips": [{"ip": "172.30.xxx.xxx", "timems": 1618477200000, "time": "2021-04-15 09:00:00", "sid": "5x"}], "sid": "5x", "hostname": "host1", "firstSeen": 1614183727000, "lastSeen": 1618478881000, "os": "Windows NT kernel", "typename": "desktop", "typelabel": "Desktop"}]}}]
```









## Connectors
#### Darktrace - AI Incident Events Connector
Pull information about AI incident events from Darktrace. Dynamic list works with "title" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|data_type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Darktrace instance.|True|String|https:/{{api root}}|
|API Token|Darktrace API token|True|String||
|API Private Token|Darktrace API private token|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Darktrace server is valid.|False|Boolean|true|
|Lowest AI Incident Score To Fetch|Lowest score that will be used to fetch AI incidents. Maximum: 100.|True|Integer|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max AI Incidents To Fetch|How many model breaches to process per one connector iteration. Maximum is 100.|False|Integer|10|
|Use dynamic list as a blocklist|If enabled, dynamic list will be used as a blocklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|


#### Darktrace - Model Breaches Connector
Pull information about model breaches and connections events related to them from Darktrace.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|eventType|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Darktrace instance.|True|String|https:/{{api root}}|
|API Token|Darktrace API token|True|String||
|API Private Token|Darktrace API private token|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Darktrace server is valid.|False|Boolean|true|
|Lowest Model Breach Score To Fetch|Lowest score that will be used to fetch model breaches. Maximum: 100.|False|Integer|0|
|Lowest Priority To Fetch|Lowest priority that will be used to fetch model breaches. Provided as integer. 1, 2, 3 - Informational, 4 - Suspicious, 5 - Critical|False|Integer||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve model breaches from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Model Breaches To Fetch|How many model breaches to process per one connector iteration. Maximum is 1000.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Behaviour Visibility|Behavior visibility values that need to be ingested. Possible values: Critical, Suspicious, Compliance, Informational.|False|String||
|Padding Time|Amount of hours that will be used as a padding. If nothing is provided, this parameter is not going to be applied. Max 100 hours.|False|Integer||





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.