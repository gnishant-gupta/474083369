from __future__ import annotations


class ApacheKafkaException(Exception):
    """A base exception for the Apache Kafka integration."""


class KafkaClientError(ApacheKafkaException):
    """Exception for general errors that occur within the KafkaClient."""


class KafkaConnectionError(ApacheKafkaException):
    """Exception for errors that occur while connecting to the Kafka cluster."""


class KafkaInvalidJsonException(ApacheKafkaException):
    """Exception for errors that occur while parsing a JSON object."""
