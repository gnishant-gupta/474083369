
# Tools

A set of utility actions for data manipulation and common platform tasks to power up playbook capabilities.

Python Version - 3


#### Dependencies
| |
|-|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|dnspython-2.7.0-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|filelock-3.20.3-py3-none-any.whl|
|nltk-3.9.1-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|joblib-1.5.3-py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|requests_file-3.0.1-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.3-py3-none-any.whl|
|click-8.3.1-py3-none-any.whl|
|regex-2026.1.15-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|tldextract-5.1.3-py3-none-any.whl|
|tqdm-4.67.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyspellchecker-0.8.2-py3-none-any.whl|
|six-1.17.0-py2.py3-none-any.whl|
|pytz-2025.2-py2.py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|protobuf-6.33.4-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_auth-2.47.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|proto_plus-1.27.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|TIPCommon-2.3.5-py3-none-any.whl|
|croniter-6.0.0-py2.py3-none-any.whl|


## Actions
#### Append to Context Value
Append a value to an existing context property or create a new context property and add the value.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|The scope of the context value. Options: Alert or Case or Global|True|List|Alert|
|Key|The context property key.|True|String||
|Value|The value to append to the context property.|True|String||
|Delimiter|The delimiter for the value of the context property.|True|String|,|



##### JSON Results
```json
{}
```



#### Add Alert Scoring Information
This action will add an entry to the alert scoring database.  Alert score is based off the ratio: 5 Low = 1 Medium.  3 Medium = 1 High.  2 High = 1 Critical.  Optional tag added to case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|The name of the check being performed on the alert.|True|String||
|Description|The description of the check being performed on the alert.|True|String||
|Severity|The severity.|True|List|Informational|
|Category|The category of the check that was performed.|True|String||
|Source|Optional. The part of the alert that the score was derived from.  Examples are Files, Email, User... |False|String||



##### JSON Results
```json
[{"category": "Users", "category_score": 1, "score_data": [{"description": "A description.", "score": 1, "score_name": "RecentHire", "severity": "Low", "source": "UserA"}, {"description": "Another description", "score": 1, "score_name": "Remote", "severity": "Low", "source": "UserA"}]}, {"category": "Files", "category_score": 2, "score_data": [{"description": "This file contains VBA macros. No suspicious keyword was found. Use olevba and mraptor for more info.", "score_name": "VBA Macros", "severity": "Medium", "score": 2, "source": "DECODED-20220203175129.XLS"}]}]
```



#### Add Or Update Alert Additional Data
The action adds or updates fields in the alert additional data. The result will be all accumulated data that was added to the alert. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Json Fields|You can enter either free text (for one variable) or a string representing a JSON (Dict/List - Can be nested)|True|String|{}|



##### JSON Results
```json
{"list": [{"key": "PhishingBodyAnalysisUnmatchedDomains", "value": "onlineservicetech.websit"}, {"key": "PhishingBodyAnalysisSpellingMistakes", "value": "perfomance"}], "dict": {}, "data": "Just some string"}
```



#### Add Comment to Entity Log
This action will add a comment to the Entity Log for each entity in scope in the Entity Explorer.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User|The user who created the comment.|True|Users|@Administrator|
|Comment|The comment that will be added to the entity log.|True|Content|<insert comment>|



##### JSON Results
```json
{}
```



#### Buffer
The action receives a json and returns it as a json result
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ResultValue|Result Value input|False|String|None|
|JSON|JSON input|False|String|None|



