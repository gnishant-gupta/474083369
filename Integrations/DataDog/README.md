
# DataDog

Datadog is an essential monitoring platform for cloud applications. It brings together data from servers, containers, databases, and third-party services to make your stack entirely observable. These capabilities help DevOps teams avoid downtime, resolve performance issues, and ensure customers are getting the best user experience.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|API Key|True|Password|*****|
|APP Key|APP Key (Application Key)|True|Password|*****|


#### Dependencies
| |
|-|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|certifi-2025.6.15-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Get Event Details

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|The event id you want to retrieve|True|String||



##### JSON Results
```json
{"event": {"date_happened": 1614781413, "alert_type": "error", "resource": "/api/v1/events/<event_id>", "title": "Event Title", "url": "/event/event?id=<event_id>", "text": "", "tags": ["tag1", "tag2"], "id": "< event_id >", "priority": "normal", "host": "None", "device_name": "None", "payload": {"transition": {"trans_name": "Triggered", "trans_type": "alert"}, "monitor": {"created_at": 1614781411000, "name": "", "tags": [], "deleted": null, "templated_name": "", "org_id": 123456, "modified": 1614781411000, "options": {"notify_audit": false, "locked": false, "timeout_h": 0, "silenced": {}, "include_tags": true, "thresholds": {"critical": 50.0, "warning": 40.0}, "new_host_delay": 300, "queryConfig": {"logset": {"name": "*"}, "track": "logs", "timeRange": {"to": 1614767945471, "live": true, "from": 1614767045471}, "queryString": "", "indexes": ["*"], "queryIsFailed": false}, "notify_no_data": false, "enable_logs_sample": true, "groupby_simple_monitor": false, "renotify_interval": 0, "no_data_timeframe": 2, "aggregation": {"metric": "count", "type": "count", "groupBy": "tag_kube_namespace"}}, "query": "", "message": "", "type": "log alert", "id": 22222}, "text_only_message": "Namespace: Namespace", "states": {"dest_state": "Alert", "source_state": "OK"}, "avalanche_window": null, "result": {"group": "kube_namespace:kube_namespace", "display_logs_sample": {}, "result_ts": 1614781411, "rum_url": "", "trace_analytics_url": "", "state_counts": {"1": 1, "0": 0, "3": 0, "2": 0, "5": 0, "6": 0}, "avalanche": false, "groups": {"kube_namespace:kub_namespace": {"status": 1, "latest_ts": 0}}, "logs_url": "", "group_key": "kube_namespace", "state_id": 1, "result_id": 0, "num_groups": 1, "metadata": {"to_js_ts": 1614781413000, "monitor_id": 111111, "snap_url": "", "from_js_ts": 1614738213000, "alert_url": "/", "process_url": "", "is_usertest": true}}, "alert_cycle_key": 0}}}
```



#### Get Logs
Get logs by a given Kubernetes Namespace.
For more information: https://docs.datadoghq.com/api/latest/logs/#get-a-list-of-logs
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|End Time|The end time which you want to retrieve the logs to.|True|String|2020-02-02T02:02:02Z|
|Start Time|The start time which you want to retrieve the logs from.|True|String|2020-02-02T02:02:02Z|
|Namespace|The Kubernetes namespace you would like to get logs for.|True|String|name_space1, name_space2|



##### JSON Results
```json
{"NameSpace: kube-system": {"status": "done", "nextLogId": "1111111", "logs": [{"content": {"timestamp": "2021-01-01T02:02:01.894Z", "host": "i-11111", "message": "The messasge content", "service": "snapshot-controller", "tags": ["image_name:name", "container_name:name", "source:source name", "kube_namespace:kube-system"]}, "id": "123456789"}, {"content": {"timestamp": "2021-01-01T02:02:01.894Z", "host": "i-22222", "message": "The messasge content", "service": "snapshot-controller", "tags": ["image_name:name"]}, "id": "123456789"}], "requestId": "aaaabbbb11112222"}}
```



#### Get Beautiful Metric
Get metrics timeseries points of a given query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Series|The timeseries points you want to analyze|True|Code|{}|



