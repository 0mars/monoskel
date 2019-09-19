import falcon
from meerkat.configurations.app import settings
from falcon_marshmallow import JSONEnforcer, EmptyRequestDropper

from meerkat.configurations.app.middlewares import RequestLoader
from injector_provider import InjectorProvider
from registry.services import Container, Registry

app = falcon.API(middleware=[
    JSONEnforcer(),
    EmptyRequestDropper(),
    RequestLoader()
])

container = Container()

container.set(settings.Props.DI_PROVIDER, InjectorProvider())
container.set(settings.Props.FALCON, app)

service_registry = Registry()

for service in settings.services:
    service_registry.register(service)

service_registry.boot(container)
