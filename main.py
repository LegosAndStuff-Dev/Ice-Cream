import discord
import os
from discordToken import discordToken
from discord.ext import commands

client = discord.Client()

# the bot prefix
bot = commands.Bot(command_prefix="i!", case_insensitive=True)
bot.remove_command("help")

# start
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    #await bot.change_presence(activity=discord.Game(name="Just started up!"))
    #await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Game(name='with 🍦'))

    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{fn[:-3]}")
                print(f"loaded {fn[:-3]} cog")

            except Exception as e:
                print(e)


token = discordToken()
bot.run(token)