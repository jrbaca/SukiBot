import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    await client.get_channel(818248549300437055).send(
        f'Hi {member.name}, welcome to my empire!'
    )

client.run(TOKEN)
