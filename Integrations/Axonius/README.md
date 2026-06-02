
# Axonius

Axonius is the cybersecurity asset management platform that gives organizations a comprehensive asset inventory, uncovers security solution coverage gaps, and automatically validates and enforces security policies. By seamlessly integrating with over 300 security and management solutions.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String|https://{root}|
|API Key|None|True|String||
|API Secret|None|True|Password|*****|
|Verify SSL|None|False|Boolean|true|


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Add Note
Add a note to entities in Axonius. Supported entities: Hostname, IP, Mac Address, User, Email Addresses (User entities that match email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Note|Specify what note needs to be added.|True|String||



##### JSON Results
```json
[{"Entity":"XXXXXX","EntityResult":{"data":{"attributes":{"accurate_for_datetime":"2021-04-01T14:34:59.172279+00:00","note":"XXXXX","user_id":"XXXXXXXXXXXXXXX","user_name":"XXXXXXXXXXXXXXX","uuid":"XXXXXXX-XXXX-XXXX-XXXX-XXXXXXX"},"type":"notes_details_schema"}}}]
```



#### Add Tags
Add tags to entities in Axonius. Supported entities: Hostname, IP, Mac Address, User, Email Addresses (User entities that match email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tags|Specify the comma-separated list of tags that need to be added to the entities.|True|String||



#### Enrich Entities
Enrich entities using information from Axonius. Supported entities: IP Address, Hostname, Mac Address, User, Email Addresses (User entities that match email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Endpoint Insight|If enabled, action will create an insight containing information about the endpoints.|False|Boolean|True|
|Create User Insight|If enabled, action will create an insight containing information about the user.|False|Boolean|True|
|Max Notes To Return|Specify how many notes to show in the case wall table. Default: 50.|False|String|50|



##### JSON Results
```json
[{"Entity":"xxxxx.xxxx@xxxx.xxxx","EntityResult":{"adapters":[{"accurate_for_datetime":"Wed,31Mar202115:45:14GMT","client_used":"xxxxx.xxxxx.xxxxx","plugin_name":"xxxxx.xxxxx.xxxxx","plugin_type":"xxxxx","plugin_unique_name":"xxxxx.xxxxx.xxxxx","quick_id":"xxxxx.xxxxx","type":"xxxxx","raw":{"account_disabled":"False","ad_display_name":"XXXXXXXXXX","ad_distinguished_name":"CN=xxxxx.xxxxx,CN=xxxxx,DC=xxxxx,DC=xxxxx","ad_sid":"xxxxx-xxxxx-xxxxx-xxxxx-xxxxx-xxxxx","ad_uac_dont_expire_password":"False","ad_uac_password_not_required":"False","display_name":"xxxxxxxxxx","domain":"xxxxx.xxxxx","employee_id":"xxxxx","first_name":"xxxxx","id":"CN=xxxxx.xxxxx,CN=xxxxx,DC=xxxxx,DC=xxxxx","is_admin":"False","is_local":"False","is_locked":"False","last_name":"xxxxx","last_password_change":"Sat,27Mar202121:12:24GMT","last_seen":"Sun,28Mar202121:25:21GMT","mail":"xxxxx.xxxxx@xxxxx.xxxxx","password_never_expires":"False","password_not_required":"False","user_city":"xxxxx","user_telephone_number":"xxxxx-xxxxx-xxxxx-xxxxx","username":"xxxxx.xxxxx@xxxxx.xxxxx"}}],"internal_axon_id":"xxxxx","labels":["xxxxx","xxxxx"],"notes":[{"accurate_for_datetime":"Sun,21Mar202115:35:00GMT","note":"xxxxx","user_id":"xxxxx","user_name":"xxxxxxxxxx","uuid":"xxxxx-xxxxx-xxxxx-xxxxx-xxxxx"}]}}]
```



#### Ping
Test connectivity to the Axonius with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Remove Tags
Remove tags from entities in Axonius. Supported entities: Hostname, IP, Mac Address, User, Email Addresses (User entities that match email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tags|Specify the comma-separated list of tags that need to be removed from the entities.|True|String||










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.