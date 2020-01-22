from bot.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

class Poll(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def poll_make(self, ctx, *, data : str, option0 : str = None, option1 : str = None, option2 : str = None, option3 : str = None ):

        if option0 is not None:
            msg = '{0}|\n\r'.format(data)
            msg = '{0} {1} :one:\n\r'.format(msg, option0)
            msg = '{0} {1} :two:\n\r'.format(msg, option1)
            if option2:
                msg = '{0} {1} :three:\n\r'.format(msg, option2)
            if option3:
                msg = '{0} {1} :four:\n\r'.format(msg, option3)
                                
            poll_msg = await ctx.send('\n{0}'.format(msg.replace('"', '')))
            await poll_msg.add_reaction(':one:')
            await poll_msg.add_reaction(':two:')
            if option2:
                await poll_msg.add_reaction(':three:')
            if option3:
                await poll_msg.add_reaction(':four:')
        else:
            poll_msg = await ctx.send('\n{0}'.format(data.replace('"', '')))
            await poll_msg.add_reaction(':regional_indicator_n:')
            await poll_msg.add_reaction(':regional_indicator_y:')            


def setup(bot):
    bot.add_cog(Poll(bot))
    
def teardown(bot):
    bot.remove_cog('Poll')