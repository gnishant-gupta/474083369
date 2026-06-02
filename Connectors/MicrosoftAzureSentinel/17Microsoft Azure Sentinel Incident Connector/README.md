# 17Microsoft Azure Sentinel Incident Connector
DEPRECATED! Fetches Incidents from Azure Sentinel.


Integration: MicrosoftAzureSentinel

Integration Version: 62.0

Device Product Field: ProductName

Event Name Field: AlertName
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Script Timeout (Seconds)|The timeout limit (in seconds) for the python process running current script|True|180|
|Environment Field Name|Describes the name of the field where the environment name is stored.|False||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False||
|API Root|The API Root of Microsoft Azure Sentinel REST API root.|True|https://management.azure.com|
|OAUTH2 Login Endpoint Url|Specify the url, that connector should use for OAUTH2 Login.|True|https://login.microsoftonline.com|
|Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|dfghjk|
|Client Secret|Secret that was entered for Azure AD app registration|True|*****|
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|fghjk|
|Azure Sentinel Workspace Name|Name of the Azure Sentinel workspace to work with, can be viewed in Azure portal > Azure Sentinel > Azure Sentinel Workspaces.|True|rtyguhj|
|Azure Subscription ID|Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> > Subscription ID. |True|dfghj|
|Azure Resource Group|Name of Azure Resource Group where Azure Sentinel is located.|True|rtfygh|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|false|
|Max Incidents per Cycle|How many incidents should be processed during one connector run|False|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default value: 24 hours.|False|24|
|Incident Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|Draft, New, InProgress, Closed|
|Incident Severities to Fetch|Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|Informational, Low, Medium, High, Critical|
|Proxy Server Address|Proxy server to use for connection.|False||
|Proxy Server Username|Proxy server username|False||
|Proxy Server Password|Proxy server password|False|*****|


Connector readme updated