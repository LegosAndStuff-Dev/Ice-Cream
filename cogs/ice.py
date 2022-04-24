from shutil import which
from turtle import title
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
        
    #💩
    #🍓
    #🍦

    @commands.command()
    async def make(self, ctx):
        def check(reaction, user):
            return user == ctx.author

        reactions = ["💩", "🍓", "🍦"]
        ice = ["", "", ""]

        cost = 0

        numScopes = random.randint(1, 3)

        for i in range(3):
            print(i)
            whichIce = random.randint(1, 3)
            
            if whichIce == 1:
                ice[i] = "Vanilla Scope"
                cost += 5

            elif whichIce == 2:
                ice[i] = "Choclate Scope"
                cost += 6

            elif whichIce == 3:
                ice[i] = "Strawberry Scope"
                cost =+ 7


        embed: discord.Embed = discord.Embed(
            title="Ice Cream Making",
            description="Order *The ticket shows of which order the ice cream needs to be scoped*.",
        )
        embed.add_field(name="Ticket", value=f"{ice[0]}\n{ice[1]}\n{ice[2]}\n\nCost - {cost}")


        msg = await ctx.send(embed=embed)

        for emoji in reactions:
            await msg.add_reaction(emoji)
    
        for i in range(3):
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            print(reaction)

            await msg.remove_reaction(reaction, user)
        
    
def setup(bot):
	bot.add_cog(Ice(bot)) 