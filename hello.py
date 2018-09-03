from datetime import date
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8888, help="run on user's defined port", type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print "I was called"
        self.write("Welcome to Tornado!")

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        print "Version called"
        response = {
            'version' : '7.8',
            'date' : date.today().isoformat()
        }
        self.write(response)

class GameHandler(tornado.web.RequestHandler):
    def get(self, id):
        print "Game called"
        response = {
            'id' : int(id),
            'name': 'the_game',
            'release_date': date.today().isoformat()
        }
        self.write(response)

if __name__ == "__main__":
    app = tornado.web.Application(handlers=[
        (r"/",HelloHandler),
        (r"/version", VersionHandler),
        (r"/getgamebyid/([0-9]+)", GameHandler)
    ])
    http_server =  tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print "server starting"
    tornado.ioloop.IOLoop.instance().start()
