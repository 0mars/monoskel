import logging

import falcon
from falcon import HTTPUnprocessableEntity, HTTPBadRequest
from falcon_marshmallow import Marshmallow
from falcon_marshmallow.middleware import get_stashed_content
from marshmallow import ValidationError, Schema

log = logging.getLogger(__name__)


class HTTPValidationError(falcon.HTTPError):
    """
    HTTPError that stores a dictionary of validation error messages.
    """

    def __init__(self, status, errors=None, *args, **kwargs):
        self.errors = errors
        super().__init__(status, *args, **kwargs)

    def to_dict(self, *args, **kwargs):
        """
        Override `falcon.HTTPError` to include error messages in responses.
        """

        ret = super().to_dict(*args, **kwargs)

        if self.errors is not None:
            ret['errors'] = self.errors

        return ret


class RequestLoader(Marshmallow):
    def process_resource(self, *args, **kwargs):
        try:
            self.process_resource_inner(*args, **kwargs)
        except ValidationError as err:
            raise HTTPValidationError(status=falcon.status_codes.HTTP_400, errors=err.messages)
        except ValueError as err:
            raise falcon.HTTPError(status=falcon.status_codes.HTTP_400, title='Validation Error', description=str(err))

    def process_resource_inner(self, req, resp, resource, params):
        # type: (Request, Response, object, dict) -> None
        """Deserialize request body with any resource-specific schemas

        Store deserialized data on the ``req.context`` object
        under the ``req_key`` provided to the class constructor
        or on the ``json`` key if none was provided.

        If a Marshmallow schema is defined on the passed ``resource``,
        use it to deserialize the request body.

        If no schema is defined and the class was instantiated with
        ``force_json=True``, request data will be deserialized with
        any ``json_module`` passed to the class constructor or
        ``simplejson`` by default.

        :param falcon.Request req: the request object
        :param falcon.Response resp: the response object
        :param object resource: the resource object
        :param dict params: any parameters parsed from the url

        :rtype: None
        :raises falcon.HTTPBadRequest: if the data cannot be
            deserialized or decoded
        """
        log.debug(
            'Marshmallow.process_resource(%s, %s, %s, %s)',
            req, resp, resource, params
        )
        if req.content_length in (None, 0):
            return

        sch = self._get_schema(resource, req.method, 'request')

        if sch is not None:
            if not isinstance(sch, Schema):
                raise TypeError(
                    'The schema and <method>_schema properties of a resource '
                    'must be instantiated Marshmallow schemas.'
                )

            try:
                body = get_stashed_content(req)
                parsed = self._json.loads(body)
            except UnicodeDecodeError:
                raise HTTPBadRequest('Body was not encoded as UTF-8')
            except self._json.JSONDecodeError:
                raise HTTPBadRequest('Request must be valid JSON')
            log.info(sch)

            data = sch.load(parsed)

            req.context[self._req_key] = data

        elif self._force_json:

            body = get_stashed_content(req)
            try:
                req.context[self._req_key] = self._json.loads(body)
            except (ValueError, UnicodeDecodeError):
                raise HTTPBadRequest(
                    description=(
                        'Could not decode the request body, either because '
                        'it was not valid JSON or because it was not encoded '
                        'as UTF-8.'
                    )
                )
