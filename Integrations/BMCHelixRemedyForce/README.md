
# BMCHelixRemedyForce

BMC Helix Remedyforce is comprehensive IT service management that easily scales and adapts to the needs of mid-size companies. Built on Salesforce cloud, it allows you to seamlessly combine IT operations management (ITOM) and cognitive capabilities to ensure the business is efficient, compliant, and secure.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|None|https://{{your instance}}.my.salesforce.com|
|Login API Root|None|True|None|https://login.salesforce.com|
|Username|None|False|String||
|Password|None|False|Password|*****|
|Client ID|None|False|String||
|Client Secret|None|False|Password|*****|
|Refresh Token|None|False|Password|*****|
|Verify SSL|None|False|Boolean|true|


#### Dependencies
| |
|-|
|my_test_package-0.1.1.tar.gz|
|idna-3.8-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|xmltodict-0.13.0-py2.py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|filelock-3.16.0-py3-none-any.whl|
|lxml-5.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|PyPika-0.48.9.tar.gz|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|setuptools-74.1.2-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|netaddr-1.3.0-py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|


## Actions
#### Delete Record
Delete a record in BMC Helix Remedyforce.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify the type of the record that needs to be deleted. If you don't know what kind of records are available, please execute action "List Record Types".|True|String||
|Record ID|Specify the id of the record that needs to be deleted.|True|String||



#### Get OAuth Refresh Token
Generate the refresh token that is needed for the integration configuration. Authorization code can be generated using "Get OAuth Authorization Code". Please refer to the documentation portal for more information.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Redirect URL|Specify the redirect URL that was used when the "Connector App" was created.|True|String|https://localhost|
|Authorization Code|Specify the authorization code from action "Get OAuth Authorization Code".|True|String||



#### List Record Types
List available record types from BMC Helix Remedyforce. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among record types and if "Contains" is selected, action will try to find record types that contain that substring. If nothing is provided in this parameter, the filter will not be applied.|False|String||
|Max Record Types To Return|Specify how many record types to return. Default: 50.|False|String|50|
|Filter Logic|Specify what filter logic should be applied.|False|List|Equal|



##### JSON Results
```json
[{"activateable": false, "associateEntityType": null, "associateParentEntity": null, "createable": false, "custom": false, "customSetting": false, "deepCloneable": false, "deletable": false, "deprecatedAndHidden": false, "feedEnabled": false, "hasSubtypes": false, "isInterface": false, "isSubtype": false, "keyPrefix": null, "label": "Accepted Event Relation", "labelPlural": "Accepted Event Relations", "layoutable": false, "mergeable": false, "mruEnabled": false, "name": "AcceptedEventRelation", "queryable": true, "replicateable": false, "retrieveable": true, "searchable": false, "triggerable": false, "undeletable": false, "updateable": false, "urls": {"rowTemplate": "/services/data/v51.0/sobjects/AcceptedEventRelation/{ID}", "defaultValues": "/services/data/v51.0/sobjects/AcceptedEventRelation/defaultValues?recordTypeId&fields", "describe": "/services/data/v51.0/sobjects/AcceptedEventRelation/describe", "sobject": "/services/data/v51.0/sobjects/AcceptedEventRelation"}}]
```



#### Ping
Test connectivity to the BMC Helix Remedyforce with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Get OAuth Authorization Code
Generate an OAuth authorization code in BMC Helix Remedyforce. Please refer to the documentation portal for more information.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Redirect URL|Specify the redirect URL that was used when the "Connector App" was created.|True|String|https://localhost|



#### Update Record
Update record in BMC Helix Remedyforce.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify the type of the record that needs to be updated. If you don't know what kind of records are available, please execute action "List Record Types".|True|String||
|Record ID|Specify the id of the record that needs to be updated.|True|String||
|Fields To Update|Specify a JSON object containing all of the needed fields and  values that need to be updated.|True|String|{"field":"value"}|



#### Wait For Fields Update
Wait for fields update in BMC Helix Remedyforce.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify the type of the record for which you are waiting an update. If you don't know what kind of records are available, please execute action "List Record Types".|True|String||
|Record ID|Specify the ID of the record that needs to be updated.|True|String||
|Fields To Check|Specify a JSON object containing all of the needed fields and  values.|True|String|{"field":"value"}|
|Fail If Timeout|If enabled, action will be failed, if not all of the fields were updated.|False|Boolean|true|



