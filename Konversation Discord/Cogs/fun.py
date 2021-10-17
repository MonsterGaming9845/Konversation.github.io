import discord
from discord.ext import commands
import random
from discord.ext.commands.core import command

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['Yes!', 'No!', 'Maby?', 'Yeh!', 'Without A Doubt Yes!', 'Bad Luck No!', 'Nice Luck Yes!']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def flip(self, ctx, *, question):
        responses = ['Yes!', 'No!', 'Try Once Again', 'Yeh!', '**Whers The Coin?** *Reflip*']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(fun(client))