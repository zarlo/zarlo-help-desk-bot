from app.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

class Debug(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True, name='debug')
    @is_dev()
    async def debug_command(self, ctx):
        await ctx.send(ctx.__dict__)



def setup(bot):
    bot.add_cog(Debug(bot))
    
def teardown(bot):
    bot.remove_cog('Debug')