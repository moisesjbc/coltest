import tornado
import json


class LoginHandler(tornado.web.RequestHandler):
    def put(self):
        data = json.loads(self.request.body)
        self.write({
            "username": data['username'],
            "password": data['password']
        })
