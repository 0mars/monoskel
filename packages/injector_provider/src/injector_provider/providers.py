from typing import List, Union
from injector import Injector


class InjectorProvider(object):
    def __init__(self):
        self.configurators: List = []
        self.tainted: bool = True
        self.injector: Union[Injector, None] = None

    def get_injector(self) -> Injector:
        if self.tainted:
            self.injector = Injector(self.configurators)
            self.clean()
            return self.injector
        else:
            return self.injector

    def add_configurator(self, configurator) -> None:
        self.configurators.append(configurator)
        self.taint()

    def taint(self) -> None:
        self.tainted = True

    def clean(self) -> None:
        self.tainted = False
