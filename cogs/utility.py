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


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    #Feedback Command -feedback
    @commands.command()
    async def feedback(self, ctx, *, message=None):
        feedback = self.bot.get_channel(840422064975249418)
        user_id = ctx.message.author.id
        user_name = ctx.message.author

        if message == None:
            await ctx.send("Please provide some feedback that we can improve on!")
        
        else:
            embed: discord.Embed = discord.Embed(
                title="Feedback",
                description=f"<@!{user_id}> gave some feedback!",
                color=discord.Color.green()
            )
            embed.add_field(name="User Name:", value=f"{user_name}")
            embed.add_field(name="User ID:", value=f"{user_id}")
            embed.add_field(name="Feedback:", value=message, inline=False)

            await feedback.send(embed=embed)

            await ctx.send("Feedback Was Submitted!")

    #Bot Command -bot
    @commands.command()
    async def bot(self, ctx):
        bot_version = "0.0.0"
        servers = len(self.bot.guilds)
        members = sum([len(guild.members) for guild in self.bot.guilds])
        dev = "LegosAndStuff#0501"

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
    

    #Ping Command -ping
    @commands.command(aliases=['latency', 'lag'])
    async def ping(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=":ping_pong: pong!",
            description=f'The Latency is {round(self.bot.latency * 1000)}ms',
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)


    #Bug Command -bug
    @commands.command()
    async def bug(self, ctx, *, message=None):
        bug = self.bot.get_channel(842160990196203520)
        user_id = ctx.message.author.id
        user_name = ctx.message.author

        if message == None:
            await ctx.send("Please report the bug after you do the command.")

        else:
            embed: discord.Embed = discord.Embed(
                tilte="Bug Report",
                description=f"<@!{user_id}> Has reported a bug!!",
                color=discord.Color.green() 
            )
            embed.add_field(name="User Name:", value=f"{user_name}")
            embed.add_field(name="User ID:", value=f"{user_id}")
            embed.add_field(name="Bug:", value=message, inline=False)

            await bug.send(embed=embed)

            await ctx.send("The bug was reported!")
    

    #Servers Command -servers
    @commands.command()
    async def servers(self, ctx):
        servers = len(self.bot.guilds)

        await ctx.send(f"I'm in ``{servers}`` servers!")

    
    #Support Command -support
    @commands.command()
    async def support(self, ctx):
        await ctx.send("If you ever need support with Dinosaur join with the link bellow\nhttps://discord.gg/KxPuFvazuF")


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