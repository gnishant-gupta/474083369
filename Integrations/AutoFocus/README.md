
# AutoFocus

AutoFocus contextual threat intelligence service accelerates analysis, correlation and prevention workflows. Unique, targeted attacks are automatically prioritized with full context, allowing security teams to respond to critical attacks faster, without additional IT security resources.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Key||True|String||
|Results Limit||True|Integer|10|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|requests-2.33.1-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|urllib3-2.6.3-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|
|pan_python-0.25.0-py3-none-any.whl|


## Actions
#### Hunt Domain
Hunt a domain and retrieve a list of associated tags
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"visible": true, "_id": "8002b33fdf1caec503a25ee39297005e84c6af169df65d8be82e2465baa9b2b0", "_source": {"malware": 1, "sha1": "d2884e3655ce4ba167f0083054d2a9ed02669241", "create_date": "2019-09-20T01:57:15", "finish_date": "2019-09-20T02:03:48", "imphash": "ca6f8d49909b618c106e9274d41caec8", "filetype": "DLL64", "ispublic": 1, "tag": [], "tag_groups": [], "tasks": [{"metadata_compilation_ts": "2019-09-20T07:31:06"}], "ssdeep": "3072:656zgKIvACBkQTQzhH6ejYF9aIRQkfGRLe0oaf:JtIvNTKhakYF9lRQKPaf", "sha256": "8002b33fdf1caec503a25ee39297005e84c6af169df65d8be82e2465baa9b2b0", "region": ["us"], "md5": "0e1e960c1de792f71b70eb8c8ab47a00", "size": 131072}}], "Entity": "heroisshit.com"}]
```



#### Ping
Test connectivity to AutoFocus
Timeout - 600 Seconds



#### Hunt Ip
Hunt an IP address and retrieve a list of associated tags
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"visible": true, "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "_source": {"size": 165888, "malware": 0, "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26", "create_date": "2019-08-14T23:01:24", "finish_date": "2019-08-14T23:07:40", "imphash": "0a38e850afb4bc720ee47a34e25f5b35", "filetype": "DLL64", "ispublic": 1, "tasks": [{"metadata_compilation_ts": "2019-07-30T14:47:02"}], "region": ["us"], "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e", "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "tag_groups": [], "tag": [], "md5": "385eab250b3164ef84bb71efca8e305d"}}], "Entity": "95.179.168.51"}]
```



#### Hunt Url
Hunt a URL and retrieve a list of associated tags
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"visible": true, "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "_source": {"size": 165888, "malware": 0, "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26", "create_date": "2019-08-14T23:01:24", "finish_date": "2019-08-14T23:07:40", "imphash": "0a38e850afb4bc720ee47a34e25f5b35", "filetype": "DLL64", "ispublic": 1, "tasks": [{"metadata_compilation_ts": "2019-07-30T14:47:02"}], "region": ["us"], "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e", "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "tag_groups": [], "tag": [], "md5": "385eab250b3164ef84bb71efca8e305d"}}], "Entity": "http://heroisshit.com"}]
```



#### Hunt File
Hunt a file and retrieve a list of associated tags
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"visible": true, "_id": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "_source": {"size": 165888, "malware": 0, "sha1": "81bb895a833594013bc74b429fb1f24f9ec9df26", "create_date": "2019-08-14T23:01:24", "finish_date": "2019-08-14T23:07:40", "imphash": "0a38e850afb4bc720ee47a34e25f5b35", "filetype": "DLL64", "ispublic": 1, "tasks": [{"metadata_compilation_ts": "2019-07-30T14:47:02"}], "region": ["us"], "ssdeep": "3072:JYS22GGzr5yt8XBlkWj/ld/4Pq+HZk/4mQp39pXdxRvA6ppg+ea:ZIWRd/4PqI41QpTFpg+e", "sha256": "1a0e60bdaed45635be8dfe2ada5b3897c5346604d9c29df3db6e6e2f7ea5f5fd", "tag_groups": [], "tag": [], "md5": "385eab250b3164ef84bb71efca8e305d"}}], "Entity": "81bb895a833594013bc74b429fb1f24f9ec9df26"}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.