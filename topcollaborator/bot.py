import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os 
import sys
from discord.ext import commands
from discord.ext.commands import CommandNotFound
load_dotenv()
client=commands.Bot(command_prefix='$')
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="$help"))
async def on_disconnect():
    general_channel = client.get_channel(os.getenv('general_channel'))
    await general_channel.send('Bye')



@client.event
async def on_command_error(ctx, error):
    await ctx.trigger_typing()
    if isinstance(error, CommandNotFound):
        await ctx.send('Uhh! There is no command of such sort. Try:"$help"')
    

# @client.command(name='greet',help=': simple greeting')
# async def simple(ctx):
#     await ctx.send('ok ok ok')
client.load_extension('cogs.reddit_commands')
client.load_extension('cogs.gif_commands')
client.load_extension('cogs.moderation')
client.load_extension('cogs.fpl')
client.load_extension('cogs.roast_and_compliment')
client.run(os.getenv("discord_token"))
