
# FireEyeHX

The FireEye HX series is a threat prevention platform that helps drive faster, more accurate decisions about potential security incidents on endpoints.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|None|https://x.x.x.x:<port>|
|Username||True|String||
|Password||True|Password|*****|
|Verify SSL||False|Boolean||


#### Dependencies
| |
|-|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|six-1.17.0-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20260408-py3-none-any.whl|
|TIPCommon-1.0.11.1-py2.py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Acknowledge Alert Groups
Acknowledge alert groups handled by Siemplify to better sync between HX platform and Siemplify. Note - you can acknowledge alert groups only , not alerts, via the HX API.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Groups IDs|Specify the Alert Groups IDs you would like to Acknowledge.|True|String||
|Acknowledgment Comment|Specify the acknowledgment comment you would like to add to the relevant alert groups|False|String||
|Acknowledgment|Specify whether you would like to Acknowledge or Un-acknowledge the specified alert groups|True|List|Acknowledge|
|Limit|Specify the maximum amount of alert group listings coming back from the API, in the JSON result.|False|String||



##### JSON Results
```json
{"sort": {}, "offset": 0, "limit": 55, "entries": [{"last_alert": {"decorator_sources": [], "event_id": 880771, "event_type": "regKeyEvent", "md5values": [], "reported_at": "2020-12-10T09:27:08.735+00:00", "decorators": [], "agent": {"url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjxxx", "_id": "9GJe9n4Ynd5dFtZ8wCjxxx", "hostname": "HW-HOST-FXXX", "containment_state": "normal"}, "is_false_positive": false, "event_at": "2020-12-10T09:26:14.114+00:00", "source": "IOC", "matched_at": "2020-12-10T09:26:56+00:00", "decorator_statuses": [], "url": "/hx/api/v3/alerts/723", "_id": 723, "resolution": "ALERT", "condition": {"url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g==", "_id": "2npvcLf_arxPaH717hQZ9g=="}, "event_values": {"regKeyEvent/eventType": 1, "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe", "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=", "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger", "regKeyEvent/valueName": "Debugger", "regKeyEvent/pid": 8740, "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE", "regKeyEvent/username": "FIREEYE-LAB\\Administrator", "regKeyEvent/timestamp": "2020-12-10T09:26:14.114Z", "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe", "regKeyEvent/process": "reg.exe", "regKeyEvent/processPath": "C:\\Windows\\System32", "regKeyEvent/valueType": "REG_SZ"}}, "last_event_at": "2020-12-10T09:26:14.114Z", "_id": "e9f4d7baaa362d9d5d0b6e053ba0dxxx", "stats": {"events": 2}, "acknowledgement": {"comment": "asd", "comment_update_time": "2021-01-07T07:37:04.065Z", "acknowledged_by": "admin", "acknowledged": true, "acknowledged_time": "2021-01-07T07:37:37.144Z"}, "dispositions": [], "created_at": "2020-12-10T08:04:54.740Z", "grouped_by": {"detected_by": "ioc_engine", "host": {"url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjxxx", "_id": "9GJe9n4Ynd5dFtZ8wCjxxx", "hostname": "HW-HOST-FXXX", "primary_ip_address": "172.30.202.152"}, "condition_id": "2npvcLf_arxPaH717hQZ9g=="}, "generic_alert_label": null, "source": "IOC", "has_fp_disposition": false, "url": "/hx/api/v3/alert_groups/e9f4d7baaa362d9d5d0b6e053ba0dxxx", "file_full_path": "", "first_event_at": "2020-12-10T08:04:09.521Z", "assessment": "[Registry key event] EASE OF ACCESS BACKDOORS (METHODOLOGY)", "generic_alert_badge": null}], "query": {}, "total": 1}
```



#### Cancel Host Contain
Create a cancel host contain task on the FireEye HX server based on the Siemplify IP or Host Siemplify entities. Note: Action is not supported for Linux hosts by Fireye HX.
Timeout - 600 Seconds



#### Get Alerts in Alert Group
Get all the alerts found in the specified alert group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Group ID|Specify a comma-separated list of Alert Group IDs for which you want to retrieve alerts.|True|String||
|Limit|Specify the maximum amount of alerts listings coming back from the API, for the alert group. Default is 50.|False|String|50|



