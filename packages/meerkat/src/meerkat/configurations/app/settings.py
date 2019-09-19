from meerkat.configurations.infrastructure.db import DataBaseService
from meerkat.configurations.infrastructure.environment import EnvironmentService
from meerkat.configurations.infrastructure.logging import LoggingService
from meerkat.configurations.infrastructure.rest.health.registry import HealthService
from meerkat.configurations.infrastructure.rest.swagger.registry import SwaggerService
from registry.services import Props as BaseProps

services = [
    LoggingService(),
    EnvironmentService(),
    DataBaseService(),
    HealthService(),
    SwaggerService()
]


class Props(BaseProps):
    DI_PROVIDER = 0
    FALCON = 1

    APP_URL = 'APP_URL'

    MONGO_HOST = 'MONGO_HOST'
    MONGO_PORT = 'MONGO_PORT'
    MONGO_DB = 'MONGO_DB'
