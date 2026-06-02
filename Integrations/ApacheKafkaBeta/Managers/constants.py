from enum import Enum


INTEGRATION_NAME: str = "Apache Kafka"
PING_SCRIPT_NAME: str = f"{INTEGRATION_NAME} - Ping"

INTEGRATION_IDENTIFIER: str = "ApacheKafka"
KAFKA_CONNECTOR_SCRIPT_NAME: str = f"{INTEGRATION_IDENTIFIER} - Messages Connector"
VENDOR: str = "Apache Kafka"
PRODUCT: str = "Message"
ALERT_NAME: str = "{connector_name} - Alert"
RULE_GENERATOR: str = "{connector_name} - Rule Generator"
CONNECTOR_DISPLAY_ID_TEMPLATE: str = "ApacheKafka_{alert_id}_{connector_identifier}"

INVALID_PARTITION: int = -1
INVALID_OFFSET: int = -1001
EARLIEST_OFFSET_INT: int = 0
EARLIEST_OFFSET_STR: str = "earliest"
LATEST_OFFSET_STR: str = "latest"
DEFAULT_TIMEOUT: int = 5

SEVERITY_MAPPING_DEFAULT_KEY: str = "Default"
SASL_PROTOCOL_PREFIX: str = "SASL_"
PLAINTEXT_PROTOCOL: str = "PLAIN"


class SecurityProtocol(Enum):
    PLAINTEXT: str = "PLAINTEXT"
    SASL_PLAINTEXT: str = "SASL_PLAINTEXT"
    SASL_SSL: str = "SASL_SSL"
    SSL: str = "SSL"
