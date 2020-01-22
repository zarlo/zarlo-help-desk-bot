from bot.utils.checks import is_dev, is_dev_check, role_or_permissions
from discord.ext import commands, tasks
from discord.ext.commands import Cog
from models.guild import Guild

class Chat_Fliter(Cog):
    def __init__(self, bot):
        pass


def setup(bot):
    bot.add_cog(Chat_Fliter(bot))
    
def teardown(bot):
    bot.remove_cog('Chat_Fliter')