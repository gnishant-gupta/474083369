
# GoogleCloudCompute

Google Cloud Compute is the Infrastructure as a Service (IaaS) component of Google Cloud Platform which is built on the global infrastructure that runs Google's search engine, Gmail, YouTube and other services. Google Cloud Compute enables users to launch virtual machines (VMs) on demand. VMs can be launched from the standard images or custom images created by users. Google Cloud Compute users must authenticate based on OAuth 2.0 before launching the VMs.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Google Cloud Compute instance.|False|String|https://compute.googleapis.com|
|OS Config API Root|API root of the OS Config service.|False|String|https://osconfig.googleapis.com|
|Account Type|Type of the Google Cloud account. Located at the “type” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|service_account|
|Project ID|Project ID of the Google Cloud account. Located at the “project_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Private Key ID|Private Key ID of the Google Cloud account. Located at the “private_key_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|*****|
|Private Key|Private Key of the Google Cloud account. Located at the “private_key” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|Password|*****|
|Client Email|Client Email of the Google Cloud account. Located at the “client_email” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Client ID|Client ID of the Google Cloud account. Located at the “client_id” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Auth URI|Auth URI of the Google Cloud account. Located at the “auth_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://accounts.google.com/o/oauth2/auth|
|Token URI|Token URI of the Google Cloud account. Located at the “token_uri” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://oauth2.googleapis.com/token|
|Auth Provider X509 URL|Auth Provider X509 URL of the Google Cloud account. Located at the “auth_provider_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String|https://www.googleapis.com/oauth2/v1/certs|
|Client X509 URL|Client X509 URL of the Google Cloud account. Located at the “client_x509_cert_url” parameter in the authentication JSON file. You need to copy the value and put it in this integration configuration parameter.|False|String||
|Service Account Json File Content|Optional: Instead of specifying private key id, private key and other parameters, specify here the full JSON content of the service account file. Other connection parameters will be ignored if this parameter is provided.|False|Password|*****|
|Workload Identity Email|A Service Account Client Email to replace the usage of "Service Account Json File Content", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Cloud Compute service is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|google_api_core-2.19.1-py3-none-any.whl|
|pyparsing-3.1.2-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|google_cloud-0.34.0-py2.py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|idna-3.7-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|setuptools-73.0.1-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|TIPCommon-2.3.8-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|tldextract-5.1.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|google-3.0.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.63.2-py2.py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|protobuf-5.27.3-cp38-abi3-manylinux2014_x86_64.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|


## Actions
#### Add Labels To Instance
Add labels to the Google Cloud Compute Instance.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to add labels to. Instance id can be found with the "List Instances" action.|False|String||
|Instance Labels|Specify instance lables to add to instance. Lables should be provided in the following format - label_key_name:label_value, for example: vm_label_key:label1. Parameter accepts multiple values as a comma separated string.|True|String||



##### JSON Results
```json
[{"id": "XXXXXXXXX", "name": "operation-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX", "zone": "XXX-XXXXXXXXX", "operationType": "setLabels", "targetLink": "https://www.googleapis.com/compute/v1/projects/XXXXXX-XXXXXXXXX-XXXXXXXXX/XXXXX/XX-XXXXX-XX/instances/XXXXXXXXX", "targetId": "XXXXXXXXX", "status": "RUNNING", "user": "XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX@XXXXXXXXX-XXXXXXXXX-XXXXXXXXX.XXXXXXXXX.XXXXXXXXX.XXXXXXXXX", "progress": 0, "insertTime": "2021-06-03T09:43:56.015-07:00", "startTime": "2021-06-03T09:43:56.023-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/XXXXXXXXX-XXXXXXXXX-XXXXXXXXX/zones/XX-XXXXXX-XXXX/operations/operation-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX", "kind": "compute#operation"}]
```