##### JSON Results
```json
{"attributes": {"type": "BMCServiceDesk__Incident__c", "url": "/services/data/v51.0/sobjects/BMCServiceDesk__Incident__c/a2U5e000000kl6NEAQ"}, "Id": "a2U5e000000kl6NEAQ", "OwnerId": "00G5e000001mqf7EAA", "IsDeleted": false, "Name": "00000002", "CreatedDate": "2021-05-10T19:00:26.000+0000", "CreatedById": "0055e000001zFloAAE", "LastModifiedDate": "2021-05-26T16:37:48.000+0000", "LastModifiedById": "0055e000001zFloAAE", "SystemModstamp": "2021-05-26T16:37:48.000+0000", "LastActivityDate": null, "LastViewedDate": "2021-05-26T16:39:32.000+0000", "LastReferencedDate": "2021-05-26T16:39:32.000+0000", "BMCServiceDesk__ACApprovalStatus__c": null, "BMCServiceDesk__ACSeverity__c": null, "BMCServiceDesk__Actual_Outage_Time_Hours__c": 0.0, "BMCServiceDesk__Additional_email_information__c": null, "BMCServiceDesk__AllTaskCloseController__c": false, "BMCServiceDesk__Approved__c": false, "BMCServiceDesk__BLANK__c": null, "BMCServiceDesk__Category_ID__c": "Hardware", "BMCServiceDesk__Client_Account__c": "Universal Systems LLC", "BMCServiceDesk__Client_Manager__c": null, "BMCServiceDesk__Client_Name__c": "test123", "BMCServiceDesk__Client_Phone__c": "(713)918-8800", "BMCServiceDesk__Client_Type__c": "test123", "BMCServiceDesk__Clock_Status__c": "Paused", "BMCServiceDesk__Closed_By__c": null, "BMCServiceDesk__ClosureCategory__c": null, "BMCServiceDesk__Compliant__c": "NO", "BMCServiceDesk__Compliments_and_Complaints__c": null, "BMCServiceDesk__Due_Date_Progress__c": "<img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/light_red.gif\" alt=\"Due date of a record has passed\" border=\"0\"/>", "BMCServiceDesk__EmailServiceAddress__c": null, "BMCServiceDesk__Event_ID__c": null, "BMCServiceDesk__FKAccount__c": "0015e000005bVzVAAU", "BMCServiceDesk__FKBMC_BaseElement__c": "a0K5e000000RQM2EAO", "BMCServiceDesk__FKBroadcast__c": null, "BMCServiceDesk__FKBusinessService__c": null, "BMCServiceDesk__FKCategory__c": "a215e000000xL5GAAU", "BMCServiceDesk__FKClient__c": "0055e000002R4oUAAS", "BMCServiceDesk__FKClosedBy__c": null, "BMCServiceDesk__FKContact__c": null, "BMCServiceDesk__FKImpact__c": "a2M5e000000l1HxEAI", "BMCServiceDesk__FKIncident__c": null, "BMCServiceDesk__FKLead__c": null, "BMCServiceDesk__FKOpenBy__c": "0055e000001zFloAAE", "BMCServiceDesk__FKPriority__c": "a2h5e000000nHTnAAM", "BMCServiceDesk__FKRequestDefinition__c": null, "BMCServiceDesk__FKRequestDetail__c": null, "BMCServiceDesk__FKServiceOffering__c": null, "BMCServiceDesk__FKStatus__c": "a3w5e000000U1xcAAC", "BMCServiceDesk__FKTemplate__c": null, "BMCServiceDesk__FKUrgency__c": "a475e000000gSuKAAU", "BMCServiceDesk__Feedback_Last_Submitted__c": null, "BMCServiceDesk__Feedback__c": null, "BMCServiceDesk__Impact_Id__c": "LOW", "BMCServiceDesk__IncidentType__c": null, "BMCServiceDesk__Is_New_Record__c": false, "BMCServiceDesk__Launch_console__c": "<a href=\"/apex/BMCServiceDesk__ConsoleRedirect?formulaFieldName=IncidentLaunchConsole&amp;recordName=00000002&amp;recordId=a2U5e000000kl6N&amp;incType=Incident&amp;isdtp=vw&amp;uiTheme=Theme3&amp;formLayoutId=\" target=\"_self\">IN00000002</a>", "BMCServiceDesk__New_Incident__c": null, "BMCServiceDesk__PreferredContactMethod__c": null, "BMCServiceDesk__Priority_ID__c": "4", "BMCServiceDesk__Recurrence__c": null, "BMCServiceDesk__RecurringParentRecordId__c": null, "BMCServiceDesk__RequestDetailCloneId__c": null, "BMCServiceDesk__ServiceRequest__c": "No", "BMCServiceDesk__Service_Request_Title__c": "htest title", "BMCServiceDesk__ShowDueDateDialog__c": false, "BMCServiceDesk__StatusChangeDate__c": "2021-05-14T12:15:09.000+0000", "BMCServiceDesk__Status_ID__c": "ASSIGNED", "BMCServiceDesk__Task_Closed_Controller__c": null, "BMCServiceDesk__TemplateAlreadyApplied__c": false, "BMCServiceDesk__TemplateName__c": null, "BMCServiceDesk__TimeSpentInCurrentStatus__c": 17544.0, "BMCServiceDesk__Time_Remaining_Percentage__c": 0.0, "BMCServiceDesk__TotalWorkTime__c": 0.0, "BMCServiceDesk__Type__c": "Incident", "BMCServiceDesk__UpdateCount__c": 27.0, "BMCServiceDesk__Urgency_ID__c": "MEDIUM", "BMCServiceDesk__VIP_Client__c": "-", "BMCServiceDesk__WorkflowController__c": null, "BMCServiceDesk__actualDuration__c": null, "BMCServiceDesk__actualOutageDuration__c": null, "BMCServiceDesk__call__c": 1.0, "BMCServiceDesk__clientEmail__c": "bmcremedyforcetrial@example.com", "BMCServiceDesk__clientFirstName__c": "Jackson", "BMCServiceDesk__clientId__c": "jackson.smith.sibjajid55jl.it9nt65wjny0.s3pxpmb8mh0n@bmcremedyforce.com", "BMCServiceDesk__clientLastName__c": "Smith", "BMCServiceDesk__closeDateTime__c": null, "BMCServiceDesk__closeTasks__c": false, "BMCServiceDesk__completedDate__c": null, "BMCServiceDesk__contactType__c": null, "BMCServiceDesk__dueDateTime__c": "2021-05-16T04:15:09.000+0000", "BMCServiceDesk__firstCallResolution__c": false, "BMCServiceDesk__followUpDateTime__c": null, "BMCServiceDesk__followUp__c": false, "BMCServiceDesk__inactive__c": false, "BMCServiceDesk__inc_console_detail_link__c": "<a href=\"/apex/BMCServiceDesk__ConsoleRouting?objectName=Incident&amp;record_name=00000002&amp;record_id=a2U5e000000kl6N&amp;isdtp=vw&amp;isServiceCloudConsole=true\" target=\"_blank\">00000002</a>", "BMCServiceDesk__incidentDescription__c": "My hard disk crashed. I need a replacement and to have any data transferred.", "BMCServiceDesk__incidentResolution__c": null, "BMCServiceDesk__maximumDuration__c": null, "BMCServiceDesk__note__c": null, "BMCServiceDesk__openDateTime__c": "2021-05-14T12:15:09.000+0000", "BMCServiceDesk__outageFrom__c": null, "BMCServiceDesk__outageTo__c": null, "BMCServiceDesk__queueName__c": "Incident Queue", "BMCServiceDesk__recommendedFixDateTime__c": null, "BMCServiceDesk__respondedDateTime__c": null, "BMCServiceDesk__responseDateTime__c": null, "BMCServiceDesk__shortDescription__c": "test", "BMCServiceDesk__state__c": true, "BMCServiceDesk__timeSpent__c": null, "BMCServiceDesk__Total_Duration__c": 0.0, "BMCServiceDesk__Incorrect_category__c": false, "Client_VIP__c": false, "BMCServiceDesk__Incorrect_owner__c": false, "BMCServiceDesk__LockedRecordTimestamp__c": null, "BMCServiceDesk__Queue__c": "Incident Queue", "BMCServiceDesk__Reassigned_Count__c": null, "BMCServiceDesk__isServiceRequest__c": false, "BMCServiceDesk__Approval_Status__c": null, "Alternate_Contact_Name__c": null, "Alternate_Contact_Number__c": null, "Client_Phone__c": null, "External_Ticket_Ref__c": null, "Affected_Application__c": null, "Affected_Hardware__c": null, "BMCServiceDesk__Deep_View__c": "<a href=\"/apex/BMCServiceDesk__DeepView?id=a2U5e000000kl6N\" target=\"_blank\"><img src=\"/resource/BMCServiceDesk__SDEFStyles/SDEFbuttons/deep-view.png\" alt=\" \" style=\"height:18px; width:18px;\" border=\"0\"/></a>", "BMCServiceDesk__RF_TimeToClose__c": null, "BMCServiceDesk__RF_FKLayout__c": null, "BMCServiceDesk__RF_LTEC__c": 1.0, "BMCServiceDesk__RF_SkipTriggerExecution__c": false, "BMCServiceDesk__Categorization_Mode__c": null, "BMCServiceDesk__RF_Attachments__c": null, "BMCServiceDesk__RF_HasAttachments__c": null, "BMCServiceDesk__RF_IntegrationData__c": null}
```



