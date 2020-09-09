from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command(name='clear', help=': clear messages')
    async def clear(self,ctx, number=1):
        try:
            await ctx.channel.purge(limit=number+1)
        except:
            print('error during clear command')
def setup(bot):
    bot.add_cog(Moderation(bot))