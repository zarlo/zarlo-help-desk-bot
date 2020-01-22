from mongoengine import StringField, BooleanField, Document, EmbeddedDocumentListField
from mongoengine import EmbeddedDocument, DateTimeField, IntField, ListField

class Modules(Document):
    name   = StringField(unique=True)
    disabled = BooleanField(default=True)
