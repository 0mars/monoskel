from registry.services import BootableService, Container
from mongoengine import connect


class DataBaseService(BootableService):

    def boot(self, container: Container):
        from meerkat.configurations.app.settings import Props

        host = container.get(Props.MONGO_HOST)
        port = container.get(Props.MONGO_PORT)
        db = container.get(Props.MONGO_DB)

        connect(db, host=host, port=port)