#### Create Record
Create a record in BMC Helix Remedyforce.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify the type of the record that needs to be created. If you don't know what kind of records are available, please execute action "List Record Types".|True|String||
|Record Payload|Specify a JSON object containing all of the needed fields and values.|True|String||



##### JSON Results
```json
{"id": "0015e000005fmIxxxx", "success": true, "errors": []}
```



#### Execute Simple Query
Execute a SOQL query based on parameters in BMC Helix Remedyforce.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify what record type should be queried.|True|String||
|Where Filter|Specify the WHERE filter for the query  that needs to be executed. Note: you don't need to provide time filter, limiting and sorting. Also, you don't need to provide WHERE string in the payload.|False|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Fields To Return|Specify what fields to return. If nothing is provided action will return all fields.|False|String||
|Sort Field|Specify what parameter should be used for sorting.|False|String|CreatedDate|
|Max Results To Return|Specify how many results to return. Default: 50. Maximum is 200.|False|String|50|
|Sort Order|Specify the order of sorting.|False|List|ASC|



##### JSON Results
```json
[{"attributes": {"type": "Account", "url": "/services/data/v51.0/sobjects/Account/0015e000005fkuKAAQ"}, "Id": "0015e000005fkuKAAQ", "IsDeleted": false, "MasterRecordId": null, "Name": "KOKO", "Type": null, "ParentId": null, "BillingStreet": null, "BillingCity": null, "BillingState": null, "BillingPostalCode": null, "BillingCountry": "HIGH", "BillingLatitude": null, "BillingLongitude": null, "BillingGeocodeAccuracy": null, "BillingAddress": {"city": null, "country": "HIGH", "geocodeAccuracy": null, "latitude": null, "longitude": null, "postalCode": null, "state": null, "street": null}, "ShippingStreet": null, "ShippingCity": null, "ShippingState": null, "ShippingPostalCode": null, "ShippingCountry": null, "ShippingLatitude": null, "ShippingLongitude": null, "ShippingGeocodeAccuracy": null, "ShippingAddress": null, "Phone": null, "Fax": null, "Website": null, "PhotoUrl": "/services/images/photo/0015e000005fkuKAAQ", "Industry": null, "AnnualRevenue": null, "NumberOfEmployees": null, "Description": null, "OwnerId": "0055e000001zFloAAE", "CreatedDate": "2021-05-21T18:07:40.000+0000", "CreatedById": "0055e000001zFloAAE", "LastModifiedDate": "2021-05-21T18:07:40.000+0000", "LastModifiedById": "0055e000001zFloAAE", "SystemModstamp": "2021-05-21T18:07:40.000+0000", "LastActivityDate": null, "LastViewedDate": "2021-05-21T18:07:40.000+0000", "LastReferencedDate": "2021-05-21T18:07:40.000+0000", "Jigsaw": null, "JigsawCompanyId": null, "AccountSource": null, "SicDesc": null, "BMCServiceDesk__Active__c": null, "BMCServiceDesk__CustomerPriority__c": null, "BMCServiceDesk__FKSelfService_Theme__c": null, "BMCServiceDesk__FKUrgency__c": null, "BMCServiceDesk__NumberofLocations__c": null, "BMCServiceDesk__Remedyforce_Account__c": false, "BMCServiceDesk__SLA__c": null, "BMCServiceDesk__ServiceProvider__c": false, "BMCServiceDesk__Vendor__c": false, "BMCServiceDesk__costCenter__c": null, "BMCServiceDesk__inactive__c": false, "BMCServiceDesk__Business_Hour__c": null, "BMCServiceDesk__FKSelfService3_Theme__c": null, "BMCServiceDesk__SLAExpirationDate__c": null, "BMCServiceDesk__SLASerialNumber__c": null, "BMCServiceDesk__UpsellOpportunity__c": null}]
```