##### JSON Results
```json
[{"group_id": "e4d7c7bc5360b79xxxxxxxxxxxxxx", "indicator": {"category": "Mandiant", "display_name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)", "name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)", "url": "/hx/api/v3/indicators/mandiant/f0e49db2_1c28_4529_a426_732xxx92de7d", "signature": null, "_id": "f0e49db2-1c28-4529-a426-73251d92de7d", "uri_name": "f0e49db2-1c28-4529-a426-73251d92de7d"}, "event_id": 853899, "event_values": {"regKeyEvent/eventType": 1, "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe", "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=", "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger", "regKeyEvent/valueName": "Debugger", "regKeyEvent/pid": 8800, "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE", "regKeyEvent/username": "FIREEYE-LAB\\Administrator", "regKeyEvent/timestamp": "2020-12-10T08:04:09.521Z", "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe", "regKeyEvent/process": "reg.exe", "regKeyEvent/processPath": "C:\\Windows\\System32", "regKeyEvent/valueType": "REG_SZ"}, "event_type": "regKeyEvent", "subtype": null, "reported_at": "2020-12-10T08:04:49.607Z", "decorators": [], "md5values": [], "appliance": {"_id": "86B7F11ACF8D"}, "agent": {"url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjxxx", "_id": "9GJe9n4Ynd5dFtZ8wCjxxx", "containment_state": "normal"}, "is_false_positive": false, "event_at": "2020-12-10T08:04:09.521Z", "source": "IOC", "matched_at": "2020-12-10T08:04:43.000Z", "decorator_statuses": [], "url": "/hx/api/v3/alerts/712", "_id": 712, "resolution": "ALERT", "condition": {"url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g==", "_id": "2npvcLf_arxPaH717hQZ9g=="}, "matched_source_alerts": []}, {"group_id": "e4d7c7bc5360b79xxxxxxxxxxxxxx", "indicator": {"category": "Mandiant", "display_name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)", "name": "EASE OF ACCESS BACKDOORS (METHODOLOGY)", "url": "/hx/api/v3/indicators/mandiant/f0e49db2_1c28_4529_a426_732xxx92de7d", "signature": null, "_id": "f0e49db2-1c28-4529-a426-73251d92de7d", "uri_name": "f0e49db2-1c28-4529-a426-73251d92de7d"}, "event_id": 880771, "event_values": {"regKeyEvent/eventType": 1, "regKeyEvent/text": "C:\\Windows\\System32\\cmd.exe", "regKeyEvent/value": "QwA6AFwAVwBpAG4AZABvAHcAcwBcAFMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUAAAA=", "regKeyEvent/path": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe\\Debugger", "regKeyEvent/valueName": "Debugger", "regKeyEvent/pid": 8740, "regKeyEvent/hive": "HKEY_LOCAL_MACHINE\\SOFTWARE", "regKeyEvent/username": "FIREEYE-LAB\\Administrator", "regKeyEvent/timestamp": "2020-12-10T09:26:14.114Z", "regKeyEvent/keyPath": "Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe", "regKeyEvent/process": "reg.exe", "regKeyEvent/processPath": "C:\\Windows\\System32", "regKeyEvent/valueType": "REG_SZ"}, "event_type": "regKeyEvent", "subtype": null, "reported_at": "2020-12-10T09:27:08.735Z", "decorators": [], "md5values": [], "appliance": {"_id": "86B7F11ACF8D"}, "agent": {"url": "/hx/api/v3/hosts/9GJe9n4Ynd5dFtZ8wCjxxx", "_id": "9GJe9n4Ynd5dFtZ8wCjxxx", "containment_state": "normal"}, "is_false_positive": false, "event_at": "2020-12-10T09:26:14.114Z", "source": "IOC", "matched_at": "2020-12-10T09:26:56.000Z", "decorator_statuses": [], "url": "/hx/api/v3/alerts/723", "_id": 723, "resolution": "ALERT", "condition": {"url": "/hx/api/v3/conditions/2npvcLf_arxPaH717hQZ9g==", "_id": "2npvcLf_arxPaH717hQZ9g=="}, "matched_source_alerts": []}]
```



