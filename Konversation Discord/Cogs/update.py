import discord
from discord.ext import commands
import time


class test(commands.Cog, name="ping command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

        
	@commands.command()
	async def update(self, ctx):
		await ctx.send('_**This Bot Is Under Dev. The Next Update Of Konversation Will Be**_ **October 23**')

def setup(bot:commands.Bot):
	bot.add_cog(test(bot))