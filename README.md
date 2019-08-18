
# Mono Python Repo [REST over Falcon]  
  
### installation  
```bash  
make start  
```  
 
 ### new REST resource
 see health resource incode, example is something like:
 ```python
 # schema  
class HealthSchema(Schema):  
    status: fields.Str = fields.Str(required=True)  
    message: fields.Str = fields.Str(required=True)  
  
  
class HealthCheck:  
    # Handles GET requests  
    def on_get(self, req, resp):  
        """Internal description not shown in swagger docs.
                ---
                    summary: Check application health
                    responses:
                        200:
                            description: status response
                            schema: HealthSchema
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"status": resp.status, "message": "healthy"})
 ```
 in swagger/__init__.py
 ```python
self.spec.components.schema('Health', schema=injector.get(HealthSchema))  
self.spec.path(resource=injector.get(HealthCheck))
 ```
 
### usage  
Swagger UI:  
http://localhost:8021/api/docs
