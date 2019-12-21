from app.utils.checks import is_dev, is_dev_check
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member
from app.utils.checks import role_or_permissions

class admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='admin')
    @role_or_permissions("admin")
    async def admin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('\n base admin command')

    @admin.command()
    async def nick(self, ctx, *, nick_name: str):
        me = ctx.message.guild.me
        await self.bot.change_nickname(me, nick_name)
        await ctx.send('\n bot nick name is now {0}'.format(nick_name))
        


def setup(bot):
    bot.add_cog(admin(bot))
    
def teardown(bot):
    bot.remove_cog('admin')