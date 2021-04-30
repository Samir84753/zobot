from discord.ext import commands
import discord
import praw
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
class Reddit_commands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.reddit_config = praw.Reddit(client_id = os.getenv('client_id'),
                    client_secret = os.getenv('client_secret'),
                    username = os.getenv('reddit_username'),
                    password = os.getenv('reddit_password'),
                    user_agent = "memebot"
                    )
        self.nsfw_enabled=False
    def test(self,word):
        randomword=random.choice(word)
        gif_choice = random.randint(0, 9)
        return randomword,gif_choice
    #reddit commands
    @commands.command(name='nsfw',hidden=True)
    async def Filter(self,ctx,option=''):
        try:
            if option=='disable':
                self.nsfw_enabled=False
                await ctx.send("NSFW subreddits are now disabled.")
            elif option=='letmeseee':
                self.nsfw_enabled=True
                await ctx.send("NSFW subreddits are now enabled.")
            elif option=='-i':
                await ctx.send("NSFW subreddits are currently enabled" if self.nsfw_enabled else "NSFW subreddits are currently disabled")
            elif option=='':
                await ctx.send("We don't do that here.")
        except:
            print("error2")
    	
    	
    
    @commands.command(name='reddit' ,help=' :summons pictures from reddit',aliases=['r'])
    async def meme(self,ctx,subred = "memes"):
        try:
            session = aiohttp.ClientSession()
            await ctx.trigger_typing()
            subreddit = self.reddit_config.subreddit(subred)
            all_subs=[]
            hot = subreddit.hot(limit=50)
            for submission in hot :
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name=random_sub.title
            url = random_sub.url
            emb = discord.Embed(title = name, url= url)
            emb.set_image(url = url)
            if subreddit.over18:
                
                embed = discord.Embed(colour=discord.Colour.blue())
                if not self.nsfw_enabled:
                    await ctx.send("NSFW content is disabled.")
                    word=['Go away']
                    randomword,gif_choice=self.test(word)
                    response = await session.get('http://api.giphy.com/v1/gifs/search?q='+randomword+'&api_key='+os.getenv('giphy_key')+'&limit=10')
                    data = json.loads(await response.text())
                    embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("NSFW content")
                    await ctx.send(embed = emb)

            elif random_sub.is_self:
                text= random_sub.selftext
                emb = discord.Embed(title = name, url= url)
                emb.set_footer(text = text)
                await ctx.send(embed = emb)
            elif not random_sub.over_18:
                await ctx.send(embed = emb)
            else:
                await ctx.send('Nsfw post')
            await session.close()
        except:
            print("Reddit command error")
            await ctx.send('Maybe there is no subreddit of that name. Try using a real subreddit name. ')
            embed = discord.Embed(colour=discord.Colour.blue())
            session = aiohttp.ClientSession()
            word=['God no','We dont do that here']
            randomword,gif_choice=self.test(word)
            response = await session.get('http://api.giphy.com/v1/gifs/search?q='+randomword+'&api_key='+os.getenv('giphy_key')+'&limit=10')
            data = json.loads(await response.text())
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])
            await session.close()
            await ctx.send(embed=embed)
            


    @commands.command(name='roast' ,help=' :summons random comment roasts from r/roastme',aliases=['ro'])
    async def roast(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subreddit=self.reddit_config.subreddit('roastme')
        hot = subreddit.hot(limit=50)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        random_submission.comment_sort = 'best'
        random_submission.comment_limit = 10
        random_submission.comments.replace_more(limit=0)
        random_comments=[]
        for top_level_comment in random_submission.comments.list():
            random_comments.append(top_level_comment.body)
        await session.close()
        insult=random.choice(random_comments)
        await ctx.send(insult)
    @commands.command(name='til',help=':summons random til, TIL means Today I Learned')
    async def til(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subreddit=self.reddit_config.subreddit('todayilearned')
        hot = subreddit.hot(limit=100)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        post=random_submission.title
        await session.close()
        await ctx.send(post)
        
    @commands.command(name='facts',help=':summons random facts.')
    async def fact(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subreddit=self.reddit_config.subreddit('facts')
        hot = subreddit.hot(limit=110)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        if random_submission.is_self:
            text= random_submission.selftext
            name=random_submission.title
            emb = discord.Embed(title = name)
            emb.set_footer(text = text)
            await ctx.send(embed = emb)
        else:
            pass
        await session.close()
    @commands.command(name='quotes',help=':summons random quotes.')
    async def quote(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subreddit=self.reddit_config.subreddit('quotes')
        hot = subreddit.hot(limit=110)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        if random_submission.is_self:
            text= random_submission.selftext
            name=random_submission.title
            emb = discord.Embed(title = name)
            emb.set_footer(text = text)
            await ctx.send(embed = emb)
        else:
            pass
        await session.close()
    @commands.command(name='protip',help=':summons random protip.')
    async def Protip(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subreddit=self.reddit_config.subreddit('LifeProTips')
        hot = subreddit.hot(limit=60)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        if random_submission.is_self:
            text= random_submission.selftext
            name=random_submission.title
            emb = discord.Embed(title = name)
            emb.set_footer(text = text)
            await ctx.send(embed = emb)
        else:
            pass
        await session.close()
    @commands.command(name='comics',help=':summons random comics.')
    async def comic(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subs=['webcomics','comics','DCcomics']
        subreddit=self.reddit_config.subreddit(random.choice(subs))
        hot = subreddit.hot(limit=100)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        name=random_submission.title
        url = random_submission.url
        emb = discord.Embed(title = name, url= url)
        emb.set_image(url = url)
        await ctx.send(embed = emb)
        await session.close()
    @commands.command(name='food',help=':summons random food pictures.')
    async def food(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        sub=['FoodPorn','food','recipes','Pizza','BBQ','sushi','grilledcheese','ramen']
        subreddit=self.reddit_config.subreddit(random.choice(sub))
        hot = subreddit.hot(limit=80)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        url = random_submission.url
        emb = discord.Embed()
        emb.set_image(url = url)
        await ctx.send(embed = emb)
        await session.close()
    @commands.command(name='motivate',help=':Motivation quotes.')
    async def Motivate(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subs=['motivation','GetMotivated']
        subreddit=self.reddit_config.subreddit(random.choice(subs))
        hot = subreddit.hot(limit=60)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        name=random_submission.title
        url = random_submission.url
        emb = discord.Embed(title = name, url= url)
        emb.set_image(url = url)
        await session.close()
        await ctx.send(embed = emb)

    @commands.command(name='wallpaper',help=':summons random wallpaper.',aliases=['w'])
    async def wallpaper(self,ctx):
        await ctx.trigger_typing()
        session = aiohttp.ClientSession()
        subs=['Art']
        subreddit=self.reddit_config.subreddit(random.choice(subs))
        hot = subreddit.hot(limit=50)
        all_subs=[]
        for submission in hot :
            all_subs.append(submission)
        random_submission = random.choice(all_subs)
        url = random_submission.url
        emb = discord.Embed(url= url)
        emb.set_image(url = url)
        await ctx.send(embed = emb)
        await session.close()
def setup(bot):
    bot.add_cog(Reddit_commands(bot))
