from mongoengine import StringField, BooleanField, Document, ReferenceField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField
from .Modules import Modules
import datetime

from enum import IntEnum

class Guild(Document):
    guild_id       = IntField()
    nick_name      = StringField(default="")
    command_prefix = StringField(default="!")
    modules        = ListField(StringField())
    
    