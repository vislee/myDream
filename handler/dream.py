#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base
import tornado.web

class IndexHandler(base.BaseHandler):
    # @tornado.web.authenticated
    def get(self, id):
        print id
        dream = {"id":3, "title":"hello test","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content. test test test test"}
        self.render("dream/index.html", title="", dream=dream, side=self.get_side())

    def post(self, args, **argList):
        pass


class AddHandler(base.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tts = [{"tag":"python"}, {"tag":"tornado"}]
        self.render("dream/add.html", title="记录", side=self.get_side(), tags=tts)


    def post(self, context):
	    pass