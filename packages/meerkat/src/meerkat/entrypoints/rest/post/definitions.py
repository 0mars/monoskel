from injector import singleton, provider, Module

from meerkat.domain.post.use_cases import AddNewPostUseCase, PublishPostUseCase
from meerkat.entrypoints.rest.post.resources import PostCollection, Post


class PostConfigurator(Module):
    @singleton
    @provider
    def post_collection(self) -> PostCollection:
        return PostCollection(self.__injector__.get(AddNewPostUseCase))

    @singleton
    @provider
    def post_item(self) -> Post:
        return Post(self.__injector__.get(PublishPostUseCase))
