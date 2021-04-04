import logging
import logging.config
import os
from typing import Optional

from discord.message import Message
from dotenv import load_dotenv

from sukibot.discord_client import DiscordClient
from sukibot.handlers import BaseIntent
from sukibot.handlers import HandlerInput, HandlerResponse
from sukibot.handlers.list_action_handlers import CreateListIntent
from sukibot.handlers.ping_pong_handlers import PingPongIntent, PingPongEvil
from sukibot.handlers.give_me_blank_handlers import GiveMeSomethingIntent


class SukiBot:

    def __init__(self, client: DiscordClient):
        self._registered_intents: list[BaseIntent] = []

        client.set_sukibot(self)
        self._client = client

    def register_intents(self, *intents: BaseIntent):
        for intent in intents:
            self._registered_intents.append(intent)

    def run(self):
        self._client.run()

    def handle_message(self, message: Message) -> Optional[HandlerResponse]:
        handler_input = HandlerInput(message.content)

        for intent in self._registered_intents:
            can_handle = intent.can_handle(handler_input)
            if can_handle:
                return intent.handle(handler_input)

        return None


def run():
    logging.config.fileConfig('logging.conf')
    logging.info("Starting up SukiBot...")

    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = DiscordClient(token)
    sukibot = SukiBot(client)

    sukibot.register_intents(
        PingPongIntent(),
        CreateListIntent(),
        PingPongEvil(),
        GiveMeSomethingIntent()
    )

    sukibot.run()
