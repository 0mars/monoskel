from injector import inject

from meerkat.domain.post.data_providers import PostDataProvider
from meerkat.domain.post.entities import Post
from meerkat.domain.post.value_objects import Id
from meerkat.domain.post.data_providers.exceptions import EntityNotFoundException
from meerkat.data_providers.database.mongo.transformers import PostDocumentTransformer
from meerkat.data_providers.database.mongo.documents import PostDocument


class PostMongoRepository(PostDataProvider):
    @inject
    def __init__(self, transformer: PostDocumentTransformer):
        self.transformer = transformer

    def save(self, post: Post):
        post_document = self.transformer.transform_to_document(post)
        post_document.save()

    def get(self, id: Id) -> Post:
        posts = PostDocument.objects(id=id.value)
        if posts.count() < 1:
            raise EntityNotFoundException('Cannot find document with id #{}'.format(str(id)))

        return self.transformer.transform_to_domain_object(next(posts))
