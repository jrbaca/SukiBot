import os

from dotenv import load_dotenv

from DiscordClient import DiscordClient


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = DiscordClient()
    client.run(token)


if __name__ == "__main__":
    main()
