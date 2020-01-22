from bot.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

class ticket(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ticket')
    async def ticket_base(self, ctx):
        await ctx.send('\nCore Module has been reloaded.')

def setup(bot):
    bot.add_cog(ticket(bot))
    
def teardown(bot):
    bot.remove_cog('ticket')