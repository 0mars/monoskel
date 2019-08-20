import os

from registry.services import BootableService, Container


class EnvironmentService(BootableService):

    def boot(self, container: Container):
        from meerkat.configurations.app.settings import Props
        container.set(Props.APP_URL, os.environ.get('APP_URL'))
