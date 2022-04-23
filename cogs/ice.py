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


class Ice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def test(self, ctx):
        await ctx.send("hello world")
        
    
def setup(bot):
	bot.add_cog(Ice(bot)) 