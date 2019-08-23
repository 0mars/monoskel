import uuid
from buslane.events import EventBus
from dataclasses import dataclass

from meerkat.domain.post.data_providers import PostDataProvider
from meerkat.domain.post.entities import Post
from meerkat.domain.post.events import PostCreated
from meerkat.domain.post.value_objects import Title, Body, Id

@dataclass(frozen=True)
class CreatePostCommand:
    title: str
    body: str


class CreatePostUseCase:
    def __init__(self, data_provider: PostDataProvider, event_bus: EventBus):
        self.data_provider = data_provider
        self.event_bus = event_bus

    def exec(self, command: CreatePostCommand) -> None:
        post = Post.create(Id(uuid.uuid4()), Title(command.title), Body(command.body))
        self.data_provider.save(post)
        self.event_bus.publish(PostCreated(post))