##### JSON Results
```json
{"body": [{"uri": ["https://thisisreallyphishy.somethingmadeup.com"], "email": ["craig.h.leabhart@emcins.com"], "domain": ["somethingmadeup.com"], "content_header": {"content-type": ["text/plain;charset=\"Windows-1252\""], "content-transfer-encoding": ["quoted-printable"]}, "content": "Testing!Don\u2019t delete this.\r\n\r\n\r\n\r\nhttps://thisisreallyphishy.somethingmadeup.com\r\n\r\n\r\n\r\nCraigH Leabhart\r\nInformation Security Analyst I\r\nGREM, AINS, CYB, Splunk EnterpriseCertified Admin, AWS Certified Security - Specialty\r\n\r\nCorporate Office| IT IS Security Engineering\r\n\r\n515-345-7427\r\nCraig.H.Leabhart@EMCIns.com<mailto:Craig.H.Leabhart@EMCIns.com>\r\n\r\n\r\n\r\n\r\n\r\n", "content_type": "text/plain", "hash": "bb278d83c3415eaf8dd02e7e68e56bb7a16bef6e9851e08057def5fd7735bb8a"}, {"email": ["craig.h.leabhart@emcins.com"], "domain": ["microsoft.com", "w3.org", "somethingmadeup.com"], "content_header": {"content-type": ["text/html;charset=\"Windows-1252\""], "content-transfer-encoding": ["quoted-printable"]}, "content": "<htmlxmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\"xmlns:w=\"urn:schemas-microsoft-com:office:word\" xmlns:m=\"http://schemas.microsoft.com/office/2004/12/omml\"xmlns=\"http://www.w3.org/TR/REC-html40\"><head>\r\n<meta http-equiv=\"Content-Type\"content=\"text/html; charset=Windows-1252\">\r\n<meta name=\"Generator\" content=\"MicrosoftWord 15 (filtered medium)\">\r\n<style><!--\r\n/* Font Definitions */\r\n@font-face\r\n\t{font-family:\"CambriaMath\";\r\n\tpanose-1:2 4 5 3 5 4 6 3 2 4;}\r\n@font-face\r\n\t{font-family:Calibri;\r\n\tpanose-1:215 5 2 2 2 4 3 2 4;}\r\n/* Style Definitions */\r\np.MsoNormal, li.MsoNormal,div.MsoNormal\r\n\t{margin:0in;\r\n\tmargin-bottom:.0001pt;\r\n\tfont-size:11.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\na:link,     span.MsoHyperlink\r\n\t{mso-style-priority:99;\r\n\tcolor:#0563C1;\r\n\ttext-decoration:underline;}\r\nspan.EmailStyle17\r\n\t{mso-style-type:personal-compose;\r\n\tfont-family:\"Calibri\",sans-serif;\r\n\tcolor:windowtext;}\r\n.MsoChpDefault\r\n\t{mso-style-type:export-only;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\n@page     WordSection1\r\n\t{size:8.5in 11.0in;\r\n\tmargin:1.0in 1.0in 1.0in 1.0in;}\r\ndiv.WordSection1\r\n\t{page:WordSection1;}\r\n--></style><!--[if     gte mso 9]><xml>\r\n<o:shapedefaults v:ext=\"edit\" spidmax=\"1026\" />\r\n</xml><![endif]--><!--[ifgte mso 9]><xml>\r\n<o:shapelayout v:ext=\"edit\">\r\n<o:idmap v:ext=\"edit\"data=\"1\" />\r\n</o:shapelayout></xml><![endif]-->\r\n</head>\r\n<body lang=\"EN-US\"link=\"#0563C1\" vlink=\"#954F72\">\r\n<div class=\"WordSection1\">\r\n<pclass=\"MsoNormal\">Testing! Don\u2019t delete this.<o:p></o:p></p>\r\n<p class=\"MsoNormal\"><o:p>&nbsp;</o:p></p>\r\n<pclass=\"MsoNormal\"><a href=\"https://thisisreallyphishy.somethingmadeup.com\">https://thisisreallyphishy.somethingmadeup.com</a>\r\n<o:p></o:p></p>\r\n<pclass=\"MsoNormal\"><o:p>&nbsp;</o:p></p>\r\n<table class=\"MsoNormalTable\"border=\"0\" cellspacing=\"6\" cellpadding=\"0\">\r\n<tbody>\r\n<tr>\r\n<tdvalign=\"top\" style=\"padding:.75pt .75pt .75pt .75pt\">\r\n<p class=\"MsoNormal\"><b><spanstyle=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0077C8\">CraigH Leabhart</span></b><span style=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0077C8\"><br>\r\n</span><spanstyle=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">InformationSecurity Analyst I<br>\r\nGREM, AINS, CYB, Splunk Enterprise Certified Admin,AWS Certified Security - Specialty<o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><spanstyle=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">CorporateOffice | IT IS Security Engineering</span><span style=\"font-family:&quot;Arial&quot;,sans-serif\"><o:p></o:p></span></p>\r\n</td>\r\n</tr>\r\n<tr>\r\n<tdstyle=\"padding:.75pt .75pt .75pt .75pt\">\r\n<p class=\"MsoNormal\"><spanstyle=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">515-345-7427<br>\r\n<ahref=\"mailto:Craig.H.Leabhart@EMCIns.com\"><span style=\"color:#0077C8\">Craig.H.Leabhart@EMCIns.com</span></a></span><spanstyle=\"font-family:&quot;Arial&quot;,sans-serif\"><o:p></o:p></span></p>\r\n</td>\r\n</tr>\r\n</tbody>\r\n</table>\r\n<pclass=\"MsoNormal\"><o:p>&nbsp;</o:p></p>\r\n<p class=\"MsoNormal\"><o:p>&nbsp;</o:p></p>\r\n</div>\r\n</body>\r\n</html>\r\n", "content_type": "text/html", "hash": "5f58e1a3d77d8143653937696748222b96ca17db5304584d4d138cbb5539de63"}], "header": {"subject": "PhishingEmail Reported: testing. don''t delete", "from": "craig.h.leabhart@emcins.com", "to": ["it.security.reporting@emcins.com"], "date": "2020-12-1820:45:22+00:00", "received": [{"src": "from dm6pr20mb3316.namprd20.prod.outlook.com(2603:10b6:5:2ae::15) by dm6pr20mb2907.namprd20.prod.outlook.com with https;fri, 18 dec 2020 20:45:23 +0000", "from": ["2603:10b6:5:2ae::15", "dm6pr20mb3316.namprd20.prod.outlook.com"], "by": ["dm6pr20mb2907.namprd20.prod.outlook.com"], "with": "https", "date": "2020-12-1820:45:23+00:00"}, {"src": "from dm6pr20mb3065.namprd20.prod.outlook.com (2603:10b6:5:1d6::15)by dm6pr20mb3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15) with microsoftsmtp server (version=tls1_2, cipher=tls_ecdhe_rsa_with_aes_256_gcm_sha384)id 15.20.3676.25; fri, 18 dec 2020 20:45:22 +0000", "from": ["dm6pr20mb3065.namprd20.prod.outlook.com", "2603:10b6:5:1d6::15"], "by": ["2603:10b6:5:2ae::15", "dm6pr20mb3316.namprd20.prod.outlook.com"], "with": "microsoftsmtp server (version=tls1_2, cipher=tls_ecdhe_rsa_with_aes_256_gcm_sha384)id 15.20.3676.25", "date": "2020-12-18 20:45:22+00:00"}, {"src": "from dm6pr20mb3065.namprd20.prod.outlook.com([fe80::680e:fe50:ba92:6f6e]) by dm6pr20mb3065.namprd20.prod.outlook.com ([fe80::680e:fe50:ba92:6f6e%5])with mapi id 15.20.3654.025; fri, 18 dec 2020 20:45:22 +0000", "from": ["dm6pr20mb3065.namprd20.prod.outlook.com", "fe80::680e:fe50:ba92:6f6e"], "by": ["dm6pr20mb3065.namprd20.prod.outlook.com", "fe80::680e:fe50:ba92:6f6e"], "with": "mapiid 15.20.3654.025", "date": "2020-12-18 20:45:22+00:00"}], "received_domain": ["outlook.com", "outlook.com"], "received_ip": ["2603:10b6:5:2ae::15", "2603:10b6:5:1d6::15", "2603:10b6:5:2ae::15", "2603:10b6:5:1d6::15"], "received_domains_internal": [], "sending": [{"ips": ["2603:10b6:5:2ae::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3316.namprd20.prod.outlook.com"]}, {"ips": ["2603:10b6:5:1d6::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}, {"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}], "receiving": [{"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb2907.namprd20.prod.outlook.com"]}, {"ips": ["2603:10b6:5:2ae::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3316.namprd20.prod.outlook.com"]}, {"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}], "header": {"x-microsoft-antispam": ["BCL:0;"], "authentication-results": ["EMCIns.com;dkim=none (message not signed) header.d=none;EMCIns.com; dmarc=none action=noneheader.from=EMCIns.com;"], "x-forefront-antispam-report": ["CIP:255.255.255.255;CTRY:;LANG:en;SCL:-1;SRV:;IPV:NLI;SFV:SKI;H:DM6PR20MB3065.namprd20.prod.outlook.com;PTR:;CAT:NONE;SFS:;DIR:INB;"], "x-ms-exchange-crosstenant-fromentityheader": ["Hosted"], "date": ["Fri,18 Dec 2020 20:45:22 +0000"], "thread-topic": ["Phishing Email Reported: testing.don''t delete"], "x-ms-has-attach": ["yes"], "x-ms-exchange-organization-originalclientipaddress": ["1.1.1.1"], "x-ms-oob-tlc-oobclassifiers": ["OLM:439;"], "content-language": ["en-US"], "x-ms-traffictypediagnostic": ["DM6PR20MB3316:"], "x-ms-exchange-crosstenant-network-message-id": ["212b6340-63ca-4c79-8653-08d8a395d706"], "x-ms-exchange-organization-compliancelabelid": ["3c7e8f1c-7e98-4120-8c1e-7c1d145ac9cb"], "x-ms-exchange-crosstenant-authsource": ["DM6PR20MB3065.namprd20.prod.outlook.com"], "x-ms-exchange-crosstenant-mailboxtype": ["HOSTED"], "mime-version": ["1.0"], "subject": ["PhishingEmail Reported: testing. don''t delete"], "accept-language": ["en-US"], "x-ms-exchange-processed-by-bccfoldering": ["1.1.1.1"], "from": ["CraigLeabhart <Craig.H.Leabhart@EMCIns.com>"], "thread-index": ["AQHW1X60bcVC9xDzVU+hZyMrYHYhyw=="], "x-ms-exchange-organization-submissionquotaskipped": ["False"], "x-ms-exchange-organization-originalserveripaddress": ["::1"], "x-ms-exchange-crosstenant-id": ["e081befd-6283-4d46-8816-eb19e817bac5"], "x-ms-exchange-transport-crosstenantheadersstamped": ["DM6PR20MB3316"], "to": ["ITInformation Security Reporting <IT.Security.Reporting@EMCIns.com>"], "x-ms-office365-filtering-correlation-id": ["212b6340-63ca-4c79-8653-08d8a395d706"], "x-ms-exchange-crosstenant-originalarrivaltime": ["18Dec 2020 20:45:22.5109 (UTC)"], "x-microsoft-antispam-message-info": ["KOdOPaxhQNvZoYgAArc/9ZkIwux7juBPSk7UcafTkDWr6ArN5qYgScT6gCUDJFv4+Iw5HACM4EH51p6GwTH74pybZDkycdw6J1Xv7FYlSproEcOtEARE++JTInT9oSwoLF+g1Slo9PtD14q+lZFLi8YUlc8ZEn5pqkjq5pFjQlGRiPW4C4BsXEBF4q2mAJEgq6e7+gqVA4tfSrbu9jaZtdtC30xifGVPqbCiDF0xJBjNEi7IGwJSbLxfSY01tC7usWbm9vyD9eizzR2lFdQzFtfebO2hOUJ4iCZKYt1uILCL1cxYqQuHRKuPOxyf+W3qnkL0PTx9AUwReYEqNsmuBABHDDHC16AgWUggu5DdRxrospDvsZCRVsZde1tZfQanGL11jw6KnnDNp8OlVJ+fR8k8xCQ/gqc8aDJiuSi7qDCny8G1gzWOtPBfZZ2k3ywO"], "content-type": ["multipart/mixed;boundary=\"_004_DM6PR20MB3065B3C5FAA02A0E58A5648DB9C30DM6PR20MB3065namp_\""], "x-ms-exchange-organization-recordreviewcfmtype": ["0"], "x-ms-exchange-antispam-messagedata": ["RQPAEVTFNVw92iTyoDBF6fwbSczryyS2C5P5ZDlH3m1JwaPURNT38WuBLy9DyvuKsia80Pa+Ebv3RagPEWeyC5pehePtra0ictqIxRNj4cJj9agbBH57BpwVlLe6jF5Wx5Ps2rY75JG3mb5azo3wpVt8mKlc4OQ7/S6+9eMqtwUMbGYQhnAiAlsaX8fxnX/Ocdgc7NSNWd8mCzpKa9YQo+kTF3//lPSQ2Oq0cz1Resucd/TFCF5zBwpc0UpuACiBWdH/CDfzEgQNQ5eVuBfnVC3jWl97irN0h4+3H2qIzjNNTUYo+7AkuZzriq3nN6nZpRQm3e0qNQjeujFxn3HiTVvixBV0GvqThb3ZtK3hT0cXtp6VpB8oTi8v3m4OTMsYaOFT7P2Zl0i+19xsnFFJwzZpY9eoGeC/CB2HWQtdM5oszHfQgskBGiYW90kvuNUd7IJ7tIF1mPzcXrwqCie4mcvxXHS6neH3DIyzUnYGQqNjxMCL4f50u2cAHNFHrqdon2CjObwaQwWMp1r/7jb/tr/kx/E28ity9xmoUr8BFviIGH6BDF/2k4/ODhQd54T0siO1EC0IHQI35mhWJTkcv8/3GTdh+eZ9zumVMqgk/R4K2T0AhtAkRxASUwasGlMVECpB3G/efTy4EBUnn5K+9pPxreolRnoj6UOC40AFVRGuaEux1LrHGZRwI+kjZurlqwTOYOA556JRvJMzpD2tPC5QqW0k+28SI8M3cRTdJzGUbFeO4VA767IteQlgk77Ip73pFL2hRYZCItJrqy8pQlRhDEinGWMSW92we6jYm5bY0IvEygVNmJhlqXmQG9YNc3UV8uQVMwqG2Cl8XDx58JDeEmxLJ2SNUpKiq1iBkCILVQzEvCkhCMWk3QoQl7wWdBuMGDPYlkH/KBInyB5XXidr2w3x6wm6EEz9DAzpxPxNpnha/dUTxJ5R9Dj08KIQLQceCf2jtxHiVwokH4NaOPiCF3nwzUzVUqO0BLbYJtQ="], "x-ms-exchange-organization-network-message-id": ["212b6340-63ca-4c79-8653-08d8a395d706"], "message-id": ["<DM6PR20MB3065B3C5FAA02A0E58A5648DB9C30@DM6PR20MB3065.namprd20.prod.outlook.com>"], "x-ms-exchange-crosstenant-userprincipalname": ["xB1vfGOVsP3XFtrMfQJ1vXJbukWhCb3ZSY5gdbGz1MuzEaNqBPMYL4hxU1aSvwTpOLF3nkLCb2JYxT6DXQBDLQ=="], "received": ["fromDM6PR20MB3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15) by DM6PR20MB2907.namprd20.prod.outlook.comwith HTTPS; Fri, 18 Dec 2020 20:45:23 +0000", "from DM6PR20MB3065.namprd20.prod.outlook.com(2603:10b6:5:1d6::15) by DM6PR20MB3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15)with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)id 15.20.3676.25; Fri, 18 Dec 2020 20:45:22 +0000", "from DM6PR20MB3065.namprd20.prod.outlook.com([fe80::680e:fe50:ba92:6f6e]) by DM6PR20MB3065.namprd20.prod.outlook.com ([fe80::680e:fe50:ba92:6f6e%5])with mapi id 15.20.3654.025; Fri, 18 Dec 2020 20:45:22 +0000"], "x-ms-exchange-organization-authsource": ["DM6PR20MB3065.namprd20.prod.outlook.com"], "x-ms-exchange-transport-endtoendlatency": ["00:00:00.5390270"], "x-ms-publictraffictype": ["Email"], "x-ms-exchange-crosstenant-authas": ["Internal"], "x-ms-exchange-organization-authmechanism": ["04"], "x-microsoft-antispam-mailbox-delivery": ["ucf:0;jmr:0;auth:0;dest:I;ENG:(750128)(520011016)(706158)(944506458)(944626604);"], "x-originating-ip": ["[50.81.96.137]"]}}, "attached_emails": [{"filename": "phish_alert_sp2_2.0.0.0.eml", "email": {"body": [{"email": ["craig.h.leabhart@emcins.com"], "domain": ["microsoft.com", "w3.org", "somethingmadeup.com"], "content_header": {"content-type": ["text/html;charset=\"utf-8\""], "content-transfer-encoding": ["quoted-printable"]}, "content": "<htmlxmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\"xmlns:w=\"urn:schemas-microsoft-com:office:word\" xmlns:m=\"http://schemas.microsoft.com/office/2004/12/omml\"xmlns=\"http://www.w3.org/TR/REC-html40\"><head>\r\n<meta http-equiv=\"Content-Type\"content=\"text/html; charset=utf-8\"><meta name=\"Generator\" content=\"MicrosoftWord 15 (filtered medium)\"><style><!--\r\n/* Font Definitions */\r\n@font-face\r\n\t{font-family:\"CambriaMath\";\r\n\tpanose-1:2 4 5 3 5 4 6 3 2 4;}\r\n@font-face\r\n\t{font-family:Calibri;\r\n\tpanose-1:215 5 2 2 2 4 3 2 4;}\r\n/* Style Definitions */\r\np.MsoNormal, li.MsoNormal,div.MsoNormal\r\n\t{margin:0in;\r\n\tmargin-bottom:.0001pt;\r\n\tfont-size:11.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\na:link,span.MsoHyperlink\r\n\t{mso-style-priority:99;\r\n\tcolor:#0563C1;\r\n\ttext-decoration:underline;}\r\nspan.EmailStyle17\r\n\t{mso-style-type:personal-compose;\r\n\tfont-family:\"Calibri\",sans-serif;\r\n\tcolor:windowtext;}\r\n.MsoChpDefault\r\n\t{mso-style-type:export-only;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\n@pageWordSection1\r\n\t{size:8.5in 11.0in;\r\n\tmargin:1.0in 1.0in 1.0in 1.0in;}\r\ndiv.WordSection1\r\n\t{page:WordSection1;}\r\n--></style><!--[ifgte mso 9]><xml>\r\n<o:shapedefaults v:ext=\"edit\" spidmax=\"1026\" />\r\n</xml><![endif]--><!--[ifgte mso 9]><xml>\r\n<o:shapelayout v:ext=\"edit\">\r\n<o:idmap v:ext=\"edit\"data=\"1\" />\r\n</o:shapelayout></xml><![endif]--></head><body lang=\"EN-US\"link=\"#0563C1\" vlink=\"#954F72\"><div class=\"WordSection1\"><p class=\"MsoNormal\">Testing!Don\u2019t delete this.<o:p></o:p></p><p class=\"MsoNormal\"><o:p>&nbsp;</o:p></p><pclass=\"MsoNormal\"><a href=\"https://thisisreallyphishy.somethingmadeup.com\">https://thisisreallyphishy.somethingmadeup.com</a><o:p></o:p></p><p class=\"MsoNormal\"><o:p>&nbsp;</o:p></p><table class=\"MsoNormalTable\"border=\"0\" cellspacing=\"6\" cellpadding=\"0\"><tbody><tr><td valign=\"top\"style=\"padding:.75pt .75pt .75pt .75pt\"><p class=\"MsoNormal\"><b><spanstyle=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0077C8\">CraigH Leabhart</span></b><span style=\"font-size:10.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#0077C8\"><br></span><spanstyle=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">InformationSecurity Analyst I<br>GREM, AINS, CYB, Splunk Enterprise Certified Admin,AWS Certified Security - Specialty<o:p></o:p></span></p><p class=\"MsoNormal\"><spanstyle=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">CorporateOffice | IT IS Security Engineering</span><span style=\"font-family:&quot;Arial&quot;,sans-serif\"><o:p></o:p></span></p></td></tr><tr><tdstyle=\"padding:.75pt .75pt .75pt .75pt\"><p class=\"MsoNormal\"><span style=\"font-size:8.0pt;font-family:&quot;Arial&quot;,sans-serif;color:#454545\">515-345-7427<br><ahref=\"mailto:Craig.H.Leabhart@EMCIns.com\"><span style=\"color:#0077C8\">Craig.H.Leabhart@EMCIns.com</span></a></span><spanstyle=\"font-family:&quot;Arial&quot;,sans-serif\"><o:p></o:p></span></p></td></tr></tbody></table><pclass=\"MsoNormal\"><o:p>&nbsp;</o:p></p><p class=\"MsoNormal\"><o:p>&nbsp;</o:p></p></div></body></html>", "content_type": "text/html", "hash": "6128f51f1ae85408aa189a7b65655dfcbb0fc3bfd3102342e175a0ef4287ee9f"}], "header": {"subject": "testing.don''t delete", "from": "craig.h.leabhart@emcins.com", "to": ["craig.h.leabhart@emcins.com"], "date": "2020-12-1820:45:14+00:00", "received": [{"src": "from dm6pr20mb3316.namprd20.prod.outlook.com(2603:10b6:5:2ae::15) by dm6pr20mb3065.namprd20.prod.outlook.com with https;fri, 18 dec 2020 20:45:15 +0000", "from": ["2603:10b6:5:2ae::15", "dm6pr20mb3316.namprd20.prod.outlook.com"], "by": ["dm6pr20mb3065.namprd20.prod.outlook.com"], "with": "https", "date": "2020-12-1820:45:15+00:00"}, {"src": "from dm6pr20mb3065.namprd20.prod.outlook.com (2603:10b6:5:1d6::15)by dm6pr20mb3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15) with microsoftsmtp server (version=tls1_2, cipher=tls_ecdhe_rsa_with_aes_256_gcm_sha384)id 15.20.3676.25; fri, 18 dec 2020 20:45:15 +0000", "from": ["dm6pr20mb3065.namprd20.prod.outlook.com", "2603:10b6:5:1d6::15"], "by": ["2603:10b6:5:2ae::15", "dm6pr20mb3316.namprd20.prod.outlook.com"], "with": "microsoftsmtp server (version=tls1_2, cipher=tls_ecdhe_rsa_with_aes_256_gcm_sha384)id 15.20.3676.25", "date": "2020-12-18 20:45:15+00:00"}, {"src": "from dm6pr20mb3065.namprd20.prod.outlook.com([fe80::680e:fe50:ba92:6f6e]) by dm6pr20mb3065.namprd20.prod.outlook.com ([fe80::680e:fe50:ba92:6f6e%5])with mapi id 15.20.3654.025; fri, 18 dec 2020 20:45:14 +0000", "from": ["dm6pr20mb3065.namprd20.prod.outlook.com", "fe80::680e:fe50:ba92:6f6e"], "by": ["dm6pr20mb3065.namprd20.prod.outlook.com", "fe80::680e:fe50:ba92:6f6e"], "with": "mapiid 15.20.3654.025", "date": "2020-12-18 20:45:14+00:00"}], "received_domain": ["outlook.com"], "received_ip": ["2603:10b6:5:2ae::15", "2603:10b6:5:1d6::15"], "received_domains_internal": [], "sending": [{"ips": ["2603:10b6:5:2ae::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3316.namprd20.prod.outlook.com"]}, {"ips": ["2603:10b6:5:1d6::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}, {"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}], "receiving": [{"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}, {"ips": ["2603:10b6:5:2ae::15"], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3316.namprd20.prod.outlook.com"]}, {"ips": [], "domains": ["outlook.com"], "emails": [], "hosts": ["dm6pr20mb3065.namprd20.prod.outlook.com"]}], "header": {"authentication-results": ["EMCIns.com;dkim=none (message not signed) header.d=none;EMCIns.com; dmarc=none action=noneheader.from=EMCIns.com;"], "x-ms-exchange-organization-messagedirectionality": ["Originating"], "x-ms-exchange-crosstenant-mailboxtype": ["HOSTED"], "x-ms-exchange-organization-expirationintervalreason": ["OriginalSubmit"], "date": ["Fri,18 Dec 2020 20:45:14 +0000"], "thread-topic": ["testing. don''t delete"], "x-ms-exchange-antispam-messagedata": ["y9gmEM9LATUYtNENhmc9h0pniUc8pr7FsayjBr3evxoyZW28FLiYB5xXmiiG1yn56jyKo80/gY7Mu4bTd7kK9myR50SzjKds0p7p3sNh+7AlberiBZUuwEg8uiYXEcBHq/MBSYUtMJJY6yhnDBDQk4kJOZOFix+LY9819b+EKVXKumKAD0OYrv+ax9NCPT8IpUWhU+7AndlaXM2wUtlDhBgKh4NMqFqj2ODImDwWdq59I79uENwkDmO4XuZpg0TJuCSDJdMyO9jSOo7YW4xP/zvSR6z4tJ3G6YZ+eyfbj4tQrEdBjHpiGqSMQJ1/XHsqQYkFkxqOoSZxPTxNccq6vSllo7rssusjzXNQcDw11hR7rL1tobC7VmKWt9o/DrLxPKfy8M9vB1ipI1JwXiDABkl7Dtg0IvkoAJZVuxYxAqPjh/Sg081qJ8976qAkHgAyoVLBeiUdsZvuURnLHmQqYcql8V+oUnfcq9WY2N246dxIm9maj9TVI0kn7JNvgaWb7APJwMD2wozCapCEPAuIlTb5r5AcQtsECCVMqHxK2J5TV71F3DcT2qvFoiguq+kA7MmXtOFlRBy6B2j5MDLq3lE4NL+IDs4Uy8ESkRv5ksPFjAZUdMq7tkM4ButSuXAqmD9zkmRGg+o0x4Oz6/lKotkKc32bpsDM/kQNJMXpo87R2HQ5xgPzVqo7TDrWFnoBu3zaC3GDt/46twRDkNyLgJwdoqm0OWVxDZeq0/0r4eEB+6VOAQSUQjUlqOi8/is4Iqmka13Bc4KFv8LHUKG/D9j5kQY5WXufOyifLWgYJVD6nxf6WacJUSSELGEqiX/rs3qzal1KpwM3IyxuGSJof+JzXie90ScnWqdVWco23VbHN68XCk32eEnDqQpBxQ4Gn7fK4QxQtNsLO+HaLj7jaaAKn/EGwMteoVPLFmO6L/NWOZP0nDXgH2XsSh5YuD8OuEhbmoX7uT6Z1c3F5MS4To6kxXP/8tFA91I+1eBpCAs="], "x-ms-exchange-crosstenant-originalarrivaltime": ["18Dec 2020 20:45:14.8223 (UTC)"], "content-language": ["en-US"], "x-ms-exchange-crosstenant-authas": ["Internal"], "return-path": ["Craig.H.Leabhart@EMCIns.com"], "x-ms-exchange-crosstenant-id": ["e081befd-6283-4d46-8816-eb19e817bac5"], "x-ms-publictraffictype": ["Email"], "x-ms-exchange-processed-by-bccfoldering": ["1.1.1.1"], "message-id": ["<DM6PR20MB3065E75D3C7C8C6BEB791B5AB9C30@DM6PR20MB3065.namprd20.prod.outlook.com>"], "mime-version": ["1.0"], "x-microsoft-antispam": ["BCL:0;"], "subject": ["testing.don''t delete"], "x-ms-exchange-organization-network-message-id": [" 5cbebd44-be2f-49c0-ee5f-08d8a395d273"], "accept-language": ["en-US"], "x-ms-exchange-organization-authmechanism": ["04"], "x-ms-exchange-crosstenant-userprincipalname": ["MhyBC+Xe07rIO0nQZ+3IfiMMhKtY6xepBoFb7r/7mWTrUh+fX5p/ag6O/HxuVboWYS/mj3rgbzKxtLw0OCKV3w=="], "from": ["CraigLeabhart <Craig.H.Leabhart@EMCIns.com>"], "thread-index": ["AdbVfpjfWgrxTbCLQlmOT+ugX7UxLQ=="], "x-ms-oob-tlc-oobclassifiers": ["OLM:439;"], "content-transfer-encoding": ["7bit"], "x-ms-office365-filtering-correlation-id": ["5cbebd44-be2f-49c0-ee5f-08d8a395d273"], "to": ["Craig Leabhart <Craig.H.Leabhart@EMCIns.com>"], "x-originating-ip": ["[50.81.96.137]"], "x-ms-tnef-correlator": ["<DM6PR20MB3065E75D3C7C8C6BEB791B5AB9C30@DM6PR20MB3065.namprd20.prod.outlook.com>"], "x-ms-exchange-organization-authas": ["Internal"], "x-ms-exchange-organization-expirationstarttime": ["18Dec 2020 20:45:15.0578 (UTC)"], "x-forefront-antispam-report": [" CIP:255.255.255.255;CTRY:;LANG:en;SCL:-1;SRV:;IPV:NLI;SFV:SKI;H:DM6PR20MB3065.namprd20.prod.outlook.com;PTR:;CAT:NONE;SFS:;DIR:INB;"], "x-microsoft-antispam-message-info": ["SEjSnBQ+oVZvWfqi2+GAj4J8PHBxbgU/JpILkJ7Gl49fDkWr8Dh3ZhwjEldKTRS+uzucvEcjQeOac3OLN63Pu+lv2JxYloTMw5M+kK91lzRt1yc7r/fmsKk/CKLdTP1NrvAifzzrQ7MBPBU4wQaRSkPJZfAaoEek3W4iLNxqnXR4QA+jATz7/ZmLnNigZqhZ4jRzLhMNpZ0DjLMmxb0wlFbN7qmYdkn4mtDlgKvsxL8r/Agyz4NLRzoweYIL3vqi6LmG+ozcF/cvXFeqF8CzVpoN1T3fWxz5ElwhaotkZRPF8JUJXzKh9QmcUnpw9QnhDjQAg7adcCys8cm+jRDusV+s54Gde9o9q2KDOeuq+mPQsWTfdKHtlh+6gw+TJ79K"], "x-ms-exchange-organization-expirationinterval": ["1:00:00:00.0000000"], "content-type": ["multipart/mixed;boundary=\"----sinikael-?=_1-16083243222280.5868206868234287\""], "x-ms-exchange-transport-endtoendlatency": ["00:00:00.5677096"], "x-ms-exchange-crosstenant-authsource": ["DM6PR20MB3065.namprd20.prod.outlook.com"], "x-ms-exchange-organization-scl": ["-1"], "received": ["fromDM6PR20MB3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15) by DM6PR20MB3065.namprd20.prod.outlook.comwith HTTPS; Fri, 18 Dec 2020 20:45:15 +0000", "from DM6PR20MB3065.namprd20.prod.outlook.com(2603:10b6:5:1d6::15) by DM6PR20MB3316.namprd20.prod.outlook.com (2603:10b6:5:2ae::15)with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)id 15.20.3676.25; Fri, 18 Dec 2020 20:45:15 +0000", "from DM6PR20MB3065.namprd20.prod.outlook.com([fe80::680e:fe50:ba92:6f6e]) by DM6PR20MB3065.namprd20.prod.outlook.com ([fe80::680e:fe50:ba92:6f6e%5])with mapi id 15.20.3654.025; Fri, 18 Dec 2020 20:45:14 +0000"], "x-ms-exchange-crosstenant-fromentityheader": ["Hosted"], "x-ms-exchange-transport-crosstenantheadersstamped": ["DM6PR20MB3316"], "x-ms-exchange-organization-expirationstarttimereason": ["OriginalSubmit"], "x-ms-exchange-crosstenant-network-message-id": ["5cbebd44-be2f-49c0-ee5f-08d8a395d273"], "x-ms-exchange-organization-authsource": ["DM6PR20MB3065.namprd20.prod.outlook.com"], "x-ms-traffictypediagnostic": ["DM6PR20MB3316:"], "x-microsoft-antispam-mailbox-delivery": ["ucf:0;jmr:0;auth:0;dest:I;ENG:(750128)(520002050)(706158)(944506458)(944626604);"]}}}}], "attachments": [{"filename": "phish_alert_sp2_2.0.0.0.eml", "size": 8452, "extension": "eml", "hash": {"md5": "8414feaca17c819448c887bb8fa73788", "sha1": "c63eda9c9b4c1e7db3abf5dcd669cb702505fc59", "sha256": "6eac026fe55d1443d7d65c323d4785e5c349b87bb322f81cc98f56c2e6759533", "sha512": "c097f40bfb09eefceac7a5a60bd4aed9e9cf0fee7c0db6609fafd06b3726449df42f5c0a463723fd2706a827b8378f8ef1827fc022eb212dcaa8e791a3878cea"}, "raw": "UmVjZWl2ZWQ6IGZyb20gRE02UFIyME1CMzMxNi5uYW1wcmQyMC5wcm9kLm91dGxvb2suY29tDQogKDI2MDM6MTBiNjo1OjJhZTo6MTUpIGJ5IERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbSB3aXRoDQogSFRUUFM7IEZyaSwgMTggRGVjIDIwMjAgMjA6NDU6MTUgKzAwMDANClJlY2VpdmVkOiBmcm9tIERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbQ0KICgyNjAzOjEwYjY6NToxZDY6OjE1KSBieSBETTZQUjIwTUIzMzE2Lm5hbXByZDIwLnByb2Qub3V0bG9vay5jb20NCiAoMjYwMzoxMGI2OjU6MmFlOjoxNSkgd2l0aCBNaWNyb3NvZnQgU01UUCBTZXJ2ZXIgKHZlcnNpb249VExTMV8yLA0KIGNpcGhlcj1UTFNfRUNESEVfUlNBX1dJVEhfQUVTXzI1Nl9HQ01fU0hBMzg0KSBpZCAxNS4yMC4zNjc2LjI1OyBGcmksIDE4DQogRGVjIDIwMjAgMjA6NDU6MTUgKzAwMDANClJlY2VpdmVkOiBmcm9tIERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbQ0KIChbZmU4MDo6NjgwZTpmZTUwOmJhOTI6NmY2ZV0pIGJ5IERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbQ0KIChbZmU4MDo6NjgwZTpmZTUwOmJhOTI6NmY2ZSU1XSkgd2l0aCBtYXBpIGlkIDE1LjIwLjM2NTQuMDI1OyBGcmksIDE4IERlYw0KIDIwMjAgMjA6NDU6MTQgKzAwMDANCkF1dGhlbnRpY2F0aW9uLVJlc3VsdHM6IEVNQ0lucy5jb207IGRraW09bm9uZSAobWVzc2FnZSBub3Qgc2lnbmVkKQ0KIGhlYWRlci5kPW5vbmU7RU1DSW5zLmNvbTsgZG1hcmM9bm9uZSBhY3Rpb249bm9uZSBoZWFkZXIuZnJvbT1FTUNJbnMuY29tOw0KQ29udGVudC1UeXBlOiBtdWx0aXBhcnQvbWl4ZWQ7DQogYm91bmRhcnk9Ii0tLS1zaW5pa2FlbC0/PV8xLTE2MDgzMjQzMjIyMjgwLjU4NjgyMDY4NjgyMzQyODciDQpDb250ZW50LVRyYW5zZmVyLUVuY29kaW5nOiA3Yml0DQpTdWJqZWN0OiB0ZXN0aW5nLiBkb24ndCBkZWxldGUNClRocmVhZC1Ub3BpYzogdGVzdGluZy4gZG9uJ3QgZGVsZXRlDQpUaHJlYWQtSW5kZXg6IEFkYlZmcGpmV2dyeFRiQ0xRbG1PVCt1Z1g3VXhMUT09DQpEYXRlOiBGcmksIDE4IERlYyAyMDIwIDIwOjQ1OjE0ICswMDAwDQpNZXNzYWdlLUlkOg0KIDxETTZQUjIwTUIzMDY1RTc1RDNDN0M4QzZCRUI3OTFCNUFCOUMzMEBETTZQUjIwTUIzMDY1Lm5hbXByZDIwLnByb2Qub3V0bG9vay5jb20+DQpBY2NlcHQtTGFuZ3VhZ2U6IGVuLVVTDQpDb250ZW50LUxhbmd1YWdlOiBlbi1VUw0KWC1Ncy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tU2NsOiAtMQ0KWC1Ncy1UbmVmLUNvcnJlbGF0b3I6DQogPERNNlBSMjBNQjMwNjVFNzVEM0M3QzhDNkJFQjc5MUI1QUI5QzMwQERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbT4NCk1JTUUtVmVyc2lvbjogMS4wDQpYLU1zLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1NZXNzYWdlZGlyZWN0aW9uYWxpdHk6IE9yaWdpbmF0aW5nDQpYLU1zLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1BdXRoc291cmNlOg0KIERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbQ0KWC1Ncy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tQXV0aGFzOiBJbnRlcm5hbA0KWC1Ncy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tQXV0aG1lY2hhbmlzbTogMDQNClgtT3JpZ2luYXRpbmctSXA6IFs1MC44MS45Ni4xMzddDQpYLU1zLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1OZXR3b3JrLU1lc3NhZ2UtSWQ6DQogNWNiZWJkNDQtYmUyZi00OWMwLWVlNWYtMDhkOGEzOTVkMjczDQpYLU1zLVB1YmxpY3RyYWZmaWN0eXBlOiBFbWFpbA0KUmV0dXJuLVBhdGg6IENyYWlnLkguTGVhYmhhcnRARU1DSW5zLmNvbQ0KWC1Ncy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tRXhwaXJhdGlvbnN0YXJ0dGltZTogMTggRGVjIDIwMjAgMjA6NDU6MTUuMDU3OA0KIChVVEMpDQpYLU1zLUV4Y2hhbmdlLU9yZ2FuaXphdGlvbi1FeHBpcmF0aW9uc3RhcnR0aW1lcmVhc29uOiBPcmlnaW5hbFN1Ym1pdA0KWC1Ncy1FeGNoYW5nZS1Pcmdhbml6YXRpb24tRXhwaXJhdGlvbmludGVydmFsOiAxOjAwOjAwOjAwLjAwMDAwMDANClgtTXMtRXhjaGFuZ2UtT3JnYW5pemF0aW9uLUV4cGlyYXRpb25pbnRlcnZhbHJlYXNvbjogT3JpZ2luYWxTdWJtaXQNClgtTXMtT2ZmaWNlMzY1LUZpbHRlcmluZy1Db3JyZWxhdGlvbi1JZDoNCiA1Y2JlYmQ0NC1iZTJmLTQ5YzAtZWU1Zi0wOGQ4YTM5NWQyNzMNClgtTXMtVHJhZmZpY3R5cGVkaWFnbm9zdGljOiBETTZQUjIwTUIzMzE2Og0KWC1Ncy1Pb2ItVGxjLU9vYmNsYXNzaWZpZXJzOiBPTE06NDM5Ow0KWC1NaWNyb3NvZnQtQW50aXNwYW06IEJDTDowOw0KWC1Gb3JlZnJvbnQtQW50aXNwYW0tUmVwb3J0Og0KIENJUDoyNTUuMjU1LjI1NS4yNTU7Q1RSWTo7TEFORzplbjtTQ0w6LTE7U1JWOjtJUFY6TkxJO1NGVjpTS0k7SDpETTZQUjIwTUIzMDY1Lm5hbXByZDIwLnByb2Qub3V0bG9vay5jb207UFRSOjtDQVQ6Tk9ORTtTRlM6O0RJUjpJTkI7DQpYLU1zLUV4Y2hhbmdlLUFudGlzcGFtLU1lc3NhZ2VkYXRhOg0KIHk5Z21FTTlMQVRVWXRORU5obWM5aDBwbmlVYzhwcjdGc2F5akJyM2V2eG95WlcyOEZMaVlCNXhYbWlpRzF5bjU2anlLbzgwL2dZN011NGJUZDdrSzlteVI1MFN6aktkczBwN3Azc05oKzdBbGJlcmlCWlV1d0VnOHVpWVhFY0JIcS9NQlNZVXRNSkpZNnlobkRCRFFrNGtKT1pPRml4K0xZOTgxOWIrRUtWWEt1bUtBRDBPWXJ2K2F4OU5DUFQ4SXBVV2hVKzdBbmRsYVhNMndVdGxEaEJnS2g0Tk1xRnFqMk9ESW1Ed1dkcTU5STc5dUVOd2tEbU80WHVacGcwVEp1Q1NESmRNeU85alNPbzdZVzR4UC96dlNSNno0dEozRzZZWitleWZiajR0UXJFZEJqSHBpR3FTTVFKMS9YSHNxUVlrRmt4cU9vU1p4UFR4TmNjcTZ2U2xsbzdyc3N1c2p6WE5RY0R3MTFoUjdyTDF0b2JDN1ZtS1d0OW8vRHJMeFBLZnk4TTl2QjFpcEkxSndYaURBQmtsN0R0ZzBJdmtvQUpaVnV4WXhBcVBqaC9TZzA4MXFKODk3NnFBa0hnQXlvVkxCZWlVZHNadnVVUm5MSG1RcVljcWw4VitvVW5mY3E5V1kyTjI0NmR4SW05bWFqOVRWSTBrbjdKTnZnYVdiN0FQSndNRDJ3b3pDYXBDRVBBdUlsVGI1cjVBY1F0c0VDQ1ZNcUh4SzJKNVRWNzFGM0RjVDJxdkZvaWd1cStrQTdNbVh0T0ZsUkJ5NkIyajVNRExxM2xFNE5MK0lEczRVeThFU2tSdjVrc1BGakFaVWRNcTd0a000QnV0U3VYQXFtRDl6a21SR2crbzB4NE96Ni9sS290a0tjMzJicHNETS9rUU5KTVhwbzg3UjJIUTV4Z1B6VnFvN1REcldGbm9CdTN6YUMzR0R0LzQ2dHdSRGtOeUxnSndkb3FtME9XVnhEWmVxMC8wcjRlRUIrNlZPQVFTVVFqVWxxT2k4L2lzNElxbWthMTNCYzRLRnY4TEhVS0cvRDlqNWtRWTVXWHVmT3lpZkxXZ1lKVkQ2bnhmNldhY0pVU1NFTEdFcWlYL3JzM3F6YWwxS3B3TTNJeXh1R1NKb2YrSnpYaWU5MFNjbldxZFZXY28yM1ZiSE42OFhDazMyZUVuRHFRcEJ4UTRHbjdmSzRReFF0TnNMTytIYUxqN2phYUFLbi9FR3dNdGVvVlBMRm1PNkwvTldPWlAwbkRYZ0gyWHNTaDVZdUQ4T3VFaGJtb1g3dVQ2WjFjM0Y1TVM0VG82a3hYUC84dEZBOTFJKzFlQnBDQXM9DQpYLU1zLUV4Y2hhbmdlLUNyb3NzdGVuYW50LU9yaWdpbmFsYXJyaXZhbHRpbWU6IDE4IERlYyAyMDIwIDIwOjQ1OjE0LjgyMjMNCiAoVVRDKQ0KWC1Ncy1FeGNoYW5nZS1Dcm9zc3RlbmFudC1Gcm9tZW50aXR5aGVhZGVyOiBIb3N0ZWQNClgtTXMtRXhjaGFuZ2UtQ3Jvc3N0ZW5hbnQtSWQ6IGUwODFiZWZkLTYyODMtNGQ0Ni04ODE2LWViMTllODE3YmFjNQ0KWC1Ncy1FeGNoYW5nZS1Dcm9zc3RlbmFudC1BdXRoc291cmNlOg0KIERNNlBSMjBNQjMwNjUubmFtcHJkMjAucHJvZC5vdXRsb29rLmNvbQ0KWC1Ncy1FeGNoYW5nZS1Dcm9zc3RlbmFudC1BdXRoYXM6IEludGVybmFsDQpYLU1zLUV4Y2hhbmdlLUNyb3NzdGVuYW50LU5ldHdvcmstTWVzc2FnZS1JZDoNCiA1Y2JlYmQ0NC1iZTJmLTQ5YzAtZWU1Zi0wOGQ4YTM5NWQyNzMNClgtTXMtRXhjaGFuZ2UtQ3Jvc3N0ZW5hbnQtTWFpbGJveHR5cGU6IEhPU1RFRA0KWC1Ncy1FeGNoYW5nZS1Dcm9zc3RlbmFudC1Vc2VycHJpbmNpcGFsbmFtZToNCiBNaHlCQytYZTA3cklPMG5RWiszSWZpTU1oS3RZNnhlcEJvRmI3ci83bVdUclVoK2ZYNXAvYWc2Ty9IeHVWYm9XWVMvbWozcmdiekt4dEx3ME9DS1Yzdz09DQpYLU1zLUV4Y2hhbmdlLVRyYW5zcG9ydC1Dcm9zc3RlbmFudGhlYWRlcnNzdGFtcGVkOiBETTZQUjIwTUIzMzE2DQpYLU1zLUV4Y2hhbmdlLVRyYW5zcG9ydC1FbmR0b2VuZGxhdGVuY3k6IDAwOjAwOjAwLjU2NzcwOTYNClgtTXMtRXhjaGFuZ2UtUHJvY2Vzc2VkLUJ5LUJjY2ZvbGRlcmluZzogMTUuMjAuMzY1NC4wMjUNClgtTWljcm9zb2Z0LUFudGlzcGFtLU1haWxib3gtRGVsaXZlcnk6DQogdWNmOjA7am1yOjA7YXV0aDowO2Rlc3Q6STtFTkc6KDc1MDEyOCkoNTIwMDAyMDUwKSg3MDYxNTgpKDk0NDUwNjQ1OCkoOTQ0NjI2NjA0KTsNClgtTWljcm9zb2Z0LUFudGlzcGFtLU1lc3NhZ2UtSW5mbzoNCiBTRWpTbkJRK29WWnZXZnFpMitHQWo0SjhQSEJ4YmdVL0pwSUxrSjdHbDQ5ZkRrV3I4RGgzWmh3akVsZEtUUlMrdXp1Y3ZFY2pRZU9hYzNPTE42M1B1K2x2Mkp4WWxvVE13NU0ra0s5MWx6UnQxeWM3ci9mbXNLay9DS0xkVFAxTnJ2QWlmenpyUTdNQlBCVTR3UWFSU2tQSlpmQWFvRWVrM1c0aUxOeHFuWFI0UUErakFUejcvWm1Mbk5pZ1pxaFo0alJ6TGhNTnBaMERqTE1teGIwd2xGYk43cW1ZZGtuNG10RGxnS3ZzeEw4ci9BZ3l6NE5MUnpvd2VZSUwzdnFpNkxtRytvemNGL2N2WEZlcUY4Q3pWcG9OMVQzZld4ejVFbHdoYW90a1pSUEY4SlVKWHpLaDlRbWNVbnB3OVFuaERqUUFnN2FkY0N5czhjbStqUkR1c1YrczU0R2RlOW85cTJLRE9ldXErbVBRc1dUZmRLSHRsaCs2Z3crVEo3OUsNCkZyb206IENyYWlnIExlYWJoYXJ0IDxDcmFpZy5ILkxlYWJoYXJ0QEVNQ0lucy5jb20+DQpUbzogQ3JhaWcgTGVhYmhhcnQgPENyYWlnLkguTGVhYmhhcnRARU1DSW5zLmNvbT4NCg0KLS0tLS0tc2luaWthZWwtPz1fMS0xNjA4MzI0MzIyMjI4MC41ODY4MjA2ODY4MjM0Mjg3DQpDb250ZW50LVR5cGU6IHRleHQvaHRtbDsgY2hhcnNldD11dGYtOA0KQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogcXVvdGVkLXByaW50YWJsZQ0KDQo8aHRtbCB4bWxuczp2PTNEInVybjpzY2hlbWFzLW1pY3Jvc29mdC1jb206dm1sIiB4bWxuczpvPTNEInVybjpzY2hlbWFzLW1pY3I9DQpvc29mdC1jb206b2ZmaWNlOm9mZmljZSIgeG1sbnM6dz0zRCJ1cm46c2NoZW1hcy1taWNyb3NvZnQtY29tOm9mZmljZTp3b3JkIiA9DQp4bWxuczptPTNEImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vb2ZmaWNlLzIwMDQvMTIvb21tbCIgPQ0KeG1sbnM9M0QiaHR0cDovL3d3dy53My5vcmcvVFIvUkVDLWh0bWw0MCI+PGhlYWQ+DQo8bWV0YSBodHRwLWVxdWl2PTNEIkNvbnRlbnQtVHlwZSIgY29udGVudD0zRCJ0ZXh0L2h0bWw7ID0NCmNoYXJzZXQ9M0R1dGYtOCI+PG1ldGEgbmFtZT0zRCJHZW5lcmF0b3IiIGNvbnRlbnQ9M0QiTWljcm9zb2Z0IFdvcmQgMTUgPQ0KKGZpbHRlcmVkIG1lZGl1bSkiPjxzdHlsZT48IS0tDQovKiBGb250IERlZmluaXRpb25zICovDQpAZm9udC1mYWNlDQoJe2ZvbnQtZmFtaWx5OiJDYW1icmlhIE1hdGgiOw0KCXBhbm9zZS0xOjIgNCA1IDMgNSA0IDYgMyAyIDQ7fQ0KQGZvbnQtZmFjZQ0KCXtmb250LWZhbWlseTpDYWxpYnJpOw0KCXBhbm9zZS0xOjIgMTUgNSAyIDIgMiA0IDMgMiA0O30NCi8qIFN0eWxlIERlZmluaXRpb25zICovDQpwLk1zb05vcm1hbCwgbGkuTXNvTm9ybWFsLCBkaXYuTXNvTm9ybWFsDQoJe21hcmdpbjowaW47DQoJbWFyZ2luLWJvdHRvbTouMDAwMXB0Ow0KCWZvbnQtc2l6ZToxMS4wcHQ7DQoJZm9udC1mYW1pbHk6IkNhbGlicmkiLHNhbnMtc2VyaWY7fQ0KYTpsaW5rLCBzcGFuLk1zb0h5cGVybGluaw0KCXttc28tc3R5bGUtcHJpb3JpdHk6OTk7DQoJY29sb3I6IzA1NjNDMTsNCgl0ZXh0LWRlY29yYXRpb246dW5kZXJsaW5lO30NCnNwYW4uRW1haWxTdHlsZTE3DQoJe21zby1zdHlsZS10eXBlOnBlcnNvbmFsLWNvbXBvc2U7DQoJZm9udC1mYW1pbHk6IkNhbGlicmkiLHNhbnMtc2VyaWY7DQoJY29sb3I6d2luZG93dGV4dDt9DQouTXNvQ2hwRGVmYXVsdA0KCXttc28tc3R5bGUtdHlwZTpleHBvcnQtb25seTsNCglmb250LWZhbWlseToiQ2FsaWJyaSIsc2Fucy1zZXJpZjt9DQpAcGFnZSBXb3JkU2VjdGlvbjENCgl7c2l6ZTo4LjVpbiAxMS4waW47DQoJbWFyZ2luOjEuMGluIDEuMGluIDEuMGluIDEuMGluO30NCmRpdi5Xb3JkU2VjdGlvbjENCgl7cGFnZTpXb3JkU2VjdGlvbjE7fQ0KLS0+PC9zdHlsZT48IS0tW2lmIGd0ZSBtc28gOV0+PHhtbD4NCjxvOnNoYXBlZGVmYXVsdHMgdjpleHQ9M0QiZWRpdCIgc3BpZG1heD0zRCIxMDI2IiAvPg0KPC94bWw+PCFbZW5kaWZdLS0+PCEtLVtpZiBndGUgbXNvIDldPjx4bWw+DQo8bzpzaGFwZWxheW91dCB2OmV4dD0zRCJlZGl0Ij4NCjxvOmlkbWFwIHY6ZXh0PTNEImVkaXQiIGRhdGE9M0QiMSIgLz4NCjwvbzpzaGFwZWxheW91dD48L3htbD48IVtlbmRpZl0tLT48L2hlYWQ+PGJvZHkgbGFuZz0zRCJFTi1VUyIgPQ0KbGluaz0zRCIjMDU2M0MxIiB2bGluaz0zRCIjOTU0RjcyIj48ZGl2IGNsYXNzPTNEIldvcmRTZWN0aW9uMSI+PHAgPQ0KY2xhc3M9M0QiTXNvTm9ybWFsIj5UZXN0aW5nISBEb249RTI9ODA9OTl0IGRlbGV0ZSB0aGlzLjxvOnA+PC9vOnA+PC9wPjxwID0NCmNsYXNzPTNEIk1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+PHAgY2xhc3M9M0QiTXNvTm9ybWFsIj48YSA9DQpocmVmPTNEImh0dHBzOi8vdGhpc2lzcmVhbGx5cGhpc2h5LnNvbWV0aGluZ21hZGV1cC5jb20iPmh0dHBzOi8vdGhpc2lzcmVhbGw9DQp5cGhpc2h5LnNvbWV0aGluZ21hZGV1cC5jb208L2E+IDxvOnA+PC9vOnA+PC9wPjxwIGNsYXNzPTNEIk1zb05vcm1hbCI+PG86cD49DQombmJzcDs8L286cD48L3A+PHRhYmxlIGNsYXNzPTNEIk1zb05vcm1hbFRhYmxlIiBib3JkZXI9M0QiMCIgPQ0KY2VsbHNwYWNpbmc9M0QiNiIgY2VsbHBhZGRpbmc9M0QiMCI+PHRib2R5Pjx0cj48dGQgdmFsaWduPTNEInRvcCIgPQ0Kc3R5bGU9M0QicGFkZGluZzouNzVwdCAuNzVwdCAuNzVwdCAuNzVwdCI+PHAgY2xhc3M9M0QiTXNvTm9ybWFsIj48Yj48c3BhbiA9DQpzdHlsZT0zRCJmb250LXNpemU6MTAuMHB0O2ZvbnQtZmFtaWx5OiZxdW90O0FyaWFsJnF1b3Q7LD0NCnNhbnMtc2VyaWY7Y29sb3I6IzAwNzdDOCI+Q3JhaWcgSCBMZWFiaGFydDwvc3Bhbj48L2I+PHNwYW4gPQ0Kc3R5bGU9M0QiZm9udC1zaXplOjEwLjBwdDtmb250LWZhbWlseTomcXVvdDtBcmlhbCZxdW90Oyw9DQpzYW5zLXNlcmlmO2NvbG9yOiMwMDc3QzgiPjxicj48L3NwYW4+PHNwYW4gc3R5bGU9M0QiZm9udC1zaXplOjguPQ0KMHB0O2ZvbnQtZmFtaWx5OiZxdW90O0FyaWFsJnF1b3Q7LHNhbnMtc2VyaWY7Y29sb3I6IzQ1NDU0NSI+SW5mb3JtYXRpb24gPQ0KU2VjdXJpdHkgQW5hbHlzdCBJPGJyPkdSRU0sIEFJTlMsIENZQiwgU3BsdW5rIEVudGVycHJpc2UgQ2VydGlmaWVkIEFkbWluLCA9DQpBV1MgQ2VydGlmaWVkIFNlY3VyaXR5IC0gU3BlY2lhbHR5PG86cD48L286cD48L3NwYW4+PC9wPjxwID0NCmNsYXNzPTNEIk1zb05vcm1hbCI+PHNwYW4gc3R5bGU9M0QiZm9udC1zaXplOjguMHB0O2ZvbnQtZmFtaWx5OiZxdW90O0FyaWFsJj0NCnF1b3Q7LHNhbnMtc2VyaWY7Y29sb3I6IzQ1NDU0NSI+Q29ycG9yYXRlIE9mZmljZSB8IElUIElTIFNlY3VyaXR5ID0NCkVuZ2luZWVyaW5nPC9zcGFuPjxzcGFuIHN0eWxlPTNEImZvbnQtZmFtaWx5OiZxdW90O0FyaWFsJnF1b3Q7LD0NCnNhbnMtc2VyaWYiPjxvOnA+PC9vOnA+PC9zcGFuPjwvcD48L3RkPjwvdHI+PHRyPjx0ZCBzdHlsZT0zRCJwYWRkaW5nOi43NXB0ID0NCi43NXB0IC43NXB0IC43NXB0Ij48cCBjbGFzcz0zRCJNc29Ob3JtYWwiPjxzcGFuIHN0eWxlPTNEImZvbnQtc2l6ZTo4Lj0NCjBwdDtmb250LWZhbWlseTomcXVvdDtBcmlhbCZxdW90OyxzYW5zLXNlcmlmO2NvbG9yOiM0NTQ1NDUiPjUxNS0zNDUtNzQyNzxicj0NCj48YSBocmVmPTNEIm1haWx0bzpDcmFpZy5ILkxlYWJoYXJ0QEVNQ0lucy5jb20iPjxzcGFuID0NCnN0eWxlPTNEImNvbG9yOiMwMDc3QzgiPkNyYWlnLkguTGVhYmhhcnRARU1DSW5zLmNvbTwvc3Bhbj48L2E+PC9zcGFuPjxzcGFuID0NCnN0eWxlPTNEImZvbnQtZmFtaWx5OiZxdW90O0FyaWFsJnF1b3Q7LHNhbnMtc2VyaWYiPjxvOnA+PC9vOnA+PC9zcGFuPjwvcD48Lz0NCnRkPjwvdHI+PC90Ym9keT48L3RhYmxlPjxwIGNsYXNzPTNEIk1zb05vcm1hbCI+PG86cD4mbmJzcDs8L286cD48L3A+PHAgPQ0KY2xhc3M9M0QiTXNvTm9ybWFsIj48bzpwPiZuYnNwOzwvbzpwPjwvcD48L2Rpdj48L2JvZHk+PC9odG1sPg0KLS0tLS0tc2luaWthZWwtPz1fMS0xNjA4MzI0MzIyMjI4MC41ODY4MjA2ODY4MjM0Mjg3LS0NCg==", "content_header": {"content-type": ["application/octet-stream;name=\"phish_alert_sp2_2.0.0.0.eml\""], "content-description": ["phish_alert_sp2_2.0.0.0.eml"], "content-disposition": ["attachment;filename=\"phish_alert_sp2_2.0.0.0.eml\"; size=\"8452\"; creation-date=\"Fri,18 Dec 2020 20:45:22 GMT\"; modification-date=\"Fri, 18 Dec 2020 20:45:22GMT\""], "content-transfer-encoding": ["base64"]}, "subject": "Phishing EmailReported: testing. don''t delete"}], "urls": ["https://thisisreallyphishy.somethingmadeup.com"], "domains": ["somethingmadeup.com", "microsoft.com", "outlook.com", "w3.org"], "emails": ["craig.h.leabhart@emcins.com"], "observed": {"urls": ["https://thisisreallyphishy.somethingmadeup.com"], "domains": ["somethingmadeup.com", "microsoft.com", "w3.org"], "emails": ["craig.h.leabhart@emcins.com"], "ips": []}, "received": {"ips": ["2603:10b6:5:2ae::15", "2603:10b6:5:1d6::15"], "emails": [], "domains": ["outlook.com"], "domains_internal": [], "foremail": []}, "ips": ["2603:10b6:5:2ae::15", "2603:10b6:5:1d6::15"]}
```



