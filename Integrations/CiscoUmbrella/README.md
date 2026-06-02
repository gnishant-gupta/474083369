
# CiscoUmbrella

Cisco Umbrella is a cloud security platform that provides the first line of defense against threats on the internet. Protect users in minutes.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enforcement ApiToken|None|True|Password|*****|
|Investigate ApiToken|None|True|Password|*****|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|


## Actions
#### Delete Domain
Delete domain from the OpenDNS block list
Timeout - 600 Seconds



#### Get Associated Domains
Get associated domains for  a particular hostname
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": ["google.com", "twilio.com", "gmail.com"], "Entity": "amazon.com"}]
```



#### Add Domain
Add domain to the OpenDNS block list
Timeout - 600 Seconds



#### Get Domain Security Info
Provide security information about a domain (as an attachment)
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"found": false, "popularity": 0.0, "geodiversity_normalized": [], "dga_score": -16.878373381058395, "rip_score": 0.0, "asn_score": 0.0, "securerank2": 0.0, "geoscore": 0.0, "attack": "", "ks_test": 0.0, "pagerank": 0.0, "geodiversity": [], "prefix_score": 0.0, "perplexity": 0.9961472993373601, "entropy": 2.2516291673878226, "fastflux": false, "threat_type": "", "tld_geodiversity": []}, "Entity": "zahav1.ru"}]
```



#### Get Domain Status
Provide domain status, its content categories, and security categories.Supported entities: Hostname, URL
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"content_categories": "Ecommerce/Shopping", "status": "1", "security_categories": ""}, "Entity": "amazon.com"}]
```



#### Get Malicious Domains
Get malicious domains for an IP address
Timeout - 600 Seconds



##### JSON Results
```json
{"192.168.0.2": ["d.applovin.com.doesntexist.com", "atdmt.com.doesntexist.com", "adservice.google.com.doesntexist.com"]}
```



#### List Top Domains
Use the “List Top Domains” action to return information about top domains from Cisco Popularity List.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Domains To Return|Max number of domains to return from the list. Maximum: 100000.|False|String|100|



##### JSON Results
```json
[{"order": 123456,"domain": "abcdef"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Is Domain In Cisco Popularity List
Use the Is Domain In Cisco Popularity List action to verify if a domain is present in the Cisco Popularity List. Supported Entities: URL (domain extracted automatically), Domain, Hostname.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "","EntityResult": {"found": "true","entries": [{"order": 123,"domain": ""}]}}]
```



#### Get Whois
Get domain WhoIs details
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"billingContactState": null, "administrativeContactPostalCode": "89507", "zoneContactCity": null, "addresses": ["p.o. box 8102"], "registrantFaxExt": null, "registrantName": "Hostmaster, Amazon Legal Dept.", "auditUpdatedDate": "2019-01-08 12:03:30.000 UTC", "administrativeContactCity": "Reno", "administrativeContactEmail": "john_doe@example.com", "technicalContactFax": "12062667010", "billingContactOrganization": null, "billingContactEmail": null, "technicalContactPostalCode": "89507", "registrantOrganization": "Amazon Technologies, Inc.", "zoneContactPostalCode": null, "registrantState": "NV", "administrativeContactName": "Hostmaster, Amazon Legal Dept.", "billingContactFaxExt": null, "billingContactCity": null, "technicalContactEmail": "john_doe@example.com", "registrantCountry": "UNITED STATES", "technicalContactFaxExt": null, "administrativeContactStreet": ["p.o. box 8102"], "administrativeContactOrganization": "Amazon Technologies, Inc.", "billingContactCountry": null, "billingContactName": null, "registrarName": "MarkMonitor, Inc.", "technicalContactTelephoneExt": null, "administrativeContactFax": null, "zoneContactFax": null, "timestamp": null, "registrantCity": "Reno", "administrativeContactTelephoneExt": null, "status": ["clientDeleteProhibited clientTransferProhibited clientUpdateProhibited serverDeleteProhibited serverTransferProhibited serverUpdateProhibited"], "updated": "2014-04-30", "expires": "2022-10-31", "whoisServers": "whois.markmonitor.com", "technicalContactName": "Hostmaster, Amazon Legal Dept.", "technicalContactState": "NV", "nameServers": ["ns1.p31.dynect.net", "ns2.p31.dynect.net", "ns3.p31.dynect.net"], "zoneContactFaxExt": null, "recordExpired": false, "registrantFax": "12062667010", "registrantTelephoneExt": null, "billingContactFax": null, "technicalContactOrganization": "Amazon Technologies, Inc.", "administrativeContactState": "NV", "zoneContactOrganization": null, "billingContactPostalCode": null, "zoneContactStreet": [], "zoneContactName": null, "registrantPostalCode": "89507", "billingContactTelephone": null, "emails": ["hostmaster@amazon.com"], "registrantTelephone": "12062664064", "administrativeContactCountry": "UNITED STATES", "technicalContactCity": "Reno", "administrativeContactTelephone": "12062664064", "created": "1994-11-01", "registrarIANAID": "292", "registrantStreet": ["p.o. box 8102"], "domainName": "amazon.com", "technicalContactCountry": "UNITED STATES", "billingContactStreet": [], "timeOfLatestRealtimeCheck": 1547718689211, "zoneContactState": null, "registrantEmail": "john_doe@example.com", "administrativeContactFaxExt": null, "billingContactTelephoneExt": null, "zoneContactCountry": null, "zoneContactEmail": null, "zoneContactTelephoneExt": null, "technicalContactTelephone": "12062664064", "technicalContactStreet": ["p.o. box 8102"], "zoneContactTelephone": null, "hasRawText": true}, "Entity": "amazon.com"}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.