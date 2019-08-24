import os

from registry.services import BootableService, Container


class EnvironmentService(BootableService):

    def boot(self, container: Container):
        from meerkat.configurations.app.settings import Props

        container.set(Props.APP_URL, os.environ.get(Props.APP_URL.value))

        container.set(Props.MONGO_HOST, os.environ.get(Props.MONGO_HOST.value))
        container.set(Props.MONGO_PORT, os.environ.get(Props.MONGO_PORT.value))
        container.set(Props.MONGO_DB, os.environ.get(Props.MONGO_DB.value))