#### Add IP To Firewall Rule
Add IP range to firewall rule in Google Cloud Compute instance. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the firewall rule. Format: projects/{project_id}/global/firewalls/{firewall}. This parameter has higher priority over the combination of "Project ID", and "Firewall Rule".|False|String||
|Project ID|Specify the name of the project of your firewall rule. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Firewall Rule|Specify firewall rule name to update.|False|String||
|Type|Type of the IP range that will be added.|True|List|Source|
|IP Ranges|List of IP ranges that needs to be added to the Firewall Rule.|True|String||



##### JSON Results
```json
{"kind":"compute#operation","id":"9160761312385876914","name":"operation-1716223324528-618e5619d1f93-174eac81-6b38200d","operationType":"patch","targetLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy","targetId":"7886634413370691799","status":"DONE","user":"compute-admin@xxxxx.iam.gserviceaccount.com","progress":100,"insertTime":"2024-05-20T09:42:05.150-07:00","startTime":"2024-05-20T09:42:05.164-07:00","endTime":"2024-05-20T09:42:09.381-07:00","selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d","firewall":{"kind":"compute#firewall","id":"6297155974506248217","creationTimestamp":"2023-09-13T07:28:06.690-07:00","name":"yyyy","description":"","network":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/networks/vpc-network","priority":1000,"sourceRanges":["0.0.0.0/0"],"destinationRanges":["0.0.0.0/21"],"allowed":[{"IPProtocol":"tcp","ports":["22"]}],"direction":"INGRESS","logConfig":{"enable":false},"disabled":false,"selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy"}}
```



#### Add Network Tags
Add network tags to the Compute Engine instance. This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE for the action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|The full resource name for the Compute Engine instance, such as /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has a priority over the “Project ID”, “Instance Zone”, and “Instance ID” parameters.|False|String||
|Project ID|The project name of the Compute Engine instance. If you don’t set a value,, the action retrieves the project name from the integration configuration.|False|String||
|Instance Zone|The zone name of the Compute Engine instance. This parameter is required if you configure the Compute Engine instance using the “Instance Zone” and “Instance ID” parameters.|False|String||
|Instance ID|The Compute Engine instance ID. This parameter is required if you configure the Compute Engine instance using the “Instance Zone” and “Instance ID” parameters.|False|String||
|Network Tags|A comma-separated list of network tags to add to the Compute Engine instance. This parameter only accepts tags that contain lowercase letters, numbers, and hyphens.|True|String||



##### JSON Results
```json
{"kind": "compute#instance", "id": "1459671903146615834", "creationTimestamp": "2023-09-13T04:20:21.993-07:00", "name": "instance-2", "description": "", "tags": {"items": ["another-tag",  "tag"], "fingerprint": "BCeEINC7Ths="}, "machineType": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/machineTypes/e2-micro", "status": "RUNNING", "zone": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a", "canIpForward": false, "networkInterfaces": [{"kind": "compute#networkInterface", "network": "https://www.googleapis.com/compute/v1/projects/test-project/global/networks/default", "subnetwork": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/subnetworks/default", "networkIP": "10.128.0.3", "name": "nic0", "fingerprint": "-ZnnV7hiDfs=", "stackType": "IPV4_ONLY"}], "disks": [{"kind": "compute#attachedDisk", "type": "PERSISTENT", "mode": "READ_WRITE", "source": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/disks/instance-2", "deviceName": "instance-2", "index": 0, "boot": true, "autoDelete": true, "licenses": ["https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-7"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "GVNIC"}], "diskSizeGb": "20", "architecture": "X86_64"}], "metadata": {"kind": "compute#metadata", "fingerprint": "NBmH4-7Jw9U=", "items": []}, "serviceAccounts": [{"email": "1111111111-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/instances/instance-2", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false, "provisioningModel": "STANDARD"}, "cpuPlatform": "Intel Broadwell", "labelFingerprint": "42WmSpB8rSM=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "UWo2c6E_mlM=", "lastStartTimestamp": "2023-09-13T04:20:29.718-07:00", "keyRevocationActionType": "NONE"}
```