#### Change Case Name
The action changes the case's name (title)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|New Name|The new name of the case|False|String|None|
|Only If First Alert|If marked as True, will only change the case's name if the action was executed on the first alert in the case|False|Boolean|false|



##### JSON Results
```json
{}
```



#### Assign Case to User
This action will assign a user to a case.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Case Id|Case to merge with.|True|String||
|Assign To|assign|True|String|@Admin|
|Alert Id|Alert Id|True|String|id|



##### JSON Results
```json
{}
```



#### Check Entities Fields In Text
This actions allows to search for a specific field from each entity in the scope (or multiple fields using regex) and compare it with one or more values. The compared values can also go through regex. A match is found if one of the post regex values from the entity enrichment is in one or more values searched in.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SearchInData|A JSON that represents the string(s) you want to search in[{ "Data": "", "RegEx": ""}]|True|String|[     {         "Data": "[Event.from]",         "RegEx": "(?<=@)[^.]+(?=\\.)"     } ]|
|FieldsInput|A JSON that describes what fields should be tested for[{ "RegexForFieldName": "", "FieldName": "Field name to search", "RegexForFieldValue": ""}]|True|String|[     {         "RegexForFieldName": "",         "FieldName": "body",         "RegexForFieldValue": ""     },     {         "RegexForFieldName": ".*(_url_).*",         "FieldName": "",         "RegexForFieldValue": ""     },     {         "RegexForFieldName": "",         "FieldName": "body",         "RegexForFieldValue": "HostName: (.*?)"     } ]|
|ShouldEnrichEntity|If set to "<VAL>" will also put an enrichment value on the entity to be recognized as "matched" with the value. The key will be "<VAL>"|False|String|domain_matched|
|IsCaseSensitive|Is the field case sensitive |False|Boolean|false|



