import json
from typing import List

import falcon
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from falcon import Request
from falcon.response import Response
from falcon_apispec import FalconPlugin


from product_manager.entrypoints.rest.health import HealthSchema, HealthCheck


class SwaggerResource:
    def __init__(self, injector):
        from product_manager.configurations.app.settings import Props
        from product_manager.configurations.app.main import app
        from product_manager.configurations.app.main import container
        # todo: should be moved to env vars
        self.spec = APISpec(title='product_manager',
                            version='1.0.0',
                            openapi_version='2.0',
                            plugins=[
                                FalconPlugin(app),
                                MarshmallowPlugin(),
                            ])
        injector = container.get(Props.DI_CONTAINER_BUILDER).get_injector()

        # todo: should somehow make a list of schemas, and resources
        self.spec.components.schema('Health', schema=injector.get(HealthSchema))
        self.spec.path(resource=injector.get(HealthCheck))

    def on_get(self, req: Request, resp: Response):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(self.spec.to_dict(), ensure_ascii=False)
