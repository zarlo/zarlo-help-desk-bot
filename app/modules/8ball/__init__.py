from app.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member

import random

class _8ball(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.msg = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.'
            
        ]
        
        print("8ball {0}".format(len(self.msg)))

    @commands.command(name='8ball')
    async def run(self, ctx):
        await ctx.send('\n:8ball: {0}'.format(self.msg[random.randint(1, len(self.msg) - 1)]))



def setup(bot):
    bot.add_cog(_8ball(bot))
    
def teardown(bot):
    bot.remove_cog('_8ball')