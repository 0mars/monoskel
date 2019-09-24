from buslane.events import EventBus
from injector import singleton, provider, Module

from meerkat.data_providers.database.mongo import PostMongoRepository
from meerkat.domain.post.use_cases import AddNewPostUseCase, PublishPostUseCase


class UseCasesConfigurator(Module):
    @singleton
    @provider
    def add_new(self) -> AddNewPostUseCase:
        return AddNewPostUseCase(self.__injector__.get(PostMongoRepository), self.__injector__.get(EventBus))

    @singleton
    @provider
    def publish(self) -> PublishPostUseCase:
        return PublishPostUseCase(self.__injector__.get(PostMongoRepository), self.__injector__.get(EventBus))
