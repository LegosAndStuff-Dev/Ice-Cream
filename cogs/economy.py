import discord
import os
from discord.ext import commands
from discord.ext.commands import BucketType
from Disecon import *
import asyncio
import random
import math
import sqlite3

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        view = results.view(user_ID=ctx.message.author.id)
        
        wallet = view.wallet()
        bank = view.bank()
        
        embed: discord.Embed = discord.Embed(
            title="Balace",
            description=f"{ctx.message.author.mention} Balance\n\nWallet Amount: **{wallet}**\n\nBank Amount: **{bank}**",
            color=discord.Color.green()
        )
        
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def work(self, ctx):
        number = int(random.randint(5, 25))
        
        wallet = money.wallet(amount=number, user_ID=ctx.message.author.id)
        wallet.add()
            
        embed: discord.Embed = discord.Embed(
            title="Work",
            description=f"You gained **{number}** coins form working",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)
        

    @commands.command(aliases=['dep'])
    async def deposit(self, ctx, what: str = None):
        view = results.view(user_ID=ctx.message.author.id)
        
        if what == None:
            await ctx.send("Invalid use of command do **d/dep all** or **d/dep [number]**")
            
        else:
            what_check = what.isdigit()
            
            if what_check == True:
                what = int(what)
                
                if view.wallet() >= what:
                    wallet = money.wallet(amount=what, user_ID=ctx.message.author.id)
                    wallet.sub()
                    
                    bank = money.bank(amount=what, user_ID=ctx.message.author.id)
                    bank.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Deposit",
                        description=f"You deposited **{what}** coins into your bank",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                else:
                    await ctx.send("You don't have that many coins in your wallet")
                
            if what_check == False:
                all = view.wallet()
                
                wallet = money.wallet(amount=all, user_ID=ctx.message.author.id)
                wallet.sub()
                
                bank = money.bank(amount=all, user_ID=ctx.message.author.id)
                bank.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Deposit",
                    description=f"You deposited **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await ctx.send(embed=embed)
        

    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, what: str = None):
        view = results.view(user_ID=ctx.message.author.id)
        
        if what == None:
            await ctx.send("Invalid use of command do **d/with all** or **d/with [number]**")
            
        else:
            what_check = what.isdigit()
            
            if what_check == True:
                what = int(what)
                
                if view.bank() >= what:
                    bank = money.bank(amount=what, user_ID=ctx.message.author.id)
                    bank.sub()
                    
                    wallet = money.wallet(amount=what, user_ID=ctx.message.author.id)
                    wallet.add()
                    
                    embed: discord.Embed = discord.Embed(
                        title="Withdraw",
                        description=f"You withdrew **{what}** coins into your wallet",
                        color=discord.Color.green()
                    )
                    
                    await ctx.send(embed=embed)
                    
                else:
                    await ctx.send("You don't have that many coins in your bank")
            
            elif what_check == False:
                all = view.bank()
                
                bank = money.bank(amount=all, user_ID=ctx.message.author.id)
                bank.sub()
                
                wallet = money.wallet(amount=all, user_ID=ctx.message.author.id)
                wallet.add()
                
                embed: discord.Embed = discord.Embed(
                    title="Withdraw",
                    description=f"You withdrew **{all}** coins into your bank",
                    color=discord.Color.green()
                )
                
                await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Economy(bot))