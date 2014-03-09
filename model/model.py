#!/usr/bin/env python
# -*-coding:utf-8 -*-

from peewee import *
from datetime import datetime
# import sys
# sys.path.append("../")
from config.config import database as dbconfig

db = MySQLDatabase(dbconfig['database'], user=dbconfig['user'], passwd=dbconfig['password'])

class BaseModel(Model):
    class Meta:
        database = db

class BlogUser(BaseModel):
    username = CharField(unique=True, max_length=10)
    email = CharField(unique=True)
    password = CharField()
    regdate = DateTimeField(default=datetime.now())
    state = CharField(default='1', max_length=2)
    statedate = DateTimeField(default=datetime.now())
    class Meta:
        db_table = 'Blog_User'

class BlogDream(BaseModel):
    title = CharField(max_length=50)
    content = TextField()
    user = ForeignKeyField(BlogUser, related_name='blogdreams')
    pubDate = DateTimeField(default=datetime.now())
    isopen = CharField(default='1', max_length=2)
    openDate = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'Blog_Dream'
        order_by = ('-pubDate',)
        indexes = (
            (('title',), False),
        )

class BlogTag(BaseModel):
    tag = CharField(unique=True, max_length=25)
    class Meta:
        db_table = 'Blog_Tag'


class BlogDreamTag(BaseModel):
    dream = ForeignKeyField(BlogDream, related_name='blogdreams')
    tag = ForeignKeyField(BlogTag, related_name='blogtags')

    class Meta:
        db_table = 'Blog_Dream_Tag'


def main():
    BlogUser.create_table()
    BlogDream.create_table()
    BlogTag.create_table()
    BlogDreamTag.create_table()

if __name__ == '__main__':
    main()
