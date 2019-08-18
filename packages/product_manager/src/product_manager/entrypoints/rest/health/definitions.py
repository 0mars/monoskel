from product_manager.entrypoints.rest.health import HealthCheck
from injector import Module, singleton, provider


class HealthConfigurator(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self) -> HealthCheck:
        return HealthCheck()
