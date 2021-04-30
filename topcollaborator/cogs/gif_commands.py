from discord.ext import commands
import discord
import random
import aiohttp
import asyncio
import json
from dotenv import load_dotenv
load_dotenv()
import os 
import sys
from discord.ext import commands

class Gif_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    def test(self,word):
        randomword=random.choice(word)
        gif_choice = random.randint(0, 9)
        return randomword,gif_choice
    #giphy command
    @commands.command(name='giphy' , help =": summons giphy gifs" ,aliases=['gif'])
    async def giphy(self,ctx,search=''):
        await ctx.trigger_typing()
        embed = discord.Embed(colour=discord.Colour.blue())
        session = aiohttp.ClientSession()
        if search == '':
            await ctx.send('Put some search keyword. usage:"$giphy keyword"')
            word=['God no','We dont do that here']
            randomword,gif_choice=self.test(word)
            response = await session.get('http://api.giphy.com/v1/gifs/search?q='+randomword+'&api_key='+os.getenv('giphy_key')+'&limit=10')
            data = json.loads(await response.text())
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
            await ctx.send(embed=embed)
            
        else:
            search.replace(' ', '+')
            response = await session.get(f'http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key='+os.getenv('giphy_key')+'&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
            await ctx.send(embed=embed)

        await session.close()
def setup(bot):
    bot.add_cog(Gif_commands(bot))