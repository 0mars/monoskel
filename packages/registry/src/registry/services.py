from abc import ABC, abstractmethod

from enum import Enum


class Props(Enum):
    pass


class Container(object):
    def __init__(self):
        self.vars = {}

    def set(self, prop: Props, value):
        self.vars[prop] = value

    def get(self, key: Props):
        return self.vars[key]


class BootableService(ABC):

    @abstractmethod
    def boot(self, container: Container):
        raise NotImplemented('Service not implemented')

    def post_boot(self, container):
        pass


class Registry(object):
    """ Service registry is where to register bootable services to be booted
    """

    def __init__(self):
        self.services: list = []

    def register(self, service: BootableService):
        self.services.append(service)

    def boot(self, container: Container):
        for service in self.services:
            service.boot(container)

        for service in self.services:
            service.post_boot(container)
