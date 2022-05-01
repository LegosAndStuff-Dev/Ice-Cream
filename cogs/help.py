import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Help Command
    @commands.command()
    async def help(self, ctx, *, arg1 = None):
        if arg1 == None:
            embed: discord.Embed = discord.Embed(
                title="**Help**",
                color=discord.Color.green()
            )
            embed.add_field(name="Ice Cream", value="Want to see all the ice cream related commands do `ice help ice cream`")
            embed.add_field(name="Economy", value="Want to see all the economy commands do `ice help economy`", inline=False)
            embed.add_field(name="Utility", value="Want to see all the utility commands do `ice help utility`", inline=False)

            await ctx.send(embed=embed)

        if arg1.lower() == "ice cream":
            embed: discord.Embed = discord.Embed(
                title="Ice Cream Help"
            )
            embed.add_field(name="Make", value="Make some ice cream with this command `ice make`", inline=False)
            embed.add_field(name="Day", value="""Have a "day" of work with this command `ice day`""", inline=False)
            embed.add_field(name="Advertise", value="See how many advertisements you have do `ice advertise`\n > Buy an ad by doing `ice advertise buy`\n > Use an ad by doing `ice advertise use`", inline=False)
            embed.add_field(name="Location", value="Want to see how many locations you own do `ice location`\n > Want to buy another location do `ice location buy`", inline=False)
            
            await ctx.send(embed=embed)

        elif arg1.lower() == "economy":
            embed: discord.Embed = discord.Embed(
                title="Economy Help",
                color=discord.Color.green()
            )
            embed.add_field(name="Balance", value="Want to see your balance do `ice bal`", inline=False)
            embed.add_field(name="Work", value="Want to do some extra work do `ice word`", inline=False)
            embed.add_field(name="Withdraw", value="Want to withdraw money do `ice with [amount]`", inline=False)
            embed.add_field(name="Deposit", value="Want to deposit money do `ice dep [amount]`", inline=False)

            await ctx.send(embed=embed)

        elif arg1.lower() == "utility":
            embed: discord.Embed = discord.Embed(
                title="Utility Help",
                color=discord.Color.green()
            )
            embed.add_field(name="Bot", value="Look at some bot information by doing `ice bot`")
            embed.add_field(name="Invite", value="Get the bot invite by doing `ice invite`")
            embed.add_field(name="Ping", value="Get the bots ping by doing `ice ping`")
            embed.add_field(name="Servers", value="Get the amount of servers the bot is in by doing `ice servers`")
            embed.add_field(name="Uptime", value="Get the date when the bot was last restarted `ice uptime`")

            await ctx.send(embed=embed)

        

def setup(client):
	client.add_cog(Help(client))   