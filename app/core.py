from discord.ext import commands
from app.commands import register_commands
from mongoengine import connect
from .config import config
import discord


connect(config.MONGODB_DB, host=config.MONGODB_URI)
bot = commands.Bot(command_prefix='!', description="")

bot.load_extension('app.modules.admin')