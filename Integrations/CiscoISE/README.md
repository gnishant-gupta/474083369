
# CiscoISE

The Cisco Identity Services Engine (ISE) is your one-stop solution to streamline security policy management and reduce operating costs. With ISE, you can see users and devices controlling access across wired, wireless, and VPN connections to the corporate network.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|None|https://x.x.x.x/|
|Username||True|String||
|Password||True|Password|*****|
|Verify SSL||False|Boolean||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|xmltodict-0.13.0-py2.py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Add Endpoint To Endpoint Identity Group
Add endpoint to endpoint identity group in Cisco ISE. Supported entity types: IP Address, MAC Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint Identity Group Name|Specify the name of the endpoint identity group to which you want to add the endpoint.|True|String||



##### JSON Results
```json
[{"EntityResult": {"UpdatedFieldsList": {"updatedField": [{"field": "groupId", "newValue": "ffa36b00-8bff-xxxx-xxxx-xxxxxxx", "oldValue": "0cc7ad00-8c00-xxxx-xxxx-xxxxxxx"}]}}, "Entity": "00:50:xx:xx:xx:xx"}, {"EntityResult": {"UpdatedFieldsList": {"updatedField": []}}, "Entity": "00:50:xx:xx:xx:xx"}]
```



#### Enrich Endpoint
Enrich endpoint by data from Cisco ISE
Timeout - 600 Seconds



#### Get Endpoints
Get requested endpoint data from endpoints monitored by Cisco ISE
Timeout - 600 Seconds



#### List Endpoint Identity Group
List available endpoint entity groups in Cisco ISE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter endpoint entity groups.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 100 records. Maximum: 100.|False|String|100|



##### JSON Results
```json
[{"id": "73d1a120-ab0f-xxxx-xxxx-xxxxxxxx", "name": "Windows11-Workstation", "description": "Identity Group for Profile: Windows11-Workstation"}, {"id": "73d1a120-ab0f-xxxx-xxxx-xxxxxxxx", "name": "OS_X_BigSur-Workstation", "description": "Identity Group for Profile: OS_X_BigSur-Workstation"}, {"id": "73d1a120-ab0f-xxxx-xxxx-xxxxxxxx", "name": "Workstation", "description": "Identity Group for Profile: Workstation"}]
```



#### Terminate Session
Session disconnect via an API call
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Node Server Name|ISE node server name, e.g. ciscoISE.|True|String|None|
|Calling Station ID|The ID value of the calling station, e.g. 1.|True|String|None|
|Terminate Type|Terminate Type value will be an integer between 0 and 2, e.g. 0 (0=DYNAMIC_AUTHZ_PORT_DEFAULT, 1=DYNAMIC_AUTHZ_PORT_BOUNCE, 2=DYNAMIC_AUTHZ_PORT_SHUTDOWN)|False|String|None|



#### Unquarantine Address
Unquarantine endpoint by MAC address
Timeout - 600 Seconds



#### Get Sessions
Get a list of active sessions
Timeout - 600 Seconds



#### Quarantine Address
Quarantine endpoint by MAC address
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Name|Policy name to attach the endpoint to.|True|String|None|



#### Ping
Check connectivity
Timeout - 600 Seconds



#### Update Endpoint
Update endpoint object
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Description|endpoint's description|False|String|None|
|Group ID|Endpoint's property to update.|False|String|None|
|Portal User|Endpoint's property to update.|False|String|None|
|Identity Store|Endpoint's property to update.|False|String|None|
|Identity Store ID|Endpoint's property to update.|False|String|None|
|Custom Attributes|Custom attributes will be added to the entity object, e.g. {'param':'val'}.|False|String||
|MDM Server Name|Endpoint's property to update.|False|String|None|
|MDM Reachable|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM Enrolled|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM Compliance Status|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM OS|Endpoint's property to update.|False|String|None|
|MDM Manufacturer|Endpoint's property to update.|False|String|None|
|MDM Model|Endpoint's property to update.|False|String|None|
|MDM Encrypted|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM Pinlock|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM Jail Broken|Endpoint's property to update, e.g. true or false.|False|String|None|
|MDM IMEI|Endpoint's property to update.|False|String|None|
|MDM Phone Number|Endpoint's property to update.|False|String|None|










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.