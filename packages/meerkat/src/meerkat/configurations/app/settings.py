from meerkat.configurations.db import DataBaseService
from meerkat.configurations.environment import EnvironmentService
from meerkat.configurations.logging import LoggingService
from meerkat.entrypoints.rest.health.registry import HealthService
from meerkat.entrypoints.rest.swagger.registry import SwaggerService
from registry.services import Props as BaseProps

services = [
    LoggingService(),
    EnvironmentService(),
    DataBaseService(),
    HealthService(),
    SwaggerService()
]


class Props(BaseProps):
    DI_CONTAINER_BUILDER = 0
    FALCON = 1

    APP_URL = 'APP_URL'

    MONGO_HOST = 'MONGO_HOST'
    MONGO_PORT = 'MONGO_PORT'
    MONGO_DB = 'MONGO_DB'
