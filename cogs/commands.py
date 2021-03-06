import discord
from discord import Guild, Interaction, Member, app_commands
from discord.ext import commands
import datetime
import asyncio
import time
from discord.ext.commands import MissingPermissions
from discord.app_commands import AppCommandError, CommandInvokeError


class Slash(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="purge", description="clear Messages")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(manage_messages=True)
    async def okok(self, interaction: discord.Interaction, amount: int) -> None:
        await interaction.response.defer(ephemeral=True, thinking=True)

        deleted = await interaction.channel.purge(limit=amount)

       
        logs = self.bot.get_channel(974312836018868264)
        await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} used Purge And delted {len(deleted)} message(s)"))
        await interaction.followup.send(f'Deleted {len(deleted)} message(s)')

    @okok.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7
            , description="<a:dvloper:974560024200351744> **You are missing manage message permission**")
            

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="kick", description="kick User")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(kick_members=True)
    async def Bc(self, interaction: discord.Interaction, user: discord.Member, reason: str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7, 
         description="<a:settings:974560701291057162> You cant Kick A Moderator")
        

        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)

        elif interaction.guild.me.top_role <= user.top_role:
            embed = discord.Embed(color=0x55a7f7,description="<a:settings:974560701291057162> That user is a mod/admin, Try giving me a higher role")
            await interaction.followup.send(embed=embed)
        else:
            embed = discord.Embed(
                color=0x55a7f7, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="If you think this is unfair Join Our Ban appeal Server",
                             icon_url=f"{interaction.user.avatar}")
            embed.add_field(
                name='Kicked', value=f"{user} was kicked \n Reason :- **{reason}** ")
            await user.send(embed=embed)
            await user.kick(reason=reason)
            
            logs = self.bot.get_channel(974312840724889600)
            await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} Kicked {user}\nReason - ``{reason}``"))
            await interaction.followup.send(embed=embed)
    @Bc.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7,
             description="**<a:settings:974560701291057162> You are missing kick members permission**")
            

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="ban", description="Ban A User")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(ban_members=True)
    async def MC(self, interaction: discord.Interaction, user: discord.Member, reason: str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7, 
         description="**<a:settings:974560701291057162> You cant Ban A Moderator**")
        

        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)

        elif interaction.guild.me.top_role <= user.top_role:
            embed = discord.Embed(color=0x55a7f7,description="<a:settings:974560701291057162> That user is a mod/admin, Try giving me a higher role")
            
            logs = self.bot.get_channel(974312840724889600)
            await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} Banned {user}\nReason - ``{reason}``"))
            await interaction.followup.send(embed=embed)
        else:
            embed = discord.Embed(
                color=0x55a7f7, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="If you think this is unfair Join Our Ban appeal Server",
                             icon_url=f"{interaction.user.avatar}")
            embed.add_field(
                name='Banned', value=f"{user} was Banned \n Reason :- **{reason}** ")
            await user.send(embed=embed)
            await user.ban(reason=reason)

            await interaction.followup.send(embed=embed)
            logs = self.bot.get_channel(974312840724889600)
            await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} Banned {user}\nReason - ``{reason}``"))

    @MC.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7, 
             description="**<a:settings:974560701291057162> You are missing ban member Permission**")
            

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="mute", description="Mute A User")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(mute_members=True)
    async def mute(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7
        , description="<a:settings:974560701291057162> You cant Mute A Moderator")
        

        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)

        elif interaction.guild.me.top_role <= user.top_role:
            embed = discord.Embed(color=0x55a7f7,description="<a:settings:974560701291057162> That user is a mod/admin, Try giving me a higher role")
            await interaction.followup.send(embed=embed)

        else:
            role = discord.utils.get(interaction.guild.roles, name="Muted")
            guild = interaction.guild
            if role not in guild.roles:
                perm = discord.Permissions(send_messages=False, speak=False)
                await guild.create_role(name="Muted", permissions=perm)
                await user.add_roles(role)
                embed = discord.Embed(
                    color=0x55a7f7, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text="Sad Noises",
                                 icon_url=f"{interaction.user.avatar}")
                embed.add_field(
                    name='Mute', value=f"{user} was muted\nPlease follow Rules To Avoid Mute next time ")
                await interaction.followup.send(embed=embed)

            else:
                await user.add_roles(role)
                embed = discord.Embed(
                    color=0x55a7f7, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text="User Muted",
                                 icon_url=f"{interaction.user.avatar}")
                embed.add_field(
                    name='Mute', value=f"{user} was muted .Please follow Rules To Avoid Mute next time ")
                
                logs = self.bot.get_channel(974312840724889600)
                await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} Muted {user}"))
                await interaction.followup.send(embed=embed)
    @mute.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7,
             description="<a:settings:974560701291057162> **You are missing mute member permission**")
            

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="unmute", description="unmute members no rickroll  no troll")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(mute_members=True)
    async def unmute(self, interaction: discord.Interaction, user: discord.Member):
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(color=0x55a7f7
        , description="<a:settings:974560701291057162> You cant Unmute a mod ")
        

        if interaction.user.top_role <= user.top_role:
            await interaction.followup.send(embed=embed)

        elif interaction.guild.me.top_role <= user.top_role:
            embed = discord.Embed(color=0x55a7f7,description="<a:settings:974560701291057162> That user is a mod/admin, Try giving me a higher role")
            await interaction.followup.send(embed=embed)

        else:
            unlol = discord.utils.get(interaction.guild.roles, name="Muted")
            await user.remove_roles(unlol)
            embed = discord.Embed(
                color=0x55a7f7, timestamp=datetime.datetime.utcnow())
            
            embed.add_field(
                name='Unmute', value=f"{user} was Unmuted\nNow Be a Good Member ")
            
            logs = self.bot.get_channel(974312840724889600)
            await logs.send(embed = discord.Embed(description=f"{interaction.user.mention} unmuted {user}"))
            await interaction.followup.send(embed=embed)
    @unmute.error
    async def on_app_command_error(self,
                                   interaction: Interaction,
                                   error: AppCommandError):
        await interaction.response.defer(ephemeral=False, thinking=True)

        if isinstance(error, app_commands.MissingPermissions):
            embed = discord.Embed(color=0x55a7f7
            , description="<a:settings:974560701291057162> **You are missing mute member permission to unmute this user**")
            

            await interaction.followup.send(embed=embed)

    @app_commands.command(name="poll", description="choices huh i want to do a poll too")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(embed_links=True)
    async def du(self, interaction: discord.Interaction, topic: str, choice1: str, choice2: str) -> None:
        await interaction.response.defer(ephemeral=False, thinking=True)
        embed = discord.Embed(title=topic, description=f":one: {choice1}\n\n:two: {choice2}",
                              color=interaction.user.color, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f"Poll by {interaction.user.name}")
        embed.set_thumbnail(url=interaction.user.avatar)
        message = await interaction.followup.send(embed=embed)
        await message.add_reaction("1??????")
        await message.add_reaction("2??????")
        await asyncio.sleep(5)

    @app_commands.command(name="poll-result", description="choices huh i want to do a poll too")
    @app_commands.guild_only()
    @app_commands.checks.has_permissions(embed_links=True)
    async def Result(self, interaction: discord.Interaction, messageid: str):
        mc = messageid
        onechoice = [user async for user in mc.reaction[0].users()]
        secchoice = [user async for user in mc.reaction[1].users()]
        result = "Tie"
        if len(onechoice) > len(secchoice):
            result = "choice1"
        elif len(secchoice) > len(onechoice):
            result = "choice2"

        embed = discord.Embed(
            description=f"Result : {result}", color=interaction.user.color, timestamp=datetime.datetime.utcnow())

        await mc.edit(embed)


# end
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Slash(bot))
