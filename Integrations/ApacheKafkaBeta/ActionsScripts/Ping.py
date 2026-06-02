from __future__ import annotations

from typing import TYPE_CHECKING

from TIPCommon.base.action import Action

from action_init import create_kafka_client
import constants

if TYPE_CHECKING:
    from typing import Any, NoReturn

    from kafka_manager import KafkaClient


SUCCESS_MESSAGE: str = (
    f"Successfully connected to the {constants.INTEGRATION_NAME} server with "
    "the provided connection parameters!"
)
ERROR_MESSAGE: str = f"Failed to connect to the {constants.INTEGRATION_NAME} server!"


class Ping(Action):
    def __init__(self) -> None:
        super().__init__(constants.PING_SCRIPT_NAME)
        self.output_message: str = SUCCESS_MESSAGE
        self.error_output_message: str = ERROR_MESSAGE

    def _init_api_clients(self) -> KafkaClient:
        return create_kafka_client(self.soar_action)

    def _perform_action(self, _: Any = None) -> None:
        self.api_client.test_connectivity()


def main() -> NoReturn:
    Ping().run()


if __name__ == "__main__":
    main()
