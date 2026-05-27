#Imports
import os
import random
from time import sleep
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import app_commands
from datetime import timedelta, datetime
load_dotenv()

#Variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
intents.message_content = True

#Functions
def signature_print():
    return datetime.now().strftime('[%Y-%m-%d %H:%M:%S]') + " [HellBot] "


#Bot Startup
class HellBot(commands.Bot):
    async def setup_hook(self):
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await self.load_extension(f'commands.{filename[:-3]}')
                print(signature_print() + f'Loaded command: {filename}')

    async def on_ready(self):
        print(signature_print() + f'Logged on as {self.user}!')
        await self.tree.sync()
        print(signature_print() + 'Synced Commands Globally!')
        await self.tree.sync(guild=discord.Object(id=1442700064136101908))
        print(signature_print() + 'Synced Commands in Home Server!')
        await bot.change_presence(activity=discord.Game(name="For Super Earth!!"))
        print(signature_print() + f"{bot.user.name} presence set!")

bot = HellBot(command_prefix='HB!', intents=intents)

#Error Handler
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    err_msg = ""
    if isinstance(error, app_commands.MissingPermissions):
        err_msg = "You do not have the necessary permission(s) for this command."
    if isinstance(error, app_commands.BotMissingPermissions):
        err_msg = "Bot does not have required permission(s)."
    if isinstance(error, discord.HTTPException):
        err_msg = "An HTTP Exception has occurred, try again."
    if isinstance(error, discord.HTTPException) and error.status == 429:
        err_msg = "We are being rate limited, please try again after a couple seconds."
    if isinstance(error, discord.Forbidden):
        err_msg = "Bot missing permissions."
    else:
        if isinstance(error, app_commands.CommandInvokeError):
            error = error.original
            err_msg = "An error has occurred, please try again."
        else:
            err_msg = f"A fatal error has occurred: {str(error)}"

    print(signature_print() + f"Error: {str(error)} \n{signature_print()}What the user saw: '{err_msg}'")

    if interaction.response.is_done():
        await interaction.followup.send(f"{err_msg}", ephemeral=True)
    else:
        await interaction.response.send_message(f"{err_msg}", ephemeral=True)
#Bot Startup P2
bot.run(token=DISCORD_TOKEN)