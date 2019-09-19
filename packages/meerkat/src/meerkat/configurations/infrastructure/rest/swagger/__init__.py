import json

import falcon
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from falcon import Request
from falcon.response import Response
from falcon_apispec import FalconPlugin

from meerkat.configurations.infrastructure.rest.health import HealthSchema, HealthCheck


class SwaggerResource:
    def __init__(self):
        from meerkat.configurations.app.settings import Props
        from meerkat.configurations.app.main import app
        from meerkat.configurations.app.main import container
        # todo: should be moved to env vars
        self.spec = APISpec(title='meerkat',
                            version='1.0.0',
                            openapi_version='2.0',
                            plugins=[
                                FalconPlugin(app),
                                MarshmallowPlugin(),
                            ])
        injector = container.get(Props.DI_PROVIDER).get_injector()

        self.spec.components.schema('Health', schema=injector.get(HealthSchema))
        self.spec.path(resource=injector.get(HealthCheck))

    def on_get(self, req: Request, resp: Response):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(self.spec.to_dict(), ensure_ascii=False)
