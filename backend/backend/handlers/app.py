import tornado
from .main_handler import MainHandler
from .login_handler import LoginHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
    ])
