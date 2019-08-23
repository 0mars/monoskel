from unittest.mock import patch
from injector import Injector, Module
from injector_provider.providers import InjectorProvider


class TestObjectGraphBuilder:
    def test_can_build_without_any_configurations(self):
        provider = InjectorProvider()
        assert isinstance(provider.get_injector(), Injector)

    @patch('injector_provider.providers.Injector.__init__')
    def test_add_class(self, mocked_injector_init):
        mocked_injector_init.return_value = None
        provider = InjectorProvider()

        class Configurator(Module):
            pass

        configurator1 = Configurator()
        provider.add_configurator(configurator1)
        provider.get_injector()

        mocked_injector_init.assert_called_once_with([configurator1])
