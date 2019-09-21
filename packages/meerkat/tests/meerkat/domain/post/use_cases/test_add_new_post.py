import uuid
from unittest import mock

from meerkat.domain.post.events import PostCreated
from meerkat.domain.post.use_cases.add_new_post import AddNewPostUseCase, AddNewPostCommand


class TestCreatePost:

    @mock.patch('meerkat.domain.post.use_cases.add_new_post.uuid.uuid4')
    def test_can_add_new_post(self, uuid4_mock):
        uuid4_mock.return_value = uuid.uuid4()
        data_provider_mock = mock.Mock()
        event_bus_mock = mock.Mock()

        use_case = AddNewPostUseCase(data_provider_mock, event_bus_mock)

        command = AddNewPostCommand(title='title1', body='body1')

        use_case.exec(command)

        data_provider_mock.save.assert_called_once()

        post = self.first_called_arg(data_provider_mock.save)
        assert str(post.id) == str(uuid4_mock.return_value)
        assert post.title.value == command.title
        assert post.body.value == command.body
        assert post.is_published() is False

        post_created_event = self.first_called_arg(event_bus_mock.publish)
        assert isinstance(post_created_event, PostCreated)
        assert post_created_event.post == post

    def first_called_arg(self, method_mock):
        return method_mock.call_args_list[0][0][0]
