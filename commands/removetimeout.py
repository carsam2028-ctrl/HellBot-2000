import discord
from discord import app_commands
from discord.ext import commands


class RemoveTimeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="untimeout", description="Un-time outs selected user")
    @app_commands.checks.has_permissions(mute_members=True, moderate_members=True)
    @app_commands.describe(reason="Reason to unmute this user.")
    @app_commands.guild_only
    async def mute(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await interaction.response.defer(ephemeral=False)
        duration = None
        if member == interaction.user:
            await interaction.followup.send("You cannot un-time out yourself!", ephemeral=True)
        if not member.is_timed_out():
            await interaction.followup.send("User is not timed out!")
        await member.timeout(duration, reason=reason)
        await interaction.followup.send(f"{member} has been untimed out. Reason: {reason}", ephemeral=False)

async def setup(bot):
    await bot.add_cog(RemoveTimeout(bot))