##### JSON Results
```json
[{"Entity": "F.ATTACKER4@GMAIL.COM", "EntityResult": [{"RegexForFieldName": ".*", "FieldName": "", "RegexForFieldValue": "", "ResultsToSearch": {"val_to_search": [[{"key": "Type", "val": "USERUNIQNAME"}, {"key": "Identifier", "val": "F.ATTACKER4@GMAIL.COM"}, {"key": "Environment", "val": "Default Environment"}, {"key": "OriginalIdentifier", "val": "f.attacker4@gmail.com"}, {"key": "OrigIdentifier", "val": "f.attacker4@gmail.com"}, {"key": "IsFromLdapString", "val": "False"}, {"key": "IsInternalAsset", "val": "False"}, {"key": "IsSuspicious", "val": "False"}, {"key": "IsEnriched", "val": "False"}, {"key": "IsVulnerable", "val": "False"}, {"key": "IsArtifact", "val": "False"}, {"key": "IsTestCase", "val": "False"}, {"key": "domain_mathed", "val": "true"}, {"key": "domain_matched", "val": "true"}]], "found_results": [{"to_search": {"key": "domain_mathed", "val": "true"}, "searched_in": "true "}, {"to_search": {"key": "domain_matched", "val": "true"}, "searched_in": "true "}], "num_of_results": 2}}]}, {"Entity": "VICKIE.B@SIEMPLIFY.CO", "EntityResult": [{"RegexForFieldName": ".*", "FieldName": "", "RegexForFieldValue": "", "ResultsToSearch": {"val_to_search": [[{"key": "Type", "val": "USERUNIQNAME"}, {"key": "Identifier", "val": "VICKIE.B@SIEMPLIFY.CO"}, {"key": "Environment", "val": "Default Environment"}, {"key": "OriginalIdentifier", "val": "vickie.b@siemplify.co"}, {"key": "OrigIdentifier", "val": "vickie.b@siemplify.co"}, {"key": "IsFromLdapString", "val": "False"}, {"key": "IsInternalAsset", "val": "False"}, {"key": "IsSuspicious", "val": "False"}, {"key": "IsEnriched", "val": "False"}, {"key": "IsVulnerable", "val": "False"}, {"key": "IsArtifact", "val": "False"}, {"key": "IsTestCase", "val": "False"}, {"key": "domain_mathed", "val": "true"}, {"key": "domain_matched", "val": "true"}]], "found_results": [{"to_search": {"key": "domain_mathed", "val": "true"}, "searched_in": "true "}, {"to_search": {"key": "domain_matched", "val": "true"}, "searched_in": "true "}], "num_of_results": 2}}]}, {"Entity": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP", "EntityResult": [{"RegexForFieldName": ".*", "FieldName": "", "RegexForFieldValue": "", "ResultsToSearch": {"val_to_search": [[{"key": "Type", "val": "DestinationURL"}, {"key": "Identifier", "val": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP"}, {"key": "Environment", "val": "Default Environment"}, {"key": "OriginalIdentifier", "val": "http://markossolomon.com/F1q7QX.php"}, {"key": "IsInternalAsset", "val": "True"}, {"key": "IsSuspicious", "val": "False"}, {"key": "IsEnriched", "val": "False"}, {"key": "IsVulnerable", "val": "False"}, {"key": "IsArtifact", "val": "True"}, {"key": "IsTestCase", "val": "False"}, {"key": "domain_mathed", "val": "true"}, {"key": "domain_matched", "val": "true"}]], "found_results": [{"to_search": {"key": "domain_mathed", "val": "true"}, "searched_in": "true "}, {"to_search": {"key": "domain_matched", "val": "true"}, "searched_in": "true "}], "num_of_results": 2}}]}, {"Entity": "YOUR NEW SALARY NOTIFICATION", "EntityResult": [{"RegexForFieldName": ".*", "FieldName": "", "RegexForFieldValue": "", "ResultsToSearch": {"val_to_search": [[{"key": "Type", "val": "EMAILSUBJECT"}, {"key": "Identifier", "val": "YOUR NEW SALARY NOTIFICATION"}, {"key": "Environment", "val": "Default Environment"}, {"key": "IsInternalAsset", "val": "True"}, {"key": "IsSuspicious", "val": "False"}, {"key": "IsEnriched", "val": "False"}, {"key": "IsVulnerable", "val": "False"}, {"key": "IsArtifact", "val": "True"}, {"key": "IsTestCase", "val": "False"}, {"key": "domain_mathed", "val": "true"}, {"key": "domain_matched", "val": "true"}]], "found_results": [{"to_search": {"key": "domain_mathed", "val": "true"}, "searched_in": "true "}, {"to_search": {"key": "domain_matched", "val": "true"}, "searched_in": "true "}], "num_of_results": 2}}]}]
```



