from discord.ext import commands
import requests
import json
import asyncio
import aiohttp
import discord

class Roast_Compliment_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command(name='roast' , help =": insult")
    async def roast(self,ctx,roastee=''):
        session = aiohttp.ClientSession()
        await ctx.trigger_typing()
        url='https://evilinsult.com/generate_insult.php?lang=en&type=json'
        insult=requests.get(url).json()
        await ctx.send(insult['insult'])
        await session.close()
    @commands.command(name='compliment' , help =": compliment")
    async def compliment(self,ctx,user=''):
        session = aiohttp.ClientSession()
        await ctx.trigger_typing()
        url='https://complimentr.com/api'
        compliment=requests.get(url).json()
        await ctx.send(compliment['compliment'])
        await session.close()
def setup(bot):
    bot.add_cog(Roast_Compliment_commands(bot))

