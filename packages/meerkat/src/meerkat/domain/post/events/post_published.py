from dataclasses import dataclass

from buslane.events import Event

from meerkat.domain.post.entities.post import Post


@dataclass(frozen=True)
class PostPublished(Event):
    post: Post
