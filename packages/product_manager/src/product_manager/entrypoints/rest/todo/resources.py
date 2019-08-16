
class product_manager():
    # Handles GET requests
    def on_get(self, req, resp):
        name = "This is my first API!!"
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"response": name, "status": resp.status})

    # Handles POST requests
    def on_post(self, req, resp):
        pass
