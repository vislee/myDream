#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base
import tornado.web
from config.config import pageConf, aboutMe
# from model.model import BlogUser, BlogDream, BlogTag, BlogPostTag

class MainHandler(base.BaseHandler):
    def get(self, page=1):
        dreams = BlogDream.paginate(int(page), pageConf['POST_NUM'])
        # dreams = [{"id":1, "title":"test_1","pub_date":"20131212 01:02:03","content":"i am liwq ... this is test content..."},
        #           {"id":2, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},
        #           {"id":3, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},
        #           {"id":4, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},
        #           {"id":5, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},
        #           {"id":6, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},
        #           {"id":7, "title":"test_2","pub_date":"20141012 01:05:03","content":"i am vince ... this is test content..."},]
        nav = {
            'model': 'index',
            'num': BlogDream.select().count(),
            # 'num': 12,
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
        # 验证用户名和密码
        # if eMail.startswith("liwq"):
        blogUser = BlogUser.select().where(email=eMail, password=pswd)
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
