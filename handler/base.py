#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#
#


import tornado.web
from peewee import DoesNotExist, fn
from model.model import BlogUser, BlogDream, BlogTag, BlogDreamTag
from config.config import pageConf

class BaseHandler(tornado.web.RequestHandler):
    def test(self, message=None):
        self.write('hello, this is a test message!!!    ')
        if message:
            self.write(message)


    def get(self):
        return write_error(404)


    def get_current_user(self):
        email = self.get_secure_cookie('usereMail')
        if not email:
            return None
        else:
            try:
                user = BlogUser.get(BlogUser.email == email)
            except DoesNotExist:
                self.clear_cookie('usereMail')
            return user


    def get_side(self):
        side = {
        "recent_dream": BlogDream.select().limit(pageConf["RECENT_DREAM_NUM"]),
        # "recent_dream":[{"id":"3","title":"liwq"},{"id":"5","title":"vince"}],
        # "tags":BlogTag.select().limit(pageConf["TAG_NUM"])
        # "tags":[{"tag":"python","count":3},{"tag":"tornado","count":5}]
        "tags": BlogTag.select(BlogTag, fn.Count(BlogDream.id).alias('count')).join(BlogDreamTag).join(BlogDream).group_by(BlogTag)
        }
        return side


