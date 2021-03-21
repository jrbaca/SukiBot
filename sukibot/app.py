import os

from dotenv import load_dotenv

from sukibot.discord_client import DiscordClient
import logging
import logging.config


def run():
    logging.config.fileConfig('logging.conf')
    logging.info("Starting up SukiBot...")

    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = DiscordClient()
    client.run(token)
