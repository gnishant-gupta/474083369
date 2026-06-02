
# DeepSight

Symantec DeepSight Intelligence, formerly known as DeepSight Security Intelligence, is a cloud-based threat intelligence platform that provides data feeds for business security systems and applications, as well as a customer portal with support tools that provide early warnings and alerts, patch details and business.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api key|None|True|Password|*****|
|Use SSL|None|False|Boolean||



## Actions
#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Scan Domain
DeepSight scan domain
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"domain": "amazon.com", "whitelisted": true, "schemaVersion": 2, "whois": {"city": "Reno", "updated": "2014-04-30T00: 00: 00Z", "created": "1994-11-01T00: 00: 00Z", "nameServers": ["NS1.P31.DYNECT.NET", "NS2.P31.DYNECT.NET", "NS3.P31.DYNECT.NET"], "country": "Us", "expires": "2022-10-31T00: 00: 00Z", "person": "Hostmaster,AmazonLegalDept.", "registrar": "MarkmonitorInc.", "postalCode": "89507", "organization": "AmazonTechnologies,Inc.", "email": "john_doe@example.com"}}, "Entity": "amazon.com"}]
```



#### Scan Hash
DeepSight scan hash
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"matiReports": [{"date": "2015-04-27T01:10:47Z", "title": "Laziok Trojan Activity and Infrastructure\u2014January to April 2015", "uri": "/v1/mati/reports/300156", "id": 300156}], "intelligence": {"countries": ["kor", "gtm", "are"], "paths": ["CSIDL_PROFILE\\appdata\\local\\searchlike"], "fileNames": ["SEARCHLIKE.EXE"], "parentProcesses": ["f8403ce30c3a2a42b4604c2cf952533ed828a3d7bdb289b0cec82b8844a72a5a"], "filesCreated": [{"path": "CSIDL_PROFILE\\appdata\\local\\searchlike", "sha256": "6d873e6198f7aca685b4c697dfbf82e3450ed5277c5f3c55b1b6fb0338521e0f", "fileName": "B_SEARCHLIKEEX.EXE"}]}, "detection_name": "Trojan.Mdropper", "activity": {"dns": [{"type": "A", "target": "acroipm2.adobe.com"}], "urls": [{"url": "http://acroipm.adobe.com/assets/102.zip"}]}, "schemaVersion": 3, "sha256": "e46d5472e49793017892cb18a0aa174ff9c5b79cec0a9451f1b70e21b19855c2", "events": [{"pid": 2528, "type": "PROCESS:CURRENT", "target": "C:\\Windows\\SysWOW64\\cmd.exe", "severity": 1, "details": "B41859D39D786D32B23A9D2E00F4011DEC7A02402AE"}], "md5": "a77e89bf60e931477f5858a004fb5e0a", "reputation": "Malicious"}, "Entity": "a77e89bf60e931477f5858a004fb5e0a"}]
```



#### Scan File Name
DeepSight scan file name
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"date": "2015-04-27T01:10Z", "title": "Laziok Trojan Activity and Infrastructure\u2014January to April 2015", "uri": "/v1/mati/reports/300156", "id": 300156}, "Entity": "BadGuy1"}]
```



#### Scan Email
DeepSight scan email
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"date": "2015-04-27T01:10Z", "title": "Laziok Trojan Activity and Infrastructure\u2014January to April 2015", "uri": "/v1/mati/reports/300156", "id": 300156}, "Entity": "john_doe@example.com"}]
```



#### Scan URL
DeepSight scan URL
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"url": "https: //www.facebook.com", "host": {"domain": "facebook.com", "uri": "/v1/domains/facebook.com"}, "whitelisted": true, "schemaVersion": 2, "whois": {"city": "MenloPark", "updated": "2015-08-25T00: 00: 00Z", "created": "1997-03-29T00: 00: 00Z", "nameServers": ["A.NS.FACEBOOK.COM", "B.NS.FACEBOOK.COM"], "country": "Us", "expires": "2020-03-30T00: 00: 00Z", "person": "DomainAdministrator", "registrar": "MarkmonitorInc.", "postalCode": "94025", "organization": "Facebook,Inc.", "email": "john_doe@example.com"}}, "Entity": "https: //www.facebook.com"}]
```



#### Scan IP
DeepSight scan IP address
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"geolocation": {"latitude": 39.91176055, "city": "Beijing", "longitude": 116.3792325, "country": "China"}, "network": {"carrier": "ChinaUnicomBeijingProvinceNetwork", "asn": 4808, "lineSpeed": "High", "ipRouting": "Fixed"}, "targetIndustries": [{"name": "Utilities", "naics": 221}, {"name": "Telecommunications", "naics": 517}], "ip": "1.1.1.1", "whitelisted": false, "behaviours": [{"behaviour": "Attacks", "type": "WWWAttacks", "description": "FakeBrowserUpdate"}], "targetCountries": ["fra", "tur", "twn"], "lastSeen": "2019-01-20T00: 00: 00Z", "urls": [{"url": "http: //iremedypro.com/assets/img/jQuery/014/LOGS/c1dabc02e7c9c23688fcdccb9c94379f", "uri": "/v1/urls/http: //iremedypro.com/assets/img/jQuery/014/LOGS/c1dabc02e7c9c23688fcdccb9c94379f"}], "domains": [{"domain": "iremedypro.com", "uri": "/v1/domains/iremedypro.com"}], "organization": {"isic": "J6110", "type": "InternetServiceProvider", "name": "ChinaUnicomBeijingProvinceNetwork", "naics": 517110}, "schemaVersion": 2, "firstSeen": "2016-01-01T00: 00: 00Z"}, "Entity": "1.1.1.1"}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.