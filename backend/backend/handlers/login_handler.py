from tornado.web import RequestHandler
import json
from backend.authentication.authentication import Authentication


class LoginHandler(RequestHandler):
    def put(self):
        try:
            data = json.loads(self.request.body)
            if data["username"] == "Admin" and data["password"] == "Admin-1234":
                self.write({
                    "token": Authentication().generate_token(data)
                })
            else:
                self.clear()
                self.set_status(401)
                self.finish({
                    "cause": "Invalid username or password"
                })
        except json.decoder.JSONDecodeError:
            self.clear()
            self.set_status(400)
            self.finish({
                "cause": "Invalid JSON"
            })
