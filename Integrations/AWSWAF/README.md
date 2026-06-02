
# AWSWAF

AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|AWS Access Key ID|None|True|String||
|AWS Secret Key|None|True|Password|*****|
|AWS Default Region|None|True|String||


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|jmespath-1.0.1-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|boto3-1.35.10-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|botocore-1.35.10-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|


## Actions
#### Add Pattern To Regex Pattern Set
Add string patterns to the Regex Pattern Set in AWS WAF. Note: Regex Pattern Set can only contain 10 patterns per set.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Regex Pattern Set Names|Specify the comma-separated list of Regex Pattern set names. Example: name_1,name_2|True|String||
|Patterns|Specify the comma-separated list of patterns that should be added to the Regex Pattern Set. Example: pattern_1,pattern_2|True|String||
|Scope|Specify what should be the scope of the set. If “Both” is selected, action will add patterns base on entities to Regex Pattern sets in Regional and CloudFront scopes.|True|List|CloudFront|



#### Add Entity To Regex Pattern Set
Add string patterns based on entities to the Regex Pattern Set in AWS WAF. Note: Regex Pattern Set can only contain 10 patterns per set
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Regex Pattern Set Names|Specify the comma-separated list of Regex Pattern set names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope for the creation of Regex Pattern sets. If “Both” is selected, action will add patterns base on entities to Regex Pattern sets in Regional and CloudFront scopes.|True|List|CloudFront|
|Domain Pattern|If enabled, action will retrieve domain part out of urls and create a regex pattern based on them. If enabled, action will retrieve domain part out of urls and create a regex pattern based on them. Example: http://test.com/folder will be converted to a pattern ^(http|https)(:\/\/)(\Qtest.com\E).*|False|Boolean|True|
|IP Pattern|If enabled, action will construct a proper regex pattern out of IP address instead of using raw value. Example: 10.0.0.1 will be converted into ^(http|https)(:\/\/)(\Q10.0.0.1\E).*|False|Boolean|True|



#### Add IP To IP Set
Add IP addresses to the IP Set in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Set Names|Specify the comma-separated list of IP set names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope of the set. If “Both” is selected, action will add IP addresses to IP sets in Regional and CloudFront scopes.|True|List|CloudFront|



#### Create IP Set
Create an IP Set in AWS WAF, based on entities. Note: IP Set is created in the following format Siemplify_{Name}_{IP Type}.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the IP set. Note: action will create an IP set in the following format: Siemplify_{Name}_{IP Type}. The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Scope|Specify what should be the scope for the creation of IP sets. If “Both” is selected, action will create an IP set in Regional and CloudFront scopes.|True|List|CloudFront|
|Description|Specify the description for the IP set.|False|String||
|Tags|Specify additional tags that should be added to the IP set. Format: key_1:value_1,key_2:value_1|False|String||



##### JSON Results
```json
[{"Regional":["Siemplify_Test_IPv4","Siemplify_Test_IPv6"],"CloudFront":["Siemplify_Test_IPv4","Siemplify_Test_IPv6"]}]
```



#### Add Rule To Rule Group
Add a rule to the rule group in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Group Names|Specify the comma-separated list of Rule Group  names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope for the new rules. If “Both” is selected, action will add Rule to a Rule Group in Regional and CloudFront scopes.|True|List|CloudFront|
|Rule JSON Object|Specify the JSON object of the rule. Please refer to the action documentation to get information about the structure of the rule.|True|String||



#### Add Rule To Web ACL
Add a rule based on IP Sets or Rule Groups to Web ACL in AWS WAF. Note: at maximum Web ACL can contain 1500 rules.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Web ACL Names|Specify the comma-separated list of Web ACL names. Example: name_1,name_2|True|String||
|Rule Source Type|Specify what rule type should be used.|True|List|IP Set|
|Rule Source Name|Specify the name of the source, which should be used for Web ACL. If “Rule Source Type” is “IP Set”, action will search for IP Sets with that name. If “Rule Source Type” is “Rule Group”, action will search for Rule Groups with that name.|True|String||
|Scope|Specify what should be the scope for the new rules. If “Both” is selected, action will add a Rule to a Web ACL in Regional and CloudFront scopes.|True|List|CloudFront|
|Rule Priority|Specify what should be the priority of the rule. Priorities in Web ACL should be unique.|True|String||
|IP Set Action|Specify what should be the action for rules that are based on the IP set.|False|List|Block|



