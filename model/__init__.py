#!/usr/bin/env python
# -*- config:utf -*-
#
#


from .model import *


def strip(str):
    return str.strip()

def getTagList(tag):
    if tag is None or len(tag)<1:
        return []
    return map(strip, tag.split(','))


def saveTag(tag, id):
    try:
        postTag = BlogDreamTag.delete().where(BlogDreamTag.id == id)
        postTag.execute()
    except:
        pass

    if tag is not None and len(tag)>1:
        tagList = getTagList(tag)
        for t in tagList:
            try:
                blogTag = BlogTag.get((BlogTag.tag == t) | (BlogTag.tag == t[:30]))
            except DoesNotExist:
                bt = BlogTag.create(tag = t[0:30])
            BlogDreamTag.create(tag=bt.id, dream=id)

