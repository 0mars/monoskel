from injector import singleton, provider, Module

from meerkat.domain.post.use_cases import AddNewPostUseCase
from meerkat.entrypoints.rest.post.resources import PostCollection


class PostConfigurator(Module):
    @singleton
    @provider
    def post_collection(self) -> PostCollection:
        return PostCollection(self.__injector__.get(AddNewPostUseCase))
