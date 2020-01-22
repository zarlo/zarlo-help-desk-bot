from bot.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

class reload_core(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load_core', hidden=True)
    @is_dev()
    async def load_core(self, ctx):
        """Reloads a module."""
        try:
            self.bot.unload_extension('bot.modules.core')
            self.bot.load_extension('bot.modules.core')
        except Exception as e:
            await ctx.send('\nCore Module could not be reloaded.')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\nCore Module has been reloaded.')

    @commands.command(name='reload_core', hidden=True)
    @is_dev()
    async def reload_core(self, ctx):
        """Reloads a module."""
        try:
            self.bot.unload_extension('bot.modules.core')
            self.bot.load_extension('bot.modules.core')
        except Exception as e:
            await ctx.send('\nCore Module could not be reloaded.')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\nCore Module has been reloaded.')


def setup(bot):
    bot.add_cog(reload_core(bot))
    
def teardown(bot):
    bot.remove_cog('reload_core')