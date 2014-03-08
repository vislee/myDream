#! /usr/bin/env python
#　-*- coding:utf-8 -*-


aplct = {
    'name': 'myDream',
    'title': 'my dream country',
}

settings = {
    "app": aplct,
    "template_path": "template",
    "static_path": "static",
    "cookie_secret": "entercookiesecret",
    "login_url": "/login",
    "xsrf_cookies": True,
    "debug": True,
}

database = {
    'host': '127.0.0.1',
    'database': 'mydream',
    'user': 'liwq',
    'password': 'liwq123',
    'autocommit': True,
    'buffered': True,
}

pageConf = {
    'DREAM_NUM': 5,
    'RECENT_DREAM_NUM': 10,
    'RANDOM_DREAM_NUM': 6,
    'TAG_NUM': 100,
}