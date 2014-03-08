#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web
# from model.model import BlogUser, BlogDream, BlogTag, BlogPostTag
from config.config import pageConf
class BaseHandler(tornado.web.RequestHandler):
    def test(self, message=None):
        self.write('hello, this is a test message!!!    ')
        if message:
            self.write(message)

    def get(self):
        raise write_error(404)


    def get_current_user(self):
        uid = self.get_secure_cookie('usereMail')
        if not uid:
            return None
        else:
            return uid
            user = 'liwq'
            try:
                pass
                # user = BlogUser.get(BlogUser.id == uid)
            except DoesNotExist:
                self.clear_cookie('uid')
            return user

    def get_side(self):
        side = {
        # "recent_dream": BlogDream.select().limit(pageConf["RECENT_DREAM_NUM"]),
        "recent_dream":[{"id":"3","title":"liwq"},{"id":"5","title":"vince"}],
        # "tags":BlogTag.select().limit(pageConf["TAG_NUM"])
        "tags":[{"tag":"python","count":3},{"tag":"tornado","count":5}]
        }
        return side