import logging

import discord

import sukibot.app as sb
from typing import Optional


class DiscordClient(discord.Client):

    def __init__(self, token):
        self._token = token
        self._sukibot: Optional['sb.SukiBot'] = None

        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)

    def set_sukibot(self, sukibot: 'sb.SukiBot'):
        self._sukibot = sukibot

    async def on_ready(self):
        logging.info(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
        await self.get_channel(818248549300437055).send(
            f'Hi {member.name}, welcome to my empire!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return

        response = self._sukibot.handle_message(message)

        if response is not None:
            await message.channel.send(response.message)

    def run(self):
        super().run(self._token)
