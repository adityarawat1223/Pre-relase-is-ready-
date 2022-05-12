import discord
from discord import Embed, Interaction, app_commands
from discord.ext import commands
import datetime
import asyncio
import time
from discord.ext.commands import MissingPermissions
from discord.app_commands import AppCommandError, CommandInvokeError
import animec

class anime(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @app_commands.command(name="anime", description="search a anime")
    @app_commands.guild_only()
    
    async def anime(self, interaction: discord.Interaction, query:str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        try:
            anime = animec.Anime(query)
        except:
            await interaction.followup.send(embed=discord.Embed(color=0x55a7f7,description="**Sorry No anime is found for The search query**"))
            return
        embed = discord.Embed(title=anime.title_english, url = anime.url,description=f"{anime.description[:200]}...",color=0x55a7f7)
        embed.add_field(name="Episodes", value=str(anime.episodes))
        embed.add_field(name="Ratings", value=str(anime.rating))
        embed.add_field(name="Brodcast", value=str(anime.broadcast))
        embed.add_field(name="Type", value=str(anime.type))
        embed.set_thumbnail(url=anime.poster)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name="character", description="search a anime character")
    @app_commands.guild_only()
    async def image(self, interaction: discord.Interaction, query:str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        try:
            char = animec.Charsearch(query)
        except:
            await interaction.followup.send(embed=discord.Embed(color=0x55a7f7,description="**Sorry No anime character is found for The search query**"))

        embed = discord.Embed(title=char.title, url = char.url,color=0x55a7f7)
        embed.set_image(url=char.image_url)
        embed.set_footer(text=",".join(list(char.references.keys())[:2]))
        await interaction.followup.send(embed=embed)


#end
async def setup(bot) -> None:
  await bot.add_cog(anime(bot))