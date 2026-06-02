
# AzureActiveDirectory

Azure Active Directory (Azure AD) is Microsoft's cloud-based identity and access management service, which helps your employees sign in and access  both internal and external resources.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|None|False|String|https://login.microsoftonline.com|
|API Root|None|False|String|https://graph.microsoft.com|
|Client ID|None|True|String||
|Client Secret|None|True|Password|*****|
|Directory ID|None|True|String||
|Verify SSL|None|False|Boolean|True|


#### Dependencies
| |
|-|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|TIPCommon-2.3.8-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|googleapis_common_protos-1.73.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|tldextract-5.1.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|


## Actions
#### Add User To a Group
Add user to a specific Azure AD group. Action expects Siemplify user entity in username@domain format and group id in 00e40000-1971-439d-80fc-d0e000001dbd format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group ID|Azure AD group id in 00e40000-1971-439d-80fc-d0e000001dbd format.|True|String||



#### Disable Account
Disable account in Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### Enrich Host
Enrich Siemplify Host entity with information from Azure Active Directory. Action finds a match for a provided Host entity based on the devices displayName field in Azure AD
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity":"SENINELONE-xxxxx","EntityResult":{"@odata.id":"https://graph.microsoft.com/v2/d48f52ca-5b1a-4708-8ed0-xxxxx/directoryObjects/433e2228-0aea-448c-9b78-xxxxx/Microsoft.DirectoryServices.Device","id":"433e2228-0aea-448c-9b78-xxxxxx","if":"433e2228-0aea-448c-9b78-xxxxxx","deletedDateTime":null,"accountEnabled":true,"approximateLastSignInDateTime":"2021-08-05T06:24:30Z","complianceExpirationDateTime":null,"createdDateTime":"2021-02-08T12:14:31Z","deviceCategory":null,"deviceId":"356c1602-7255-4191-8590-xxxxx","deviceMetadata":null,"deviceOwnership":"Personal","deviceVersion":2,"displayName":"SENINELONE-H01","domainName":null,"enrollmentProfileName":null,"enrollmentType":"AutoEnrollment","externalSourceName":null,"isCompliant":true,"isManaged":true,"isRooted":false,"managementType":"MDM","manufacturer":"VMware, Inc.","mdmAppId":"0000000a-0000-0000-xxxx-xxxx","model":"VMware Virtual Platform","onPremisesLastSyncDateTime":null,"onPremisesSyncEnabled":null,"operatingSystem":"Windows","operatingSystemVersion":"10.0.18363.1679","physicalIds":["[USER-GID]:b786d3cf-e97d-4511-b61c-xxxxx:6825788988304991","[GID]:g:6825788988xxxx","[USER-HWID]:b786d3cf-e97d-4511-b61c-xxxxx:6825788988304990","[HWID]:h:6825788988xxxx"],"profileType":"RegisteredDevice","registrationDateTime":"2021-02-08T12:14:31Z","sourceType":null,"systemLabels":[],"trustType":"Workplace","extensionAttributes":{"extensionAttribute1":null,"extensionAttribute2":null},"alternativeSecurityIds":[{"type":2,"identityProvider":null,"key":"WAA1ADAAOQA6ADwAUwBIAEEAMQAtAFQAUAAtAFAAVQBCAEsARQBZAD4AMQA4AEYARAAwADUAMwBDAEUAMgBGADEAOABBAEQARQA2ADQAQgA0AEUAQQA1ADMARgA5ADIARABGADgAOQA1AEIARAA2AEYARAAzADcxxxxxxxx"}]}}]
```



#### Force Password Update
Force password update for user so the user will have to change their password on next login. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### Enrich User
Enrich Siemplify User entity with information from Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields To Return|A comma-separated list of fields that you want to return. If nothing is provided, action will return fields that are considered to be default by API.|False|String|accountEnabled,ageGroup,assignedLicenses,businessPhones,city,companyName,consentProvidedForMinor,country,createdDateTime,creationType,department,displayName,mail,employeeId,employeeHireDate,employeeOrgData,employeeType,onPremisesExtensionAttributes,externalUserStateChangeDateTime,faxNumber,givenName,imAddresses,identities,externalUserState,jobTitle,surname,lastPasswordChangeDateTime,legalAgeGroupClassification,mailNickname,mobilePhone,id,officeLocation,onPremisesSamAccountName,onPremisesDistinguishedName,onPremisesDomainName,onPremisesImmutableId,onPremisesLastSyncDateTime,onPremisesProvisioningErrors,onPremisesSecurityIdentifier,onPremisesSyncEnabled,onPremisesUserPrincipalName,otherMails,passwordPolicies,passwordProfile,preferredDataLocation,preferredLanguage,proxyAddresses,signInSessionsValidFromDateTime,sponsors,state,streetAddress,usageLocation,userPrincipalName,userType,postalCode,authorizationInfo,deletedDateTime,showInAddressList,isResourceAccount,refreshTokensValidFromDateTime|
|Include MFA Details|If enabled, action will return MFA details about the user.|False|Boolean|false|
|Include Last Sign In Details|If selected, the action retrieves the user's sign-in activity, including both interactive and non-interactive sign-in timestamps.|False|Boolean|true|



##### JSON Results
```json
[{"Entity":"user@domain.com","EntityResult":{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users/$entity","accountEnabled":true,"ageGroup":null,"businessPhones":[],"city":"New York","companyName":"ExampleCorp","consentProvidedForMinor":null,"country":"US","createdDateTime":"2025-01-01T00:00:00Z","creationType":null,"department":"Security","displayName":"User Name","mail":"user@domain.com","employeeId":"12345","employeeHireDate":null,"employeeType":null,"externalUserStateChangeDateTime":null,"faxNumber":null,"givenName":"User","imAddresses":[],"externalUserState":null,"jobTitle":"Security Analyst","surname":"Surname","lastPasswordChangeDateTime":"2025-01-01T00:00:00Z","legalAgeGroupClassification":null,"mailNickname":"usernickname","mobilePhone":"+11234567890","id":"user-id-12345","officeLocation":null,"onPremisesSamAccountName":null,"onPremisesDistinguishedName":null,"onPremisesDomainName":null,"onPremisesImmutableId":null,"onPremisesLastSyncDateTime":null,"onPremisesProvisioningErrors":[],"onPremisesSecurityIdentifier":null,"onPremisesSyncEnabled":null,"onPremisesUserPrincipalName":null,"otherMails":[],"passwordPolicies":"None","preferredDataLocation":null,"preferredLanguage":"en-US","proxyAddresses":[],"signInSessionsValidFromDateTime":"2025-01-01T00:00:00Z","state":"NY","streetAddress":"123 Main St","usageLocation":"US","userPrincipalName":"user@domain.com","userType":"Member","postalCode":"10001","deletedDateTime":null,"showInAddressList":null,"isResourceAccount":null,"refreshTokensValidFromDateTime":"2025-01-01T00:00:00Z","employeeOrgData":null,"passwordProfile":null,"authorizationInfo":{"certificateUserIds":[]},"mfa_details":{"id":"user-id-12345","userPrincipalName":"user@domain.com","userDisplayName":"User Name","userType":"member","isAdmin":false,"isSsprRegistered":true,"isSsprEnabled":true,"isSsprCapable":true,"isMfaRegistered":true,"isMfaCapable":true,"isPasswordlessCapable":false,"methodsRegistered":["email","mobilePhone"],"defaultMfaMethod":"mobilePhone","isSystemPreferredAuthenticationMethodEnabled":false,"systemPreferredAuthenticationMethods":[],"userPreferredMethodForSecondaryAuthentication":"oath","lastUpdatedDateTime":"2026-01-01T00:00:00Z"},"sign_in_details":{"lastSignInDateTime":"2025-12-29T12:31:14Z","lastSignInRequestId":"8d002042-da0b-4cfc-aada-d0a04ab9d700","lastNonInteractiveSignInDateTime":"2025-12-29T14:03:57Z","lastNonInteractiveSignInRequestId":"7578a9b8-cd6b-4338-9e3e-4aa2297def00","lastSuccessfulSignInDateTime":"2025-12-29T14:03:57Z","lastSuccessfulSignInRequestId":"7578a9b8-cd6b-4338-9e3e-4aa2297def00"}}}]
```



#### Get Manager Contact Details
Get manager contact details for user. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields To Return|A comma-separated list of fields that you want to return. If nothing is provided, the action will return the Display Name, Mobile Phone, and Mail.|False|String|accountEnabled,ageGroup,assignedLicenses,businessPhones,city,companyName,consentProvidedForMinor,country,createdDateTime,creationType,department,displayName,mail,employeeId,employeeHireDate,employeeOrgData,employeeType,onPremisesExtensionAttributes,externalUserStateChangeDateTime,faxNumber,givenName,imAddresses,identities,externalUserState,jobTitle,surname,lastPasswordChangeDateTime,legalAgeGroupClassification,mailNickname,mobilePhone,id,officeLocation,onPremisesSamAccountName,onPremisesDistinguishedName,onPremisesDomainName,onPremisesImmutableId,onPremisesLastSyncDateTime,onPremisesProvisioningErrors,onPremisesSecurityIdentifier,onPremisesSyncEnabled,onPremisesUserPrincipalName,otherMails,passwordPolicies,passwordProfile,preferredDataLocation,preferredLanguage,proxyAddresses,signInSessionsValidFromDateTime,sponsors,state,streetAddress,usageLocation,userPrincipalName,userType,postalCode,authorizationInfo,deletedDateTime,showInAddressList,isResourceAccount,refreshTokensValidFromDateTime|
|Include MFA Details|If enabled, action will return MFA details about the user.|False|Boolean|false|
|Include Last Sign In Details|If selected, the action retrieves the user's sign-in activity, including both interactive and non-interactive sign-in timestamps.|False|Boolean|true|



##### JSON Results
```json
[{"Entity":"user@domain.com","EntityResult":{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users(accountEnabled,ageGroup,assignedLicenses,businessPhones,city,companyName,consentProvidedForMinor,country,createdDateTime,creationType,department,displayName,mail,employeeId,employeeHireDate,employeeOrgData,employeeType,onPremisesExtensionAttributes,externalUserStateChangeDateTime,faxNumber,givenName,imAddresses,identities,externalUserState,jobTitle,surname,lastPasswordChangeDateTime,legalAgeGroupClassification,mailNickname,mobilePhone,id,officeLocation,onPremisesSamAccountName,onPremisesDistinguishedName,onPremisesDomainName,onPremisesImmutableId,onPremisesLastSyncDateTime,onPremisesProvisioningErrors,onPremisesSecurityIdentifier,onPremisesSyncEnabled,onPremisesUserPrincipalName,otherMails,passwordPolicies,passwordProfile,preferredDataLocation,preferredLanguage,proxyAddresses,signInSessionsValidFromDateTime,state,streetAddress,usageLocation,userPrincipalName,userType,postalCode,authorizationInfo,deletedDateTime,showInAddressList,isResourceAccount,refreshTokensValidFromDateTime,sponsors())/$entity","accountEnabled":true,"ageGroup":null,"businessPhones":[],"city":"New York","companyName":"ExampleCorp","consentProvidedForMinor":null,"country":"US","createdDateTime":"2025-01-01T00:00:00Z","creationType":null,"department":"Security","displayName":"Manager Name","mail":"manager@domain.com","employeeId":"12345","employeeHireDate":null,"employeeType":"Full-time","externalUserStateChangeDateTime":null,"faxNumber":null,"givenName":"Manager","imAddresses":[],"externalUserState":null,"jobTitle":"Lead Manager","surname":"Surname","lastPasswordChangeDateTime":"2025-01-01T00:00:00Z","legalAgeGroupClassification":null,"mailNickname":"managernickname","mobilePhone":"+11234567890","id":"manager-id-12345","officeLocation":null,"onPremisesSamAccountName":null,"onPremisesDistinguishedName":null,"onPremisesDomainName":null,"onPremisesImmutableId":null,"onPremisesLastSyncDateTime":null,"onPremisesProvisioningErrors":[],"onPremisesSecurityIdentifier":null,"onPremisesSyncEnabled":null,"onPremisesUserPrincipalName":null,"otherMails":[],"passwordPolicies":null,"passwordProfile":null,"preferredDataLocation":null,"preferredLanguage":"en-US","proxyAddresses":[],"signInSessionsValidFromDateTime":"2025-01-01T00:00:00Z","state":"NY","streetAddress":"123 Main St","usageLocation":"US","userPrincipalName":"manager@domain.com","userType":"Member","postalCode":"10001","deletedDateTime":null,"showInAddressList":null,"isResourceAccount":null,"refreshTokensValidFromDateTime":"2025-01-01T00:00:00Z","employeeOrgData":null,"authorizationInfo":{"certificateUserIds":[]},"sponsors":[],"mfa_details":{"id":"manager-id-12345","userPrincipalName":"manager@domain.com","userDisplayName":"Manager Name","userType":"member","isAdmin":true,"isSsprRegistered":false,"isSsprEnabled":true,"isSsprCapable":false,"isMfaRegistered":true,"isMfaCapable":true,"isPasswordlessCapable":false,"methodsRegistered":["mobilePhone","softwareOneTimePasscode"],"defaultMfaMethod":"softwareOneTimePasscode","isSystemPreferredAuthenticationMethodEnabled":true,"systemPreferredAuthenticationMethods":["SoftwareOTP"],"userPreferredMethodForSecondaryAuthentication":"oath","lastUpdatedDateTime":"2026-01-01T00:00:00Z"},"sign_in_details":{"lastSignInDateTime":"2025-12-29T12:31:14Z","lastSignInRequestId":"8d002042-da0b-4cfc-aada-d0a04ab9d700","lastNonInteractiveSignInDateTime":"2025-12-29T14:03:57Z","lastNonInteractiveSignInRequestId":"7578a9b8-cd6b-4338-9e3e-4aa2297def00","lastSuccessfulSignInDateTime":"2025-12-29T14:03:57Z","lastSuccessfulSignInRequestId":"7578a9b8-cd6b-4338-9e3e-4aa2297def00"}}}]
```



#### Is User In a Group
Check if user has membership in a specific Azure AD group. Action expects Siemplify user entity in username@domain format and group id in 00e40000-1971-439d-80fc-d0e000001dbd format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group ID|Azure AD group id in 00e40000-1971-439d-80fc-d0e000001dbd format.|True|String||



##### JSON Results
```json
[{"EntityResult": "true","Entity": "user@mail.com"}]
```



#### Enable Account
Enable account in Azure Active Directory. Action expects Siemplify user entity in username@domain format.
Timeout - 600 Seconds



#### List Groups
List Azure Active Directory groups based on the specified search criteria. Note that action is not working on Siemplify entities. Additionally, filtering is working on the Name field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Order By|Specifies the result order. Groups are sorted by their display name.|False|List|ASC|
|Results Limit|Specify max number of groups to return.|False|String||
|Filter Logic|Specify what filter logic should be applied. Filtering is working on the Name field.|False|List|Equal|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering is working on the Name field.|False|String||



##### JSON Results
```json
[{"Group_Type": "managed", "Id": "1212-12312-123","Name": "Group Name","Description": "This group is ...", "Created_Time":"2019-10-24T19:10:18Z", "onPremisesSamAccountName": "jdoe"}]
```



#### List Members in the Group
List members in the specified Azure AD group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|
|Group Name|Specify group name to return user list for.|False|String||
|Group ID|Specify the ID of the group in which you want to list the members. If both "Group Name" and "Group ID" are provided, then "Group ID" will have priority. Example of the id: 00e40000-1971-439d-80fc-d0e000001dbd.|False|String||
|Filter Key|Specify the key that needs to be used to filter group members.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||



##### JSON Results
```json
[{"@odata.type": "#microsoft.graph.user", "id": "b786d3cf-e97d-4511-b61c-0559e9f4da75", "businessPhones": [], "displayName": "John Doe", "givenName": "John", "jobTitle": "Software Engineer", "mail": "john.doe@example.com", "mobilePhone": null, "officeLocation": "Building A", "preferredLanguage": "en-US", "surname": "Doe", "userPrincipalName": "john.doe@example.com"}]
```



#### List User's Groups Membership
List Azure AD groups user is a member of. Note: The user name can be provided either as a Siemplify entity or as an action input parameter. If the user name is passed to action both as an entity and input parameter - action will be executed on the input parameter. User name should be specified in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Name|Specify user name to return groups membership for. User name should be specified in username@domain format. Parameter accepts multiple values as a comma separated string.|False|String||
|Return Only Security Enabled Groups|If enabled, only security groups that the user is a member of will be returned.|False|Boolean|false|
|Return Detailed Groups Information|If enabled, detailed information on the AD groups will be returned.|False|Boolean|false|
|Filter Key|Specify the key that needs to be used to filter groups.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|



##### JSON Results
```json
[{"Entity": "test@example.com", "EntityResult": [{"id": "00b135d0-603d-4b1e-93e4-24xxxxxxxxxx", "deletedDateTime": null, "classification": null, "createdDateTime": "2021-11-28T20:28:56Z", "creationOptions": ["ProvisionGroupHomepage", "HubSiteId:00000000-0000-0000-0000-000000000000", "SPSiteLanguage:1033"], "description": "SiemplifyIntegration2", "displayName": "SiemplifyIntegration2", "expirationDateTime": null, "groupTypes": ["Unified"], "isAssignableToRole": null, "mail": "test@example.com", "mailEnabled": true, "mailNickname": "SiemplifyIntegration2", "membershipRule": null, "membershipRuleProcessingState": null, "onPremisesDomainName": null, "onPremisesLastSyncDateTime": null, "onPremisesNetBiosName": null, "onPremisesSamAccountName": null, "onPremisesSecurityIdentifier": null, "onPremisesSyncEnabled": null, "preferredDataLocation": null, "preferredLanguage": null, "proxyAddresses": ["SPO:SPO_80b058c6-6886-47d4-adcc-8cffa88aca4c@SPO_d48f52ca-5b1a-4708-8ed0-ebxxxxxxxxxx", "SMTP:test@example.com"], "renewedDateTime": "2021-11-28T20:28:56Z", "resourceBehaviorOptions": [], "resourceProvisioningOptions": [], "securityEnabled": false, "securityIdentifier": "S-1-12-1-11613648-1260281917-3844400275-xxxxxxxxxx", "theme": null, "visibility": "Private", "onPremisesProvisioningErrors": []}, {"id": "59a278af-e84f-48ed-acab-84xxxxxxxxxx", "deletedDateTime": null, "classification": null, "createdDateTime": "2021-11-10T13:36:47Z", "creationOptions": [], "description": "k8s", "displayName": "k8s", "expirationDateTime": null, "groupTypes": [], "isAssignableToRole": true, "mail": null, "mailEnabled": false, "mailNickname": "4eccf442-d", "membershipRule": null, "membershipRuleProcessingState": null, "onPremisesDomainName": null, "onPremisesLastSyncDateTime": null, "onPremisesNetBiosName": null, "onPremisesSamAccountName": null, "onPremisesSecurityIdentifier": null, "onPremisesSyncEnabled": null, "preferredDataLocation": null, "preferredLanguage": null, "proxyAddresses": [], "renewedDateTime": "2021-11-10T13:36:47Z", "resourceBehaviorOptions": [], "resourceProvisioningOptions": [], "securityEnabled": true, "securityIdentifier": "S-1-12-1-1503819951-1223551055-3062148012-xxxxxxxxx", "theme": null, "visibility": "Private", "onPremisesProvisioningErrors": []}]}]
```



#### Ping
Test connectivity to the Azure Active Directory service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Remove User from a Group
Remove User from the specified group. Note: The user name can be provided either as a Siemplify entity or as an action input parameter. If the user name is passed to action both as an entity and input parameter - action will be executed on the input parameter. User name should be specified in username@domain format.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Name|Specify user name to remove from the target group. User name should be specified in username@domain format. Parameter accepts multiple values as a comma separated string.|False|String||
|Group Name|Specify group name to remove user from.|False|String||
|Group ID|Specify the ID of the group from which you want to remove the user. If both "Group Name" and "Group ID" are provided, then "Group ID" will have priority. Example of the id: 00e40000-1971-439d-80fc-d0e000001dbd.|False|String||



#### Revoke User Session
Revoke user session. Supported entities: Username, Email Address (username that matches email regex).
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity":"user@domain.onmicrosoft.com","EntityResult":{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#Edm.Boolean","value":true}},{"Entity":"username","EntityResult":{"error":"User not found."}}]
```



#### List Users
List Azure Active Directory users based on the specified search criteria. Note that action is not working on Siemplify entities. Additionally, advanced filtering is working on the Username (userPrincipalName) field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter|Specifies which fields will be included in the results. By default, we will return all the fields.|False|List|All Fields|
|Order By Field|Specifies the field based on which the results are ordered.|False|List|displayName|
|Order By|Specifies the result order.|False|List|DESC|
|Results Limit|Specify max number of users to return.|False|String||
|Advanced Filter Logic|Specify what filter logic should be applied. Advanced filtering is working on the Username (userPrincipalName) field.|False|List|Equal|
|Advanced Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied.  Advanced filtering is working on the Username (userPrincipalName) field.|False|String||



##### JSON Results
```json
[{"Username": "someusername@mail.com", "Surname": "TestSurname", "Name": "TestName", "Job_Title": "Engineer", "Mobile_Phone": "123456789", "Preferred_Language": "English", "Mail": "someusername@mail.com", "Givenname": "TestGivenName", "Id": "12345678-1234-1234-1234-1234567890"}]
```



#### Reset User Password
Change user password to the password specified in the action. User will have to change their password on next login. Action expects User to change password for as  SecOps User entity in username@domain format or as an action input parameter. If the User name is passed to action both as a SecOps entity and input parameter - action will be executed on the input parameter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Username|User name to change password for. Parameter expects value in a username@domain format and accepts multiple values as a comma separated string.|False|String||
|Password|User Authentication password.|True|Password|*****|










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.