#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from websocket import create_connection

class Common(object):
    def __init__(self,url_root,api_type):
        '''
        :param url_root: 接口类似当前支持http协议，ws websocket协议
        :param api_type: 被测试系统的跟路径
        '''
        if api_type =='ws':
            self.ws = create_connection(url_root)
        elif api_type =='http':
            self.ws = 'null'
            self.url_root = url_root
    #ws协议的消息发送
    def send(self,params):
        '''
        :param params: websocket 接口的参数
        :return: 访问接口的返回值
        '''
        self.ws.send(params)
        res = self.ws.recv()
        return res
    #common类的析构函数，清理没有用的资源
    def __del__(self):
        '''

        :return:
        '''
        if self.ws != 'null':
            self.ws.close()

    #封装get方法
    def get(self,uri,params=None):
        '''
        :param uri: 访问路由
        :param params: 传递参数
        :return:
        '''
        if params is not None:
            url = self.url_root + uri + params
        else:
            url = self.url_root + uri
        res = requests.get(url)
        return res
    #封装post方法
    def post(self,uri,params=None):
        '''
        :param uri: 访问路径
        :param params: 传递参数string，默认是None
        :return:
        '''
        url = self.url_root + uri
        if params is not None:
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