#### Create Regex Pattern Set
Create a Regex Pattern Set in AWS WAF based on entities. Note: Regex Pattern Set can only contain 10 patterns per set and there can only be 10 Regex Pattern Sets at max.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the Regex Pattern set. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Scope|Specify what should be the scope for the creation of Regex Pattern sets. If “Both” is selected, action will create a Regex Pattern set in Regional and CloudFront scopes.|True|List|CloudFront|
|Description|Specify the description for the Regex Pattern set.|False|String||
|Tags|Specify additional tags that should be added to the Regex Pattern set. Format: key_1:value_1,key_2:value_1.|False|String||
|Domain Pattern|If enabled, action will retrieve domain part out of urls and create a regex pattern based on them. Example: http://test.com/folder will be converted to a pattern ^(http)(s|)(://)(test.com).*|False|Boolean|True|
|IP Pattern|If enabled, action will construct a proper regex pattern out of IP address instead of using raw value. Example: 10.0.0.1 will be converted into ^(http)(s|)(://)(10.0.0.1).*|False|Boolean|True|



##### JSON Results
```json
[{"Regional":["Regex_set"],"CloudFront":["Regex_set"]}]
```



#### Create Rule Group
Create a rule group in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enable CloudWatch Metrics|If enabled, the associated resource sends metrics to CloudWatch.|False|Boolean|True|
|Name|Specify the name of the rule group. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Scope|Specify what should be the scope for the creation of the rule group. If “Both” is selected, action will create a Rule Group in Regional and CloudFront scopes.|True|List|CloudFront|
|Capacity|Specify the capacity of the rule group. Note: you can’t change the capacity after the group is created. Maximum is 1500.|True|String|100|
|Enable Sampled Requests|If enabled, AWS WAF will store a sampling of the web requests that match the rules.|False|Boolean|True|
|CloudWatch Metric Name|Specify the name of the CloudWatch Metric. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Description|Specify the description for the Rule Group.|False|String||
|Tags|Specify additional tags that should be added to the Rule Group. Format: key_1:value_1,key_2:value_1.|False|String||



##### JSON Results
```json
[{"Regional":["Rule_group_name"],"CloudFront":["Rule_group_name"]}]
```



#### List IP Sets
List available IP Sets in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|Specify what should be the scope for the listing of IP Sets.|True|List|CloudFront|
|Max IP Sets To Return|Specify hou many IP sets to return. Default is 50. Maximum is 100.|False|String|50|



##### JSON Results
```json
[{"Regional":[{"Name":"My_IP_Set","Id":"XXXXX-XXXXX-XXXXX-XXXXX","Description":"XXXXXX",  "LockToken":"XXXXX-XXXXX-XXXXX-XXXXX","ARN":"XXXXX-XXXXX-XXXXX-XXXXX/ipset/My_IP_Set/XXXXX-XXXXX-XXXXX-XXXXX"}],"CloudFront":[{"Name":"My_IP_Set","Id":"XXXXX-XXXXX-XXXXX-XXXXX","Description":"my IP Set","LockToken":"XXXXX-XXXXX-XXXXX-XXXXX","ARN":"XXXXX-XXXXX-XXXXX-XXXXX/ipset/My_IP_Set/XXXXX-XXXXX-XXXXX-XXXXX"}]}]
```



#### List Regex Pattern Sets
List available Regex Pattern Sets in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|Specify what should be the scope for the listing of Regex Pattern Sets.|True|List|CloudFront|
|Max Regex Pattern Sets To Return|Specify how many Regex Patttern Sets to return. Default is 5. Maximum is 10|False|String|5|



##### JSON Results
```json
[{"Regional":[{"Name":"XXXXXXXXX", "Id":"XXXXXX-XXXX-XXXX-XXXX-XXXXXXXX","Description":"","LockToken":"XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXX","ARN":"arn:aws:wafv2:us-east-1:XXXXXXXXX"}],"CloudFront":[{"Name":"XXXXXXXXX","Id":"XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX","Description":"XXXXX","LockToken":"XXXXXX-XXXXX-XXXX-XXXX-XXXXXX","ARN":"arn:aws:wafv2:us-east-1:XXXXXXX"}]}]
```



#### List Rule Groups
List available rule groups in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|Specify what should be the scope for the listing of Rule Groups.|True|List|CloudFront|
|Max Rule Groups To Return|Specify how many Rule Groups to return. Default is 50. Maximum is 100.|False|String|50|



##### JSON Results
```json
{"CloudFront": [{"Name": "BothRuleGroup", "Id": "123456", "Description": "", "LockToken": "123456", "ARN": "arn:aws:wafv2:us-east-1:123456:global/rulegroup/BothRuleGroup/123456"}], "Regional": [{"Name": "BothRuleGroup", "Id": "123456", "Description": "", "LockToken": "123456", "ARN": "arn:aws:wafv2:us-east-1:123456:regional/rulegroup/BothRuleGroup/123456"}]}
```



#### List Web ACLs
List available web ACLs in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|Specify what should be the scope for the listing of Web ACLs.|True|List|CloudFront|
|Max Web ACLs To Return|Specify how many Web ACLs to return. Default is 50. Maximum is 100.|False|String|50|



##### JSON Results
```json
{"CloudFront": [{"Name": "ACL1", "Id": "123456-1234-1234-1234-123456", "Description": "descript", "LockToken": "123456789", "ARN": "arn:aws:wafv2:us-east-1:123456798:global/webacl/ACL1/123456"}], "Regional": [{"Name": "ACL13", "Id": "123456", "Description": "", "LockToken": "123456", "ARN": "arn:aws:wafv2:us-east-1:123456:regional/webacl/ACL13/123456"}]}
```



#### Ping
Test connectivity to AWS WAF with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Remove Entity From Regex Pattern Set
Remove string patterns based on entities from the Regex Pattern Set in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Regex Pattern Set Names|Specify the comma-separated list of Regex Pattern set names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope of the set. If "Both" is selected, action will remove patterns based on entities from Regex Pattern sets in Regional and CloudFront scopes.|True|List|CloudFront|
|Domain Pattern|If enabled, action will retrieve domain part out of urls and search for a regex pattern based on them in the Regex Pattern Set. Example: http://test.com/folder will be searched as pattern ^(http|https)(:\/\/)(\Qtest.com\E).*|False|Boolean|True|
|IP Pattern|If enabled, action will search for a regex pattern out of IP address instead of raw value. Example: 10.0.0.1 will be searched as ^(http|https)(:\/\/)(\Q10.0.0.1\E).*|False|Boolean|True|



#### Remove Rule From Rule Group
Remove a rule from the rule group in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Group Names|Specify the comma-separated list of Rule Group  names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope of the rule group. If “Both” is selected, action will remove a rule from Rule Group in Regional and CloudFront scopes.|True|List|CloudFront|
|Rule Name|Specify the name of the rule that should be deleted.|True|String||



#### Remove IP From IP Set
Remove IP addresses from the IP Set in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Set Names|Specify the comma-separated list of IP set names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope of the set. If "Both" is selected, action will remove IP addresses from IPsets in Regional and CloudFront scopes.|True|List|CloudFront|



#### Remove Pattern From Regex Pattern Set
Remove patterns from the Regex Pattern Set in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Regex Pattern Set Names|Specify the comma-separated list of Regex Pattern set names. Example: name_1,name_2|True|String||
|Patterns|Specify the comma-separated list of patterns that should be removed from the Regex Pattern set. Example: pattern_1,pattern_2|True|String||
|Scope|Specify what should be the scope of the set. If "Both" is selected, action will remove patterns from Regex Pattern sets in Regional and CloudFront scopes.|True|List|CloudFront|



#### Remove Rule From Web ACL
Remove a rule from Web ACL in AWS WAF.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Web ACL Names|Specify the comma-separated list of Web ACL names. Example: name_1,name_2|True|String||
|Scope|Specify what should be the scope for the removal of the Web ACL. If “Both” is selected, action will remove a Web ACL in Regional and CloudFront scopes.|True|List|CloudFront|
|Rule Name|Specify the name of the rule that should be deleted.|True|String||



#### Create Web ACL
Create a Web ACL in AWS WAF. Note: You can have only 100 Web ACLs per region.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the Web ACL. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Rule Source Type|Specify what rule type should be used.|True|List|IP Set|
|Rule Source Name|Specify the name of the source, which should be used for Web ACL. If “Rule Source Type” is “IP Set”, action will search for IP Sets with that name. If “Rule Source Type” is “Rule Group”, action will search for Rule Groups with that name.|True|String||
|Scope|Specify what should be the scope for the creation of the web acl. If “Both” is selected, action will create a Web ACL in Regional and CloudFront scopes.|True|List|CloudFront|
|Enable Sampled Requests|If enabled, AWS WAF will store a sampling of the web requests that match the rules.|False|Boolean|True|
|Enable CloudWatch Metrics|If enabled, the associated resource sends metrics to CloudWatch.|False|Boolean|True|
|CloudWatch Metric Name|Specify the name of the CloudWatch Metric. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).|True|String||
|Default Action|Specify what should be the default action for requests that don't match any rules.|True|List|Allow|
|IP Set Action|Specify what should be the action for rules that are based on the IP set.|False|List|Block|
|Rule Priority|Specify what should be the priority of the rule. Priorities in Web ACL should be unique.|True|String||
|Description|Specify the description for the Web ACL.|False|String||
|Tags|Specify additional tags that should be added to the Web ACL. Format: key_1:value_1,key_2:value_1.|False|String||



##### JSON Results
```json
[{"Regional":["Web_Acl_name"],"CloudFront":["Web_Acl_name"]}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.