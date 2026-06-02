
# BitSight

BitSight offers the world's leading security ratings solution with a mission to change the way the world manages cybersecurity analytics and risk.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the BitSight instance.|True|String|https://api.bitsighttech.com|
|API Key|API Key of the BitSight instance.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the BitSight is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|


## Actions
#### Ping
Test connectivity to the BitSight with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Company Highlights
List highlights related to the company in BitSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company Name|Specify the name of the company for which you want to return highlights.|True|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide the "Start Time" parameter.|False|List|Last Month|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.|False|String||
|Max Highlights To Return|Specify the number of  highlights you want to return. Default: 20.|False|String|20|



##### JSON Results
```json
[{"date":"2022-07-11","guid":"6bd65231-ba0d-4cc0-9dfb-59xxxxxxxxxx","start_score":530,"end_score":510,"reasons":[{"start_percentile":100,"risk_vector":"botnet","evidence":[{"type":"infection","name":"ZeroAccess","kbid":"1xx"}],"start_score":820,"end_percentile":82,"end_score":780}],"type":"rating-change","entity":"a940bb61-33c4-42c9-9231-c8xxxxxxxxxx"},{"date":"2022-06-30","guid":"9cf3c8bb-20bd-4872-90e6-60xxxxxxxxxx","start_score":560,"end_score":540,"reasons":[{"start_percentile":79,"risk_vector":"torrent","evidence":[{"end_grade":"D","start_grade":"B"}],"start_score":750,"end_percentile":36,"end_score":640}],"type":"rating-change","entity":"a940bb61-33c4-42c9-9231-c8xxxxxxxxxx"}]
```



#### Get Company Details
Get information about a company in BitSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company Name|Specify the name of the company for which you want to return details.|True|String||



