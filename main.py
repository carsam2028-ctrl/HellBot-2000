#Imports
import os
import discord
import dotenv
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
load_dotenv()

#Variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
intents.message_content = True
signature_print = "[HellBot] "

#Bot Startup
class HellBot(commands.Bot):
    async def on_ready(self):
        print(signature_print + f'Logged on as {self.user}!')
        await self.tree.sync()
        print(signature_print + 'Synced Commands Globally!')
        await self.tree.sync(guild=discord.Object(id=1442700064136101908))
        print(signature_print + 'Synced Commands in Home Server!')
        await bot.change_presence(activity=discord.Game(name="For Super Earth!!"))
        print(signature_print + f"{bot.user.name} presence set!")

bot = HellBot(command_prefix='CB!', intents=intents)
#Error Handler
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    err_msg = ""
    print(signature_print + f"Error: {str(error)}")
    if isinstance(error, app_commands.CommandInvokeError):
        error = error.original
        err_msg = "An error has occurred, please try again."
    elif isinstance(error, app_commands.MissingPermissions):
        err_msg = "You do not have the necessary permission(s) for this command."
    elif isinstance(error, app_commands.BotMissingPermissions):
        err_msg = "Bot does not have required permission(s)."
    elif isinstance(error, discord.HTTPException):
        err_msg = "An HTTP Exception has occurred, try again."
    elif isinstance(error, discord.HTTPException) and error.status == 429:
        err_msg = "We are being rate limited, please try again after a couple seconds."
    else:
        err_msg = f"A fatal error has occurred: {str(error)}"


    if interaction.response.is_done():
        await interaction.followup.send(f"{err_msg}", ephemeral=True)
    else:
        await interaction.response.send_message(f"{err_msg}", ephemeral=True)


#Commands
@bot.tree.command(name="mute", description="Mutes selected user")
@app_commands.checks.has_permissions(mute_members=True)
async def mute(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.defer()

#Bot Startup P2
bot.run(token=DISCORD_TOKEN)