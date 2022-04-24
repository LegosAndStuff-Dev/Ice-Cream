import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Employee(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def day(self, ctx):
        pay = 800
        cost = 0

        for c in range(50):
            for i in range(3):
                whichIce = random.randint(1, 3)
                
                if whichIce == 1:
                    cost += 5

                elif whichIce == 2:
                    cost += 6

                elif whichIce == 3:
                    cost += 7

        embed: discord.Embed = discord.Embed(
            description=f"An employee made Ice Cream for the day.\n\nCost - {cost}\nPayroll - 800"
        )

        bank = money.bank(amount=cost, user_ID=ctx.message.author.id)
        bank.add()

        bank = money.bank(amount=800, user_ID=ctx.message.author.id)
        bank.sub()

        await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Employee(bot))