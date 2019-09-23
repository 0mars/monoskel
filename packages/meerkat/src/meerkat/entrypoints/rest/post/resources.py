import json

import falcon
from marshmallow import ValidationError

from meerkat.configurations.app.middlewares import HTTPValidationError
from meerkat.domain.post.use_cases import AddNewPostUseCase
from meerkat.domain.post.use_cases.add_new_post import AddNewPostCommand
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
