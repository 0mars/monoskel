import json
import logging
import uuid

import falcon

from meerkat.configurations.app.middlewares import HTTPValidationError
from meerkat.domain.post.use_cases import AddNewPostUseCase, PublishPostUseCase
from meerkat.domain.post.use_cases.add_new_post import AddNewPostCommand
from meerkat.domain.post.use_cases.publish_post import PublishPostCommand
from meerkat.domain.post.value_objects import Id
from meerkat.entrypoints.rest.post.schemas import PostSchema, AddNewPostSchema


class PostCollection:
    schema = PostSchema()
    post_schema = AddNewPostSchema()

    def __init__(self, add_new_post: AddNewPostUseCase):
        self.add_new_post = add_new_post

    def on_post(self, req, resp):
        """Add new a post
                ---

                    summary: Add new post
                    consumes:
                        - application/json
                    produces:
                        - application/json
                    parameters:
                        - in: body
                          schema: AddNewPostSchema
                    responses:
                        201:
                            description: post added
                            schema: PostSchema
                        415:
                            description: Unsupported Media Type

        """
        # PostCollection.schema = AddNewPostSchema
        try:
            request_json = req.context['json']
        except KeyError:
            raise HTTPValidationError(status=falcon.status_codes.HTTP_400, errors=["Empty request body"])

        command = AddNewPostCommand(**request_json)

        post = self.add_new_post.exec(command)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(PostSchema.from_domain_object(post))


class Post:
    schema = PostSchema()

    def __init__(self, publish_post: PublishPostUseCase):
        self.publish_post_usecase = publish_post

    def on_put(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
               ---
               summary: Get movie from database
               tags:
                   - Movie
               parameters:
                   - in: path
                     schema: MoviePathSchema
               produces:
                   - application/json
               responses:
                   200:
                       description: Return requested movie details
                       schema: MovieSchema
                   401:
                       description: Unauthorized
                   404:
                       description: Movie does not exist
        """
        from meerkat.configurations.app.main import app
        logging.getLogger().info("{} = id".format(id))

        command = PublishPostCommand(Id(uuid.UUID(id)))

        self.publish_post_usecase.exec(command)

        resp.status = falcon.HTTP_204
