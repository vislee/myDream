#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base
import tornado.web
from config.config import pageConf, aboutMe
from model.model import BlogUser, BlogDream, BlogTag

class MainHandler(base.BaseHandler):
    def get(self, page=1):
        dreams = BlogDream.select().paginate(int(page), int(pageConf['DREAM_NUM']))
        nav = {
            'model': 'index',
            'num': BlogDream.select().count(),
        }
        sides = self.get_side()
        self.render('index/index.html', title="首页", dreams=dreams, side=sides, nav=nav)

class AboutHandler(base.BaseHandler):
    def get(self):
        about = aboutMe
        self.render("index/about.html", title="关于", about=about)

class LoginHandler(base.BaseHandler):
    def get(self):
        nextUrl = self.get_argument("next", "/")
        self.render("index/login.html", title="登录", next = nextUrl)

    def post(self, *args, **kwargs):
        eMail = self.get_argument("email", "")
        pswd = self.get_argument("pswd", "")
        print eMail
        print pswd
        # 验证用户名和密码
        # if eMail.startswith("liwq"):
        blogUser = BlogUser.select().where(BlogUser.email==eMail, BlogUser.password==pswd)
        if blogUser.count() == 1:
            self.set_secure_cookie("usereMail", str(eMail))
            # print "eMail is %s" %(str(eMail))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.write("<script>alert('用户密码不存在');history.back();</script>")

class LogoutHandler(base.BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie('usereMail')
        self.redirect(self.get_argument("next", "/"))
