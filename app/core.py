from discord.ext import commands
from mongoengine import connect
from app.modules.core.Guild import Guild
import discord
import os
    
    
def MONGODB_URI():
    if os.environ.get('DB_USER', False):
        return 'mongodb://{0}:{1}@{2}'.format(os.environ.get('DB_USER', None), os.environ.get('DB_PASS', None), os.environ.get('DB_HOST', "127.0.0.1"))
    return 'mongodb://{0}'.format(os.environ.get('DB_HOST', "127.0.0.1"))

async def get_prefix(bot, message):
    guild = message.guild
    if guild:
        try:
            command_prefix = Guild.objects.get(guild_id=guild.id).command_prefix
            if command_prefix:
                return command_prefix
        except:
            pass
    return '!'

connect(os.environ.get('DB_DB', "zhdb"), host=MONGODB_URI())
bot = commands.Bot(command_prefix=get_prefix, description="a bot that zarlo use'")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('app.modules.core')
bot.load_extension('app.modules.reload_core')