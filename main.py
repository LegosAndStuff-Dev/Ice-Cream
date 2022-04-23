import discord
import os
from discordToken import discordToken
from discord.ext import commands

client = discord.Client()

# the bot prefix
bot = commands.Bot(command_prefix="ice!", case_insensitive=True)
bot.remove_command("help")

# start
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    #await bot.change_presence(activity=discord.Game(name="Just started up!"))
    #await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Game(name='with 🍦'))


token = discordToken()
bot.run(token)