#### Check List Subset
Check if one list is a subset of another list.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Original|List of items to check against. Json list or comma separated.|True|String||
|Subset|Subset list.  Json list or comma separated.|True|String||



##### JSON Results
```json
{}
```



#### Convert Into Simulated Case

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Push to Simulated Cases|Full Acuracy|False|Boolean|false|
|Save JSON as Case Wall File|Whether to save the json definition to the case wall for downloading|False|Boolean|true|
|Override Alert Name|Override Alert name in the config for tracking/separation|False|String|None|
|Full path name|Create a name in the full format 'source_product_eventType'|False|Boolean|false|



##### JSON Results
```json
{"Cases": [{"Events": [{"_fields": {"BaseEventIds": "[]", "ParentEventId": -1, "deviceEventClassId": "Email check", "DeviceProduct": "Phishing email detector", "StartTime": "1592847448454", "EndTime": "1592847448454"}, "_rawDataFields": {"sourcetype": "Phishing email detector", "DeviceVendor": "Email server", "StartTime": "1592847662304", "EndTime": "1592847662304", "EventId": "220", "Name": "Your New Salary Notification", "Mail_OriginalEmailBody": "Hello, You have an important email from the Human Resources Department with regards to your December 2015 Paycheck\r\n\r\nThis email is enclosed in the Marquette University secure network, hence access it below\r\n\r\nAccess the documents here <http://markossolomon.com/F1q7QX.php<link removed>\r\n\r\n***Ensure your login credentials are correct to avoid cancellations**\r\n\r\nFaithfully \r\nHuman Resources \r\nUniversity of California, Berkeley\r\n\r", "Severity": "High", "CategoryOutcome": "allowed", "DeviceEventClassId": "Email check", "SourceUserName": "f.attacker4@gmail.com", "DestinationUserName": "vickie.b@siemplify.co", "DestinationURL": "http://markossolomon.com/F1q7QX.php", "sentTime": "1522059431000", "message_id": "220", "subject": "Your New Salary Notification", "body": "Hello, You have an important email from the Human Resources Department with regards to your December 2015 Paycheck\r\n\r\nThis email is enclosed in the Marquette University secure network, hence access it below\r\n\r\nAccess the documents here <http://markossolomon.com/F1q7QX.php<link removed>\r\n\r\n***Ensure your login credentials are correct to avoid cancellations**\r\n\r\nFaithfully \r\nHuman Resources \r\nUniversity of California, Berkeley\r\n\r"}, "Environment": null, "SourceSystemName": null}], "Environment": "Default Environment", "SourceSystemName": "Arcsight", "TicketId": "8dcaf2f2-5ed6-4bcc-8a49-61e0850c3881", "Description": "The email from <f.attacker4@gmail.com> to <vickie.b@siemplify.co> detected as phishing email.", "DisplayId": "8dcaf2f2-5ed6-4bcc-8a49-61e0850c3881", "Reason": "Phishing email detector", "Name": "Suspicious phishing email", "DeviceVendor": "Email server", "DeviceProduct": "Phishing email detector", "StartTime": 1592847662304, "EndTime": 1592847662304, "IsTestCase": true, "Priority": -1, "RuleGenerator": "Simulation_Original_Phishing email detector", "SourceGroupingIdentifier": null, "PlaybookTriggerKeywords": [], "Extensions": [], "Attachments": null}], "IsTestCase": true, "DebugOutput": null, "ConnectorIdentifier": null}
```



