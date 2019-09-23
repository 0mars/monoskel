from meerkat.configurations.app import settings
from meerkat.configurations.infrastructure.di.domain import UseCasesConfigurator
from registry.services import BootableService, Container


class DiService(BootableService):
    def boot(self, container: Container):
        provider = container.get(settings.Props.DI_PROVIDER)
        provider.add_configurator(UseCasesConfigurator)

