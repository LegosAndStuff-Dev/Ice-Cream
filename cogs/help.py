import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Help Command
    @commands.command()
    async def help(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="**Help**",
            description="Below are all the help commands that you can do to see all the different commands that we have.",
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Help(client))   