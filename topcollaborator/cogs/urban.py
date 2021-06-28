from discord.ext import commands
import requests
import json
import asyncio
import aiohttp
import discord
class Urban_dictionary_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.url='http://api.urbandictionary.com/v0/define?term='
    @commands.command(name='urban',help=": urban defination")
    async def urban(self,ctx,*,search='urban'):
        session = aiohttp.ClientSession()
        await ctx.trigger_typing()
        try:
            url=self.url+str(search)
            defn=requests.get(url).json()

            if len(defn['list'])>1:
                defination_One=defn['list'][0]['definition']
                example_One=defn['list'][0]['example']
                defination_Two=defn['list'][1]['definition']
                example_Two=defn['list'][1]['example']
                defination_Tnree=defn['list'][2]['definition']
                example_Three=defn['list'][2]['example']

                embedmsg = discord.Embed(title="Urban Defination",colour=discord.Colour.blue())
                embedmsg.add_field(name='Word',value=search,inline=False)
                embedmsg.add_field(name='Defination 1',value=defination_One,inline=False)
                embedmsg.add_field(name='Example 1',value=example_One,inline=False)
                embedmsg.add_field(name='Defination 2',value=defination_Two,inline=False)
                embedmsg.add_field(name='Example 2',value=example_Two,inline=False)
                embedmsg.add_field(name='Defination 3',value=defination_Tnree,inline=False)
                embedmsg.add_field(name='Example 3',value=example_Three,inline=False)
        
                await ctx.send(embed=embedmsg)
            else:
                await ctx.send('No result found.')
        except:
            await ctx.send('Error connecting to UrbanDictionary.')
        
        
        await session.close()
def setup(bot):
    bot.add_cog(Urban_dictionary_commands(bot))