#### Execute Custom Query
Execute a custom SOQL query in BMC Helix Remedyforce. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SOQL Query|Specify what query should be executed.|True|String||



##### JSON Results
```json
[{"attributes": {"type": "Account", "url": "/services/data/v51.0/sobjects/Account/0015e000005fq27AAA"}, "Id": "0015e000005fq27AAA", "IsDeleted": false, "MasterRecordId": null, "Name": "2312123132123123", "Type": null, "ParentId": null, "BillingStreet": null, "BillingCity": null, "BillingState": null, "BillingPostalCode": null, "BillingCountry": "HIGH", "BillingLatitude": null, "BillingLongitude": null, "BillingGeocodeAccuracy": null, "BillingAddress": {"city": null, "country": "HIGH", "geocodeAccuracy": null, "latitude": null, "longitude": null, "postalCode": null, "state": null, "street": null}, "ShippingStreet": null, "ShippingCity": null, "ShippingState": null, "ShippingPostalCode": null, "ShippingCountry": null, "ShippingLatitude": null, "ShippingLongitude": null, "ShippingGeocodeAccuracy": null, "ShippingAddress": null, "Phone": null, "Fax": null, "Website": null, "PhotoUrl": "/services/images/photo/0015e000005fq27AAA", "Industry": null, "AnnualRevenue": null, "NumberOfEmployees": null, "Description": null, "OwnerId": "0055e000001zFloAAE", "CreatedDate": "2021-05-22T18:48:19.000+0000", "CreatedById": "0055e000001zFloAAE", "LastModifiedDate": "2021-05-22T18:48:19.000+0000", "LastModifiedById": "0055e000001zFloAAE", "SystemModstamp": "2021-05-22T18:48:19.000+0000", "LastActivityDate": null, "LastViewedDate": "2021-05-22T18:48:28.000+0000", "LastReferencedDate": "2021-05-22T18:48:28.000+0000", "Jigsaw": null, "JigsawCompanyId": null, "AccountSource": null, "SicDesc": null, "BMCServiceDesk__Active__c": null, "BMCServiceDesk__CustomerPriority__c": null, "BMCServiceDesk__FKSelfService_Theme__c": null, "BMCServiceDesk__FKUrgency__c": null, "BMCServiceDesk__NumberofLocations__c": null, "BMCServiceDesk__Remedyforce_Account__c": false, "BMCServiceDesk__SLA__c": null, "BMCServiceDesk__ServiceProvider__c": false, "BMCServiceDesk__Vendor__c": false, "BMCServiceDesk__costCenter__c": null, "BMCServiceDesk__inactive__c": false, "BMCServiceDesk__Business_Hour__c": null, "BMCServiceDesk__FKSelfService3_Theme__c": null, "BMCServiceDesk__SLAExpirationDate__c": null, "BMCServiceDesk__SLASerialNumber__c": null, "BMCServiceDesk__UpsellOpportunity__c": null}]
```



