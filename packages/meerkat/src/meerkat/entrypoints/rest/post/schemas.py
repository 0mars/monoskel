from marshmallow import fields, Schema

from meerkat.domain.post.entities import Post


class PostSchema(Schema):
    class Meta:
        ordered = True

    id: fields.Str = fields.Str()
    title: fields.Str = fields.Str(required=True)
    body: fields.Str = fields.Str(required=True)

    @classmethod
    def from_domain_object(cls, post: Post):
        object = cls()
        # object.id = str(post.id)
        # object.title = str(post.title)
        # object.body = str(post.body)
        return object.load({
            "id": str(post.id),
            "title": str(post.title),
            "body": str(post.body)
        })


class AddNewPostSchema(Schema):
    class Meta:
        ordered = True

    title: fields.Str = fields.Str(required=True)
    body: fields.Str = fields.Str(required=True)
