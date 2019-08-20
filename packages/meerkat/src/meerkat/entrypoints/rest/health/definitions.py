from meerkat.entrypoints.rest.health import HealthCheck
from injector import Module, singleton, provider


class HealthConfigurator(Module):
    @singleton
    @provider
    def provide_health_check_resource(self) -> HealthCheck:
        return HealthCheck()
