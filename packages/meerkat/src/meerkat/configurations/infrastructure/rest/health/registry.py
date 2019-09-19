from meerkat.configurations.app import settings
from meerkat.configurations.infrastructure.rest.health import HealthCheck
from meerkat.configurations.infrastructure.rest.health.definitions import HealthConfigurator
from registry.services import BootableService, Container


class HealthService(BootableService):
    def boot(self, container: Container):
        provider = container.get(settings.Props.DI_PROVIDER)
        provider.add_configurator(HealthConfigurator())

    def post_boot(self, container):
        falcon = container.get(settings.Props.FALCON)
        provider = container.get(settings.Props.DI_PROVIDER)
        injector = provider.get_injector()

        health_check = injector.get(HealthCheck)
        falcon.add_route("/api", health_check)
        falcon.add_route("/api/health", health_check)