##### JSON Results
```json
{"rating":1,"guid":"a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx","custom_id":null,"name":"Saperix, Inc.","description":"Saperix Technologies LLC develops risk analysis software solutions.","ipv4_count":4320,"people_count":500,"shortname":"Saperix","industry":"Technology","industry_slug":"technology","sub_industry":"Computer & Network Security","sub_industry_slug":"computer_network_security","homepage":"http://www.saperix.com","primary_domain":"saperix.com","type":"CURATED","display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/overview/","rating_details":{"botnet_infections":{"name":"Botnet Infections","rating":700,"grade":"C","percentile":50,"grade_color":"#ecb870","category":"Compromised Systems","category_order":0,"beta":false,"order":0,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/compromised-systems/?filter=Botnet%20Infections"},"spam_propagation":{"name":"Spam Propagation","rating":820,"grade":"A","percentile":100,"grade_color":"#2c4d7f","category":"Compromised Systems","category_order":0,"beta":false,"order":1,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/compromised-systems/?filter=Spam%20Propagation"},"malware_servers":{"name":"Malware Servers","rating":820,"grade":"A","percentile":100,"grade_color":"#2c4d7f","category":"Compromised Systems","category_order":0,"beta":false,"order":2,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/compromised-systems/?filter=Malware%20Servers"},"unsolicited_comm":{"name":"Unsolicited Communications","rating":820,"grade":"A","percentile":100,"grade_color":"#2c4d7f","category":"Compromised Systems","category_order":0,"beta":false,"order":3,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/compromised-systems/?filter=Unsolicited%20Communications"},"potentially_exploited":{"name":"Potentially Exploited","rating":570,"grade":"F","percentile":14,"grade_color":"#b24053","category":"Compromised Systems","category_order":0,"beta":false,"order":4,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/compromised-systems/?filter=Potentially%20Exploited"},"spf":{"name":"SPF","rating":770,"grade":"B","percentile":81,"grade_color":"#526d96","category":"Diligence","category_order":1,"beta":false,"order":5,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=spf"},"dkim":{"name":"DKIM","rating":700,"grade":"C","percentile":55,"grade_color":"#ecb870","category":"Diligence","category_order":1,"beta":false,"order":6,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=dkim"},"ssl_certificates":{"name":"SSL Certificates","rating":760,"grade":"B","percentile":77,"grade_color":"#526d96","category":"Diligence","category_order":1,"beta":false,"order":7,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=certificate"},"ssl_configurations":{"name":"SSL Configurations","rating":680,"grade":"C","percentile":48,"grade_color":"#ecb870","category":"Diligence","category_order":1,"beta":false,"order":8,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=ssl"},"open_ports":{"name":"Open Ports","rating":760,"grade":"B","percentile":77,"grade_color":"#526d96","category":"Diligence","category_order":1,"beta":false,"order":9,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx3/diligence-details/?filter=open_port"},"application_security":{"name":"Web Application Headers","rating":480,"grade":"F","percentile":6,"grade_color":"#b24053","category":"Diligence","category_order":1,"beta":false,"order":10,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=http_headers"},"patching_cadence":{"name":"Patching Cadence","rating":710,"grade":"C","percentile":59,"grade_color":"#ecb870","category":"Diligence","category_order":1,"beta":false,"order":11,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=pc"},"insecure_systems":{"name":"Insecure Systems","rating":620,"grade":"D","percentile":34,"grade_color":"#c77481","category":"Diligence","category_order":1,"beta":false,"order":12,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=insecure_sys"},"server_software":{"name":"Server Software","rating":810,"grade":"A","percentile":99,"grade_color":"#2c4d7f","category":"Diligence","category_order":1,"beta":false,"order":13,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=server_software"},"desktop_software":{"name":"Desktop Software","rating":540,"grade":"F","percentile":14,"grade_color":"#b24053","category":"Diligence","category_order":1,"beta":false,"order":14,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=endpoint_pc"},"mobile_software":{"name":"Mobile Software","rating":590,"grade":"D","percentile":23,"grade_color":"#c77481","category":"Diligence","category_order":1,"beta":false,"order":15,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=endpoint_mobile"},"dnssec":{"name":"DNSSEC","rating":300,"grade":"F","percentile":0,"grade_color":"#b24053","category":"Diligence","category_order":1,"beta":true,"order":16,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=dnssec"},"mobile_application_security":{"name":"Mobile Application Security","rating":"N/A","grade":"N/A","percentile":"N/A","grade_color":"#495057","category":"Diligence","category_order":1,"beta":true,"order":17,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/diligence-details/?filter=mobile_appsec"},"file_sharing":{"name":"File Sharing","rating":550,"grade":"F","percentile":11,"grade_color":"#b24053","category":"User Behavior","category_order":2,"beta":false,"order":18,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/user-behavior"},"data_breaches":{"name":"Security Incidents","rating":810,"grade":"A","percentile":90,"grade_color":"#2c4d7f","category":"Public Disclosures","category_order":3,"beta":false,"order":19,"display_url":"https://service.bitsighttech.com/app/company/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/rating-details/?vector=news"}},"ratings":[{"rating_date":"2022-10-24","rating":470,"range":"Basic","rating_color":"#b24053"},{"rating_date":"2022-10-23","rating":500,"range":"Basic","rating_color":"#b24053"}],"search_count":11189,"subscription_type":"Total Risk Monitoring","sparkline":"https://api.bitsighttech.com/ratings/v1/companies/a940bxxx-xxxx-xxxx-xxxx-xxxxxxxxx/sparkline?size=small","subscription_type_key":"continuous_monitoring","subscription_end_date":null,"bulk_email_sender_status":"NONE","service_provider":false,"customer_monitoring_count":232,"available_upgrade_types":[],"has_company_tree":true,"has_preferred_contact":true,"is_bundle":false,"rating_industry_median":"below","primary_company":{"guid":"eed24xxx-xxxx-xxxx-xxxx-xxxxxxxxxx","name":"Saperix Corporate"},"permissions":{"can_manage_primary_company":true,"can_annotate":true,"can_view_ip_attributions":true,"can_view_infrastructure":true,"can_view_forensics":true,"can_download_company_report":true,"can_view_company_reports":true,"can_view_service_providers":true,"can_request_self_published_entity":true,"has_control":true},"is_primary":false,"security_grade":null,"in_spm_portfolio":true,"is_mycomp_mysubs_bundle":false,"company_features":[],"compliance_claim":{"trust_page":"https://saperix.com/compliance","certifications":[{"name":"SOC 2 Type 2","slug":"soc-2-type-2"},{"name":"ISO-27001","slug":"iso-27001"}]},"is_csp":false,"related_companies":[]}
```



#### List Company Vulnerabilities
List vulnerabilities related to the company in BitSight.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company Name|Specify the name of the company for which you want to return vulnerabilities.|True|String||
|Only High Confidence|If enabled, action will only return vulnerabilities with high confidence.|False|Boolean|true|
|Max Vulnerabilities To Return|Specify how many vulnerabilities you want to return. Default: 50.|False|String|50|



##### JSON Results
```json
{"stats":[{"id":"CVE-2xxx-xxx","name":"CVE-2xxx-xxxx","first_seen":"2021-07-15","event_count":4,"host_count":4,"confidence":"LOW"},{"id":"CVE-2xxx-xxxx","name":"CVE-2xxx-xxxx","first_seen":"2021-07-15","event_count":4,"host_count":4,"confidence":"LOW"}]}
```









## Connectors
#### BitSight - Alerts Connector
Pull information about alerts from BitSight. Note: dynamic list filter works with "trigger" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|siemplify_type|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|trigger|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the BitSight instance.|True|String|https://api.bitsighttech.com|
|API Key|API Key of the BitSight account. |True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the BitSight server is valid.|False|Boolean|true|
|Lowest Severity To Fetch|Lowest severity that needs to be used to fetch alerts. Possible values: Informational, Increase, Warn, Critical. If nothing is specified, the connector will ingest alerts with all severities.|False|String|WARN|
|Max Days Backwards|Number of days before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Alerts To Fetch|Specify the number of alerts to process per one connector iteration. Default: 20.|False|Integer|20|
|Use dynamic list as a blacklist|If enabled, dynamic lists will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.