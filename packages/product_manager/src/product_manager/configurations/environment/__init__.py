import os

from registry.services import BootableService, Container


class EnvironmentService(BootableService):

    def boot(self, container: Container):
        from product_manager.configurations.app.settings import Props
        container.set(Props.APP_URL, os.environ.get('APP_URL'))
