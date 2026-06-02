
# DigitalShadows

Digital Shadows is designed to protect you from external threats, continually identifying where your assets are exposed, providing sufficient context to understand the risk, and options for remediation.


Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Key||True|String||
|Api Secret||True|Password|*****|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### EnrichCVE
Enrich a CVE using Digital Shadows information.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"content": [{"snippet": "CVE ID: <em>CVE-2011-0489</em><br><br>", "sortDate": "2017-08-17T01:33:00.000Z", "type": "VULNERABILITY", "entity": {"updated": "2017-08-17T01:33:00.000Z", "cveIdentifier": "CVE-2011-0489", "description": "The server components in Objectivity/DB 10.0 do not require authentication for administrative commands, which allows remote attackers to modify data, obtain sensitive information, or cause a denial of service by sending requests over TCP to (1) the Lock Server or (2) the Advanced Multithreaded Server, as demonstrated by commands that are ordinarily sent by the (a) ookillls and (b) oostopams applications.  NOTE: some of these details are obtained from third party information.", "sourceUri": "https://nvd.nist.gov/vuln/detail/CVE-2011-0489", "created": "2011-01-18T18:03:00.000Z", "cvss2Score": {"accessComplexity": "LOW", "availabilityImpact": "PARTIAL", "authentication": "NONE", "baseScore": 7.5, "integrityImpact": "PARTIAL", "confidentialityImpact": "PARTIAL", "accessVector": "NETWORK"}, "relatedCPEs": ["cpe:/a:objectivity:objectivity%2fdb:10.0"]}}, {"snippet": "Related CVEs: <em>CVE-2011-0489</em><br><br>#!/usr/bin/python\r\n# obj.py\r\n# Objectivity/DB Lack of Authentication Remote Exploit\r\n# Jeremy Brown [0xjbrown41-gmail-com]\r\n# Jan 2011\r\n#\r\n# &quot;Objectivity, Inc. is a leader in distributed, scalable database technology.\r\n# Our patented data management engine and persistent object store is the enabling", "sortDate": "2011-01-14T00:00:00.000Z", "type": "EXPLOIT", "entity": {"sourceUri": "https://www.exploit-db.com/exploits/15988", "sourceCode": "IyEvdXNyL2Jpbi9weXRob24NCiMgb2JqLnB5DQojIE9iamVjdGl2aXR5L0RCIExhY2sgb2YgQXV0aGVudGljYXRpb24gUmVtb3RlIEV4cGxvaXQNCiMgSmVyZW15IEJyb3duIFsweGpicm93bjQxLWdtYWlsLWNvbV0NCiMgSmFuIDIwMTENCiMNCiMgIk9iamVjdGl2aXR5LCBJbmMuIGlzIGEgbGVhZGVyIGluIGRpc3RyaWJ1dGVkLCBzY2FsYWJsZSBkYXRhYmFzZSB0ZWNobm9sb2d5Lg0KIyBPdXIgcGF0ZW50ZWQgZGF0YSBtYW5hZ2VtZW50IGVuZ2luZSBhbmQgcGVyc2lzdGVudCBvYmplY3Qgc3RvcmUgaXMgdGhlIGVuYWJsaW5nDQojIHRlY2hub2xvZ3kgcG93ZXJpbmcgc29tZSBvZiB0aGUgbW9zdCBjb21wbGV4IGFwcGxpY2F0aW9ucyBhbmQgbWlzc2lvbiBjcml0aWNhbA0KIyBzeXN0ZW1zIHVzZWQgaW4gZ292ZXJubWVudCwgYnVzaW5lc3MgYW5kIHNjaWVuY2Ugb3JnYW5pemF0aW9ucyB0b2RheS4iDQojDQojIE9iamVjdGl2aXR5L0RCIGluY2x1ZGVzIG1hbnkgZGlmZmVyZW50IHRvb2xzIGZvciBhZG1pbmlzdHJhdGlvbi4gVGhlDQojIHByb2JsZW0gaXMsIGFueW9uZSBjYW4gdXNlIHRoZXNlIHRvb2xzIHRvIHBlcmZvcm0gb3BlcmF0aW9ucyBvbiB0aGUgaG9zdA0KIyBydW5uaW5nIHRoZSBsb2NrIHNlcnZlciwgYWR2YW5jZWQgbXVsdGl0aHJlYWRlZCBzZXJ2ZXIsIGFuZCBwcm9iYWJseQ0KIyBpdCdzIG90aGVyIHNlcnZlcnMgYXMgd2VsbCwgd2l0aG91dCBhbnkgYXV0aGVudGljYXRpb24uIFRoaXMgZGVzaWduIGZsYXcNCiMgcHV0cyB0aGUgaG9zdCBydW5uaW5nIHRoZXNlIHNlcnZlcnMgYXQgcmlzayBvZiBwb3RlbnRpYWxseSB1bmF1dGhvcml6ZWQNCiMgb3BlcmF0aW9ucyBiZWluZyBwZXJmb3JtZWQgb24gdGhlIHN5c3RlbSwgbG9jYWxseSBvciByZW1vdGVseS4NCiMNCiMgVGhpcyBjb2RlIGRlbW9zdHJhdGVzIGEgY291cGxlIG9mIHRoZSBlYXNpZXN0IG9wZXJhdGlvbnMgdG8gcmVwbGljYXRlDQojIGJ5IGhhbmQsIGxpa2Uga2lsbGluZyB0aGUgbG9jayBhbmQgYW0gc2VydmVycy4gVGhlIHN1aXRlIGNvbnRhaW5zIGxvdHMNCiMgb2Ygb3RoZXIgYWRtaW4gdG9vbHMgdGhhdCBkbyB2YXJpb3VzLCBtb3JlIGludGVyZXN0aW5nIHRhc2tzIHdpdGggdGhlDQojIE9iamVjdGl2aXR5L0RCLCBzdWNoIGFzIG9vYmFja3VwLCBvb25ld2ZkLCBvb2RlbGV0ZWZkLCBvb2RlYnVnLCBldGMuLi4NCiMNCiMgVGVzdGVkIG9uIE9iamVjdGl2aXR5L0RCIDEwIHJ1bm5pbmcgb24gV2luZG93cw0KIw0KIyBGaXhlZCB2ZXJzaW9uOiBOL0EsIFVTLUNFUlQgY29vcmRpbmF0ZWQgdGhlIGNvbW11bmljYXRpb24gYW5kIHJlbGVhc2VkDQojIGEgdnVsbmVyYWJpbGl0eSBub3RlIGFmdGVyIHRoZSB2ZW5kb3IgZGlkIG5vdCBwcm92aWRlIGFkZGl0aW9uYWwgZmVlZGJhY2suDQojDQojIGh0dHA6Ly93d3cua2IuY2VydC5vcmcvdnVscy9pZC83ODI1NjcNCiMNCg0KaW1wb3J0IHN5cw0KaW1wb3J0IHNvY2tldA0KDQpraWxsX29vYW1zPSgNCiJceDBkXHgwMyIrDQoiXHgwMCIqNSsNCiJceDAyIisNCiJceDAwIiozKw0KIlx4MTlceGYwXHg5Mlx4ZWRceDg5XHhmNFx4ZThceDk1XHg0M1x4MDMiKw0KIlx4MDAiKjE1Kw0KIlx4NjFceDYyXHg2MyIrDQoiXHgwMCIrDQoiXHgzMVx4MzJceDMzXHgzNCIrDQoiXHgwMCIqMysNCiJceDA1XHg4YyIrDQoiXHgwMCIqMysNCiJceDBkIisNCiJceDAwIio0DQopDQoNCmtpbGxfb29scz0oDQoiXHgwZFx4MDMiKw0KIlx4MDAiKjUrDQoiXHg3NyIrDQoiXHgwMCIqMysNCiJceDA0XHhhZFx4YzRceGFlXHhkYVx4OWVceDQ4XHhkNlx4NDRceDAzIisNCiJceDAwIioxNQ0KKQ0KDQppZiBsZW4oc3lzLmFyZ3YpPDM6DQogICAgIHByaW50ICJPYmplY3Rpdml0eS9EQiBSZW1vdGUgRXhwbG9pdCINCiAgICAgcHJpbnQgIlVzYWdlOiAlcyA8dGFyZ2V0PiA8b3BlcmF0aW9uPiIlc3lzLmFyZ3ZbMF0NCiAgICAgcHJpbnQgIlxuV2hhdCB3b3VsZCB5b3UgbGlrZSB0byBkbz9cbiINCiAgICAgcHJpbnQgIlsxXSBLaWxsIHRoZSBhZHZhbmNlZCBtdWx0aXRocmVhZGVkIHNlcnZlciINCiAgICAgcHJpbnQgIlsyXSBLaWxsIHRoZSBsb2NrIHNlcnZlciINCiAgICAgcHJpbnQgIkZvciBvdGhlciBvcGVyYXRpb25zLCBjaGVjayBvdXQgb29iYWNrdXAsIG9vZGVidWcsIGV0YyINCiAgICAgc3lzLmV4aXQoMCkNCg0KdGFyZ2V0PXN5cy5hcmd2WzFdDQpvcD1pbnQoc3lzLmFyZ3ZbMl0pDQoNCmlmKChvcDwxKXwob3A+MikpOg0KICAgICBwcmludCAiSW52YWxpZCBvcGVyYXRpb24iDQogICAgIHN5cy5leGl0KDEpDQoNCmlmKG9wPT0xKToNCiAgICAgcG9ydD02Nzc5DQogICAgIGRhdGE9a2lsbF9vb2Ftcw0KDQppZihvcD09Mik6DQogICAgIHBvcnQ9Njc4MA0KICAgICBkYXRhPWtpbGxfb29scw0KDQpjcz10YXJnZXQscG9ydA0KDQpzb2NrPXNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsc29ja2V0LlNPQ0tfU1RSRUFNKQ0Kc29jay5jb25uZWN0KGNzKQ0KDQpzb2NrLnNlbmQoZGF0YSkNCg0Kc29jay5jbG9zZSgp", "internalId": 1864, "title": "Objectivity/DB - Lack of Authentication Remote Exploit", "relatedExploits": [], "source": "EXPLOIT_DB", "platform": "windows", "relatedCveIds": ["CVE-2011-0489"], "published": "2011-01-14", "type": "DOS", "id": "114e9534-0bc9-4aef-928f-63a838c700af"}}]}, "Entity": "CVE-2011-0489"}]
```



#### EnrichURL
Enrich a Url using Digital Shadows information.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"content": [{"snippet": "Domain: <em>example.com</em><br><br>", "sortDate": "2019-10-10T11:29:36.000Z", "type": "DOMAIN_WHOIS", "entity": {"rawText": "xxxxxxx", "domain": "example.com", "zone": {"address": {}}, "billing": {"address": {}}, "created": "2017-05-26T11:11:13.000Z", "nameServers": ["ns2.example.com", "ns1.example.com", "ns3.example.com"], "expires": "2025-05-26T00:00:00.000Z", "updated": "2019-10-10T11:29:36.000Z", "technical": {"name": "xxxxxxx", "address": {"street1": "xxxxxxx", "country": "xxxxxxx", "city": "Praha 9"}}, "registrar": "xxxxxxx", "administrative": {"address": {}}, "registrant": {"organization": "xxxxxx", "name": "xxxxxxxx", "address": {"street1": "xxxxxx", "country": "xxxxxxx", "city": "Praha 9"}}, "statuses": []}}]}, "Entity": "example.com"}, {"EntityResult": {"content": [{"snippet": "Domain: <em>example.com</em><br><br>", "sortDate": "2019-10-10T11:29:36.000Z", "type": "DOMAIN_WHOIS", "entity": {"rawText": "xxxxxxxx", "domain": "example.com", "zone": {"address": {}}, "billing": {"address": {}}, "created": "2001-02-22T16:12:00.000Z", "nameServers": ["ns2.example.com", "ns1.example.com", "ns3.example.com"], "expires": "2024-02-23T00:00:00.000Z", "updated": "2019-10-10T11:29:36.000Z", "technical": {"name": "example.com", "address": {"street1": "example.com", "country": "example.com", "city": "Praha 9"}}, "registrar": "example.com", "administrative": {"organization": "xxxxxxxx", "name": "xxxxxxxx", "address": {"street1": "xxxxxxx", "country": "xxxxxxx", "city": "Praha 9"}}, "registrant": {"organization": "xxxxxxxx", "name": "xxxxxxxx", "address": {"street1": "xxxxx 217", "country": "xxxxx REPUBLIC", "city": "Praha 9"}}, "statuses": []}}]}, "Entity": "example.com"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### EnrichHash
Deprecated: Enrich a Hash using Digital Shadows information.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"content": [{"type": "CYLANCE_FILE_HASH", "entity": {"status": 0, "fileHashInfo": {"status": "COMPLETE", "hashes": {"sha256": "617F7301FD67E8B5D8AD42D4E94E02CB313FE5AD51770EF93323C6115E52FE98", "md5": "8FE94843A3E655209C57AF587849AC3A", "sha1": "CF0743ED381ADE69BBA3D1DD3D357A8300BCD4AE"}, "generalScore": -1, "classifiers": {"ml": 1, "industry": -1, "human": -1}, "statusCode": 1}, "requestedHash": "617f7301fd67e8b5d8ad42d4e94e02cb313fe5ad51770ef93323c6115e52fe98"}}]}, "Entity": "617f7301fd67e8b5d8ad42d4e94e02cb313fe5ad51770ef93323c6115e52fe98"}]
```