#### Get Record Details
Get detailed information about the record from BMC Helix Remedyforce. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Record Type|Specify the type of the record for which you want to retrieve details. If you don't know what kind of records are available, please execute action "List Record Types".|True|String||
|Record IDs|Specify the ids of records for which you want to return details.|True|String||
|Fields To Return|Specify what fields to return. If none of the provided fields were found, action will fail. If nothing is provided, action will return all fields. |False|String||



##### JSON Results
```json
[{"attributes": {"type": "Account", "url": "/services/data/v51.0/sobjects/Account/0015e000005fq1sxxx"}, "Id": "0015e000005fq1sxxx", "IsDeleted": false, "MasterRecordId": null, "Name": "KOKO", "Type": null, "ParentId": null, "BillingStreet": null, "BillingCity": null, "BillingState": null, "BillingPostalCode": null, "BillingCountry": "HIGH", "BillingLatitude": null, "BillingLongitude": null, "BillingGeocodeAccuracy": null, "BillingAddress": {"city": null, "country": "HIGH", "geocodeAccuracy": null, "latitude": null, "longitude": null, "postalCode": null, "state": null, "street": null}, "ShippingStreet": null, "ShippingCity": null, "ShippingState": null, "ShippingPostalCode": null, "ShippingCountry": null, "ShippingLatitude": null, "ShippingLongitude": null, "ShippingGeocodeAccuracy": null, "ShippingAddress": null, "Phone": null, "Fax": null, "Website": null, "PhotoUrl": "/services/images/photo/0015e000005fq1sxxx", "Industry": null, "AnnualRevenue": null, "NumberOfEmployees": null, "Description": null, "OwnerId": "0055e000001zFloxxx", "CreatedDate": "2021-05-22T18:41:59.000+0000", "CreatedById": "0055e000001zFloxxx", "LastModifiedDate": "2021-05-22T18:41:59.000+0000", "LastModifiedById": "0055e000001zFloxxx", "SystemModstamp": "2021-05-22T18:41:59.000+0000", "LastActivityDate": null, "LastViewedDate": "2021-05-22T18:48:56.000+0000", "LastReferencedDate": "2021-05-22T18:48:56.000+0000", "Jigsaw": null, "JigsawCompanyId": null, "AccountSource": null, "SicDesc": null, "BMCServiceDesk__Active__c": null, "BMCServiceDesk__CustomerPriority__c": null, "BMCServiceDesk__FKSelfService_Theme__c": null, "BMCServiceDesk__FKUrgency__c": null, "BMCServiceDesk__NumberofLocations__c": null, "BMCServiceDesk__Remedyforce_Account__c": false, "BMCServiceDesk__SLA__c": null, "BMCServiceDesk__ServiceProvider__c": false, "BMCServiceDesk__Vendor__c": false, "BMCServiceDesk__costCenter__c": null, "BMCServiceDesk__inactive__c": false, "BMCServiceDesk__Business_Hour__c": null, "BMCServiceDesk__FKSelfService3_Theme__c": null, "BMCServiceDesk__SLAExpirationDate__c": null, "BMCServiceDesk__SLASerialNumber__c": null, "BMCServiceDesk__UpsellOpportunity__c": null}]
```









