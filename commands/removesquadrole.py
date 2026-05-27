import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
from discord.utils import get

class RemoveSquadRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="remove_squad_role", description="Removes the members squad role.")
    async def removesquadrole(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]):
        await interaction.response.defer()
        if reason is None:
            reason = "No reason provided"
        squad_role = [member.guild.get_role(1507894552768282664) and member.guild.get_role(1507894704061288468)]
        if squad_role in member.roles:
            await member.remove_roles(squad_role, reason=reason)
            await interaction.followup.send(f"{member.name}'s role has been removed!")
        else:
            await interaction.followup.send(f"{member.name} does not have a squad role.")
async def setup(bot):
    await bot.add_cog(RemoveSquadRole(bot))