#### Get Host Alert Groups
List alert groups related to a host in FireEye HX. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Acknowledgment Filter|Specify whether you want to return all of the alert groups or only acknowledged/unacknowledged.|False|List|ALL|
|Max Alert Groups To Return|Specify how many Alert Groups to return per entity. Default: 20.|False|String|20|



##### JSON Results
```json
[{"EntityResult": [{"_id": "1f9e59316ca218543cb39xxxxxxxxxx", "assessment": "[Heur.BZC.WBO.Pantera.61.053FABD1]", "file_full_path": "C:\\Windows\\System32\\Tasks\\GameOver", "first_event_at": "2021-07-14T13:02:01.488Z", "last_event_at": "2021-07-14T13:02:01.488Z", "dispositions": [], "source": "MAL", "has_fp_disposition": false, "last_alert": {"_id": 844, "agent": {"_id": "JS2asEbMWGgfxxxxxxxxxx", "url": "/hx/api/v3/hosts/JS2asEbMWGgfxT0aHVu034", "hostname": "FireEye-Domain", "containment_state": "normal"}, "event_at": "2021-07-14T13:02:01.488+00:00", "matched_at": "2021-07-14T13:02:01.488+00:00", "reported_at": "2021-07-14T13:02:06.256+00:00", "source": "MAL", "resolution": "QUARANTINED", "decorators": [], "md5values": ["9a3420f24c33dbf3d05ab7daxxxxxxxxx"], "decorator_sources": [], "decorator_statuses": [], "url": "/hx/api/v3/alerts/844", "condition": null, "event_id": null, "event_type": null, "event_values": {"system-data": {"xmlns": "http://www.fireeye.com/antimalware-alert", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation": "http://www.fireeye.com/antimalware-alert AM-alert.xsd", "alert-version": "3", "correlation-id": "ca419bd2-0f1f-417e-a0e4-xxxxxxxxxxx", "timestamp": "2021-07-14T13:02:01.488Z", "product-version": "32.36.0", "engine-version": "11.0.1.19", "content-version": "7.89160", "mg-engine-version": "32.30.0.8460", "mg-content-version": "25", "whitelist-schema-version": "1.0.0", "whitelist-content-version": "1.32.5"}, "os-details": {"$": {"name": "windows", "version": "10.0.14393", "patch": "0", "os-arch": "64-bit", "os-language": "en-US"}}, "scan-type": "oas", "scanned-object": {"scanned-object-type": "file-event", "file-event": {"file-path": "C:\\Windows\\System32\\Tasks\\GameOver", "actor-process": {"pid": "2416", "path": "C:\\Windows\\System32\\MRT.exe", "user": {"username": "SYSTEM", "domain": "NT AUTHORITY"}}, "sub-type": "FILE_OPERATION_OPENED"}}, "detections": {"detection": [{"engine": {"engine-type": "av", "engine-version": "11.0.1.19", "content-version": "7.89160"}, "infected-object": {"object-type": "file", "file-object": {"file-path": "C:\\Windows\\System32\\Tasks\\GameOver", "inner-file-path": "(Exec)", "original-file-name": "", "container": "true", "packed": "false", "hidden": "false", "system-file": "false", "read-only": "false", "temporary": "false", "md5sum": "9a3420f24c33dbf3d05ab7xxxxxxx", "sha1sum": "cb181a46b6f65176464e175945f6fbxxxxxxxx", "sha256sum": "82da24a6b54bce022f0bf9e5baee0337df1f686d6332524a67241xxxxxxxx", "size-in-bytes": "3670", "creation-time": "2020-05-26T07:24:41.764Z", "modification-time": "2021-07-01T09:46:48.958Z", "access-time": "2020-05-26T07:24:41.764Z"}}, "infection": {"confidence-level": "high", "infection-type": "malware", "infection-name": "Heur.BZC.WBO.Pantera.61.053FABD1"}, "action": {"actioned-object": {"object-type": "file", "file-object": {"file-path": "C:\\Windows\\System32\\Tasks\\GameOver", "inner-file-path": "(Exec)", "original-file-name": "", "container": "true", "packed": "false", "hidden": "false", "system-file": "false", "read-only": "false", "temporary": "false", "md5sum": "9a3420f24c33dbf3d05ab7xxxxxxxx", "sha1sum": "cb181a46b6f65176464e175945f6xxxxxxxx", "sha256sum": "82da24a6b54bce022f0bf9e5baee0337df1f686d6332524a6724xxxxxxxxx", "size-in-bytes": "3670", "creation-time": "2020-05-26T07:24:41.764Z", "modification-time": "2021-07-01T09:46:48.958Z", "access-time": "2020-05-26T07:24:41.764Z"}}, "requested-action": "clean", "applied-action": "quarantine", "result": "success", "error": "0", "reboot-required": "false"}}]}, "scan-statistics": {"total-scan-time-in-ms": "12455"}}, "is_false_positive": false}, "generic_alert_badge": null, "generic_alert_label": null, "stats": {"events": 1}, "url": "/hx/api/v3/alert_groups/1f9e59316ca218543cb39fbxxxxxxxxx", "created_at": "2021-07-14T13:02:15.669Z", "acknowledgement": {"acknowledged": false, "acknowledged_by": null, "acknowledged_time": null, "comment": null, "comment_update_time": null}, "grouped_by": {"md5sum": "9a3420f24c33dbf3d05axxxxxxxxxx", "file-path": "C:\\Windows\\System32\\Tasks\\GameOver", "infection-name": "Heur.BZC.WBO.Pantera.61.053FABD1", "detected_by": "malware_file_access_scan", "host": {"_id": "JS2asEbMWGgfxTxxxxxxxx", "url": "/hx/api/v3/hosts/JS2asEbMWGgfxxxxxxxxx", "hostname": "FireEye-Domain", "primary_ip_address": "172.xx.xxx.xxx"}}}], "Entity": "FireEye-Domain"}]
```



