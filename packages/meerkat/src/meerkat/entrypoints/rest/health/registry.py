from meerkat.configurations.app import settings
from meerkat.entrypoints.rest.health.definitions import HealthConfigurator
from registry.services import BootableService, Container
from meerkat.entrypoints.rest.health import HealthCheck


class HealthService(BootableService):
    def boot(self, container: Container):
        falcon = container.get(settings.Props.FALCON)

        provider = container.get(settings.Props.DI_CONTAINER_BUILDER)
        provider.add_configurator(HealthConfigurator())

        injector = provider.get_injector()

        health_check = injector.get(HealthCheck)
        falcon.add_route("/api", health_check)
        falcon.add_route("/api/health", health_check)
