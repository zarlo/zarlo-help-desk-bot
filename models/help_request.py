from mongoengine import StringField, BooleanField, Document, EmbeddedDocumentListField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField
from models.embedded_chatlog import EmbeddedChatlog
import datetime

from enum import IntEnum

class Help_Request_Status(IntEnum):
    Closed  = -1
    Pending = 0
    Open = 1

class Help_Request(Document):
    channel_id     = IntField()
    request_user   = StringField()
    request_status = IntField(default=Help_Request_Status.Pending)
    include_groups = ListField(StringField())
    include_users  = ListField(StringField())
    request_create = DateTimeField(default=datetime.datetime.utcnow)
    request_closed = DateTimeField(default=None)
    chat_log       = EmbeddedDocumentListField(EmbeddedChatlog)
