from .core import client
from app.commands import register_commands

import os

register_commands()

client.run('your token here')