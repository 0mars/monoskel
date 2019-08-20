from meerkat.configurations.environment import EnvironmentService
from meerkat.configurations.logging import LoggingService
from meerkat.entrypoints.rest.health.registry import HealthService
from meerkat.entrypoints.rest.swagger.registry import SwaggerService
from registry.services import Props as BaseProps

services = [
    LoggingService(),
    EnvironmentService(),
    HealthService(),
    SwaggerService()
]


class Props(BaseProps):
    DI_CONTAINER_BUILDER = 0
    FALCON = 1
    APP_URL = 'APP_URL'
