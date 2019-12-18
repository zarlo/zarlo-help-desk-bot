from .config import config

from mongoengine import connect
import discord

connect(config.MONGODB_DB, host=config.MONGODB_URI)
client = discord.Client()