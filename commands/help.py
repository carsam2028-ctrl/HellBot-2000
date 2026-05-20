import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Shows commands.")
    async def help_cmd(self, interaction: discord.Interaction):
        embed_help_cmd = discord.Embed(title="Commands", color=discord.Color.purple(), description="Undesignated shall protect Super Earth!")
        embed_help_cmd.add_field(name="SEMFTD", value="Abbreviated for 'Super Earth Message For The Day'", inline=False)
        embed_help_cmd.add_field(name="Ping", value="Shows bot latency.", inline=False)
        embed_help_cmd.add_field(name="Staff Commands:", value="")
        embed_help_cmd.add_field(name="Timeout", value="Times someone out, Only available users with permissions.", inline=False)
        embed_help_cmd.add_field(name="Untimeout", value=" Removes someones timeout, Only available for users with permissions.", inline=False)
        embed_help_cmd.set_author(name="SEAF Undesignated", icon_url=bot.user.avatar.url)
        await interaction.response.send_message(embed=embed_help_cmd)

async def setup(bot):
    await bot.add_cog(Help(bot))