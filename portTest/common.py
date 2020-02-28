#!/usr/bin/env python
#! -*- coding:utf-8 -*-

import requests

class Common(object):
    def __init__(self,url_root):
        self.url_root = url_root

    #封装get方法
    def get(self,uri,params=''):
        url = self.url_root + uri + params
        res = requests.get(url)
        return res
    #封装post方法
    def post(self,uri,params=''):
        url = self.url_root + uri
        if len(params)>0:
            res = requests.post(url,data=params)
        else :
            res = requests.post(url)
        return res