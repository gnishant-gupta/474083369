
# Akamai

Akamai provides security services deployed across a global edge network. This includes Web Application Firewall (WAF) capabilities identifying web-based attacks, Bot Management distinguishing between human and automated traffic, DDoS mitigation services absorbing malicious traffic floods, and API security protections. Akamai generates security event data reflecting threats detected and actions taken at the internet edge.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Host|The hostname of Akamai instance.|True|String|https://{host}|
|Client Token|The Akamai Client token.|True|Password|*****|
|Client Secret|The Akamai Client Secret.|True|Password|*****|
|Access Token|The Akamai Access token.|True|Password|*****|
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to Akamai. Selected by default.|False|Boolean|true|


#### Dependencies
| |
|-|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.24.2-py3-none-any.whl|
|pycryptodome-3.22.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.166.0-py2.py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cryptography-44.0.2-cp39-abi3-manylinux_2_34_x86_64.whl|
|ndg_httpsclient-0.5.1-py3-none-any.whl|
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
|certifi-2025.1.31-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|pyOpenSSL-25.0.0-py3-none-any.whl|
|edgegrid_python-2.0.0-py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|TIPCommon-2.2.1-py2.py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|typing_extensions-4.13.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|googleapis_common_protos-1.69.2-py3-none-any.whl|


## Actions
#### Activate Client List
Use the Activate Client List action to enable a specific client list within your Akamai environment.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client List Name|The name of the client list to activate. If both Client List Name and Client List ID are provided, the action prioritizes Client List ID.|False|String||
|Client List ID|The unique identifier of the client list to activate. If both Client List Name and Client List ID are provided, the action prioritizes Client List ID.|False|String||
|Environment|The target network environment for the activation.|False|List|Production|
|Comment|A brief description or justification associated with the activation operation.|False|String||
|Notification Recipients|A comma-separated list of email addresses that receive a notification regarding the client list activation.|False|String||



##### JSON Results
```json
{"action": "xxxx", "activations": {"xxxx": {"activationId": 11111, "activationStatus": "xxxx"}}, "createDate": "2026-02-09T12:28:14.159+00:00", "createdBy": "xxxx", "listId": "xxxx", "version": 1}
```



#### Add Items To Client List
Use the Add Items To Client List action to add items to the client list in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client List Name|Name of the client list that needs to be updated. If both "Client List Name" and "Client List ID" are provided, action will work with ID.|False|String||
|Client List ID|ID of the client list that needs to be updated. If both "Client List Name" and "Client List ID" are provided, action will work with ID.|False|String||
|Item Value|Comma-separated list of items that need to be added to the client list.|True|String||
|Item Description|Description for the items that will be added to the client list.|False|String||
|Item Expiration Date|Expiration date for the added items. Expected format: ISO 8601.|False|String||
|Item Tags|Comma-separated list of tags for the added items.|False|String||



##### JSON Results
```json
[{"createDate":"2023-04-05T19:29:02.320+00:00","createdBy":"xxxxxx","description":"xxx-xxx","expirationDate":"2023-12-31T23:59:19.700+00:00","productionStatus":"INACTIVE","stagingStatus":"INACTIVE","tags":["aaaaaaaa"],"type":"xxxx","updateDate":"2023-04-05T19:29:02.320+00:00","updatedBy":"xxx","value":"xxxx", "status": "xxxx"}, {"value": "xxxx", "status": "xxxx"}, {"value": "xxxx", "status": "xxxx", "error": "xxxx"}]
```



#### Remove Items From Network List
Use the Remove Items From Network List action to remove items from the network list in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network List Name|Name of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Network List ID|ID of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Items|Comma-separated list of items that need to be removed from the network list.|True|String||



##### JSON Results
```json
{"networkListType": "xxxx", "accessControlGroup": "xxxx", "name": "xxxx", "elementCount": 3011, "readOnly": false, "shared": false, "syncPoint": 22, "type": "xxxx", "uniqueId": "xxxx", "links": {"activateInProduction": {"href": "xxxx", "method": "xxxx"}, "activateInStaging": {"href": "xxxx", "method": "xxxx"}, "appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}}}
```



#### Ping
Use the Ping action to test the connectivity to Akamai.
Timeout - 600 Seconds



#### Add Items To Network List
Use the Add Items To Network List action to add items to the network list in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network List Name|Name of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Network List ID|ID of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Items|Comma-separated list of items that need to be added to the network list.|True|String||



##### JSON Results
```json
{"networkListType": "xxxx", "accessControlGroup": "xxxx", "name": "xxxx", "elementCount": 3011, "readOnly": false, "shared": false, "syncPoint": 22, "type": "xxxx", "uniqueId": "xxxx", "links": {"activateInProduction": {"href": "xxxx", "method": "xxxx"}, "activateInStaging": {"href": "xxxx", "method": "xxxx"}, "appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}}}
```