#### Attach Playbook to Alert
This action can attach a playbook or block to an alert.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Playbook Name|Comma-separated list of playbooks that need to be attached to the alert|True|String||
|Allow Duplicates|If selected, action will allow the same playbook to be attached multiple times to the alert.|False|Boolean|true|



##### JSON Results
```json
{}
```



#### Create Entities with Separator
Creates entities and adds them to the requested alert.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Entities Identifiers|The entity or entities to be added to the alert.|True|String|<insert string>|
|Entity Type|Siemplify entity type. Example: HOSTNAME / USERNAME / etc.|True|Entity Type|HOSTNAME|
|Is Internal|Mark if entities are part of an internal network.|False|Boolean|false|
|Entities Separator|The character to split the Entities Identifiers field by.|True|String|,|
|Enrichment JSON|Enrichment JSOn data|False|Code||
|PrefixForEnrichment|The prefix to be added to the enrichment data.|False|String|None|



##### JSON Results
```json
{}
```



#### Create Entity Relationships
Creates a relationship between the supplied entities and the linked entities.  If the supplied entities do not exist, it will create them.
Supports Siemplify 5.6+ ONLY.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Entity Identifier(s)|Create new or use existing entity identifier or comma-separated list of identifiers (Example: value1, value2, value3)|True|String||
|Entity Identifier(s) Type|Siemplify Entity type. Example: Host Name / User Name / etc.|True|Entity Type|USERUNIQNAME|
|Connect As|Connect entity identifiers using source, destination, or linked relationship to the target entity identifiers.|True|List|Source|
|Target Entity Type|Connect the entity identifier(s) to entities of this type.  |True|Entity Type|ADDRESS|
|Target Entity Identifier(s)|Entities in this comma separated list, of the type from Target Entity Type, will be linked to the entities in the Entities Identifier(s) parameter.  |False|String||
|Enrichment JSON|An optional JSON object containing key / value pairs of attributes that can be added to the newly created entities. |False|String|None|
|Separator Character|The character to separate the list of entities in Entity Identifiers and/or Target Entity Identifiers by.  Defaults to comma.|False|String|None|



##### JSON Results
```json
[{"Entity": "EMK", "EntityResult": {"status": "created", "enrichment": {"attachment": 0, "linked_entities": "SIEMPLIFY_PS@YAHOO.COM"}}}]
```



#### Create Siemplify Task
This action will assign a task to a user or a role.  The task will be related to the case the action ran on.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SLA (in minutes)|The amount of time (in minutes) the assigned user/role has to respond to the task.|False|String|480|
|Task Content|The details of the task.|True|Content| |
|Assign To|The user or the role the task will be assigned to.|True|Users|Admin|
|Task Title|The title of the task.  Supports Siemplify versions 6.0.0.0 and higher.|False|String|None|
|Due Date|Due date for the task. Expected format ISO8601. If both "Due Date" and "SLA (in minutes)" are set, then "Due Date" parameter will have a priority.|False|String|None|



##### JSON Results
```json
{}
```



#### Delay Playbook
This action will temporarily stop a playbook from completing for a period of time.  
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Seconds|The amount of seconds to delay the playbook for.|True|String|0|
|Minutes|The amount of minutes to delay the playbook for.|True|String|1|
|Hours|The amount of hours to delay the playbook for.|True|String|0|
|Days|The amount of days to delay the playbook for.|True|String|0|



##### JSON Results
```json
{}
```



#### Delay Playbook Synchronous
This action will temporarily stop a playbook from continuing execution for up to 30 seconds. If you need to delay the playbook for longer, use action "Delay Playbook V2"
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Seconds|Seconds|True|String||



##### JSON Results
```json
{}
```



#### Delay Playbook V2
This action will temporarily stop a playbook from completing for a period of time.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Seconds|The amount of seconds to delay the playbook for.|False|String|0|
|Minutes|The amount of minutes to delay the playbook for.|False|String|1|
|Hours|The amount of hours to delay the playbook for.|False|String|0|
|Days|The amount of days to delay the playbook for.|False|String|0|
|Cron Expression|Determines when the playbook should proceed using a cron expression. Will be prioritized over the other parameters.|False|String||



##### JSON Results
```json
{}
```



#### DNS Lookup
Perform a DNS lookup on an entity.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DNS Servers|Single or multiple comma separated servers.|True|String|1.1.1.1|
|Data Type|Uses ANY by default; applies only to host entities|True|List|ANY|



##### JSON Results
```json
[{"Entity": "BMAUS.BADOO.APP", "EntityResult": [{"Type": "A", "Response": "1.1.1.1", "DNSServer": "1.1.1.1"}]}]
```



#### Attach Playbook to All Case Alerts
Attach a specific playbook to all alerts in a case
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Playbook Name|Playbook, which should be attached to all alerts|True|String||



##### JSON Results
```json
{}
```



#### Extract URL Domain
This action enriches all entities with a new field "siemplifytools_extracted_domain" containing the extracted domain out of the entity identifier. If the entity has no domain (file hash for example) it will simply not return anything.
In addition to entities, the user can specify a list of URLs as a parameter and process them, without enriching, naturally.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Separator|Separator string to use to separate URLs|True|String|,|
|URLs|One or more URLs to extract the domain from|False|String|None|
|Extract subdomain|When set to True, the code will also extract the subdomain from the URLs and include it in the result.|False|Boolean|false|



##### JSON Results
```json
[{"Entity": "https://regex101.com/", "EntityResult": {"domain": "regex101.com"}}, {"Entity": "https://pay.ebay.com/rxo?action=view&sessionid=1353028532011", "EntityResult": {"domain": "ebay.com"}}, {"Entity": "YAIR@SIEMPLIFY.CO", "EntityResult": {"domain": "siemplify.co"}}, {"Entity": "JAMES.BOND@SIEMPLIFYCYARX.ONMICROSOFT.COM", "EntityResult": {"domain": "onmicrosoft.com"}}, {"Entity": "FWD: EML ATTACHED WITH PHISHING FROM TREND MICRO", "EntityResult": {"domain": "fwd"}}, {"Entity": "HTTPS://WWW.ONLINESERVICETECH.WEBSITE/LINK/L/P70IPXZLZO2CEED77GJMLWWQXFQCJSVQBYNKZZ346JQYYIKTR6QGAMNQW4L-MXXYSSTIHAEIICD-W1IURFSBN6IUMCO4GWZ_1SBG-62FGIZQK3ZPNIST9WGCBTW-62BXD-FJP7TCWFBSQKVUBEVYLIF_DTC6OYGMQFXDSTFNDB_-CFFKQ4AZNFF13ZWONARJ", "EntityResult": {"domain": "onlineservicetech.website"}}, {"Entity": "HTTPS://WWW.ONLINESERVICETECH.WEBSITE/LINK/T/KEDVS-MM3MP5MILZ6YJDRDZJBBXICMAKHKWUTCO7ZKD4J2-IWL-RGHO3GIXNJDOK)[](", "EntityResult": {"domain": "onlineservicetech.website"}}, {"Entity": "HTTPS://WWW.ONLINESERVICETECH.WEBSITE/LINK/B/KEDVS-MM3MP5MILZ6YJDRDZJBBXICMAKHKWUTCO7ZKD4J2-IWL-RGHO3GIXNJDOK", "EntityResult": {"domain": "onlineservicetech.website"}}]
```



#### Find First Alert
The action will return the identifier of the first alert in a given case
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Get Case Data
This action will get all the data from a case and return a JSON result.  The result includes comments, entity information, insights, playbooks that ran, alert information and events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Case Id|The Case ID to query.  Optional. Will use current case if empty.|False|String|None|
|Fields to Return|Specify a comma-separated list of fields that need to be returned. If nothing is provided, all fields are returned. Getting nested values can be done using "Nested Keys Delimiter" value to chain nested keys and list indexes. For example, if the delimiter is ".": key_1.nested_key_1.0.nested_key_2, key_2, key_3.1.nested_key_1|False|String|None|
|Nested Keys Delimiter|The delimiter to split nested keys. If missing or not provided fetching nested keys is not possible. Cannot be a comma (",")|False|String|.|



