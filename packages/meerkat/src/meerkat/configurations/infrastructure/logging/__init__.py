import logging as registry_logging

import sys
import registry.services


class LoggingService(registry.services.BootableService):
    def boot(self, app: registry.services.Container):
        registry_logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                 level=registry_logging.DEBUG)

        registry_logging.getLogger().addHandler(registry_logging.StreamHandler(sys.stdout))
