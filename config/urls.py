#! /usr/bin/env python
# -*-coding:utf-8 -*-

from handler import base, index, dream

urls = [
    (r"/", index.MainHandler),
    (r"/login", index.LoginHandler),
    (r"/logout", index.LogoutHandler),
    (r"/about", index.AboutHandler),
    (r"/dream/id/([0-9]+)", dream.IndexHandler),
    (r"/dream/add", dream.AddHandler),
    (r"/*", base.BaseHandler),
    ]