##### JSON Results
```json
{"id": 1, "creationTimeUnixTimeInMs": 1766566371945, "modificationTimeUnixTimeInMs": 1767085668074, "createTime": 1766566371945, "updateTime": 1767085668074, "name": "Virus Found Or security risk found", "displayName": "Virus Found Or security risk found", "priority": 80, "important": false, "incident": false, "isImportant": false, "isIncident": false, "startTimeUnixTimeInMs": 1766566371945, "endTimeUnixTimeInMs": null, "assignedUser": "@Tier1", "assignee": "@Tier1", "description": "", "isTestCase": false, "type": "External", "stage": "Triage", "environment": "Default Environment", "status": 1, "products": [{"displayName": "symantec:ep:risk:file", "alert": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B"}], "score": 0, "involvedSuspiciousEntity": false, "workflowStatus": "Completed", "source": "Server", "tasks": [], "incidentId": "", "lastModifyingUserId": "Test automation", "tags": [], "relatedAlerts": [], "alertCount": 1, "alertCards": [{"id": 1, "creationTimeUnixTimeInMs": 0, "modificationTimeUnixTimeInMs": 0, "identifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "status": "Open", "name": "VIRUS FOUND OR SECURITY RISK FOUND:", "priority": "High", "workflowsStatus": 2, "slaExpirationUnixTime": null, "slaCriticalExpirationUnixTime": null, "startTime": 1766566370354, "endTime": 1766566370354, "alertGroupIdentifier": "Virus Found Or security risk found0Hh21ZUzN/GweOk/vAgrummkZ1e/vpRc/D8HGDl4ppE=_700fe321-03d4-4006-b4d3-a99d89cdecd4", "eventsCount": 1, "title": "VIRUS FOUND OR SECURITY RISK FOUND:", "ruleGenerator": "Virus Found Or security risk found", "deviceProduct": "symantec:ep:risk:file", "deviceVendor": "WIN-24TBDNRMSVB", "caseId": 1, "playbookAttached": null, "playbookRunCount": 1, "isManualAlert": false, "sla": {"slaExpirationTime": -1, "criticalExpirationTime": -1, "expirationStatus": "NoSla", "remainingTimeSinceLastPause": -1}, "fieldsGroups": [], "sourceUrl": null, "sourceRuleUrl": null, "siemAlertId": null, "additionalProperties": "{\"Name\":\"Virus found Or security risk found:\",\"Type\":\"ALERT\",\"EndTime\":\"1766566370354\",\"Alert_Id\":\"d2897016-04ea-440e-b404-7b7d76a4190b\",\"TicketId\":\"d2897016-04ea-440e-b404-7b7d76a4190b\",\"DisplayId\":\"d2897016-04ea-440e-b404-7b7d76a4190b\",\"StartTime\":\"1766566370354\",\"IsArtifact\":\"False\",\"IsEnriched\":\"False\",\"IsTestCase\":\"False\",\"Description\":\"This case created by SPLUNK query <Virus found Or security risk found>\",\"Environment\":\"Default Environment\",\"IsSuspicious\":\"False\",\"IsVulnerable\":\"False\",\"DataAccessScope\":null,\"IsInternalAsset\":\"False\",\"AlertBaseEventIds\":\"b8fa90d8-b28d-4caa-9b87-13542a002d0f\",\"EstimatedStartTime\":\"1766566370354\"}", "ticketId": "d2897016-04ea-440e-b404-7b7d76a4190b", "closureDetails": {"reason": "Unknown"}, "productFamilies": [], "entityCards": [], "securityEventCards": [{"fields": [{"order": 0, "groupName": "Highlighted Fields", "isIntegration": false, "isHighlight": true, "items": [{"originalName": "DestinationHostName", "name": "Destination Host Name", "value": "WS-RONI@Test.LOCAL"}]}], "identifier": "d7ab8656-c862-498c-a266-69718e46b1b7", "caseId": 1, "alertIdentifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "name": "Virus found", "product": "symantec:ep:risk:file", "port": null, "sourceSystemName": "Arcsight", "outcome": null, "time": 1766566370354, "type": "Virus found", "artifactEntities": []}], "involvedRelations": [{"identifier": "ee0519f5-5460-43d0-91aa-d7f100d6e367", "alertIdentifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "caseId": 1, "relationType": "SYMANTEC:EP:RISK:FILE_VIRUS#FOUND-8751923F-8872-4445-A9B8-C8C09E6B87A1", "deviceProduct": "symantec:ep:risk:file", "deviceVendor": "symantec:ep:risk:file", "eventClassId": "Virus found", "startTime": 1766566370354, "endTime": 1766566370354, "additionalProperties": "{\"Guid\":\"40bf97ad-34fd-4adf-b17b-56f13aca7eba\",\"Name\":\"Virus found\",\"DeviceVendor\":\"symantec:ep:risk:file\",\"EventClassId\":\"Virus found\",\"AggregatedEdgesData\":\"b8fa90d8-b28d-4caa-9b87-13542a002d0f,1766566370354,1766566370354\",\"DestinationProcessName\":\"chrome.exe\"}"}]}], "wallData": [{"caseId": 1, "activityKind": "CaseUpdated", "activityDataJson": "{\"kind\": 1, \"comment\": \"Test Admin has executed a manual action \\\"Tools_Copy of Ping\\\" on case \\\"Virus Found Or security risk found\\\" (1).\", \"skipComment\": null, \"newValueJson\": null, \"activityDescription\": null}", "favorite": false, "name": "projects/project/locations/location/instances/instance/cases/1/caseWallRecords/CaseUpdatedActions9", "id": "CaseUpdatedActions9", "creatorUserId": "3e50c4ab-2696-4070-b74a-66ab035bb6bd", "activityId": 9, "activityType": "CaseStatusChange", "createTime": 1766573278621, "updateTime": 1766573278621}], "entityCards": [{"identifier": "WS-RONI@Test.LOCAL", "type": "HOSTNAME", "suspicious": false, "linkedEntities": [{"identifier": "0.0.0.0", "type": "ADDRESS", "suspicious": false, "linkedEntities": [], "direction": 0}]}], "entities": [{"caseId": 1, "type": "FILEHASH", "enriched": false, "artifact": true, "vulnerable": false, "suspicious": false, "attacker": false, "pivot": false, "internal": true, "manuallyCreated": false, "fields": [{"highlighted": false, "displayName": "Default", "hidden": false, "items": [{"name": "Network_Priority", "originalName": "Network_Priority", "value": "0"}]}], "identifier": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F", "id": 5, "alertIdentifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "environment": "Default Environment", "additionalProperties": "{\"Type\":\"FILEHASH\",\"IsArtifact\":\"True\",\"IsEnriched\":\"False\",\"IsTestCase\":\"False\",\"IsVulnerable\":\"False\",\"IsInternalAsset\":\"False\",\"OriginalIdentifier\":\"275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F\"}", "alertGroupIdentifier": "Virus Found Or security risk found0Hh21ZUzN/GweOk/vAgrummkZ1e/vpRc/D8HGDl4ppE=_700fe321-03d4-4006-b4d3-a99d89cdecd4", "networkPriority": 0}], "isOverflowCase": false, "overflowCase": false, "isManualCase": false, "manualCase": false, "slaExpirationUnixTime": null, "slaCriticalExpirationUnixTime": null, "stageSlaExpirationUnixTimeInMs": null, "stageSlaCriticalExpirationUnixTimeInMs": null, "canOpenIncident": false, "sla": {"slaExpirationTime": -1, "criticalExpirationTime": -1, "expirationStatus": "NoSla", "remainingTimeSinceLastPause": -1}, "stageSla": {"slaExpirationTime": -1, "criticalExpirationTime": -1, "expirationStatus": "NoSla", "remainingTimeSinceLastPause": -1}, "alertSla": {"slaExpirationTime": -1, "criticalExpirationTime": -1, "expirationStatus": "NoSla", "remainingTimeSinceLastPause": -1}, "insights": [{"alertIdentifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "caseId": 1, "triggeredBy": "Test", "title": "Entity insight", "content": "A new entity", "entity": {"caseId": 1, "alertIdentifier": "VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B", "alertStatus": 0, "identifier": "WS-RONI@Test.LOCAL", "entityType": "HOSTNAME", "isInternal": false, "isSuspicious": false, "isArtifact": false, "isPivot": false, "environment": "Default Environment", "highlightedFieldsGroups": [], "isManuallyCreated": false, "sourceUrl": null, "fields": [{"order": 0, "groupName": "Default", "isIntegration": false, "isHighlight": false, "items": [{"originalName": "Network_Priority", "name": "Network_Priority", "value": "0"}]}]}, "severity": 0, "type": 6, "additionalDataType": null, "additionalData": null, "additionalDataTitle": null, "creatorUserName": null, "entityIdentifier": "WS-RONI@Test.LOCAL", "insightType": 1, "alertIdentifiers": ["VIRUS FOUND OR SECURITY RISK FOUND:_D2897016-04EA-440E-B404-7B7D76A4190B"], "entityType": "HOSTNAME", "creatorUserId": null, "id": 4, "isFavorite": false, "modificationTimeUnixTimeInMs": 1766569221777, "creationTimeUnixTimeInMs": 1766569221777}]}
```



#### Get Case SLA
Gets the Case SLA and critical SLA in multiple formats.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DateTime Format|Specify the DateTime Format in which the SLA expiration time will be presented by the action. Defaults to "%Y-%m-%d %H:%M:%S"|True|String|%Y-%m-%d %H:%M:%S|



##### JSON Results
```json
{"SLA_unix": 1700748819259, "SLA": "2023-11-23 14:13:39", "critical_SLA_unix": 1700676819259, "critical_SLA": "2023-11-22 18:13:39"}
```



#### Get Certificate Details
Getting the certificate of a given URL
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Url to check|Url to check|True|String|expired.badssl.com|



##### JSON Results
```json
{"hostname": "www.abc.com", "ip": "127.0.0.1", "commonName": "www.abc.com", "is_self_signed": false, "SAN": ["www.abc.com"], "is_expired": false, "issuer": "WR2", "not_valid_before": "08/11/2025", "not_valid_after": "11/03/2025", "days_to_expiration": 63}
```



#### Get Context Value
The action gets a key and value in a specific context (alert or case)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|Alert or Case or Global|True|List|Alert|
|Key|Key|True|String|Key|



##### JSON Results
```json
{}
```



#### Get Current Time
Returns the current date and time 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Datetime Format|The format of the date and time|True|String|%d/%m/%Y %H:%M|



##### JSON Results
```json
{}
```



#### Get Integration Instances
Returns all the integration instances for an environment.
Timeout - 600 Seconds



