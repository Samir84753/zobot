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
    @commands.command(name='urban',help=": urban definition")
    async def urban(self,ctx,*,search='urban'):
        session = aiohttp.ClientSession()
        await ctx.trigger_typing()
        try:
            url=self.url+str(search)
            defn=requests.get(url).json()

            if len(defn['list'])>=2:
                definition_One=defn['list'][0]['definition']
                example_One=defn['list'][0]['example']
                definition_Two=defn['list'][1]['definition']
                example_Two=defn['list'][1]['example']
                embedmsg = discord.Embed(title="Urban Definition",colour=discord.Colour.blue())
                embedmsg.add_field(name='Word',value=search,inline=False)
                embedmsg.add_field(name='Definition 1',value=definition_One,inline=False)
                embedmsg.add_field(name='Example 1',value=example_One,inline=False)
                embedmsg.add_field(name='Definition 2',value=definition_Two,inline=False)
                embedmsg.add_field(name='Example 2',value=example_Two,inline=False)
        
                await ctx.send(embed=embedmsg)
            elif len(defn['list'])==1:
				definition_One=defn['list'][0]['definition']
                example_One=defn['list'][0]['example']

                embedmsg = discord.Embed(title="Urban Definition",colour=discord.Colour.blue())
                embedmsg.add_field(name='Word',value=search,inline=False)
                embedmsg.add_field(name='Definition',value=definition_One,inline=False)
                embedmsg.add_field(name='Example',value=example_One,inline=False)
        
                await ctx.send(embed=embedmsg)
			
            else:
                await ctx.send('No result found.')
        except:
            await ctx.send('Error connecting to Urban Dictionary.')
        
        
        await session.close()
def setup(bot):
    bot.add_cog(Urban_dictionary_commands(bot))
