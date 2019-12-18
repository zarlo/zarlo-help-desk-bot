from discord.ext import commands

def register_commands():
    bot = commands.Bot(command_prefix='!')
    return bot