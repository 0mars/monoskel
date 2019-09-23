from injector import Module, singleton, provider

from meerkat.configurations.infrastructure.rest.health import HealthCheck


class HealthConfigurator(Module):
    @singleton
    @provider
    def provide_health_check_resource(self) -> HealthCheck:
        return HealthCheck()