##### JSON Results
```json
{"unit": "cpu", "aggregation_by": "avg", "start_time": 1607040000000, "end_time": 1610668799000, "full_timeseries_points_list": [[1607040000000.0, 0.008314899947867048], [1607644800000.0, 0.04104587218344665], [1608249600000.0, 0.050120122766495044], [1608854400000.0, 0.007100906014306722], [1609459200000.0, 0.007120135038524259], [1610064000000.0, 0.0063300259286052755]], "sum_of_the_metric_values": 0.120031961879245, "average_of_the_metric_values": 0.02000532697987417, "min_of_the_metric_values": 0.0063300259286052755, "max_of_the_metric_values": 0.050120122766495044, "expression": "avg:kubernetes.cpu.system.total{kube_namespace:x,pod_name:y}"}
```



#### Get Metric Snapshot Graph
Get metric snapshot graph for a given query.
For more information: https://docs.datadoghq.com/api/v1/snapshots/
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|The metric query which you want to get the snapshot graph of.For example: avg:aws.rds.cpuutilization{cloud_env:production}by{dbinstanceidentifier}|True|String|avg:aws.rds.cpuutilization{cloud_env:production}by{dbinstanceidentifier}|
|Start Time|The start time of the metric snapshot graph in Unixtime.|True|String|1400000470|
|End Time|The end time of the metric snapshot graph in Unixtime.|True|String|1610557457|



##### JSON Results
```json
{"graph_def": "string", "metric_query": "string", "snapshot_url": "https://app.datadoghq.com/s/f12345678/aaa-bbb-ccc"}
```



#### Get Metric Timeseries Points
Get metrics timeseries points of a given query.
For more information: https://docs.datadoghq.com/api/latest/snapshots/
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|End Time|The end time of the timeseries points in Unixtime.|True|String|1610557457|
|Start Time|The start time of the timeseries points in Unixtime.|True|String|1400000470|
|Query|The metric query which you want to get the timeseries points.For example: |True|String|avg:aws.rds.dbload{dbinstanceidentifier:db}by{dbinstanceidentifier}|



##### JSON Results
```json
{"from_date": "integer", "group_by": [], "message": "string", "query": "string", "res_type": "time_series", "series": [{"aggr": "avg", "display_name": "system.cpu.idle", "end": "integer", "expression": "system.cpu.idle{host:foo,env:test}", "interval": "integer", "length": "integer", "metric": "system.cpu.idle", "pointlist": [1575317847, 0.5], "scope": "host:foo,env:test", "start": "integer", "unit": [{"family": "time", "name": "minute", "plural": "minutes", "scale_factor": 60, "short_name": "min"}]}], "status": "ok", "to_date": "integer"}
```



#### Get Pod Metric
Gets a Pod metric (CPU, Memory and processes).
For more information about Metrics: https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-points
For more information about Kubernetes metrics: https://docs.datadoghq.com/agent/kubernetes/data_collected/
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Pod Name|The Pod Namespace|True|String|pod_namespace|
|End Time|The end time of the Pod metric in Unixtime.|True|String|1610557457|
|Start Time|The start time of the Pod metric in Unixtime.|True|String|1507040000|



