import discord
from discord import Embed, Interaction, app_commands
from discord.ext import commands
import datetime
import asyncio
import time
from discord.ext.commands import MissingPermissions
from discord.app_commands import AppCommandError, CommandInvokeError
import animec

class welcome(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = channel = self.bot.get_channel(976739222700568596)

        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(), title=" Welcome To My Support Server",
                                description=f"{member.mention}\n\n════════════════\n\n:white_check_mark: Before You Start Introduce Yourself in <#974312751029706782>\n\n :unlock: check rules in <#974312732042096650>\n\n :recycle: Announcement in <#974312736932659270>\n\n════════════════\n\n Thank You For Joining Server"
                                )
        embed.set_image(
                url="https://i.imgur.com/2D9qLj1.gif")
        await channel.send(embed=embed)

#end
async def setup(bot) -> None:
  await bot.add_cog(welcome(bot))
