
# ProofPointTAP

Proofpoint Targeted Attack Protection™ is the industry's first comprehensive solution for combatting targeted threats using a full lifecycle approach, monitoring suspicious messages containing malicious URLs or malicious attachments, and observing user clicks as they attempt to reach out.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://tap-api-v2.proofpoint.com|
|Username|None|True|String||
|Password|None|True|Password|*****|
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.24.2-py3-none-any.whl|
|pycryptodome-3.22.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.166.0-py2.py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|protobuf-6.30.2-cp39-abi3-manylinux2014_x86_64.whl|
|rsa-4.9-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|anyio-4.9.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|
|pyparsing-3.2.3-py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|typing_extensions-4.13.0-py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|googleapis_common_protos-1.69.2-py3-none-any.whl|
|TIPCommon-2.2.0-py2.py3-none-any.whl|


## Actions
#### DecodeURL
Decode URLs in Proofpoint TAP. Supported entities: URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Encoded URLs|Specify a comma-separated list of URLs that need to be decoded. Note: URL entities in the scope of the alert will be decoded together.|False|String|None|
|Create URL Entities|If enabled, action will create URL entities that were successfully decoded.|False|Boolean|true|



##### JSON Results
```json
[{"encodedUrl":"https://urldefense.com/v3/__https://firebasestorage.googleapis.com/v0/b/gund-50757.appspot.com/o/owa*2Findex2gun.html?alt=media&token=02497332-ff04-xxxxxxx-a76b-xxxxx*vicky@rsrchxchange.com__;JSM!!Fjc1LPEtn8I!xxxxx-xxxxxxxx$","decodedUrl":"https://firebasestorage.googleapis.com/v0/b/gund-xxxxx.appspot.com/o/owa%2Findex2gun.html?alt=media&token=xxxx-ff04-xxxxxx-a76b-xxxxxx#vicky@rsrchxchange.com","success":true}]
```



#### Ping
Test connectivity to the Proofpoint TAP with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Get Threat Forensics
Use the Get Threat Forensics action to return forensics associated with a threat in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threat ID|Comma-separated list of threat IDs for which forensics need to be returned.|True|String||
|Include Campaign Forensics|If enabled, action will also return campaign forensics related to the provided threat.|False|Boolean|false|
|Max Results To Return|How many results to return per threat id. Default: 50. Maximum: 1000.|True|String|50|



##### JSON Results
```json
[{"scope": "THREAT", "id": "abc", "name": "abc", "threatStatus": "active", "forensics": [{"type": "attachment", "display": "Attachment with SHA-256: abc", "engine": "iee", "malicious": true, "note": "PayPal phish", "time": 0, "what": {"rule": "6a0c"}, "platforms": [{"name": "static", "os": "static", "version": "0"}]}]}]
```



#### List Campaigns
Use the List Campaigns action to return a list of active campaigns in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results to return. Default: 50. Maximum: 1000.|True|String|50|



##### JSON Results
```json
{"campaigns": [{"id": "abc", "lastUpdatedAt": "2025-04-18T11:56:49.000Z", "notable": false, "verticallyTargeted": false}]}
```



#### GetCampaign
Return information about campaigns in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Campaign ID|Specify a comma-separated list of campaign IDs for which you want to return info.|True|String||
|Create Insight|If enabled, action will create an insight containing information about the campaign.|False|Boolean|true|
|Create Threat Campaign Entity|If enabled, action will create a threat campaign entity from the enriched campaigns.|False|Boolean|true|
|Fetch Forensics Info|If enabled, action will return forensics information about the campaigns.|False|Boolean|true|
|Forensic Evidence Type Filter|Specify a comma-separated list of evidence types that need to be returned, when fetching forensic info. Possible values: attachment, cookie, dns, dropper, file, ids, mutex, network, process, registry, screenshot, url, redirect_chain, behavior.|False|String|attachment,dns, dropper, file, network, process, registry, screenshot, url, redirect_chain|
|Max Forensics Evidence To Return|Specify how much evidence to return per campaign. Default: 50. Maximum: 1000.|False|String|50|