##### JSON Results
```json
{"pod_name_X": {"pod_CPU": {"status": "ok", "res_type": "time_series", "from_date": 1507040000000, "series": [{"end": 1610668799000, "attributes": {}, "metric": "kubernetes.cpu.system.total", "interval": 604800, "tag_set": ["kube_namespace:y", "pod_name:x"], "start": 1602201600000, "length": 14, "query_index": 0, "aggr": "avg", "scope": "kube_namespace:y,pod_name:x", "pointlist": [[1602201600000.0, 0.0003853833283493937], [1602806400000.0, 0.00036236030051059264], [1603411200000.0, 0.0004022896314672298], [1604016000000.0, 0.00036836003994138866], [1604620800000.0, 0.00039237702930315773]], "expression": "avg:kubernetes.cpu.system.total{kube_namespace:y,pod_name:x}", "unit": [{"family": "cpu", "scale_factor": 1.0, "name": "core", "short_name": null, "plural": "cores", "id": 31}, null], "display_name": "kubernetes.cpu.system.total"}], "to_date": 1610557457000, "resp_version": 1, "query": "avg:kubernetes.cpu.system.total{pod_name:x}by{pod_name,kube_namespace}", "message": "", "group_by": ["kube_namespace", "pod_name"]}, "pod_memory": {"status": "ok", "res_type": "time_series", "from_date": 1507040000000, "series": [{"end": 1610668799000, "attributes": {}, "metric": "kubernetes.memory.usage_pct", "interval": 604800, "tag_set": ["kube_namespace:y", "pod_name:x"], "start": 1602201600000, "length": 14, "query_index": 0, "aggr": "avg", "scope": "kube_namespace:y,pod_name:x", "pointlist": [[1602201600000.0, 0.17388684940859045], [1602806400000.0, 0.20004428429430668], [1603411200000.0, 0.18134797875370298], [1604016000000.0, 0.25646502505858065], [1604620800000.0, 0.2630635437274736]], "expression": "avg:kubernetes.memory.usage_pct{kube_namespace:y,pod_name:x}", "unit": [{"family": "percentage", "scale_factor": 100.0, "name": "fraction", "short_name": null, "plural": "fractions", "id": 16}, null], "display_name": "kubernetes.memory.usage_pct"}], "to_date": 1610557457000, "resp_version": 1, "query": "avg:kubernetes.memory.usage_pct{pod_name:x}by{pod_name,kube_namespace}", "message": "", "group_by": ["kube_namespace", "pod_name"]}, "pod_processes": {"meta": {"page": {"after": "abcdef", "size": 6}}, "data": [{"type": "process", "id": "123456", "attributes": {"cmdline": "", "timestamp": "2021-01-21T13:50:33", "start": "2020-10-24T04:28:57", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-12345", "tags": [""]}}, {"type": "process", "id": "123456", "attributes": {"cmdline": "", "timestamp": "2021-01-21T13:45:03", "start": "2020-12-23T12:35:52", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-123456789", "tags": [""]}}, {"type": "process", "id": "123456", "attributes": {"cmdline": "", "timestamp": "2021-01-21T13:50:33", "start": "2020-12-23T13:23:30", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-123456", "tags": [""]}}, {"type": "process", "id": "123456", "attributes": {"cmdline": "", "timestamp": "2021-01-21T13:42:03", "start": "2020-12-29T15:57:01", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-123456", "tags": [""]}}, {"type": "process", "id": "123456", "attributes": {"cmdline": ".log", "timestamp": "2021-01-21T13:44:33", "start": "2020-12-29T18:12:04", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-123456", "tags": [""]}}, {"type": "process", "id": "123456", "attributes": {"cmdline": "", "timestamp": "2021-01-21T13:43:03", "start": "2020-12-30T10:57:17", "user": "root", "pid": 1234, "ppid": 1111, "host": "i-123456", "tags": [""]}}]}}}
```



#### Get RDS Metric
Gets AWS RDS metrics for a given Database instance identifier (CPU, memory and storage)
For more information about Metrics: https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-points
For more information about AWS RDS metrics: https://docs.datadoghq.com/integrations/amazon_rds/?tab=standard
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|End Time|The end time of the Pod metric in Unixtime.|True|String|1610557457|
|Start Time|The start time of the RDS metric in Unixtime.|True|String|1507040000|
|Database Instance Identifier|The identifier of the data base which you want to get the metrics to.identifier1, identifier2|True|String|identifier1|



