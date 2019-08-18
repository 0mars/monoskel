import os

from registry.services import BootableService, Container
from falcon_swagger_ui import register_swaggerui_app


class SwaggerService(BootableService):
    def boot(self, container: Container):
        from product_manager.configurations.app import settings
        from product_manager.entrypoints.rest.swagger import SwaggerResource

        falcon = container.get(settings.Props.FALCON)
        swagger_resource = SwaggerResource()
        falcon.add_route('/api/swagger.json', swagger_resource)

        page_title = 'Swagger UI'
        favicon_url = 'https://falconframework.org/favicon-32x32.png'
        swagger_ui_url = '/api/docs'  # without trailing slash
        schema_url = '{}/api/swagger.json'.format(container.get(settings.Props.APP_URL))

        register_swaggerui_app(
            falcon, swagger_ui_url, schema_url,
            page_title=page_title,
            favicon_url=favicon_url,
            config={'supportedSubmitMethods': ['get', 'post', 'put'], }
        )