##### JSON Results
```json
[{"id":"fd50bbd0-5529-41b5-b8a4-xxxxxxx","name":"Amazon Phishing Japan | 22 Aug - 28 Aug 2021","description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.","startDate":"2021-08-22T00:00:00.000Z","notable":false,"actors":[],"families":[{"id":"d8162758-80f1-46ec-9ae4-xxxxxx","name":"Consumer Credential Phishing"},{"id":"34b3f509-c74c-4d33-a29d-xxxxxx","name":"Corporate Credential Phishing"}],"malware":[],"techniques":[{"id":"70a76992-2be1-4a70-a96b-xxxxx","name":"Social Engineering"}],"brands":[{"id":"b1456f2f-b657-4853-ac8a-xxxx","name":"Amazon"}],"campaignMembers":[{"id":"55d8e1f30a7a8fff1ee5785bb543f72b22778ec690543xxxxxxx","threat":"https://arnazon.co.ip.fjdfaq.shop","threatStatus":"active","type":"url","threatTime":"2021-08-23T14:44:12.000Z"}],"forensics":{"scope":"CAMPAIGN","id":"fd50bbd0-5529-41b5-b8a4-xxxxxxxxx","name":"Amazon Phishing 22 Aug - 28 Aug 2021","forensics":[{"type":"file","display":"File 01Scss[1].css created","engine":"iee","malicious":false,"time":0,"what":{"sha256":"8afa0e13c86a1d3d734fca7fcfc187xxxxxxxxx","size":52274,"path":"C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\N6XTLFY7\\01Scss[1].css"},"platforms":[{"name":"Win10","os":"win","version":"win10"}]},{"type":"url","display":"URL: https://amazoncard-info.pyaxmcusinamz.shop/signim/style/css/61ccss.css","engine":"iee","malicious":false,"time":0,"what":{"url":"https://amazoncard-info.pyaxmcusinamz.shop/signim/style/css/61ccss.css"},"platforms":[{"name":"Win10","os":"win","version":"win10"}]},{"type":"screenshot","display":"Screenshot","engine":"tstatic","malicious":true,"note":"Screenshot","time":0,"what":{"url":"https://udscreens.proofpoint.com/torcs_url/A0/07/A0071DD54E2584884DCBDF6D5128AExxxxx5168F/40cdc0269fa9xxxxxx"},"platforms":[{"name":"static","os":"static","version":"0"}]},{"type":"network","display":"TCP connection to 54.230.xx.xxx:443","engine":"iee","malicious":false,"time":0,"what":{"action":"connect","ip":"54.230.xx.xx","port":443,"type":"tcp"},"platforms":[{"name":"Win10","os":"win","version":"win10"}]},{"type":"redirect_chain","display":"redirect chain for http://aonzon.co.ip.xxxxxx.cn/","engine":"tstatic","malicious":true,"time":0,"what":{"url":"https://aonzon.co.ip.xxxxx.cn/"},"platforms":[{"name":"static","os":"static","version":"0"}]},{"type":"dns","display":"DNS lookup of host: images-cn.ssl-images-amazon.com","engine":"iee","malicious":false,"time":0,"what":{"host":"images-cn.ssl-images-amazon.com","ips":["99.84.xx.xx"],"cnames":["d17xrurxxlapdp.cloudfront.net"]},"platforms":[{"name":"Win10","os":"win","version":"win10"}]}]}}]
```



#### Search Events
Use the Search Events action to search events in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Type|Type of the event that needs to be returned.|False|List|All|
|Threat Status|Status of threat that needs to be returned. If "Select One" is provided, then action will return “Active” and “Cleared” threats.|False|List|Select One|
|Time Frame|Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results to return. Default: 50. Maximum: 1000.|True|String|50|



##### JSON Results
```json
{"events": [{"spamScore": 100, "phishScore": 0, "threatsInfoMap": [{"threatID": "abc", "threatStatus": "active", "classification": "phish", "detectionType": "NONE", "threatUrl": "https://threatinsight.proofpoint.com/threat/email/abc", "threatTime": "2018-04-17T21:40:16.000Z", "threat": "abc", "campaignID": null, "actors": [{"id": "f426d241-59ee-4b85-abaa-33a4171048dd", "name": "TA204", "type": "ACTOR"}], "threatType": "attachment"}], "messageTime": "2025-04-17T19:00:47.000Z", "impostorScore": 0.0, "malwareScore": 0, "cluster": "proofpointdemo_cloudadminuidemo_hosted", "subject": "Aufmerksamkeit ! Ihr Konto PayPal wurde begrenzt !", "quarantineFolder": "Attachment Defense", "quarantineRule": "threat", "policyRoutes": ["default_inbound", "allow_relay", "firewallsafe", "internalnet"], "modulesRun": ["av", "spf", "sandbox", "spam", "dmarc", "urldefense"], "messageSize": 36485, "headerFrom": "PayPal <paypal@service.fr>", "headerReplyTo": null, "fromAddress": ["paypal@service.fr"], "ccAddresses": [], "replyToAddress": [], "toAddresses": ["abuse@company.com"], "xmailer": null, "messageParts": [{"disposition": "inline", "sha256": "abc", "md5": "fb5850356f812816a26eaec02716283d", "filename": "text.html", "sandboxStatus": "NOT_SUPPORTED", "oContentType": "text/html", "contentType": "text/html"}, {"disposition": "attached", "sha256": "abc", "md5": "5b3eabc04003e63e55215c236ecf7ff4", "filename": "paypal account-informationen.html", "sandboxStatus": "THREAT", "oContentType": "text/html", "contentType": "text/html"}], "completelyRewritten": false, "id": "abc", "QID": "462naj9j8w-1", "GUID": "0t_HGi7973BqEuQtpHI8qkcUUg3XHZf_", "sender": "phorton@example.com", "recipient": ["aprince@proofpointdemo.com"], "senderIP": "127.0.0.1", "messageID": "<abc>", "eventType": "messagesBlocked"}]}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.