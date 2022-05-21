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
        channel = self.bot.get_channel(962611423240945729)
        logs = self.bot.get_channel(974312830926995467)

        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(), title=f"Hey ! {member.mention} Welcome To My Support Server",
                                description=f"════════════════\n\n:white_check_mark: Before You Start Introduce Yourself in <#974312751029706782>\n\n :unlock: check rules in <#974312732042096650>\n\n :recycle: Announcement in <#974312736932659270>\n\n════════════════\n\n Thank You For Joining Server"
                                )
        embed.set_image(
                url="https://imgur.com/2D9qLj1")
        await channel.send(embed=embed)
        await logs.send(embed=discord.Embed(description=f"{member.mention} Just Joined Our server"))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logs = self.bot.get_channel(974312830926995467)
        await logs.send(embed=discord.Embed(description=f"{member.mention} Just Left Our server"))

    @app_commands.command(name="echo", description="Bot will send a message for you")
    @app_commands.checks.has_permissions(ban_members=True)
    async def echo(self, interaction: discord.Interaction,  content: str , channel: discord.TextChannel) -> None:
        await interaction.response.defer(ephemeral=True, thinking=True)
        await channel.send(content)
        await interaction.followup.send("<a:dvloper:974560024200351744> Done")
        logs = self.bot.get_channel(974312845573492826)
        await logs.send(embed=discord.Embed(description=f"{interaction.user} Used Echo \n Message -{content}"))
#end
async def setup(bot) -> None:
  await bot.add_cog(welcome(bot))