import discord
import random
from discord import app_commands
from discord.ext import commands

class Semftd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="semftd", description="Super Earth Messages for the day")
    async def semftd(self, interaction: discord.Interaction):
        await interaction.response.defer()
        semftd1 = "Super Earth liberates those from tyranny and deception!"
        semftd2 = "Automatons are lead under tyranny and control."
        semftd3 = "Helldivers protect our liberty and Managed Democracy!"
        semftd4 = "Squids, Bugs, and Automatons destroy our way of life, stop them!"
        semftd5 = "Report any undemocratic speech to your democracy officer!"
        random_semftd = random.randint(1, 5)
        if random_semftd == 1:
            await interaction.followup.send(semftd1)
        if random_semftd == 2:
            await interaction.followup.send(semftd2)
        if random_semftd == 3:
            await interaction.followup.send(semftd3)
        if random_semftd == 4:
            await interaction.followup.send(semftd4)
        if random_semftd == 5:
            await interaction.followup.send(semftd5)

async def setup(bot):
    await bot.add_cog(Semftd(bot))