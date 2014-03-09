#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base
import tornado.web
import model
from model.model import BlogUser, BlogDream, BlogTag, BlogDreamTag
from config.config import pageConf


class IndexHandler(base.BaseHandler):
    # @tornado.web.authenticated
    def get(self, id):
        dream = BlogDream.get(BlogDream.id == id)
        self.render("dream/index.html", title=dream.title, dream=dream, side=self.get_side())

    def post(self, args, **argList):
        pass


class AddHandler(base.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        tts = [{"tag":"python"}, {"tag":"tornado"}]
        self.render("dream/add.html", title="记录", side=self.get_side(), tags=tts)


    @tornado.web.authenticated
    def post(self):
        title = self.get_argument("title", "i have a dream")
        content = self.get_argument("content", "i have a dream")
        tags = self.get_argument("tags", "dream,")
        eMail = email = self.get_secure_cookie('usereMail')
        user = BlogUser.get(BlogUser.email==eMail)
        dream = BlogDream.create(title=title, content=content, user=user)
        model.saveTag(tags, dream.id)
        self.redirect("/dream/id/"+str(dream.id))




class TagHandler(base.BaseHandler):
    def get(self, tag, page=1):
        p = BlogDream.select(BlogDream).join(BlogDreamTag).join(BlogTag).where(BlogTag.tag == tag).\
            paginate(int(page), pageConf['DREAM_NUM'])
        nav = {
            'model': 'tag/' + tag,
            'num': BlogDream.select(BlogDream).join(BlogDreamTag).join(BlogTag).where(BlogTag.tag == tag).count(),
        }
        self.render("tag/index.html", dreams=p, title=tag, side=self.get_side(), nav=nav)
