from bot.core import bot
import os

bot.run(os.environ.get('BOT_TOKEN', None))