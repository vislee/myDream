#! /usr/bin/env python
# -*- coding:UTF-8 -*-
#
# 一个简单的博客系统
#
#

import tornado
import tornado.ioloop
import tornado.web
import tornado.httpserver
from config.urls import urls
from config.config import settings
from tornado.options import define, options
from handler import uimodules
settings["ui_modules"] = uimodules
define('port', default=8080, help='监听端口号', type=int)
class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)

def main():
    tornado.options.parse_command_line()
    httpServer = tornado.httpserver.HTTPServer(Application())
    httpServer.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