#### Get Client Lists
Use the Get Client Lists action to get information about client lists in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client List Name|Comma-separated list of client list names that you want to search for.|False|String||
|Client List ID|Comma-separated list of client list ids that you want to search for.|False|String||
|Include Items|If enabled, action will return information about items inside the client list. Note: this information is only returned, if either “Client List Name” or “Client List ID” is provided.|False|Boolean|false|
|Type|Type of the client list that needs to be searched. If Select One is provided, action will search among all client lists.|False|List|Select One|
|Max Client Lists To Return|How many client lists to return. The maximum is 100.|True|String|100|
|Max Client List Items To Return|How many items to return per client list. The maximum is 100.|True|String|100|



##### JSON Results
```json
[{"availableActions": {"DELETE": {"available": true}}, "createDate": "2025-05-19T13:07:39.188+00:00", "createdBy": "xxx@abc.com", "deprecated": false, "items": [{"createDate": "2025-05-19T14:17:17.432+00:00", "createdBy": "xxxxxx", "description": "xx - xx America", "expirationDate": "2025-12-31T23:59:19.700+00:00", "productionStatus": "xxx", "stagingStatus": "xxx", "tags": ["test1"], "type": "IP", "updateDate": "2025-05-19T14:17:17.432+00:00", "updatedBy": "xxxxxx", "value": "x.x.x.x"}], "itemsCount": 1, "listId": "1234_xxxxx", "listType": "CL", "name": "xxxxaaaaasssddd", "notes": "Testing_File_Hash", "productionActivationStatus": "xxxxx", "productionActiveVersion": "x.x", "readOnly": false, "rollbackPossible": false, "shared": false, "stagingActivationStatus": "INACTIVE", "stagingActiveVersion": "x.x", "tags": [], "type": "IP", "updateDate": "2025-05-19T14:18:28.514+00:00", "updatedBy": "xxxxxxx", "upgradedFromNetworkList": false, "version": 4}]
```



#### Get Network Lists
Use the Get Networks Lists action to get information about networks lists in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network List Name|Comma-separated list of network list names that you want to search for.|False|String||
|Network List ID|Comma-separated list of network list ids that you want to search for.|False|String||
|Include Items|If enabled, action will return information about items inside the network lists.|False|Boolean|false|
|Include Activation Status|If enabled, action will return information about activation status. Note: this information is only returned, if either "Network List Name" or "Network List ID" is provided.|False|Boolean|false|
|Activation Environment|Environment for which the activation status should be returned. Only returned, if you provide a specific Network List Name/Network List ID.|False|List|Both|
|Max Network Lists To Return|How many network lists to return.|True|String|100|
|Max Network List Items To Return|How many items to return per network list. Maximum is 100.|True|String|100|



##### JSON Results
```json
[{"networkListType": "xxxx", "accessControlGroup": "xxxx", "name": "xxxx", "elementCount": 3011, "readOnly": false, "shared": false, "syncPoint": 22, "type": "xxxx", "uniqueId": "xxxx", "links": {"activateInProduction": {"href": "xxxx", "method": "xxxx"}, "activateInStaging": {"href": "xxxx", "method": "xxxx"}, "appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}}, "Activation_STAGING": {"activationId": 12345, "activationComments": "xxxx", "activationStatus": "xxxx", "syncPoint": 5, "uniqueId": "xxxx", "fast": false, "dispatchCount": 1, "links": {"appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "syncPointHistory": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}, "activationDetails": {"href": "xxxx"}}}, "Activation_PRODUCTION": {"activationId": 12345, "activationComments": "xxxx", "activationStatus": "xxxx", "syncPoint": 5, "uniqueId": "xxxx", "fast": false, "dispatchCount": 1, "links": {"appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "syncPointHistory": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}, "activationDetails": {"href": "xxxx"}}}, "items": ["xxxx"]}]
```



#### Activate Network List
Use the Activate Network List action to activate the network list in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network List Name|Name of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Network List ID|ID of the network list that needs to be updated. If both "Network List Name" and "Network List ID" are provided, action will work with ID.|False|String||
|Environment|Environment for which the activation status should be returned.|False|List|Production|
|Comment|A comment that will be associated with activation operation.|False|String||
|Notification Recipients|Comma-separated list of emails that should receive the notification about activation of network list.|False|String||



##### JSON Results
```json
{"activationId": 12345, "activationComments": "xxxx", "activationStatus": "xxxx", "syncPoint": 5, "uniqueId": "xxxx", "fast": false, "dispatchCount": 1, "links": {"appendItems": {"href": "xxxx", "method": "xxxx"}, "retrieve": {"href": "xxxx"}, "statusInProduction": {"href": "xxxx"}, "statusInStaging": {"href": "xxxx"}, "syncPointHistory": {"href": "xxxx"}, "update": {"href": "xxxx", "method": "xxxx"}, "activationDetails": {"href": "xxxx"}}}
```



#### Remove Items From Client List
Use the Remove Items From Client List action to remove items from the client list in Akamai.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client List Name|Name of the client list that needs to be updated. If both "Client List Name" and "Client List ID" are provided, action will work with ID.|False|String||
|Client List ID|ID of the client list that needs to be updated. If both "Client List Name" and "Client List ID" are provided, action will work with ID.|False|String||
|Item Value|Comma-separated list of items that need to be removed from the network list.|True|String||



##### JSON Results
```json
[{"value": "xxxx", "status": "xxxx"}, {"value": "xxxx", "status": "xxxx", "error": "xxxx"}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.