#### Get List of File Acquisitions For Host
Get list of file acquisitions requested for host from FireEye HX server. Action works on Host or IP Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search Term|Searches all file acquisitions for hosts connected to the FireEye HX server. The search_term can be any condition value.|False|String|None|
|Limit|How many records action should return, for example, 100.|False|String|None|
|Filter Field|Lists only results with the specified field value, results can be filtered by external correlation identifier (external_id).|False|String|None|



##### JSON Results
```json
[{"EntityResult": [{"comment": "", "zip_passphrase": "unzip-me", "indicator": {"url": null, "_id": "FqNP4ybCdrlfVqG3lrCvRP"}, "request_actor": {"username": "admin", "_id": 1000}, "request_time": "2020-06-01T08:43:14.000Z", "finish_time": "2020-06-01T08:46:39.156Z", "_revision": "20200601084639156575147403", "error_message": "The acquisition completed with issues.", "req_use_api": false, "alert": {"url": null, "_id": "FqNP4ybCdrlfVqG3lrCvRP"}, "url": "/hx/api/v3/acqs/files/9", "state": "COMPLETE", "host": {"url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP", "_id": "FqNP4ybCdrlfVqG3lrCvRP"}, "req_filename": "reg.exe", "req_path": "C:\\Windows\\System32", "_id": 9, "external_id": null, "condition": {"url": null, "_id": "FqNP4ybCdrlfVqG3lrCvRP"}, "md5": "601bddf7691c5af626a5719f1d7e35f1"}], "Entity": "PC-01"}]
```



