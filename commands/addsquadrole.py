import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
from discord.utils import get

class AddSquadRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add_squad_role", description="Gives member the specified squad role.")
    async def addsquadrole(self, interaction: discord.Interaction, role: discord.Role, member: discord.Member):
        await interaction.response.defer()
        squad_role = [member.guild.get_role(1507894552768282664) and member.guild.get_role(1507894704061288468)]
        squad_role_id = 1507894552768282664, 1507894704061288468
        if squad_role in member.roles:
            await interaction.followup.send(f"{member.name} already has a squad role!")
        else:
            if role.id not in squad_role_id:
                await interaction.followup.send(f"{role.name} is not a squad role!")
            else:
                await member.add_roles(role)
                await interaction.followup.send(f"{member.name} now has squad role: {role.name}")

async def setup(bot):
    await bot.add_cog(AddSquadRole(bot))