##### JSON Results
```json
{"founded_db_instance_identifier": {"db_instance_identifier: db_instance": {"db_CPU": {"status": "ok", "res_type": "time_series", "from_date": 1507040000000, "series": [{"end": 1587686399000, "attributes": {}, "metric": "aws.rds.cpuutilization", "interval": 604800, "tag_set": ["dbinstanceidentifier:db_instance"], "start": 1587081600000, "length": 1, "query_index": 0, "aggr": "avg", "scope": "dbinstanceidentifier:db_instance", "pointlist": [[1587081600000.0, 2.742857142857143]], "expression": "avg:aws.rds.cpuutilization{dbinstanceidentifier:db_instance}", "unit": [{"family": "percentage", "scale_factor": 1.0, "name": "percent", "short_name": "%", "plural": "percent", "id": 17}, null], "display_name": "aws.rds.cpuutilization"}], "to_date": 1610557457000, "resp_version": 1, "query": "avg:aws.rds.cpuutilization{dbinstanceidentifier:db_instance}by{dbinstanceidentifier}", "message": "", "group_by": ["dbinstanceidentifier"]}, "db_memory": {"status": "ok", "res_type": "time_series", "from_date": 1507040000000, "series": [{"end": 1587686399000, "attributes": {}, "metric": "aws.rds.freeable_memory", "interval": 604800, "tag_set": ["dbinstanceidentifier:db_instance"], "start": 1587081600000, "length": 1, "query_index": 0, "aggr": "avg", "scope": "dbinstanceidentifier:db_instance", "pointlist": [[1587081600000.0, 5265705327.589744]], "expression": "avg:aws.rds.freeable_memory{dbinstanceidentifier:db_instance}", "unit": [{"family": "bytes", "scale_factor": 1.0, "name": "byte", "short_name": "B", "plural": "bytes", "id": 2}, null], "display_name": "aws.rds.freeable_memory"}], "to_date": 1610557457000, "resp_version": 1, "query": "avg:aws.rds.freeable_memory{dbinstanceidentifier:db_instance}by{dbinstanceidentifier}", "message": "", "group_by": ["dbinstanceidentifier"]}, "db_free_storage": {"status": "ok", "res_type": "time_series", "from_date": 1507040000000, "series": [{"end": 1587686399000, "attributes": {}, "metric": "aws.rds.free_storage_space", "interval": 604800, "tag_set": ["dbinstanceidentifier:db_instance"], "start": 1587081600000, "length": 1, "query_index": 0, "aggr": "avg", "scope": "dbinstanceidentifier:db_instance", "pointlist": [[1587081600000.0, 32846995456.0]], "expression": "avg:aws.rds.free_storage_space{dbinstanceidentifier:db_instance}", "unit": [{"family": "bytes", "scale_factor": 1.0, "name": "byte", "short_name": "B", "plural": "bytes", "id": 2}, null], "display_name": "aws.rds.free_storage_space"}], "to_date": 1610557457000, "resp_version": 1, "query": "avg:aws.rds.free_storage_space{dbinstanceidentifier:db_instance}by{dbinstanceidentifier}", "message": "", "group_by": ["dbinstanceidentifier"]}}}, "not_found_db_instance_identifier": []}
```



#### Ping
Test connectivity with DataDog
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Get Events
Get events from Datadog.
For more information: https://docs.datadoghq.com/api/v1/events/
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sources|The sources to retrieve the events from.For example in order to see events from the triggered monitor write: 'alert'  |True|String|alert|
|Start Time|The start time of the events in Unixtime.|True|String|1400000470|
|End Time|The end time of the events  in Unixtime.|True|String|1610557457|
|Priority|The priority of the events you want to retrieve. |False|List|all|
|Tags|A comma separated list of tags that will filter the list of monitors by scope.For example: 'monitor'.|False|String|monitor|
|Unaggregated|True- if you want to retrieve the full list of events.False - if you want to retrieve aggregated list of events.|False|Boolean|true|



##### JSON Results
```json
{"events": [{"date_happened": 1610487676, "alert_type": "error", "is_aggregate": false, "title": "[Triggered on {host:i-123456}] Node filesystem used in Percent i-123456", "url": "/event/event?id=1111111111", "text": "", "tags": ["monitor", "region:us-west-2", "security-group:y", "security-group:x"], "comments": [], "device_name": null, "priority": "normal", "source": "Monitor Alert", "host": "i-123456", "resource": "/api/v1/events/aaabbbccc111", "id": "aaabbbccc111"}, {"date_happened": 1610487676, "alert_type": "error", "is_aggregate": true, "title": "[Triggered on {host:i-123456}] Node filesystem used in Percent i-123456", "url": "/event/event?id=22222222", "text": "", "tags": ["monitor", "region:us-west-2"], "comments": [], "children": [{"date_happened": 1610487676, "alert_type": "error", "id": "22222222"}], "priority": "normal", "source": "Monitor Alert", "host": "i-123456", "resource": "/api/v1/events/2222222", "device_name": null, "id": 2222222}]}
```









## Connectors
#### DataDog Connector
Ingest events from DataDog by given filters(e.g. tags, priority)

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|API Key|True|Password|*****|
|APP Key|APP Key|True|Password|*****|
|Base URL|The Base url |True|String| https://api.datadoghq.com|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|True|String|event_name|
|Max Days Back|Max days back |True|Integer|7|
|Priority|The priority of the events you want to retrieve. Could be 'low', 'normal' or 'all'|False|String|all|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|30|
|Sources|The sources to retrieve the events from.For example in order to see events from the triggered monitor write: 'alert' .|True|String|alert|
|Tags|A comma separated list of tags that will filter the list of monitors by scope.For example: 'monitor'.|False|String|monitor|
|Unaggregated|True- if you want to retrieve the full list of events.False - if you want to retrieve aggregated list of events.|False|Boolean|true|





A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.