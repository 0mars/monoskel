from mongoengine import Document
from mongoengine.fields import StringField, UUIDField, BooleanField


class PostDocument(Document):
    id = UUIDField(binary=False, primary_key=True)
    title = StringField(max_length=512, required=True)
    body = StringField(max_length=1024, required=True)
    published = BooleanField()


