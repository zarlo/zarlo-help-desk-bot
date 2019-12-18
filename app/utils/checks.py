from discord.ext import commands
import discord.utils

def is_dev_check(message):
    return message.author.id == '109843425402056704'

def is_dev():
    return commands.check(lambda ctx: is_dev_check(ctx.message))

def check_permissions(ctx, perms):
    msg = ctx.message
    if is_dev_check(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def role_or_permissions(ctx, check, **perms):
    if check_permissions(ctx, perms):
        return True

    ch = ctx.message.channel
    author = ctx.message.author
    if ch.is_private:
        return False

    role = discord.utils.find(check, author.roles)
    return role is not None
