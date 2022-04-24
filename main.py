import os
import discord
import datetime
from discordToken import discordToken
from discord.ext.commands import BucketType
from discord.ext import commands
from functions.database import *
from Disecon import start
from Disecon import *

client = discord.Client()

# the bot prefix
bot = commands.Bot(command_prefix="ice ", case_insensitive=True)
bot.remove_command("help")

# start
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    #await bot.change_presence(activity=discord.Game(name="Just started up!"))
    #await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Game(name='with 🍦'))

    #start()

    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{fn[:-3]}")
                print(f"loaded {fn[:-3]} cog")

            except Exception as e:
                print(e)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):

        cooldown = int(error.retry_after)

        convert = str(datetime.timedelta(seconds = cooldown))

        embed: discord.Embed = discord.Embed(
            title="Cooldown",
            description=f"The cooldown will last {convert}"
        )

        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandNotFound):
        embed: discord.Embed = discord.Embed(
            title="Invalid Command",
            description="You gave a invalid command\nPlease try doing `d/help` to see some of the commands.\n\nIf you need more support please join the support server where we can help you.\n[Support Server](https://discord.gg/KxPuFvazuF)",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    else:
        print("===============")
        print(error)


token = discordToken()
bot.run(token)