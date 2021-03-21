import discord
import logging

class DiscordClient(discord.Client):
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)

    async def on_ready(self):
        logging.info(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
        await self.get_channel(818248549300437055).send(
            f'Hi {member.name}, welcome to my empire!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping!':
            await message.channel.send("pong!")
