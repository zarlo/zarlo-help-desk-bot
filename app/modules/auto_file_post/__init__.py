from app.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

class auto_file_post(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load_core', hidden=True)
    @is_dev()
    async def load_core(self, ctx):
        """Reloads a module."""
        try:
            self.bot.unload_extension('app.modules.core')
            self.bot.load_extension('app.modules.core')
        except Exception as e:
            await ctx.send('\nCore Module could not be reloaded.')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\nCore Module has been reloaded.')

    async def background(self):
        pass


def setup(bot):
    bot.add_cog(auto_file_post(bot))
    
def teardown(bot):
    bot.remove_cog('auto_file_post')