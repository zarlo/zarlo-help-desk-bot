from app.utils.checks import is_dev

class Admin:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(hidden=True)
    @checks.is_dev()
    async def load(self, *, module : str):
        """Loads a module."""
        try:
            self.bot.load_extension('app.modules.{0}'.format(module))
        except Exception as e:
            await self.bot.say('\nModule could not be loaded.')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\nModule has been loaded.')

    @commands.command(hidden=True)
    @checks.is_dev()
    async def unload(self, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await self.bot.say('\nModule could not be unloaded.')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\nModule has been unloaded.')

    @commands.command(name='reload', hidden=True)
    @checks.is_dev()
    async def _reload(self, *, module : str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension('app.modules.{0}'.format(module))
        except Exception as e:
            await self.bot.say('\nModule could not be reloaded.')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\nModule has been reloaded.')
