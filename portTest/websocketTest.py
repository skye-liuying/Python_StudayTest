#! /usr/bin/env python
# -*-coding:utf-8 -*-

from portTest.common import Common
#创建链接
uri_index = 'ws://echo.websocket.org'
comm = Common(uri_index,'ws')
#打印日志
print("发送 'hello , liuying'...")

#发送信息
result = comm.send("hello,liuying666")
#打印返回值
print("返回="+result)

