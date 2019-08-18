import falcon
from injector_provider.providers import InjectorProvider
from product_manager.configurations.app import settings
from product_manager.configurations.app.middlewares import RequireJSON
from registry.services import Container, Registry

app = falcon.API(middleware=[
    RequireJSON(),
    Marshmallow
])

container = Container()

container.set(settings.Props.DI_CONTAINER_BUILDER, InjectorProvider())
container.set(settings.Props.FALCON, app)

service_registry = Registry()

for service in settings.services:
    service_registry.register(service)

service_registry.boot(container)
