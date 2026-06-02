from __future__ import annotations

from typing import TYPE_CHECKING

from kafka_manager import KafkaClient
from utils import get_integration_parameters

if TYPE_CHECKING:
    from TIPCommon.types import ChronicleSOAR

    from kafka_manager import KafkaConfigurationParameters


def create_kafka_client(soar_action: ChronicleSOAR) -> KafkaClient:
    """Create Kafka client object."""
    kafka_config: KafkaConfigurationParameters = get_integration_parameters(soar_action)
    kafka_client: KafkaClient = KafkaClient(kafka_config, soar_action.logger)

    return kafka_client
