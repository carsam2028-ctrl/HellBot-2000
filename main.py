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
        await self.tree.sync(guild=discord.Object(id=1504288510650093570))
        print(signature_print + 'Synced Commands in Home Server!')
        await bot.change_presence(activity=discord.Game(name="In Development"))
        print(signature_print + f"{bot.user.name} presence set!")


bot = HellBot(command_prefix='CB!', intents=intents)

#Loop
bot.run(token=DISCORD_TOKEN)