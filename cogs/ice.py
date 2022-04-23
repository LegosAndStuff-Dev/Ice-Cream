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
    async def make(self, ctx):
        def check(reaction, user):
            return user == ctx.author
    
        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

        print(reaction)
        
    
def setup(bot):
	bot.add_cog(Ice(bot)) 