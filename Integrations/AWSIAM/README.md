
# AWSIAM

AWS Identity and Access Management (IAM) enables you to create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|AWS Access Key ID|None|True|String||
|AWS Secret Key|None|True|Password|*****|
|Verify SSL|None|False|Boolean|true|


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|TIPCommon-1.1.3.2-py2.py3-none-any.whl|
|jmespath-1.0.1-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|rsa-4.9-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|google_auth-2.34.0-py2.py3-none-any.whl|
|botocore-1.35.4-py3-none-any.whl|
|boto3-1.35.4-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|


## Actions
#### Add a User to a Group
Adds the specified user to the specified IAM group. Use groups to apply the same permissions policies across multiple users at once.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|The name of the group to update. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-|True|String||
|User Name|The name of the user to add. Note: User names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Comma separated values.|True|String||



#### Attach a Policy
Attach the specified managed policy to an identity (user, group, role).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Identity Type|IAM Identity type.|True|List|Group|
|Identity Name|The name (friendly name, not ARN) of the identity to attach the policy to. Identity names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-|True|String||
|Policy Name|The name (friendly name, not ARN) of the policy to attach the policy to. Policy names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-|True|String||



#### Create a Group
Create a new IAM group for your AWS account. To set up a group, you need to create the group. Then give the group permissions based on the type of work that you expect the users in the group to do. Finally, add users to the group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Name of the group to create. Comma separated values. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Names must be unique within an account.|True|String||



##### JSON Results
```json
[{"Arn": "arn:aws:iam::123456789:group/sssss", "CreateDate": "2020-12-10 10:05:43+00:00", "Path": "/", "GroupId": "AAAAAA", "GroupName": "sssss"}]
```



#### Create a Policy
Create an IAM customer managed policy for your AWS account. This action creates a policy version with a version identifier of v1and sets v1 as the policy's default version.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy Name|Name of the policy to create. Policy name can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Policy names must be unique within an account.|True|String||
|Policy Document|The JSON policy document that you want to use as the content for the new policy.|True|String||
|Description|Description of the policy.Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed.|False|String||



##### JSON Results
```json
[{"PolicyName":"MyPolicy322","PolicyId":"ANPAYPE7MW7ABGBKTXWER","Arn":"arn:aws:iam::582302349248:policy/MyPolicy322","Path":"/","DefaultVersionId":"v1","AttachmentCount":0,"PermissionsBoundaryUsageCount":0,"IsAttachable":"True","Description":"None","CreateDate":"2020-12-16 16:35:35+00:00","UpdateDate":"2020-12-16 16:35:35+00:00"}]
```



#### Create a User
Create a new IAM user for your AWS account. You can add multiple users at once with comma separated values. Please note that no policies will be applied at this stage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Name|Name of the user to create. Comma separated values. Note: Username can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Names must be unique within an account.|True|String||



##### JSON Results
```json
[{"Arn": "arn:aws:iam::123456789:user/asdsjsssi", "CreateDate": "2020-12-09 15:54:58+00:00", "Path": "/", "UserId": "123456789456", "UserName": "AAAAA"}]
```



#### Disable User Access
Disable User Access in AWS by adding an explicit deny inline policy. Action works with SOAR User entity type.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "username", "EntityResult": "Successfully added to the user the deny policy \"DisableUserAccessPolicy\"."},{"Entity": "arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/Username", "EntityResult": "Successfully added to the user the deny policy \"DisableUserAccessPolicy\"."}, {"Entity": "NoARealUserName", "EntityResult": "Failed to add the user to the deny policy \"DisableUserAccessPolicy\"."}]
```



#### List Users
Get a list of all users in the IAM.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Users to Return|Specify how many users to return. Maximum is 1000 users. Default is 50.|False|String|50|



##### JSON Results
```json
[{"Arn": "arn:aws:iam::123456:user/ec2-console@siemplify.co", "CreateDate": "2020-11-30 10:21:07+00:00", "Path": "/", "UserId": "123456789AAAA", "UserName": "XXXX@XXXXXX.co"}]
```



#### List Policies
List all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies. You can filter the list of policies that are returned using the optional Only Attached, Scope, and Policy Usage parameters. For example, to list only the customer managed policies in your AWS account, set Scope to Local. To list only AWS managed policies, set Scope to AWS.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Only Attached|When checked, filtering the results to only the policies that are attached to an IAM user, group or role. When unchecked, all policies will be returned.|False|Boolean|False|
|Scope|The scope to use for filtering the results. To list only AWS managed policies, set Scope to AWS. To list only the customer managed policies in your AWS account, set Scope to Local. As default, all policies will be returned.|False|List|All|
|Max Policies to Return|Specify how many policies to return. Default is 100. Maximum is 1000.|False|String|100|



##### JSON Results
```json
[{"PolicyName":"Amazon-Detective","PolicyId":"ANPAYPE7MW7ANSYSW3QPR","Arn":"arn:aws:iam::582302349248:policy/Amazon-Detective","Path":"/","DefaultVersionId":"v1","AttachmentCount":1,"PermissionsBoundaryUsageCount":"0","IsAttachable":"True","Description":"None","CreateDate":"2020-04-27 09:53:04+00:00","UpdateDate":"2020-04-27 09:53:04+00:00"}]
```



#### List Groups
Get a list of all groups in the IAM.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Groups to Return|Specify how many groups to return. Maximum is 1000 groups. Default is 50.|False|String|50|



##### JSON Results
```json
[{"Arn": "arn:aws:iam::123456789:group/aaa", "CreateDate": "2020-12-10 09:44:42+00:00", "Path": "/", "GroupId": "AAAAAAAAA", "GroupName": "AAAAAA"}]
```



#### Ping
Test connectivity to AWS IAM with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Remove a User from a Group
Removes the specified user from the specified IAM group. Use groups to apply the same permissions policies across multiple users at once.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|The name of the group to update. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-|True|String||
|User Name|The name of the user to remove. Note: User names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Comma separated values.|True|String||










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.