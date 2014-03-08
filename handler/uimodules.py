#!/usr/bin/env python
# -*-coding: utf-8 -*-
#

import tornado.web
from config.config import pageConf

class RecentDream(tornado.web.UIModule):
    def render(self, dreams, show=pageConf["RECENT_DREAM_NUM"]):
        if show:
            return self.render_string("uimodule/recent_dream.html", dreams=dreams)
        else:
            return ""


class Tag(tornado.web.UIModule):
    def render(self, tags, show=pageConf["TAG_NUM"]):
        if show:
            return self.render_string("uimodule/tag.html", tags=tags)
        else:
            return ""


class PageNav(tornado.web.UIModule):
    def render(self, nav, show=False):
        if show:
            return self.render_string("uimodule/page_nav.html", nav=nav)
        else:
            return ""