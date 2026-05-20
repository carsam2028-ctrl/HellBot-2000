import discord
from discord import app_commands
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="purge", description="Purge messages")
    @app_commands.describe(amount="How many messages you want to purge (1-100)")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.guild_only
    async def purge(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)
        cmd_user = str(interaction.user.name)
        if 100 > amount < 1:
            await interaction.followup.send("Whoa, you aren't trying to destroy the bot are you?", ephemeral=True)
        else:
            deleted_msg = await interaction.channel.purge(limit=amount, reason=f"{cmd_user} used purge command.", check=lambda msg: not msg.pinned)
            await interaction.followup.send(f"{len(deleted_msg)} message(s) deleted.", ephemeral=False)
            sleep(3.5)
            await interaction.delete_original_response()

async def setup(bot):
    await bot.add_cog(Purge(bot))