import uuid
from unittest import mock

from meerkat.domain.post.entities import Post
from meerkat.domain.post.events import PostPublished
from meerkat.domain.post.use_cases import PublishPostUseCase
from meerkat.domain.post.use_cases.publish_post import PublishPostCommand
from meerkat.domain.post.value_objects import Title, Body, Id


class TestCreatePost:

    @mock.patch('meerkat.domain.post.use_cases.add_new_post.uuid.uuid4')
    def test_can_publish_post(self, uuid4_mock):
        id = Id(uuid.uuid4())
        post = Post.create(id, Title('post title'), Body('post body'))
        data_provider_mock = mock.Mock()
        event_bus_mock = mock.Mock()

        def get(id: Id):
            return post
        data_provider_mock.get.side_effect = get

        use_case = PublishPostUseCase(data_provider_mock, event_bus_mock)

        assert post.is_published() is False

        command = PublishPostCommand(id)
        use_case.exec(command)

        data_provider_mock.save.assert_called_once_with(post)

        published_post = self.first_called_arg(data_provider_mock.save)
        assert published_post.is_published() is True

        post_published_event = self.first_called_arg(event_bus_mock.publish)
        assert isinstance(post_published_event, PostPublished)
        assert post_published_event.post == published_post

    def first_called_arg(self, method_mock):
        return method_mock.call_args_list[0][0][0]