#### Enrich Entities
Enrich Siemplify IP entities with instance information from Google Cloud Compute.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||



##### JSON Results
```json
[{"Entity": "1.1.1.1", "EntityResult": {"id": "1234", "creationTimestamp": "2021-04-28T21:34:57.369-07:00", "name": "instance-1", "description": "", "tags": {"fingerprint": "42WmSpB8rSM="}, "machineType": "f1-micro", "status": "RUNNING", "zone": "us-central1-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "nic0", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "natIP": "1.1.1.1", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "12345=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "instance-1", "deviceName": "instance-1", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "123456-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/12345/zones/us-central1-a/instances/instance-1", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Intel Haswell", "labels": {"vm_test_tag": "tag1", "vm_new_label": "label1", "vm_test_tag2": "gabrieltag"}, "labelFingerprint": "12345=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "12345=", "lastStartTimestamp": "2021-05-11T01:01:28.994-07:00", "lastStopTimestamp": "2021-05-11T00:59:53.844-07:00", "kind": "compute#instance"}}, {"Entity": "1.1.1.1 ", "EntityResult": {"id": "720750400845139023", "creationTimestamp": "2021-06-01T01:41:05.363-07:00", "name": "instance-2", "description": "", "tags": {"fingerprint": "12345="}, "machineType": "e2-medium", "status": "TERMINATED", "zone": "us-central1-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "nic0", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "12345=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "instance-2", "deviceName": "instance-2", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "123456-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/12345/zones/us-central1-a/instances/instance-2", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Unknown CPU Platform", "labels": {"amit": "23", "kok": "2"}, "labelFingerprint": "123435=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "x-123123=", "lastStartTimestamp": "2021-06-01T01:41:21.651-07:00", "lastStopTimestamp": "2021-06-03T08:15:37.366-07:00", "kind": "compute#instance"}}]
```