##### JSON Results
```json
{"instances": [{"identifier": "25dac1d5-f374-44e0-8807-c7f9f4c10e70", "integrationIdentifier": "SiemplifyUtilities", "environmentIdentifier": "*", "instanceName": "SiemplifyUtilities_1", "instanceDescription": "Thisinstance was created by Siemplify", "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "f631e423-7647-480f-adf2-eec10db342cd", "integrationIdentifier": "FileUtilities", "environmentIdentifier": "*", "instanceName": "FileUtilities_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "621facb9-c91a-4713-87e3-45633dc87614", "integrationIdentifier": "HTTP", "environmentIdentifier": "*", "instanceName": "HTTP_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "181ca4bd-21ba-4677-a662-10480e5b1756", "integrationIdentifier": "Siemplify", "environmentIdentifier": "*", "instanceName": "Siemplify_1", "instanceDescription": "Thisinstance was created by Siemplify", "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "3b818af9-970f-4cf6-8745-a6fefce9031f", "integrationIdentifier": "Insights", "environmentIdentifier": "*", "instanceName": "Insights_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "6c7a3fd8-82b4-4017-bb54-eb1105514cc4", "integrationIdentifier": "Salesforce", "environmentIdentifier": "*", "instanceName": "Salesforce_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "63b22e46-92ac-4bd1-9b2c-86c5f4d3dbeb", "integrationIdentifier": "PostgreSQL", "environmentIdentifier": "*", "instanceName": "PostgreSQL_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "9405894b-3ea5-4a57-8eb6-80c916928b2e", "integrationIdentifier": "FalconSandbox", "environmentIdentifier": "*", "instanceName": "FalconSandbox_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "6952e1e9-2a5a-45ba-a73b-a7c63203116a", "integrationIdentifier": "Lists", "environmentIdentifier": "*", "instanceName": "Lists_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "82d9e022-5921-43dc-9881-97cdf17f5a1a", "integrationIdentifier": "Tools", "environmentIdentifier": "*", "instanceName": "Tools_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "5d0058f5-3b7e-45da-a626-ee0f3fb7e953", "integrationIdentifier": "Functions", "environmentIdentifier": "*", "instanceName": "Functions_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "fd689339-931c-427a-b512-22787d187916", "integrationIdentifier": "TemplateEngine", "environmentIdentifier": "*", "instanceName": "TemplateEngine_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "916b05c4-1e5f-4d9b-bf3c-6675244d73ff", "integrationIdentifier": "Talos", "environmentIdentifier": "*", "instanceName": "Talos_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "da246d3b-3a85-4626-b255-6b0886080fe7", "integrationIdentifier": "SiemplifyReporting", "environmentIdentifier": "*", "instanceName": "SiemplifyReporting_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "70e8064e-83d1-476a-afdd-7d21c30affdf", "integrationIdentifier": "Slack", "environmentIdentifier": "*", "instanceName": "Slack_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "4abe77e5-9243-4b41-ad19-9964e1eef4f3", "integrationIdentifier": "Thinkific", "environmentIdentifier": "*", "instanceName": "Thinkific_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "95be54bd-b050-4df4-870c-b0eb34dd9368", "integrationIdentifier": "Bricata", "environmentIdentifier": "*", "instanceName": "Bricata_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "d38c7d2c-7a5e-48f4-be12-f0e9604b1e51", "integrationIdentifier": "Tempo", "environmentIdentifier": "*", "instanceName": "Tempo_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "293b1e87-6a6f-4ac0-b876-5ca1f2671979", "integrationIdentifier": "Zendesk", "environmentIdentifier": "*", "instanceName": "Zendesk_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "7e10832d-2207-4c6b-9cda-2be40b806282", "integrationIdentifier": "WHOISXML API", "environmentIdentifier": "*", "instanceName": "WHOIS XML API_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "bcb725f9-9fbc-401f-ac9f-bfaabb0fe471", "integrationIdentifier": "ScreenshotMachine", "environmentIdentifier": "*", "instanceName": "ScreenshotMachine_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "cf761104-40a2-4f58-aa78-4e00df5c19c8", "integrationIdentifier": "VirusTotalV3", "environmentIdentifier": "*", "instanceName": "VirusTotalV3_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "eca26000-8311-4451-b3e6-0db92d8a3bc5", "integrationIdentifier": "Cherwell", "environmentIdentifier": "*", "instanceName": "Cherwell_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "eba6f714-f2bf-4972-98aa-4d00b3af44d8", "integrationIdentifier": "GoogleCalendar", "environmentIdentifier": "*", "instanceName": "Google Calendar_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "c3385a3c-b391-42eb-9c0f-6999f7776732", "integrationIdentifier": "AbuseIPDB", "environmentIdentifier": "*", "instanceName": "AbuseIPDB_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "451f72f2-45b5-4d58-89bb-e5917c5634b0", "integrationIdentifier": "GitSync2", "environmentIdentifier": "*", "instanceName": "GitSync2_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "0924e3a1-a2e3-4ea3-be1e-2453a329545c", "integrationIdentifier": "Enrichment", "environmentIdentifier": "*", "instanceName": "Enrichment_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "db90e2d6-5bc7-4f7e-b187-49adbc74cab4", "integrationIdentifier": "Jira", "environmentIdentifier": "*", "instanceName": "Jira_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "377b091b-ad8b-4b43-a3a7-4dc90e30bf3e", "integrationIdentifier": "EmailUtilities", "environmentIdentifier": "*", "instanceName": "EmailUtilities_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "63321764-5e24-4757-a222-bcce81e539be", "integrationIdentifier": "EmailV2", "environmentIdentifier": "*", "instanceName": "GMX", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "5d719d2b-b154-422f-85c9-5f4149705e05", "integrationIdentifier": "GoogleSheets", "environmentIdentifier": "*", "instanceName": "Everafter", "instanceDescription": "Everafteruser to sync with Salesforce", "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "d76fd62b-b403-49c2-8ea4-c29b99135eb0", "integrationIdentifier": "GoogleDrive", "environmentIdentifier": "*", "instanceName": "Everafter", "instanceDescription": "Everafteruser to sync with Salesforce", "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "fc215fb0-c48e-4604-9381-9644ff03b198", "integrationIdentifier": "GoogleSyncs", "environmentIdentifier": "*", "instanceName": "GoogleSyncs_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "bfd8259b-02eb-40d5-90ed-3d12ce044625", "integrationIdentifier": "InDevelopment", "environmentIdentifier": "*", "instanceName": "InDevelopment_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "df164fa5-ff7f-4987-a012-024556fbe3b5", "integrationIdentifier": "XForce", "environmentIdentifier": "*", "instanceName": "XForce_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}, {"identifier": "c06fe27d-1077-4769-b5ad-dbfdb1aa1e33", "integrationIdentifier": "AnyRun", "environmentIdentifier": "*", "instanceName": "AnyRun_1", "instanceDescription": null, "isConfigured": false, "isRemote": false, "isSystemDefault": false}, {"identifier": "044b450c-aa5f-40c1-a226-337428ba15c8", "integrationIdentifier": "Anomali", "environmentIdentifier": "*", "instanceName": "Anomali_1", "instanceDescription": null, "isConfigured": true, "isRemote": false, "isSystemDefault": false}]}
```



#### Get Original Alert Json
The action gets the original alert Json (raw data) and presents it as a Json result. 
Timeout - 600 Seconds



##### JSON Results
```json
{"CreatorUserId": null, "Events": [{"_fields": {"BaseEventIds": "[]", "ParentEventId": -1, "deviceEventClassId": "Email check", "DeviceProduct": "Phishing email detector", "StartTime": "12345", "EndTime": "12345"}, "_rawDataFields": {"sourcetype": "Phishing email detector", "DeviceVendor": "Email server", "StartTime": "12345", "EndTime": "12345", "EventId": "220", "Name": "Your New Salary Notification", "Mail_OriginalEmailBody": "Hello", "Severity": "High", "CategoryOutcome": "allowed", "DeviceEventClassId": "Email check", "SourceUserName": "f.xx@xx.com", "DestinationUserName": "xx.x@xx.co", "DestinationURL": "http://xx.com/xx.php", "sentTime": "12345", "message_id": "000", "subject": "Your New Salary Notification", "body": "Hello"}, "Environment": null, "SourceSystemName": null, "Extensions": []}], "Environment": "Default Environment", "SourceSystemName": "xxxx", "TicketId": "xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx", "Description": "The email from <f.xx@xx.com> to <xx.x@xx.co> detected as phishing email.", "DisplayId": "xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxxx", "Reason": "Phishing email detector", "Name": "Suspicious phishing email", "DeviceVendor": "Email server", "DeviceProduct": "Phishing email detector", "StartTime": 12345, "EndTime": 12345, "Type": 0, "Priority": 80, "RuleGenerator": "Phishing email detector", "SourceGroupingIdentifier": null, "PlaybookTriggerKeywords": [], "Extensions": [], "Attachments": null, "IsTrimmed": false, "DataType": 1, "SourceType": 1, "SourceSystemUrl": null, "SourceRuleIdentifier": null, "SiemAlertId": null, "UpdatedFields": [], "AlertUpdateSupported": false, "AlertMetadata": {}, "DataAccessScope": null, "__TraceContext": {"traceparent": "xx-xx-xx-xx", "baggage": "xx"}, "__CorrelationId": "xxxxx"}
```



#### Get Siemplify Users
This action will return an object containing all users configured in the Siemplify system.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hide Disabled Users|Hide disabled users from the result.|False|Boolean|true|



##### JSON Results
```json
{"siemplifyUsers": [{"permissionGroup": "string", "firstName": "string", "lastName": "string", "permissionType": 1, "role": 1, "socRoleId": 1, "email": "string", "userName": "string", "imageBase64": null, "userType": 1, "identityProvider": -1, "isDisabled": false, "shouldShowLicenseAgreement": false, "lastLoginTime": 1111111111111, "previousLoginTime": 1111111111111, "environments": ["string"], "id": 1, "creationTimeUnixTimeInMs": 1111111111111, "modificationTimeUnixTimeInMs": 1111111111111}, {"permissionGroup": "string", "firstName": "string", "lastName": "string", "permissionType": 1, "role": 1, "socRoleId": 1, "email": "string", "userName": "string", "imageBase64": "string", "userType": 1, "identityProvider": -1, "isDisabled": false, "shouldShowLicenseAgreement": false, "lastLoginTime": 1111111111111, "previousLoginTime": 1111111111111, "environments": ["string"], "id": 1, "creationTimeUnixTimeInMs": 1111111111111, "modificationTimeUnixTimeInMs": 1111111111111}]}
```



#### Lock Playbook
This action will cause the current playbook to pause until all playbooks from the previous alert complete.
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Look-A-Like Domains
This action will compare domain entities against the list of domains defined for the environment.  If the domains are similar the entity will be marked as suspicious and enriched with the matching domain.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "SIEMPLIFY.CO", "EntityResult": {"look_a_like_domains": []}}, {"Entity": "0utl00k.com", "EntityResult": {"look_a_like_domains": ["outlook.com"]}}]
```



#### Normalize Entity Enrichment
The action receives a list of keys from the entity and replaces them
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Normalization Data|Enter a  JSON in the format of the example presented below. |True|String|[     {         "entitiy_field_name": "AT_fields_Name",         "new_name": "InternalEnrichment_Name"     },     {         "entitiy_field_name": "AT_fields_Direct-Manager",         "new_name": "InternalEnrichment_DirectManager_Name"     },     {         "entitiy_field_name": "AT_Manager_fields_Work-Email",         "new_name": "InternalEnrichment_DirectManager_Email"     } ]|



##### JSON Results
```json
{}
```



#### Ping
Check connectivity
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Re-Attach Playbook
This action will remove a playbook from a case, delete any result data in the case from that playbook, and re-attach the playbook so it will run again.
Requires installation of PostgreSQL integration, configured to the Shared Environment with an instance name of Siemplify.  See CSM / Support for additional details.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Playbook Name|This is the name of the playbook that will be removed from the case and re-attached.  Once re-attached, it will run again.|True|Playbook Name|Basic Phishing PB - Zero to Hero|



##### JSON Results
```json
{}
```



#### Search Text
Search for the 'Search For' parameter in the input text or loop through the 'Search For Regex' list and find matches in the input text.  If there is a match, the action will return true.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Text|Enter the text that will be searched.|True|String||
|Search For|Optional: Enter the string that the Text will be searched for.|False|String|None|
|Search For Regex|Optional.  List of regexes that will be used to search the string.  Regex should be wrapped in double quotes.  Supports comma delimited list.|False|String|None|
|Case Sensitive|Should the search be case sensitive?|False|Boolean|false|



##### JSON Results
```json
{"matches": [{"search": "input", "input": "This is the input test. I want to find a few things.", "match": true}, {"search": "few", "input": "This is the input test. I want to find a few things.", "match": true}]}
```



#### Set Context Value
The action sets a key and value in a specific context (alert or case)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Value|Value|True|String|Value|
|Key|Key|True|String|Key|
|Scope|Alert or Case or Global|True|List|Alert|



##### JSON Results
```json
{}
```



#### Spell Check String
The Spell Check String action will check the spelling of an input string.  It will output the percent accurate, total words, amount of misspelled words, list of each misspelled word and the correction, and a corrected version of the input string.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|String|The string that will be checked for spelling errors. |True|String||



##### JSON Results
```json
{"input_string": "STRING", "total_words": 112, "total_misspelled_words": 5, "misspelled_words": [{"misspelled_word": "worda", "correction": "word"}, {"misspelled_word": "wordb", "correction": "word"}], "accuracy": 95, "corrected_string": "CORRECTED STRING"}
```



#### Get Email Templates
Returns all of the email templates in a system.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Template Type|HTML or Standard Template|True|List|Standard|



##### JSON Results
```json
{"templates": [{"type": 0, "name": "Standard Template Name", "content": "Thisis the content of a standard email template.", "creatorUserName": "Rob", "forMigration": false, "environments": ["ReedSales"], "id": 1, "creationTimeUnixTimeInMs": 1618588676723, "modificationTimeUnixTimeInMs": 1618588676734}, {"type": 0, "name": "AllENV Template", "content": "All env template", "creatorUserName": "Rob", "forMigration": false, "environments": ["*"], "id": 3, "creationTimeUnixTimeInMs": 1618588714655, "modificationTimeUnixTimeInMs": 1618588714655}, {"type": 0, "name": "ReedSales_Create Record", "content": "{\n    \"state\": \"1\",\n    \"impact\":\"3\",\n    \"priority\": \"5\",\n    \"short_description\": \"Incident involvinguser(s): [Alert.Users]\",\n    \"u_incident_insights\": \"[CaseData.JsonResult|\"insights\" | filter(\"triggeredBy\", \"=\", \"VirusTotalV3\") | \"content\"]\",\n    \"severity\":\"3\"\n}\n", "creatorUserName": "Rob", "forMigration": false, "environments": ["ReedSales"], "id": 5, "creationTimeUnixTimeInMs": 1618601564841, "modificationTimeUnixTimeInMs": 1618601564841}]}
```



#### Unflatten JSON
Unflatten a JSON.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|JSON Object|Specify a JSON object that needs to be unflattened|True|String||
|Delimiter|The flattening delimiter used to chain keys with nested values, and should be used to split the keys' names. Leaving empty will separate keys by every value that is not a letter, number or underscore.|False|String|_|



##### JSON Results
```json
{"unflattened": "json"}
```



#### Update Alert Score
This will update the alert score by the amount supplied in the 'Input' parameter. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Input|The value to increment or decrement the alert score by.|True|String|0|



##### JSON Results
```json
{}
```



#### Update Case Description
This action will update the description of the case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Case Description|The description of the case will be updated to this value.|True|String|<insert value>|



##### JSON Results
```json
{}
```



#### Wait for Playbook to Complete
This action will cause a playbook to wait until another playbook or block, that is running on the same alert, completes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Playbook Name|The name of the playbook or block.|True|String||



##### JSON Results
```json
{}
```






## Jobs

#### Close Cases Based On Search
This job will close all cases based on a search query.  The Search Payload is the payload used in the 'CaseSearchEverything' API call.  To get an example of this value, go to Search in the UI and open Developer Tools.  Search for the cases to delete.  Look for the "CaseSearchEverything" api call in DevTools.  Copy the JSON payload of the POST request and paste in "Search Payload".  The Close Reason should be 0 or 1.   0 = malicious 1  = not malicious.  Root Cause comes from Settings -> Case Data -> Case Close Root Cause

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Search Payload|False|String|{}|
|Close Comment|True|String||
|Close Reason|True|Integer|1|
|Root Cause|True|String||

#### Tag Untouched Cases
This job will search all open cases, and identify cases that have not been touched in Max Time hours, and apply the tag/tags listed in the tags parameter

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Tags|True|String|Open Case Review|
|Unmodified Time|True|Integer|8|




A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.