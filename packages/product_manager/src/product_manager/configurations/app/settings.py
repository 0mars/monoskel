from product_manager.configurations.environment import EnvironmentService
from product_manager.configurations.logging import LoggingService
from product_manager.entrypoints.rest.health.registry import HealthService
from product_manager.entrypoints.rest.swagger.registry import SwaggerService
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