#### Is Contain Malware Alerts
Check if malware alerts are listed for provided Siemplify Host or IP entities on FireEye HX server.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"alerting_conditions": 10, "exploit_alerts": 0, "acqs": 4, "malware_false_positive_alerts": 0, "alerts": 10, "exploit_blocks": 0, "false_positive_alerts": 0, "malware_cleaned_count": 0, "malware_alerts": 0, "false_positive_alerts_by_source": {}, "generic_alerts": 0, "malware_quarantined_count": 0}, "Entity": "PC-01"}]
```



#### Get Alert Group Details
Get full alert group details for provided Alert Group by it’s ID.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Group ID|Specify a comma-separated list of Alert Group IDs for which you want to retrieve details.|True|String||



##### JSON Results
```json
[{"last_alert": {"decorator_sources": [], "event_id": 207, "event_type": "processEvent", "md5values": ["05cf3ce225b05b669e3118092f4c8eab"], "reported_at": "2020-12-18T14:03:18.856+00:00", "decorators": [], "agent": {"url": "/hx/api/v3/hosts/QKQ0SinOZUbehz5AgFXxxx", "_id": "QKQ0SinOZUbehz5AgFXxxx", "hostname": "HW-HOST-xxx", "containment_state": "normal"}, "is_false_positive": false, "event_at": "2020-08-06T06:32:55.761+00:00", "source": "IOC", "matched_at": "2020-08-06T06:37:55+00:00", "decorator_statuses": [], "url": "/hx/api/v3/alerts/729", "_id": 729, "resolution": "ALERT", "condition": {"url": "/hx/api/v3/conditions/yirelRwhiuXlF0bQhTL4GA==", "_id": "yirelRwhiuXlF0bQhTL4GA=="}, "event_values": {"processEvent/processCmdLine": "REG  ADD HKCU\\Environment /f /v UserInitMprLogonScript /t REG_MULTI_SZ /d \"C:\\TMP\\mim.exe sekurlsa::LogonPasswords > C:\\TMP\\o.txt\"", "processEvent/parentPid": 9456, "processEvent/md5": "05cf3ce225b05b669e3118092f4c8eab", "processEvent/processPath": "C:\\Windows\\System32\\reg.exe", "processEvent/parentProcess": "cmd.exe", "processEvent/timestamp": "2020-08-06T06:32:55.761Z", "processEvent/startTime": "2020-08-06T06:32:55.761Z", "processEvent/process": "reg.exe", "processEvent/username": "FIREEYE-LAB\\Administrator", "processEvent/pid": 10356, "processEvent/parentProcessPath": "C:\\Windows\\System32\\cmd.exe", "processEvent/eventType": "start"}}, "last_event_at": "2020-08-06T06:32:55.761Z", "_id": "622d3688031aa40faa4bd86028841276", "stats": {"events": 1}, "acknowledgement": {"comment": "test comment", "comment_update_time": "2020-12-22T14:03:54.440Z", "acknowledged_by": "test2", "acknowledged": true, "acknowledged_time": "2020-12-22T14:03:54.440Z"}, "dispositions": [], "created_at": "2020-12-18T14:03:24.535Z", "grouped_by": {"detected_by": "ioc_engine", "host": {"url": "/hx/api/v3/hosts/QKQ0SinOZUbehz5AgFXxxx", "_id": "QKQ0SinOZUbehz5AgFXxxx", "hostname": "HW-HOST-xxx", "primary_ip_address": "172.30.202.55"}, "condition_id": "yirelRwhiuXlF0bQhTL4GA=="}, "generic_alert_label": null, "source": "IOC", "has_fp_disposition": false, "url": "/hx/api/v3/alert_groups/622d3688031aa40faa4bd86028841276", "file_full_path": "C:\\Windows\\System32\\reg.exe", "first_event_at": "2020-08-06T06:32:55.761Z", "assessment": "[Process reg.exe started] MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)", "generic_alert_badge": null}]
```



#### Get Host Info
Enrich Siemplify Host or IP entities based on the information from the FireEye HX.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"last_alert": {"url": "/hx/api/v3/alerts/254", "_id": 254}, "domain": "EXAMPLE-COM", "last_exploit_block_timestamp": null, "containment_state": "normal", "timezone": "\u05e9\u05e2\u05d5\u05df \u05e7\u05d9\u05e5 \u05d9\u05e8\u05d5\u05e9\u05dc\u05d9\u05dd", "gmt_offset_seconds": 10800, "initial_agent_checkin": "2020-05-29T10:11:12.022Z", "stats": {"alerting_conditions": 10, "exploit_alerts": 0, "acqs": 4, "malware_false_positive_alerts": 0, "alerts": 10, "exploit_blocks": 0, "false_positive_alerts": 0, "malware_cleaned_count": 0, "malware_alerts": 0, "false_positive_alerts_by_source": {}, "generic_alerts": 0, "malware_quarantined_count": 0}, "primary_mac": "00-50-56-11-22-33", "hostname": "HW-HOST-025", "primary_ip_address": "1.1.1.1", "last_audit_timestamp": "2020-06-01T09:10:38.752Z", "last_alert_timestamp": "2020-06-01T08:02:30.817+00:00", "containment_queued": false, "sysinfo": {"url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP/sysinfo"}, "last_exploit_block": null, "reported_clone": false, "url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP", "excluded_from_containment": false, "last_poll_timestamp": "2020-06-01T09:10:36.000Z", "last_poll_ip": "1.1.1.1", "containment_missing_software": false, "_id": "FqNP4ybCdrlfVqG3lrCvRP", "os": {"kernel_version": null, "platform": "win", "patch_level": null, "bitness": "64-bit", "product_name": "Windows 10 Pro"}, "agent_version": "32.30.0"}, "Entity": "PC-01"}]
```