#### EnrichIP
Deprecated: Enrich an Ip using Digital Shadows information.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"content": [{"type": "WEBROOT_IP", "entity": {"reputationScore": 19, "ipReputationHistory": [{"timestamp": "2020-02-21T01:10:01.000Z", "reputation": 18}], "currentlyClassifiedAsThreat": false, "ipGeoInfo": {"city": "newark", "country": "united states", "region": "mid atlantic", "longitude": "-74.19453", "sld": "", "state": "new jersey", "carrier": "cloudflare", "tld": "", "latitude": "40.73873", "organization": "cloudflare  inc.", "asn": "13335"}, "threatCategories": [], "ipIncidentHistory": [{"scanDetails": [], "threatType": "Phishing", "eventDescription": "IP hosts phishing sites", "eventType": "Phishing IPs", "numberOfAttempts": 0, "durationSeconds": 0, "applications": [], "attackDetails": [], "hostingPhishUrls": ["mobillbahis214.com"], "startDateTime": "2020-04-15T06:33:42.000Z", "classifiedAsThreat": false}], "updatedDateTime": "2020-02-21T01:10:01.000Z", "ipThreatHistory": [], "ipAddress": "104.27.163.228", "asn": 13335}}]}, "Entity": "104.27.163.228"}]
```









## Connectors
#### Digital Shadows - Incident Connector
Connector ingest incidents from Digital Shadows into Siemplify.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Key|Digital Shadow API Key.|True|String||
|API Secret|Digital Shadow API Secret.|True|Password|*****|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch findings. Possible values: VERY_HIGH, HIGH, MEDIUM, LOW, VERY_LOW, NONE|True|String|NONE|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Incident Type Filter|Comma-separated list of incident types that should be ingested into Siemplify. By default connector pulls all of the incident types. Example: DATA_LEAKAGE,CYBER_THREAT. Possible Values: DATA_LEAKAGE, CYBER_THREAT, PHYSICAL_SECURITY, SOCIAL_MEDIA_COMPLIANCE, BRAND_PROTECTION, INFRASTRUCTURE.|False|String||
|Max Incidents To Fetch|How many incidents to process per one connector iteration.|False|Integer|50|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Digital Shadow server is valid.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.