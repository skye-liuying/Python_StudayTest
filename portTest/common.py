#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
    #封装put方法
    def put(self,uri,params=None):
        url = self.url_root + uri
        if params is not None:
            res = requests.put(url,data=params)
        else :
            res = requests.put(url)
        return res
    #封装delete方法
    def delete(self,uri,params=None):
        url = self.url_root + uri
        if params is not None:
            res = requests.delete(url,data=params)
        else :
            res = requests.delete(url)
        return res
