from mongoengine import StringField, BooleanField, Document, EmbeddedDocumentListField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField

class Poll(Document):
    channel_id     = IntField()
    mesage_id      = IntField()
    request_user   = StringField()
    timeout        = DateTimeField(default=None)
    status         = BooleanField(default=True)
    options        = ListField(StringField())