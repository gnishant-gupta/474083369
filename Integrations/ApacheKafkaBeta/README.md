
# ApacheKafkaBeta

Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Kafka Brokers|A comma-separated list of Kafka brokers to connect to, in the format `hostname:port`.|True|String||
|Use TLS for connection|If enabled, the integration uses TLS encryption for authentication. A CA certificate is mandatory for this connection.|False|Boolean|false|
|Use SASL PLAIN with TLS for connection|If enabled, the integration uses the SASL PLAIN username and password mechanism for authentication. This option requires a SASL Username and Password to be provided. It is only supported with TLS encryption, which requires a CA certificate.|False|Boolean|false|
|CA certificate of Kafka server|The Certificate Authority (CA) certificate used to verify the identity of the Kafka server.|False|Password|*****|
|Client certificate|The client's certificate for mutual TLS authentication with the Kafka server.|False|Password|*****|
|Client certificate key|The private key that corresponds to the client's certificate, used for mutual TLS authentication.|False|Password|*****|
|Client certificate key password|The password used to decrypt the client certificate's private key.|False|Password|*****|
|SASL PLAIN Username|The username for SASL PLAIN authentication with Kafka brokers.|False|String||
|SASL PLAIN Password|The password for SASL PLAIN authentication with Kafka brokers.|False|Password|*****|


#### Dependencies
| |
|-|
|httpcore-1.0.9-py3-none-any.whl|
|googleapis_common_protos-1.70.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|anyio-4.9.0-py3-none-any.whl|
|typing_extensions-4.14.1-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|TIPCommon-2.2.9-py2.py3-none-any.whl|
|google_api_python_client-2.177.0-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|google_api_core-2.25.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|confluent_kafka-2.11.0-cp311-cp311-manylinux_2_28_x86_64.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl|
|cachetools-5.5.2-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyparsing-3.2.3-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|google_auth-2.40.3-py2.py3-none-any.whl|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|sniffio-1.3.1-py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|certifi-2025.7.14-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|


## Actions
#### Ping
Use the Ping action to test the connectivity to Apache Kafka.
Timeout - 600 Seconds









