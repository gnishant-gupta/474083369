
# CloudIdentity

A unified identity, access, app, and endpoint management (IAM/EMM) platform.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service Account JSON File Content|The content of the service account key JSON file. You can configure either this parameter, or Workload Identity Email. To use this method, paste the entire JSON string from the key file downloaded during service account creation.|False|Password|*****|
|Workload Identity Email|The client email address of your service account. You can configure either this parameter or Service Account JSON File Content. To use this method for service account impersonation, you must grant the Service Account Token Creator role to your Google SecOps service account.|False|String||
|Delegated Email|The email address that the integration uses to perform actions. Ensure this account has the appropriate delegated permissions within your environment to execute the required integration tasks.|True|String||
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to the Cloud Identity server.|False|Boolean|true|


#### Dependencies
| |
|-|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|proto_plus-1.27.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|cryptography-46.0.7-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|pycparser-3.0-py3-none-any.whl|
|pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|dataclass_wizard-0.39.1-py3-none-any.whl|
|protobuf-5.29.6-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|TIPCommon-2.3.8-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|google_api_core-2.22.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|certifi-2026.2.25-py3-none-any.whl|


## Actions
#### List Policies
Use the “List Policies” action to list Cloud Identity policies.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Organization Unit Name|The name of the organizational unit from which to list policies.|True|String||
|Policy Type Filter|Type of the policy used to filter the list.|False|List|Admin|
|Setting Type Filter|The regular expression pattern used to filter policies by their settings type.This filter is applied directly to the API request.|False|String||
|Settings Display Name Filter|A comma-separated list of display names used to filter policy settings.|False|String||
|Max Results To Return|The maximum number of results to return for the action run. Max: 100.|False|String|50|



##### JSON Results
```json
[{"name": "policies/123", "customer": "customers/123", "type": "ADMIN", "policy_query": {"query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('12345'))", "orgUnit": "orgUnits/12345", "sortOrder": 1}, "setting": {"type": "settings/rule.dlp", "value": {"display_name": "Test DLP Rule"}}}]
```



#### Ping
Use the Ping action to test the connectivity to Cloud Identity.
Timeout - 600 Seconds



#### Add Entity To Detector URL List
Use the “Add Entity To Detector URL List” action to add entities to the Cloud Identity Policy detection list. Supported entities: URL, Domain.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detector Policy ID|The unique identifier of the detector policy to update.|True|String||
|URL|A comma-separated list of URLs to add to the detector list.|False|String||
|Domain|A comma-separated list of domains to add to the detector list.|False|String||



##### JSON Results
```json
{"type": "ADMIN", "customer": "customers/<CUSTOMER_ID>", "policyQuery": {"query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))", "orgUnit": "orgUnits/<ORG_UNIT_ID>"}, "setting": {"type": "settings/detector.url_list", "value": {"displayName": "test_url_list_detector", "description": "test_url_list_detector desc", "urlList": {"urls": ["http://example.com", "example.org", "bad_entity.com"]}}}}
```



#### Create Policy
Use the “Create Policy” action to create a new policy entry within Cloud Identity.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Entry|The JSON object representing the configuration of the policy entry to add.|True|String|{
    "type": "ADMIN",
    "customer": "customers/<CUSTOMER_ID>",
    "policyQuery": {
        "query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))",
        "orgUnit": "orgUnits/<ORG_UNIT_ID>"
    },
    "setting": {
        "type": "settings/rule.dlp",
        "value": {
            "display_name": "test_create_rule",
            "triggers": [
                "google.workspace.chrome.file.v1.download"
            ],
            "state": "ACTIVE",
            "action": {
                "chromeAction": {
                    "warnUser": {}
                }
            }
        }
    }
}
|



##### JSON Results
```json
{"type": "ADMIN", "customer": "customers/<CUSTOMER_ID>", "policyQuery": {"query": "entity.org_units.exists(org_unit, org_unit.org_unit_id == orgUnitId('<ORG_UNIT_ID>'))", "orgUnit": "orgUnits/<ORG_UNIT_ID>"}, "setting": {"type": "settings/rule.dlp", "value": {"display_name": "test_create_rule", "triggers": ["google.workspace.chrome.file.v1.download"], "state": "ACTIVE", "action": {"chromeAction": {"warnUser": {}}}}}}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.