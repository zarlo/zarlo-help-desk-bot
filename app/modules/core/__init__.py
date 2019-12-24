from app.utils.checks import is_dev, is_dev_check, role_or_permissions
from discord.ext import commands
from discord.ext.commands import Cog
from discord.member import Member
from app.modules.core.modules import Modules
from app.modules.core.guild import Guild

class Core(Cog):
    def __init__(self, bot):
        self.bot = bot
        print('loading Modules')
        for item in Modules.objects:
            try:
                self.bot.load_extension('app.modules.{0}'.format(item))
            except Exception as e:
                print('{0} could not be loaded.'.format(item))
                print('{}: {}'.format(type(e).__name__, e))
            else:
                print('{0} has been loaded.'.format(item))
        print('done loading Modules')
        
    @commands.command()
    @role_or_permissions("admin owner")
    async def load(self, ctx, *, module : str):
        for item in Modules.objects:
            if item.name is module:  
                Guild.objects(guild_id=ctx.guild.id).update(push__modules=module)
                await ctx.send('\n{0} loaded.'.format(module))
                return
        await ctx.send('\n{0} is not loaded on the bot.'.format(module))
        
    @commands.command()
    @role_or_permissions("admin owner")
    async def unload(self, ctx, *, module : str):
        Guild.objects(guild_id=ctx.guild.id).update(pull__modules=module)
        await ctx.send('\n{0} unloaded.'.format(module))
        
    
    @commands.command(hidden=True)
    @is_dev()
    async def gload(self, ctx, *, module : str):
        """Loads a module."""
        try:
            self.bot.load_extension('app.modules.{0}'.format(module))
        except Exception as e:
            await ctx.send('\nModule could not be loaded.')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\nModule has been loaded.')

    @commands.command(hidden=True)
    @is_dev()
    async def gunload(self, ctx, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension('app.modules.{0}'.format(module))
        except Exception as e:
            await ctx.send('\nModule could not be unloaded.')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\nModule has been unloaded.')

    @commands.command(name='reload', hidden=True)
    @is_dev()
    async def _reload(self, ctx, *, module : str):

        if module is 'all':
            for item in Modules.objects:
                try:
                    self.bot.reload_extension('app.modules.{0}'.format(item))
                except Exception as e:
                    await ctx.send('\n{0} could not be reloaded.'.format(item))
                    await ctx.send('{}: {}'.format(type(e).__name__, e))
                else:
                    await ctx.send('\n{0} has been reloaded.'.format(item))
        else:
            try:
                self.bot.reload_extension('app.modules.{0}'.format(module))
            except Exception as e:
                await ctx.send('\nModule could not be reloaded.')
                await ctx.send('{}: {}'.format(type(e).__name__, e))
            else:
                await ctx.send('\nModule has been reloaded.')

    @commands.command(hidden=True)
    @is_dev()
    async def restart(self, ctx):
        await ctx.send('\n restarting')
        await self.bot.logout()

def setup(bot):
    bot.add_cog(Core(bot))
    
def teardown(bot):
    bot.remove_cog('Core')