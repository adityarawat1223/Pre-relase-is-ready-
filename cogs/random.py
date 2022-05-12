import discord
from discord import Interaction, app_commands
from discord.ext import commands
import datetime
import asyncio
import time
from discord.ext.commands import MissingPermissions
from discord.app_commands import AppCommandError, CommandInvokeError


class info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(),
                              description="**changes -**\n\n<a:arrow_arrow:963331682847580200>**All commands are slash**\n\n<a:arrow_arrow:963331682847580200>**1 . Added Ban Command**\n\n<a:arrow_arrow:963331682847580200>**2. Added Kick command **\n\n<a:arrow_arrow:963331682847580200>**3. Added Mute command**\n\n<a:arrow_arrow:963331682847580200>**4. Added Unmute command**\n\n<a:arrow_arrow:963331682847580200>**5. Added Anime command**\n\n<a:arrow_arrow:963331682847580200>**6. Added Character search command**\n\n<a:arrow_arrow:963331682847580200>**7. Added reminder command**\n\n<a:arrow_arrow:963331682847580200>**8. Added Hug and Busted command **\n\n<a:arrow_arrow:963331682847580200>**9. Added Warn commands**\n\n<a:arrow_arrow:963331682847580200>**10. info command**\n\n<a:arrow_arrow:963331682847580200>**11. added ping command**\n\n<a:arrow_arrow:963331682847580200>**11.added server info command**\n\n<a:arrow_arrow:963331682847580200>**12.major bug fixes **")
        await ctx.send(embed=embed)

    @app_commands.command(name="ping", description="ping is ping ")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embedVar = discord.Embed(
            title="Pong", description="Pong", color=0x00ff00)
        embedVar.add_field(name="Latency", value=str(
            round(self.bot.latency * 1000)), inline=False)
        await interaction.followup.send(embed=embedVar)

    @app_commands.command(name="nick", description="chane nickname of an user ")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(change_nickname=True)
    async def nick(self, interaction: discord.Interaction, user: discord.Member, nick: str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        await user.edit(nick=nick)
        embed = discord.Embed(
            color=0x55a7f7, description=f'Nickname was changed for {user.mention} ')
        await interaction.followup.send(embed=embed)

    @nick.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(
            ), title="**Missing permissions**", description="**Only Mods Can Use this command**")
            embed.set_footer(
                text="join Our official discord Server ")

            await interaction.followup.send(embed=embed)
    
   

    @app_commands.command(name="serverinfo", description="get info about this server  ")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(change_nickname=True)
    async def sinfo(self, interaction: discord.Interaction) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(
            color=interaction.guild.owner.top_role.color
        )
        format = "%a, %d %b %Y | %H:%M:%S %ZGMT"
        text_channels = len(interaction.guild.text_channels)
        voice_channels = len(interaction.guild.voice_channels)
        categories = len(interaction.guild.categories)
        channels = text_channels + voice_channels
        embed.set_thumbnail(url=str(interaction.guild.icon))
        embed.add_field(name=f"Information About **{interaction.guild.name}**: ", value=f":white_small_square: ID: **{interaction.guild.id}** \n:white_small_square: Owner: **{interaction.guild.owner}**\n:white_small_square: Creation: **{interaction.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{interaction.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(interaction.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in interaction.guild.features)} \n:white_small_square: Splash: {interaction.guild.splash}")
        await interaction.followup.send(embed=embed)


# end

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(info(bot))