#### Get Indicator
Get information on specific Indicator from FireEye HX server.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Indicator Category|Specify indicator category uri_name value. uri_name can be found by running “Get Indicators” action. |True|String|None|
|Indicator Name|Specify indicator uri_name value. uri_name can be found by running “Get Indicators” action. |True|String|None|



##### JSON Results
```json
{"category": {"url": "/hx/api/v3/indicator_categories/mandiant_unrestricted", "_id": 7, "uri_name": "mandiant_unrestricted", "name": "Mandiant Unrestricted Intel", "share_mode": "unrestricted"}, "display_name": "FIREEYE END2END TEST", "description": "IOC used for testing HX appliances and content packages to ensure that things work end to end", "create_actor": {"username": "mandiant", "_id": 3}, "active_since": "2020-05-28T13:08:08.513Z", "url": "/hx/api/v3/indicators/mandiant_unrestricted/2b4753b0_9972_477e_ba16_1a7c29058cee", "_revision": "20200528130929238120103414", "create_text": "General_Windows_unrestricted_2020.05.270833", "created_by": "General_Windows_unrestricted_2020.05.270833", "update_actor": {"username": "mandiant", "_id": 3}, "meta": null, "signature": null, "platforms": ["win", "osx", "linux"], "stats": {"source_alerts": 0, "alerted_agents": 1, "active_conditions": 7}, "_id": "2b4753b0-9972-477e-ba16-1a7c29058cee", "uri_name": "2b4753b0-9972-477e-ba16-1a7c29058cee", "name": "FIREEYE END2END TEST"}
```



#### Contain Host
Create contain host task on the FireEye HX server based on the Siemplify IP or Host Siemplify entities. Note: Action is not supported for Linux hosts by Fireye HX.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Approve Containment|Specify if containment request for host should be automatically approved to create contain host task on FireEye HX server. If not approved automatically, containment request can be approved in FireEye HX web console.|False|Boolean|false|



#### Get Indicators
Get information on indicators of compromise (IOC) from FireEye HX server based on provided search parameters.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Indicator Category|The indicator category.|False|String|None|
|Search Term|The search term can be any name, category, signature, source, or condition value.|False|String|None|
|Limit|How many indicators action should return, for example, 100.|False|String|None|
|Share Mode|Filter indicators based on specific share mode. Available values: any, restricted, unrestricted, visible.|False|List|any|
|Sort By Field|Sorts the results by the specified field in ascending order.|False|String|None|
|Created by|Filter indicators based on author.|False|String|None|
|Has associated alerts|Specify if only indicators, which have associated alerts should be returned.|False|Boolean|None|



##### JSON Results
```json
[{"category": {"url": "/hx/api/v3/indicator_categories/mandiant_unrestricted", "_id": 7, "uri_name": "mandiant_unrestricted", "name": "Mandiant Unrestricted Intel", "share_mode": "unrestricted"}, "display_name": "FIREEYE END2END TEST", "description": "IOC used for testing HX appliances and content packages to ensure that things work end to end", "create_actor": {"username": "mandiant", "_id": 3}, "active_since": "2020-05-28T13:08:08.513Z", "url": "/hx/api/v3/indicators/mandiant_unrestricted/2b4753b0_9972_477e_ba16_1a7c29058cee", "_revision": "20200528130929238120103414", "create_text": "General_Windows_unrestricted_2020.05.270833", "created_by": "General_Windows_unrestricted_2020.05.270833", "update_actor": {"username": "mandiant", "_id": 3}, "meta": null, "signature": null, "platforms": ["win", "osx", "linux"], "stats": {"source_alerts": 0, "alerted_agents": 1, "active_conditions": 7}, "_id": "2b4753b0-9972-477e-ba16-1a7c29058cee", "uri_name": "2b4753b0-9972-477e-ba16-1a7c29058cee", "name": "FIREEYE END2END TEST"}]
```



