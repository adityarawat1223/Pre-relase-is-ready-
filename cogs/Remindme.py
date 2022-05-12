import discord
from discord import  User, app_commands
from discord.ext import commands
import datetime
import asyncio
import time


class reminder(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="reminder" , description= "Set an Reminder , You can use calendar too")
    @app_commands.guild_only()
  
   
    async def reminder(self ,interaction: discord.Interaction, time:str, *, reminder: str):
        await interaction.response.defer(ephemeral = False, thinking = True)
        print(time)
        print(reminder)
      
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())

        embed.set_footer(text="If you have any questions, suggestions or bug reports, please join our support Discord Server", icon_url=f"{interaction.user.avatar}")
        seconds = 0
        if reminder is None:
            embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds == 0:
         embed.add_field(name='Warning',
                        value='Please specify a proper duration, send `reminder_help` for more information.')
        elif seconds < 300:
            embed.add_field(name='Warning',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
        elif seconds > 7776000:
            embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
        else:
         await interaction.followup.send(f"Alright, I will remind you about {reminder} in {counter}.")
         await asyncio.sleep(seconds)
         embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())
         embed.set_footer(text="Sorry for Disturbing you", icon_url=f"{interaction.user.avatar}")
         embed.add_field(name='Reminder', value= f"Hi ,{interaction.user.mention} You asked me to remind you\n Reason :- {reminder} ") 
         await interaction.user.send(embed=embed) 
         await interaction.followup.send(embed=embed)
         return
        await interaction.followup.send(embed=embed)


#end
async def setup(bot) -> None:
  await bot.add_cog(reminder(bot))