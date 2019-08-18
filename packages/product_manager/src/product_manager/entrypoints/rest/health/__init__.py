import falcon

import json

from marshmallow import Schema, fields


# schema
class HealthSchema(Schema):
    status: fields.Str = fields.Str(required=True)
    message: fields.Str = fields.Str(required=True)


class HealthCheck:
    # Handles GET requests
    def on_get(self, req, resp):
        """A cute furry animal endpoint.
                ---
                    summary: Check application health
                    responses:
                        200:
                            description: status response
                            schema: HealthSchema
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"status": resp.status, "message": "healthy"})

