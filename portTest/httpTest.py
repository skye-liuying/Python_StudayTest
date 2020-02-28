#!/usr/bin/env python
# -*- coding:utf-8 -*-

from portTest.common import Common

uri_index = '/'
comm = Common('http://127.0.0.1:12356')
#访问主页
response_index = comm.get(uri_index)
print('Response内容：' + response_index.text)

#登录
uri_login = '/login'
username = 'criss'
password = 'criss'
payload = 'username=' + username + '&password=' + password

response_login = comm.post(uri_login,params=payload)
print('Response内容：' + response_login.text)

#选择装备
uri_selectEq = '/selectEq'
equipmentid = '10003'
payload = 'equipmentid=' + equipmentid

response_selectEq = comm.post(uri_selectEq,params=payload)
print('Response内容：' + response_selectEq.text)

#杀敌
uri_kill = '/kill'
enemyid = '20001'
payload = 'equipmentid=' + equipmentid + '&enemyid=' + enemyid

response_kill = comm.post(uri_kill,params=payload)
print('Response内容：' + response_kill.text)