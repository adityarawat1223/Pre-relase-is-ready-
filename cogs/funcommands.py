import discord
from discord import Member, app_commands 
from discord.ext import commands
import datetime
import asyncio
from discord.ext.commands.cooldowns import BucketType 


class funcommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="busted" , description= "Bust a User")
    @app_commands.guild_only()
    @app_commands.checks.cooldown(1, 15.0, key=lambda i: (i.guild_id, i.user.id))

    
    async def busted(self ,interaction: discord.Interaction , user : discord.Member):
        await interaction.response.defer(ephemeral = False, thinking = True)
        await interaction.followup.send( f"**{user} Got Busted Go To Horny Jail\n**https://tenor.com/view/busted-gif-5100301")

    @busted.error
    async def on_busted_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.followup.send("Command is On cooldown Try Again later or i will add icecream in your Ramen")


    @app_commands.command(name="hug" , description= "hug someone")
    @app_commands.guild_only()
    @app_commands.checks.cooldown(1, 15.0, key=lambda i: (i.guild_id, i.user.id))

    
    async def hug(self ,interaction: discord.Interaction , user : discord.Member):
         await interaction.response.defer(ephemeral = False, thinking = True)
         await interaction.followup.send(f"**Pov :- {interaction.user} stabbed you on back no more hugs for you rip**")

    @hug.error
    async def on_hug_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.followup.send("**Calm Down Dude you cant hug every second it makes you look SUS**")
     








#end

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(funcommands(bot))