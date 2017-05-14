# _*_ coding: utf-8 _*_
'''
windows下使用gbk编码
'''
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define('port', default=8000, help='run on the given port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class GradeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('grade.html', g1='', g2='', g3='', g4='',g5='', g6='', g7='', g8='', g9='',g10='', g11='', g12='')

    def post(self):
        for i in xrange(1, 13):
            #      locals()['name%s'%i] = self.get_argument('name%s'%i)

            locals()['grade%s' % i] = self.get_argument('grade%s' % i)

        self.render('grade.html', g1=eval('grade1'), g2=eval('grade2'), g3=eval('grade3'), g4=eval('grade4'),
                    g5=eval('grade5'), g6=eval('grade6'), g7=eval('grade7'), g8=eval('grade8'), g9=eval('grade9'),
                    g10=eval('grade10'), g11=eval('grade11'), g12=eval('grade12'))


# class ChartModule(tornado.web.UIModule):
class LogHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument('title')
        article = self.get_argument('article')
        self.render('log.html', title=title, article=article)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/grade', GradeHandler), (r'/log', LogHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static')

    )
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