#### Remove External IP Addresses
Remove external IP addresses on a Google Cloud Compute instance. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: projects/{project_id}/zones/{zone_id}/instances/{instance_id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to modify. Instance id can be found in "List Instances" action.|False|String||
|Network Interfaces|Specify a comma-separated list of network interfaces to modify. If this parameter is left empty or  “*” is provided then all of the network interfaces will be updated.|False|String|*|



##### JSON Results
```json
[{"kind": "compute#operation", "id": "1673537252688477099", "name": "operation-1716290883723-618f51c749f5b-876cd70d-3602a8a3", "zone": "us-west1-a", "operationType": "updateNetworkInterface", "targetLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/instances/yyyy", "targetId": "3905740668247239013", "status": "DONE", "user": "compute-admin@xxxxx.iam.gserviceaccount.com", "progress": 100, "insertTime": "2024-05-21T04:28:04.176-07:00", "startTime": "2024-05-21T04:28:04.190-07:00", "endTime": "2024-05-21T04:28:05.371-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/operations/operation-1716290883723-618f51c749f5b-876cd70d-3602a8a3"}, {"kind": "compute#operation", "id": "2531200345768541098", "name": "operation-1716290885077-618f51c894918-b3dbc881-cf094d9d", "zone": "us-west1-a", "operationType": "deleteAccessConfig", "targetLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/instances/yyyy", "targetId": "3905740668247239013", "status": "DONE", "user": "compute-admin@xxxxx.iam.gserviceaccount.com", "progress": 100, "insertTime": "2024-05-21T04:28:05.419-07:00", "startTime": "2024-05-21T04:28:05.430-07:00", "endTime": "2024-05-21T04:28:06.549-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/xxxxx/zones/us-west1-a/operations/operation-1716290885077-618f51c894918-b3dbc881-cf094d9d"}]
```



#### Remove IP From Firewall Rule
Remove IP from firewall rule in Google Cloud Compute instance. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the firewall rule. Format: projects/{project_id}/global/firewalls/{firewall}. This parameter has higher priority over the combination of "Project ID", and "Firewall Rule".|False|String||
|Project ID|Specify the name of the project of your firewall rule. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Firewall Rule|Specify firewall rule name to update.|False|String||
|Type|Type of the IP range that will be removed.|True|List|Source|
|IP Ranges|List of IP ranges that needs to be removed from the Firewall Rule.|True|String||



##### JSON Results
```json
{"kind":"compute#operation","id":"9160761312385876914","name":"operation-1716223324528-618e5619d1f93-174eac81-6b38200d","operationType":"patch","targetLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy","targetId":"7886634413370691799","status":"DONE","user":"compute-admin@xxxxx.iam.gserviceaccount.com","progress":100,"insertTime":"2024-05-20T09:42:05.150-07:00","startTime":"2024-05-20T09:42:05.164-07:00","endTime":"2024-05-20T09:42:09.381-07:00","selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d","firewall":{"kind":"compute#firewall","id":"6297155974506248217","creationTimestamp":"2023-09-13T07:28:06.690-07:00","name":"yyyy","description":"","network":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/networks/vpc-network","priority":1000,"sourceRanges":["0.0.0.0/0"],"destinationRanges":["0.0.0.0/21"],"allowed":[{"IPProtocol":"tcp","ports":["22"]}],"direction":"INGRESS","logConfig":{"enable":false},"disabled":false,"selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy"}}
```



#### Remove Network Tags
Remove network tags from the Compute Engine instance. This action is asynchronous. Adjust the sript timeout value in the Google SecOps IDE for the action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|The full resource name for the Compute Engine instance, such as /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has a priority over the “Project ID”, “Instance Zone”, and “Instance ID” parameters.|False|String||
|Project ID|The project name of your Compute Engine instance. If you don’t set a value, the action retrieves the project name from the integration configuration.|False|String||
|Instance Zone|The zone name of the Compute Engine instance. This parameter is required if you configure the Compute Engine instance using the “Instance Zone” and “Instance ID” parameters.|False|String||
|Instance ID|The Compute Engine instance ID. This parameter is required if you configure the Compute Engine instance using the “Instance Zone” and “Instance ID” parameters.|False|String||
|Network Tags|A comma-separated list of network tags to remove from the Compute Engine instance. This parameter only accepts tags that contain lowercase letters, numbers, and hyphens.|True|String||



##### JSON Results
```json
{"kind": "compute#instance", "id": "1459671903146615834", "creationTimestamp": "2023-09-13T04:20:21.993-07:00", "name": "instance-2", "description": "", "tags": {"items": ["another-tag",  "tag"], "fingerprint": "BCeEINC7Ths="}, "machineType": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/machineTypes/e2-micro", "status": "RUNNING", "zone": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a", "canIpForward": false, "networkInterfaces": [{"kind": "compute#networkInterface", "network": "https://www.googleapis.com/compute/v1/projects/test-project/global/networks/default", "subnetwork": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/subnetworks/default", "networkIP": "10.128.0.3", "name": "nic0", "fingerprint": "-ZnnV7hiDfs=", "stackType": "IPV4_ONLY"}], "disks": [{"kind": "compute#attachedDisk", "type": "PERSISTENT", "mode": "READ_WRITE", "source": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/disks/instance-2", "deviceName": "instance-2", "index": 0, "boot": true, "autoDelete": true, "licenses": ["https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-7"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "GVNIC"}], "diskSizeGb": "20", "architecture": "X86_64"}], "metadata": {"kind": "compute#metadata", "fingerprint": "NBmH4-7Jw9U=", "items": []}, "serviceAccounts": [{"email": "1111111111-compute@developer.gserviceaccount.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/test-project/zones/us-central1-a/instances/instance-2", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false, "provisioningModel": "STANDARD"}, "cpuPlatform": "Intel Broadwell", "labelFingerprint": "42WmSpB8rSM=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedInstanceConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedInstanceIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialInstanceConfig": {"enableConfidentialCompute": false}, "fingerprint": "UWo2c6E_mlM=", "lastStartTimestamp": "2023-09-13T04:20:29.718-07:00", "keyRevocationActionType": "NONE"}
```



#### Set Instance IAM Policy
Sets the access control policy on the specified resource. Note that policy provided in action replaces any existing policy.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to set policy for. Intsance id can be found in "List Instances" action.|False|String||
|Policy|Specify JSON policy document to set for instance.|True|String||



##### JSON Results
```json
[{"version": 1,"etag": "XXXXXXXX","bindings": [{"role": "roles/compute.XXXXXXX","members": ["user:XXXXXX@XXXXXX.XX"]}]}]
```



#### Start Instance
Start a previously stopped Google Cloud Compute Instance. Note that it can take a few minutes for the instance to enter the running status.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to start. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123456667", "name": "operation-1234-1234-1234-1234", "zone": "us-central1-a", "operationType": "start", "targetLink": "https://www.googleapis.com/compute/v1/projects/project111/zones/us-central1-a/instances/123456667", "targetId": "123456667", "status": "RUNNING", "user": "google-cloud-compute-spec@project111.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T05:44:01.508-07:00", "startTime": "2021-06-07T05:44:01.548-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/project111/zones/us-central1-a/operations/operation-1234-1234-1234-1234", "kind": "compute#operation"}
```



#### Delete Instance
Delete the specified Google Cloud Compute instance.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to delete. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123465", "name": "operation-123456-123456-123456-123456", "zone": "us-central1-a", "operationType": "delete", "targetLink": "https://www.googleapis.com/compute/v1/projects/some-project/zones/us-central1-a/instances/123456", "targetId": "123456", "status": "RUNNING", "user": "google-cloud-compute-spec@some-project.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T07:36:22.400-07:00", "startTime": "2021-06-07T07:36:22.439-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/some-project/zones/us-central1-a/operations/operation-123456-123456-123456-123456", "kind": "compute#operation"}
```



#### Stop Instance
Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to stop. Instance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
{"id": "123456789", "name": "operation-123456-123456-123456-123456", "zone": "us-central1-a", "operationType": "stop", "targetLink": "https://www.googleapis.com/compute/v1/projects/some-zone/zones/us-central1-a/instances/123456789", "targetId": "123456789", "status": "RUNNING", "user": "google-cloud-compute-spec@some-zone.iam.gserviceaccount.com", "progress": 0, "insertTime": "2021-06-07T06:59:49.897-07:00", "startTime": "2021-06-07T06:59:49.936-07:00", "selfLink": "https://www.googleapis.com/compute/v1/projects/some-zone/zones/us-central1-a/operations/operation-123456-123456-123456-123456", "kind": "compute#operation"}
```



#### Update Firewall Rule
Update a firewall rule with given parameters in Google Cloud Compute. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the firewall rule. Format: projects/{project_id}/global/firewalls/{firewall}. This parameter has higher priority over the combination of "Project ID", and "Firewall Rule".|False|String||
|Project ID|Specify the name of the project of your firewall rule. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Firewall Rule|Specify firewall rule name to update.|False|String||
|Source IP ranges|Specify a comma-separated list of source IP ranges. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|Source Tags|Specify a comma-separated list of source tags. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|Source Service Accounts|Specify a comma-separated list of source service accounts. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value.|False|String||
|TCP Ports|Specify a comma-separated list of TCP ports. If specified, action will use it to update determine allow / deny lists. Parameter supports 'all' and 'none' values.|False|String||
|UDP Ports|Specify a comma-separated list of UDP ports. If specified, action will use it to update determine allow / deny lists. Parameter supports 'all' and 'none' values.|False|String||
|Other Protocols|Specify a comma-separated list of other protocols. Parameter supports 'none' value. If 'all' specified, the action will allow all protocols including tcp and udp.|False|String||
|Destination IP Ranges|Specify a comma-separated list of destination IP ranges. Parameter supports 'none' value. If "none" value is provided, then the action will delete existing values for the firewall rule. If nothing is provided for the parameter, action will not update the existing value. |False|String||



##### JSON Results
```json
{"kind":"compute#operation","id":"9160761312385876914","name":"operation-1716223324528-618e5619d1f93-174eac81-6b38200d","operationType":"patch","targetLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy","targetId":"7886634413370691799","status":"DONE","user":"compute-admin@xxxxx.iam.gserviceaccount.com","progress":100,"insertTime":"2024-05-20T09:42:05.150-07:00","startTime":"2024-05-20T09:42:05.164-07:00","endTime":"2024-05-20T09:42:09.381-07:00","selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d","firewall":{"kind":"compute#firewall","id":"6297155974506248217","creationTimestamp":"2023-09-13T07:28:06.690-07:00","name":"yyyy","description":"","network":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/networks/vpc-network","priority":1000,"sourceRanges":["0.0.0.0/0"],"destinationRanges":["0.0.0.0/21"],"allowed":[{"IPProtocol":"tcp","ports":["22"]}],"direction":"INGRESS","logConfig":{"enable":false},"disabled":false,"selfLink":"https://www.googleapis.com/compute/v1/projects/xxxxx/global/firewalls/yyyy"}}
```



#### Ping
Test connectivity to the Google Cloud Compute service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Instances
List Google Cloud Compute instances based on the specified search criteria. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance Name|Specify instance name to search for. Parameter accepts multiple values as a comma separated string.|False|String||
|Instance Status|Specify instance status to search for. Parameter accepts multiple values as a comma separated string.|False|String||
|Instance Labels|Specify instance labels to search for in the format label_key_name:label_value, for example vm_label_key:label1. Parameter accepts multiple values as a comma separated string.|False|String||
|Max Rows to Return|Specify how many instances action should return.|False|String|50|



##### JSON Results
```json
[{"id": "12345", "creationTimestamp": "2021-04-28T21:34:57.369-07:00", "name": "xxxxxx-1", "description": "", "tags": {"fingerprint": "12345="}, "machineType": "f1-micro", "status": "RUNNING", "zone": "xxxxx-a", "canIpForward": false, "networkInterfaces": [{"network": "default", "subnetwork": "default", "networkIP": "1.1.1.1", "name": "xxx", "accessConfigs": [{"type": "ONE_TO_ONE_NAT", "name": "External NAT", "natIP": "1.1.1.1", "networkTier": "PREMIUM", "kind": "compute#accessConfig"}], "fingerprint": "1234=", "kind": "compute#networkInterface"}], "disks": [{"type": "PERSISTENT", "mode": "READ_WRITE", "source": "xxxxx-1", "deviceName": "xxxxx-1", "index": 0, "boot": true, "autoDelete": true, "licenses": ["debian-10-buster"], "interface": "SCSI", "guestOsFeatures": [{"type": "UEFI_COMPATIBLE"}, {"type": "VIRTIO_SCSI_MULTIQUEUE"}], "diskSizeGb": "10", "kind": "compute#attachedDisk"}], "metadata": {"fingerprint": "12345=", "kind": "compute#metadata"}, "serviceAccounts": [{"email": "1234-1234@1234.1234.com", "scopes": ["https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/logging.write", "https://www.googleapis.com/auth/monitoring.write", "https://www.googleapis.com/auth/servicecontrol", "https://www.googleapis.com/auth/service.management.readonly", "https://www.googleapis.com/auth/trace.append"]}], "selfLink": "https://www.googleapis.com/compute/v1/projects/1111111/zones/xxxxx-a/xxxxxs/xxxxx-1", "scheduling": {"onHostMaintenance": "MIGRATE", "automaticRestart": true, "preemptible": false}, "cpuPlatform": "Intel Haswell", "labels": {"vm_test_tag": "tag1", "vm_new_label": "label1", "vm_test_tag2": "tag2"}, "labelFingerprint": "12345=", "startRestricted": false, "deletionProtection": false, "reservationAffinity": {"consumeReservationType": "ANY_RESERVATION"}, "displayDevice": {"enableDisplay": false}, "shieldedxxxxxConfig": {"enableSecureBoot": false, "enableVtpm": true, "enableIntegrityMonitoring": true}, "shieldedxxxxxIntegrityPolicy": {"updateAutoLearnPolicy": true}, "confidentialxxxxxConfig": {"enableConfidentialCompute": false}, "fingerprint": "123123=", "lastStartTimestamp": "2021-05-11T01:01:28.994-07:00", "lastStopTimestamp": "2021-05-11T00:59:53.844-07:00", "kind": "compute#xxxxx"}]
```



#### Execute VM Patch Job
Execute a VM patch job on Compute Engine instances. This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE for the action as needed. This action requires you to enable the OS Config API.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Instance Filter Object|A JSON object to set an instance filter.|True|String|{
"all": "true"
}|
|Name|The name for the patching job.|True|String||
|Description|The description for the patching job.|False|String||
|Patching Config Object|A JSON object that specifies the steps for the patching job to execute. If you don’t set a value, the action patches Compute Engine instances using the default value. To configure this parameter, use the following format: {"key": "value"}.|False|String|{
    "rebootConfig": "DEFAULT",
    "apt": {
      "type": "DIST"
    },
    "yum": {
      "security": true
    },
    "zypper": {
      "withUpdate": true
    },
    "windowsUpdate": {
      "classifications": ["CRITICAL", "SECURITY"]
    }
  }|
|Patch Duration Timeout|The timeout value in minutes for a patching job.|True|String|60|
|Rollout Strategy|The rollout strategy for a patching job.|False|List|Zone By Zone|
|Disruption Budget|The disruption budget for a patching job. You can use a specific number or a percentage like 10%.|True|String|10%|
|Wait For Completion|If selected, the action waits for the patching job to complete.|False|Boolean|true|
|Fail If Completed With Errors|If selected and the patching job status is “Completed with errors” or the action reaches a timeout, the action fails. If you didn’t select the “Wait For Completion” parameter, the action ignores this parameter. |False|Boolean|true|



##### JSON Results
```json
{"name": "projects/1111/patchJobs/93c583e6-ce65-4b3a-9eab-e46904fdaf55", "createTime": "2024-11-06T14:29:52.628592Z", "updateTime": "2024-11-06T14:29:54.880459Z", "state": "PATCHING", "patchConfig": {}, "duration": "3600s", "instanceDetailsSummary": {"startedInstanceCount": "1"}, "percentComplete": 20, "instanceFilter": {"instances": ["zones/us-central1-a/instances/instance-2"]}, "displayName": "Test Job", "rollout": {"mode": "ZONE_BY_ZONE", "disruptionBudget": {"percent": 10}}}
```



#### Get Instance IAM Policy
Gets the access control policy for the resource. Note that policy may be empty if no policy is assigned to the resource.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Name|Specify the full resource name for the compute instance. Format: /projects/{project_id}/zones/{zone id}/instances/{instance id}. This parameter has higher priority over the combination of "Project ID", "Instance Zone" and "Instance ID".|False|String||
|Project ID|Specify the name of the project of your compute instance. If nothing is provided, the project will be extracted from integration configuration.|False|String||
|Instance Zone|Specify instance zone name to search for instances in.|False|String||
|Instance ID|Specify instance id to get policy for. Intsance id can be found in "List Instances" action.|False|String||



##### JSON Results
```json
[{"version": 1,"etag": "XXXXXXXX","bindings": [{"role": "roles/compute.XXXXXXX","members": ["user:XXXXXX@XXXXXX.XX"]}]}]
```










A paragraph is a distinct section of writing that focuses on a single controlling idea or topic. It typically consists of a topic sentence, supporting details, and a concluding sentence.