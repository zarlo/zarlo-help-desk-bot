from mongoengine import StringField, BooleanField, Document, EmbeddedDocumentListField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField, ReferenceField
import datetime

from modules.guild import Guild

class ChannelConfig(EmbeddedDocument):
    channel_id         = IntField()
    default_add_Groups = ListField(IntField())
    default_add_Users  = ListField(IntField())


class Config(Document):
    guild              = ReferenceField(Guild)
    channel_configs    = EmbeddedDocumentListField(ChannelConfig)
    default_add_Groups = ListField(IntField())
    default_add_Users  = ListField(IntField())
    