## Connectors
#### BMC Helix Remedyforce - Incidents Connector
Pull information about incidents from BMC Helix Remedyforce.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|BMCServiceDesk__Type__c|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the BMC Helix Remedyforce instance.|True|String|https://{{your instance}}.my.salesforce.com|
|Login API Root|API root that is used to authenticate in BMC Helix Remedyforce.|True|String|https://login.salesforce.com|
|Username|BMC Helix Remedyforce username.|False|String||
|Password|BMC Helix Remedyforce password.|False|Password|*****|
|Client ID|BMC Helix Remedyforce client ID of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.|False|String||
|Client Secret|BMC Helix Remedyforce client secret of the connected app. This parameter is needed for OAuth authentication. Note: this parameter has priority over Username + Password authentication.|False|Password|*****|
|Refresh Token|Refresh token for the OAuth authorization.|False|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the BMC Helix Remedyforce server is valid.|False|Boolean|true|
|Lowest Priority To Fetch|Lowest priority that will be used to fetch incidents. Maximum: 5. Minimum: 1. If nothing is provided, the connector will ingest all incidents.|False|Integer|5|
|Ingest Empty Priority Incidents|If enabled, the connector will fetch incidents that don't have priority. Siemplify Alerts created in this manner will have priority set to "Informational".|False|Boolean|true|
|Type Filter|Type filter for the incidents. If nothing is provided, the connector will ingest all incidents. Example: Incident, Service Request.|False|String|Incident,Service Request|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Incidents To Fetch|How many incidents to process per one connector iteration. Maximum is 200.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.