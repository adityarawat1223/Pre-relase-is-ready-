import discord
from discord import Guild, Interaction, app_commands
from discord.ext import commands
import datetime
import asyncio
import time
from discord.ext.commands import MissingPermissions
from discord.app_commands import AppCommandError, CommandInvokeError

import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://adityarawat:aditya1200@arson-db.zczt6.mongodb.net/Arson-db?retryWrites=true&w=majority")

databse = cluster["adityarawat"]
collection = databse["Arson-db"]


class warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="warn", description="Warn A User")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(mute_members=True)
    async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(
        ), description="You cant Warn A Moderator")
        embed.set_footer(
            text="Please Consider Reporting Bugs in Official server")

        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)
        else:

            id = user.id
            gd = interaction.guild.id
            if collection.count_documents({'memberid': id,'guildid': gd}) == 0:
                collection.insert_one(
                    {"memberid": id, "guildid": gd, "warns": 0})

            warn_count = collection.find_one({"memberid": id,"guildid": gd})
            count = warn_count["warns"]
            new_count = count + 1
            collection.update_one({'memberid': id,"guildid": gd}, {
                                  "$set": {"warns": new_count}})
            embed = discord.Embed(
                color=0x55a7f7, timestamp=datetime.datetime.utcnow())

            embed.add_field(
                name='Warn', value=f"Warned {user.mention} for **{reason}**\n They now have **{new_count} warns**")
            await interaction.followup.send(embed=embed)

    @warn.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(
            ), description="**ou need atleast mute member perm to use warn**")
            embed.set_footer(
                text="If you think this is an error plz contact Perry the platypus")

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="warnings", description="check total warns of a user")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(mute_members=True)
    async def warnings(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(),description="You cant check warns of this user")
        embed.set_footer(text="If you think this is an error plz contact Perry the platypus")
        
        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)
        
        else:
            id = user.id
            gd = interaction.guild.id
            if collection.count_documents({'memberid':id,"guildid": gd}) == 0:
                collection.insert_one({"memberid":id,"guildid":gd,"warns":0})

            warn_count = collection.find_one({"memberid":id,"guildid": gd})
            count = warn_count["warns"]
            embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())
        
            embed.add_field(name='Warning', value= f"**{user.mention} has Total {count} Warns**") 
            await interaction.followup.send(embed=embed)


    @warnings.error
    async def on_app_command_error(self,
    interaction: Interaction,
    error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error,app_commands.MissingPermissions):
            embed =  discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow(),description="**You need atleast mute member perm to check warn**")
            embed.set_footer(text="Pov You realised You Are not a mod")
            
           
            await interaction.followup.send(embed=embed) 




# end
async def setup(bot) -> None:
    await bot.add_cog(warn(bot))
