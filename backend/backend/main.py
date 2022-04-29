import tornado.ioloop
import tornado.web
from handlers.main_handler import MainHandler
from handlers.login_handler import LoginHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
