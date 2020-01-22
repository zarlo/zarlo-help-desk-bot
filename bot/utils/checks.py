from discord.ext import commands
from models.guild import Guild
import discord.utils

def is_dev_check(author):
    return author.id in [109843425402056704, 474638819866705960]

def is_dev():
    return commands.check(lambda ctx: is_dev_check(ctx.message.author))


def has_modules(module):
    return commands.check(lambda ctx: has_modules_check(ctx, module))

def has_modules_check(ctx, module):
    try:
        m = Guild.objects.get(guild_id=ctx.guild.id)
        if module in m.modules:
            return True
    except:
        pass
    
    return False
    

def permissions(perms):
    return commands.check(lambda ctx: permissions_check(ctx, perms))

def permissions_check(ctx, perms):
    msg = ctx.message
    if is_dev_check(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def role_or_permissions(check, **perms):
    return commands.check(lambda ctx: role_or_permissions_check(ctx, check, perms))

def role_or_permissions_check(ctx, check, perms):
    
    ch = ctx.message.channel

    if permissions_check(ctx, perms):
        return True

    if ctx.guild.owner.id is ctx.message.author.id:
        return True

    author = ctx.message.author
    role = discord.utils.find(check, author.roles)
    return role is not None
