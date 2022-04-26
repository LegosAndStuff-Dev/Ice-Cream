import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
import asyncio
import random
import math
from jinja2 import pass_context
import psutil
import time
from Disecon import *
import sqlite3


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

        userChoice = 0
        botChoice = 0

        makeIceCreamCorrect = True

        numScopes = random.randint(1, 3)

        for i in range(3):
            whichIce = random.randint(1, 3)
            
            if whichIce == 1:
                ice[i] = "Vanilla Scope"
                cost += 5

            elif whichIce == 2:
                ice[i] = "Choclate Scope"
                cost += 6

            elif whichIce == 3:
                ice[i] = "Strawberry Scope"
                cost += 7


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

            await msg.remove_reaction(reaction, user)

            if f'{reaction}' == u'🍦':
                userChoice = 1

            elif f'{reaction}' == u'💩':
                userChoice = 2

            elif f'{reaction}' == u'🍓':
                userChoice = 3
        
            if ice[i] == "Vanilla Scope":
                botChoice = 1

            elif ice[i] == "Choclate Scope":
                botChoice = 2

            elif ice[i] == "Strawberry Scope":
                botChoice = 3

            if makeIceCreamCorrect == False:
                makeIceCreamCorrect = False

            elif botChoice == userChoice:
                makeIceCreamCorrect = True

            elif botChoice != userChoice:
                makeIceCreamCorrect = False

        if makeIceCreamCorrect == True:
            bank = money.bank(amount=cost, user_ID=user.id)
            bank.add()

            await ctx.send(f"You make the ice cream correctly!\n{cost} coins were deposited into your bank!")


        elif makeIceCreamCorrect == False:
            bank = money.bank(amount=cost, user_ID=user.id)
            bank.sub()

            await ctx.send("You make the ice cream wrong\n5 coins will be taken away from your bank.")

        else:
            await ctx.send("There was an error that happened")

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx):
        pass

    @commands.group(invoke_without_command=True)
    async def advertise(self, ctx):
        pass
        #if ctx.invoked_subcommand is None:
        #    await ctx.send('Invalid sub command passed...')

    @advertise.command(name="buy")
    async def advertise_buy(self, ctx):
        print("hi")

    @advertise.command()
    async def use(self, ctx):
        print("hi")


    @commands.group(invoke_without_command = True)
    async def location(self, ctx):
        pass

    @location.command(name="buy")
    async def location_buy(self, ctx):
        cost = 10000


def setup(bot):
	bot.add_cog(Ice(bot)) 