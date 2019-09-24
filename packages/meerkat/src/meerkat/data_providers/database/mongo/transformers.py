from meerkat.data_providers.database.mongo.documents import PostDocument
from meerkat.domain.post.entities import Post
from meerkat.domain.post.value_objects import Id, Title, Body


class PostDocumentTransformer:
    def transform_to_document(self, post: Post) -> PostDocument:
        return PostDocument(id=post.id.value, title=post.title.value, body=post.body.value,
                            published=post.is_published())

    def transform_to_domain_object(self, post_document: PostDocument) -> Post:
        post = Post.create(Id(post_document.id), Title(post_document.title), Body(post_document.body))
        post.published = post_document.published
        return post
