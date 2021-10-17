import discord
from discord.ext import commands
from random import randint

class HelpCog(commands.Cog, name="help command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
		embedVar.add_field(name="!ping", value="Whats The Bots MS? Just Use This Commands", inline=False)
		embedVar.add_field(name="!update", value="When Is The Next Update? Just Type This Command For Info", inline=False)
		embedVar.add_field(name="8Ball", value="Need Some One TO Guess Some Think? Usage : ``!8ball <anyting to guess>``", inline=False)
		embedVar.add_field(name="!flip", value="Yes Or No Choice? Let Me Do It Just Type ``!flip <Any Ting To Guess!>``", inline=False)
		await ctx.channel.send(embed=embedVar)

def setup(bot:commands.Bot):
	bot.remove_command("help")
	bot.add_cog(HelpCog(bot))
