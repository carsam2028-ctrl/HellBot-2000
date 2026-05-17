#Imports
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from datetime import timedelta
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
    elif isinstance(error, discord.Forbidden):
        error = error.original
        err_msg = "Bot missing permissions."
    else:
        err_msg = f"A fatal error has occurred: {str(error)}"


    if interaction.response.is_done():
        await interaction.followup.send(f"{err_msg}", ephemeral=True)
    else:
        await interaction.response.send_message(f"{err_msg}", ephemeral=True)


#Commands
@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency: {round(bot.latency * 1000)}ms")

@bot.tree.command(name="timeout", description="Timeouts selected user")
@app_commands.checks.has_permissions(mute_members=True, moderate_members=True)
@app_commands.describe(time="Time (in minutes) you want to timeout this person.")
@app_commands.describe(member="Person you want to timeout.")
@app_commands.describe(reason="Reason to timeout this user.")
async def mute(interaction: discord.Interaction, member: discord.Member, time: int, reason: str):
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

@bot.tree.command(name="untimeout", description="Un-time outs selected user")
@app_commands.checks.has_permissions(mute_members=True, moderate_members=True)
@app_commands.describe(reason="Reason to unmute this user.")
async def mute(interaction: discord.Interaction, member: discord.Member, reason: str):
    await interaction.response.defer(ephemeral=False)
    duration = None
    if member == interaction.user:
        await interaction.followup.send("You cannot un-time out yourself!", ephemeral=True)
    if not member.is_timed_out():
        await interaction.followup.send("User is not timed out!")
    await member.timeout(duration, reason=reason)
    await interaction.followup.send(f"{member} has been untimed out. Reason: {reason}", ephemeral=False)

@bot.tree.command(name="semftd", description="Super Earth Messages for the day")
async def semftd(interaction: discord.Interaction):
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

@bot.tree.command(name="purge", description="Purge messages")
@app_commands.describe(amount="How many messages you want to purge (1-100)")
@app_commands.checks.has_permissions(manage_messages=True)
async def purge(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(ephemeral=True)

    if 100 > amount < 1:
        await interaction.followup.send("Whoa, you aren't trying to destroy the bot are you?", ephemeral=True)
    else:
        deleted_msg = await interaction.channel.purge(limit=amount, reason=f"{interaction.user.display_name} used purge command.", check=lambda msg: not msg.pinned)
        await interaction.followup.send(f"{len(deleted_msg)} message(s) deleted.", ephemeral=True)

#Bot Startup P2
bot.run(token=DISCORD_TOKEN)