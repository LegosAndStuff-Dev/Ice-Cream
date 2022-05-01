import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
from dislash.slash_commands import slash_command
from dislash import *
import psutil
import time
from functions.dev import developers
from functions.version import version


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Bot Command -bot
    @commands.command()
    async def bot(self, ctx):
        bot_version = version()
        servers = len(self.bot.guilds)
        members = sum([len(guild.members) for guild in self.bot.guilds])
        dev = developers()

        embed: discord.Embed = discord.Embed(
            title="Bot Infomation",
            description=f"Bot Version - {bot_version}\nServers - {servers}\nMembers - {members}\nBot Developer - {dev}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)


    #Invite command -invite
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("Invite comming soon")

    @commands.command()
    async def github(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Github Link",
            description="https://github.com/LegosAndStuff-Dev/Ice-Cream"
        )

        await ctx.send(embed=embed)

    #Ping Command -ping
    @commands.command(aliases=['latency', 'lag'])
    async def ping(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f'The Latency is {round(self.bot.latency * 1000)}ms',
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)
    

    #Servers Command -servers
    @commands.command()
    async def servers(self, ctx):
        servers = len(self.bot.guilds)

        await ctx.send(f"I'm in ``{servers}`` servers!")

    #Uptime Command -uptime
    @commands.command()
    async def uptime(self, ctx):
        p = psutil.Process(os.getpid())
        p.create_time()

        secUptime = int(p.create_time())

        #<t:1649334120:f>

        uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))

        uptime = f"<t:{secUptime}:f>"

        embed: discord.Embed = discord.Embed(
            title="Uptime",
            description=f"The bot has been online sense {uptime}",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
        
        
    
def setup(bot):
	bot.add_cog(Utility(bot)) 