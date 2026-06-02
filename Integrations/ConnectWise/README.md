
# ConnectWise

Seamlessly transition projects and tasks to keep your communication flowing without ever worrying about accountability and visibility.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|None|https://{Company URL}/v4_6_Release/apis/3.0/|
|Company Name|None|True|String||
|Public Key|None|True|String||
|Private Key|None|True|Password|*****|
|Client Id|None|True|String||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|


## Actions
#### Add Attachment To Ticket
Add an attachment to the ticket in ConnectWise.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Allow Only Owner Update|If enabled, action will only allow the owner to update the attachment.|False|Boolean|true|
|Display In Customer Portal|If enabled, attachment will be shown in the customer portal.|False|Boolean|true|
|Filename|Specify the filename behind the attachment. This value will be also used as a title. Note: action needs to provide the correct extension for the file.|True|String|{filename}.{extension}|
|Base64 Encoded File|Specify the base64 encoded file that needs to be added as an attachment.|True|String||
|Ticket ID|Specify the ID of the ticket to which the document would need to be added.|True|String||



##### JSON Results
```json
{"id":"xxxx","title":"test file","fileName":"test.json","serverFileName":"24e7db8d-41b5-4bd0-9db3-xxxxxx.json","owner":"Admin","linkFlag":false,"imageFlag":false,"publicFlag":false,"htmlTemplateFlag":false,"readOnlyFlag":true,"size":22131,"urlFlag":false,"guid":"b9fc3fc6-f368-40bb-bc06-xxxxxx","_info":{"lastUpdated":"2022-05-10T14:02:23Z","updatedBy":"Admin"}}
```



#### Close Ticket
Close ConnectWise ticket
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|ConnectWise ticket id. e.g. 608718|True|String||
|Custom Close Status|If the specific system use a custom closed status (e.g. Completed)|False|String||



#### Delete Ticket
Delete ConnectWise ticket by ID
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Ticket ID to be deleted. e.g. 607167|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Add Comment To Ticket
Add new comment to a ticket in ConnectWise
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|ConnectWise ticket id. e.g. 608718|True|String||
|Comment|Comment content to attach to a ticket|True|Content||
|Internal|If checked, put comment in internal section|False|Boolean|False|



#### Update Ticket
Update ticket details in ConnectWIse
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Ticket ID to be updated. e.g. 609620|True|String||
|Summary|Specify the summary for the updated ticket. Note: if the summary is more than 100 characters, it will be truncated.|False|Content||
|Type Name|e.g. Application|False|String||
|SubType Name|e.g. Adobe|False|String||
|Item Name|e.g. Development|False|String||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|String||
|Board|Board name.|False|String||
|Priority|e.g. Priority 3 - Normal Response.|False|String||
|Status|New ticket status, e.g. In Progress (plan of action)|False|String||
|Email Note CC|Specify a comma-separated list of email addresses that should receive all of the notes via email.|False|String||



#### Create Alerts Ticket
Create a ConnectWise ticket for each new Siemplify alert
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company|Company identifier|True|String||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|String||
|Board|Board name|True|String||
|Status|e.g. Unassigned|True|String||
|Priority|e.g. Priority 3 - Normal Response|True|String||
|Initial Description|Initial Description|True|Content||



#### Create Ticket
Create a ConnectWise ticket
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company|Company identifier|True|String||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|String||
|Board|Board name|True|String||
|Summary|Specify the summary for the new ticket. Note: if the summary is more than 100 characters, it will be truncated.|True|Content||
|Status|e.g. Unassigned|True|String||
|Priority|e.g. Priority 3 - Normal Response|True|String||
|Email Note CC|Specify a comma-separated list of email addresses that should receive all of the notes via email.|False|String||



#### Get Ticket
Get ConnectWise ticket by ID and attach ticket JSON as a file
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Fetch ticket by ID|True|String||



##### JSON Results
```json
{"773256": {"customerUpdatedFlag": false, "estimatedTimeCost": 0.0, "recordType": "ServiceTicket", "siteName": "Main", "billTime": "NoDefault", "site": {"_info": {"site_href": "", "mobileGuid": "c5e7be2e-af3b-461f-a637-1b3e7e24bdc6"}, "id": 23188, "name": "Main"}, "currency": {"symbol": "$", "isoCode": "USD", "_info": {"currency_href": ""}, "name": "US Dollars", "id": 7}, "estimatedProductCost": 0.0, "estimatedExpenseRevenue": 0.0, "contactName": "user name", "addressLine1": "110 Fifth Avenue ", "billingMethod": "ActualRates", "id": 773256, "impact": "Medium", "city": "New York", "billProducts": "NoDefault", "businessUnitId": 20, "zip": "10011", "estimatedExpenseCost": 0.0, "mobileGuid": "f7b5a0eb-6038-4e14-a661-05c393917841", "closedFlag": false, "enteredBy": "Siemplify", "priority": {"sort": 6, "_info": {"image_href": "", "priority_href": ""}, "id": 4, "name": "Priority 3 - Normal Response"}, "source": {"_info": {"source_href": ""}, "id": 2, "name": "Customer Phone Call"}, "automaticEmailCcFlag": false, "board": {"_info": {"board_href": ""}, "id": 70, "name": "Siemplify - T&M"}, "customFields": [{"numberOfDecimals": 0, "caption": "2nd Shift", "type": "Checkbox", "id": 20, "entryMethod": "EntryField"}, {"numberOfDecimals": 0, "caption": "3rd Shift", "type": "Checkbox", "id": 21, "entryMethod": "EntryField"}, {"numberOfDecimals": 0, "caption": "Huddle Rvw", "type": "Checkbox", "id": 22, "entryMethod": "EntryField"}], "contactEmailAddress": "john_doe@example.com", "status": {"_info": {"status_href": ""}, "id": 1351, "name": "Unassigned"}, "contactPhoneNumber": "+972-50-5613528", "dateResponded": "2019-01-17T09:21:03Z", "isInSla": false, "company": {"_info": {"mobileGuid": "42fcabed-a0f6-4171-bd7a-ca563ba45f7c", "company_href": ""}, "identifier": "Siemplify", "id": 18304, "name": "Siemplify"}, "automaticEmailContactFlag": false, "hasChildTicket": false, "billExpenses": "NoDefault", "estimatedTimeRevenue": 0.0, "locationId": 119, "estimatedProductRevenue": 0.0, "automaticEmailResourceFlag": false, "dateEntered": "2019-01-17T09:21:03Z", "approved": true, "severity": "Medium", "resolveMinutes": 0, "serviceLocation": {"_info": {"location_href": ""}, "id": 6, "name": "Remote"}, "resPlanMinutes": 0, "stateIdentifier": "NY", "dateResplan": "2019-01-17T09:21:03Z", "subBillingMethod": "ActualRates", "country": {"_info": {"country_href": ""}, "id": 1, "name": "United States"}, "respondMinutes": 0, "allowAllClientsPortalView": false, "hasMergedChildTicketFlag": false, "summary": "TikcetApiTest", "contact": {"_info": {"contact_href": "", "mobileGuid": "c86377ec-7726-4057-aca2-e992b550140f"}, "id": 59249, "name": "user name"}, "team": {"_info": {"team_href": ""}, "id": 78, "name": "Siemplify"}, "addressLine2": "5th Floor", "_info": {"configurations_href": "", "tasks_href": "", "updatedBy": "Siemplify", "expenseEntries_href": "", "lastUpdated": "2019-01-17T09:21:03Z", "products_href": "", "activities_href": "", "timeentries_href": "", "notes_href": "", "documents_href": "", "scheduleentries_href": ""}}}
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.