from mongoengine import StringField, BooleanField, Document, EmbeddedDocumentListField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField
import datetime


class EmbeddedChatlog(EmbeddedDocument):
    user = StringField()
    data = StringField()
    sent = DateTimeField(default=datetime.datetime.utcnow)
    change_log = EmbeddedDocumentListField('EmbeddedChatlogEdits')
        
class EmbeddedChatlogEdits(EmbeddedDocument):
    data   = StringField()
    change = DateTimeField(default=datetime.datetime.utcnow)
    
    

