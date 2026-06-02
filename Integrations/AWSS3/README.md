
# AWSS3

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications for companies all around the world.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|AWS Access Key ID|None|True|String||
|AWS Secret Key|None|True|Password|*****|
|AWS Default Region|None|True|String||


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|jmespath-1.0.1-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|botocore-1.35.4-py3-none-any.whl|
|boto3-1.35.4-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|s3transfer-0.10.2-py3-none-any.whl|


## Actions
#### Get Bucket Policy
Retrieve information about the bucket policy from AWS S3.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Bucket Name|Specify name of the bucket from which to retrieve policy information.|True|String||



##### JSON Results
```json
[{"Policy":{"Version":"2012-10-17","Statement":[{"Sid":"AddPerm","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::testsiemplify/*"}]}}]
```



#### List Bucket Objects
List objects in the bucket from AWS S3.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Bucket Name|Specify name of the bucket from which to retrieve objects.|True|String||
|Max Objects to Return|Specify how many objects to return.|False|String|50|



##### JSON Results
```json
[{"Contents":[{"Key":"test","LastModified":"2020-09-15T06:20:36","ETag":"6a8bfffdf3e3e66f317298bdcbf379e8","Size":18,"StorageClass":"STANDARD","Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"}},{"Key":"test.txt","LastModified":"2020-09-15T06:21:56","ETag":"6a8bfffdf3e3e66f317298bdcbf379e8","Size":18,"StorageClass":"STANDARD","Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"}},{"Key":"test/123.txt","LastModified":"2020-09-15T06:24:21","ETag":"6a8bfffdf3e3e66f317298bdcbf379e8","Size":18,"StorageClass":"STANDARD","Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"}},{"Key":"test/test.txt","LastModified":"2020-09-15T06:22:24","ETag":"6a8bfffdf3e3e66f317298bdcbf379e8","Size":18,"StorageClass":"STANDARD","Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"}},{"Key":"test/upload_me.txt","LastModified":"2020-09-23T09:05:22","ETag":"\"acb7b18b5c944ef2417a9e2364ed97c0\"","Size":57,"StorageClass":"STANDARD","Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"}}]}]
```



#### List Buckets
Retrieve a list of buckets from AWS S3.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Owner":{"DisplayName":"lab_aws","ID":"935dc3fed0e1d2c5b12242cf9927370824f2438681a2d3c0523f254dbde41aba"},"Buckets":[{"CreationDate":"2020-09-14T10:31:56","Name":"testsiemplify"}]}]
```



#### Ping
Test connectivity to AWS S3 with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Set Bucket Policy
Set a policy in the bucket from AWS S3.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Bucket Name|Specify the name of the bucket on which you want to update the policy.|True|String||
|Policy JSON Object|Specify the JSON object of the policy that you want to set for the bucket. Examples can be found here: https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html.|True|String||



#### Upload File To Bucket
Upload file to bucket in AWS S3.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|Specify the absolute path to the file that needs to be uploaded. Example: /folder_1/folder_2/filename|True|String|/{folder_1}/{folder_2}/{filename}|
|Bucket Upload Path|Specify the path in the bucket to where the path should be uploaded. Example: s3://siemplify/syslog/log.txt|True|String|s3://{bucket_name}/{file_name}|



##### JSON Results
```json
[{"bucket_upload_path":"s3://testsiemplify/test/123.txt","file_path":"/usr/bin/share/download.txt"}]
```



#### Download File From Bucket
Download file from bucket in AWS S3.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Bucket File Path|Specify the path of the file in the bucket. Example: s3://siemplify/syslog/log.txt|True|String|s3://{bucket_name}/{file_name}|
|Download Path|Specify the absolute path, where to download the file. Example: /folder_1/folder_2/filename|True|String|/{folder_1}/{folder_2}/{filename}|



##### JSON Results
```json
[{"bucket_file_path":"s3://testsiemplify/test/123.txt","download_path":"/usr/bin/share/download.txt"}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.