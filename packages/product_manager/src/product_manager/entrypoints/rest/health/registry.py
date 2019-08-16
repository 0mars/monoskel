from product_manager.configurations.app import settings
from registry.services import BootableService, Container
from product_manager.entrypoints.rest.health import health_check


class HealthService(BootableService):
    def boot(self, container: Container):
        falcon = container.get(settings.Props.FALCON)
        falcon.add_route("/api", health_check)
        falcon.add_route("/api/health", health_check)
