# 21Microsoft Graph Mail Delegated Connector
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email. This connector uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure the connector, make sure that the integration configuration is already finished, and the refresh token needed to communicate with Office 365 is generated.


Integration: MicrosoftGraphMailDelegated

Integration Version: 18.0

Device Product Field: device_product

Event Name Field: event_name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Mail Address|An email address for the connector to use.|True|hgfdsa|
|Max Emails Per Cycle|The maximum number of emails to fetch for every connector iteration.|True|10|
|Environment Field Name|The name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment. The default value is ""
|False||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the Environment Field Name field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value .* to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Email Exclude Pattern|A regular expression to exclude specific emails from ingestion, such as spam or news. This parameter works with both the subject and body of the email.|False||
|Script Timeout (Seconds)|The timeout limit in seconds for the Python process that runs the current script.|True|300|
|Microsoft Entra ID Endpoint|The Microsoft Entra endpoint to connect to. The default value is https://login.microsoftonline.com.|True|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|The Microsoft Graph endpoint to connect to. The default value is https://graph.microsoft.com.|True|https://graph.microsoft.com|
|Refresh Token|The refresh token that you obtained after you generated a token.|True|*****|
|Client ID|For Microsoft 365 OAuth 2.0 authentication, the application (client) ID of the Microsoft Entra application that is used in the integration.|True|hgfd|
|Client Secret Value|For Microsoft 365 OAuth 2.0 authentication, the client secret value that is provided for the authentication flow.|True|*****|
|Microsoft Entra ID Directory ID|For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra ID application that you used in the integration.|True|gfds|
|Folder To Check For Emails|An email folder to search for the emails. This parameter accepts a comma-separated list of folders to check the user response in multiple folders. To specify a subfolder, use the “/” forward slash, such as {Inbox/Subfolder}. This parameter is case-sensitive. The default value is Inbox.|True|Inbox|
|Offset Time In Hours|The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time. The connector can use this parameter as a fallback value when the timestamp from the latest connector iteration expires.|True|24|
|Unread Emails Only|If selected, the connector creates cases only for unread emails.|False|false|
|Mark Emails as Read|If selected, the connector marks ingested emails as read.|False|false|
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism.|False|false|
|Verify SSL|If selected, the integration verifies that the SSL certificate for connecting to the Microsoft Graph server is valid.|False|true|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|*****|
|Mail Field Source|If selected, the connector retrieves the mailbox address from the user details “mail” attribute. If not selected, the integration retrieves the mailbox address from the “userPrincipalName” field. Selected by default.|False|true|
|Original Received Mail Prefix|A prefix to add to the extracted event keys (for example, to, from, or subject) from the original email received in the monitored mailbox. The default value is orig.|False|orig|
|Attached Mail File Prefix|A prefix to add to the extracted event keys (for example, to, from, or subject) from the attached email file received in the monitored mailbox. The default value is attach.|False|attach|
|Create a Separate Google SecOps Alert Per Attached Mail File|If selected, the connector creates multiple alerts, with one alert for every attached email file. This behavior is useful when you process emails with multiple email files attached and set the Google SecOps event mapping to create entities from attached email files.|False|false|
|Attach Original EML|If selected, the connector attaches the original email to the case info as an EML file.|False|false|
|Headers to add to events|A comma-separated string of email headers to add to Google SecOps events, such as “DKIM-Siganture”, “Received”, “From”. You can provide an exact match for headers or set this parameter value as a regular expression. The connector filters the configured values from the “internetMessageHeaders” list and adds them to the Google SecOps event. By default, the connector adds all available headers. To prevent the connector from adding headers to the event, set the parameter value as follows: None.|False||
|Case Name Template|A custom case name. When you configure this parameter, the connector adds a new key called custom_case_name to the Google SecOps event. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value.|False||
|Alert Name Template|A custom alert name. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys that contain the string value. If you configure an invalid template or don't set a value, the connector uses the default alert name.|False||
|Proxy Server Address|The address of the proxy server to use.|False||
|Proxy Username|The proxy server username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False|*****|