#### Get Alerts
Get FireEye HX alerts based on provided Siemplify entity and search conditions. Action works on Host or IP Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Limit|How many alerts action should return, for example, 100.|False|String||
|Has Share Mode|Filter alerts that were triggered from indicators with specific share mode. Available values: any, restricted, unrestricted.|False|List|any|
|Alert Resolution Status|Filter alerts based on alert resolution status. Available values: any, active_threat, alert, block, partial_block.|False|List|any|
|Alert reported in last x hours|Filter alerts reported in last x hours, for example last 4 hours.|False|String|None|
|Alert Source|Source of alert. Available values: any, exd (exploit detection), mal (malware alert), ioc (indicator of compromise).|False|List|any|
|Alert ID|Return specific alert by alert identifier.|False|String|None|



##### JSON Results
```json
[{"EntityResult": [{"group_id": "e4d7c7bc5360b79xxxxxxxxxxxxxx", "indicator": {"category": "Mandiant", "display_name": "MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)", "name": "MIMIKATZ SUSPICIOUS PROCESS ARGUMENTS (METHODOLOGY)", "url": "/hx/api/v3/indicators/mandiant/b7eae353_be50_44cf_8773_7067e9c66d7b", "signature": null, "_id": "b7eae353-be50-44cf-8773-7067e9c66d7b", "uri_name": "b7eae353-be50-44cf-8773-7067e9c66d7b"}, "event_id": 12880, "event_values": {"processEvent/processCmdLine": "at  13:00 \"C:\\TMP\\mim.exe sekurlsa::LogonPasswords > C:\\TMP\\o.txt\"", "processEvent/parentPid": 4832, "processEvent/md5": "e2a9c62b47f64525f7eb0cb8d637ff90", "processEvent/processPath": "C:\\Windows\\System32\\at.exe", "processEvent/parentProcess": "cmd.exe", "processEvent/timestamp": "2020-05-29T10:21:03.419Z", "processEvent/startTime": "2020-05-29T10:21:03.419Z", "processEvent/process": "at.exe", "processEvent/username": "DOMAIN-COM\\Administrator", "processEvent/pid": 7332, "processEvent/parentProcessPath": "C:\\Windows\\System32\\cmd.exe", "processEvent/eventType": "start"}, "event_type": "processEvent", "subtype": null, "reported_at": "2020-05-29T10:24:05.410Z", "decorators": [], "md5values": ["e2a9c62b47f64525f7eb0cb8d637ff90"], "appliance": {"_id": "86B7F11ACF8D"}, "agent": {"url": "/hx/api/v3/hosts/FqNP4ybCdrlfVqG3lrCvRP", "_id": "FqNP4ybCdrlfVqG3lrCvRP", "containment_state": "normal"}, "is_false_positive": false, "event_at": "2020-05-29T10:21:03.419Z", "source": "IOC", "matched_at": "2020-05-29T10:23:22.000Z", "decorator_statuses": [], "url": "/hx/api/v3/alerts/88", "_id": 88, "resolution": "ALERT", "condition": {"url": "/hx/api/v3/conditions/yirelRwhiuXlF0bQhTL4GA==", "_id": "yirelRwhiuXlF0bQhTL4GA=="}, "matched_source_alerts": []}], "Entity": "PC-01"}]
```



#### Ping
Test connectivity to the FireEye HX server with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds









## Connectors
#### FireEye HX Alerts Connector
FireEye HX Alerts Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|event_type|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|FireEye HX Server API Root URL.|True|String|https://x.x.x.x:<port>|
|Username|FireEye HX user to authenticate with.|True|String||
|Password|FireEye HX user password to authenticate with.|True|Password|*****|
|Offset time in hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|24|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|Integer|25|
|Alert Type|Specify what FireEye HX alert types to ingest.  By default its set to active_threat to return alerts in ALERT and QUARANTINED/partial_block state. Other valid parameter is ALERT, which will return open alerts only.|False|String|active_threat|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Verify SSL|If specified, connector will check if FireEye HX is configured with valid SSL certificate. If certificate is not valid, connector will return error.|False|Boolean|true|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.