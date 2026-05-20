import discord
from discord import app_commands
from datetime import timedelta, datetime
from discord.ext import commands

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="timeout", description="Timeouts selected user")
    @app_commands.checks.has_permissions(mute_members=True, moderate_members=True)
    @app_commands.describe(time="Time (in minutes) you want to timeout this person.")
    @app_commands.describe(member="Person you want to timeout.")
    @app_commands.describe(reason="Reason to timeout this user.")
    @app_commands.guild_only
    async def mute(self, interaction: discord.Interaction, member: discord.Member, time: int, reason: str):
        await interaction.response.defer(ephemeral=False)
        duration = timedelta(minutes=time)
        if member == interaction.user:
            await interaction.followup.send("You cannot timeout yourself!", ephemeral=True)
        if time < 1:
            await interaction.followup.send("Time cannot be less than 1 minute.", ephemeral=True)
        if member == bot.user:
            await interaction.followup.send("You cannot timeout the bot this way.", ephemeral=True)
        await member.timeout(duration, reason=reason)
        await interaction.followup.send(f"{member} has been timed out for {time} minutes. Reason: {reason}", ephemeral=False)

async def setup(bot):
    await bot.add_cog(Timeout(bot))