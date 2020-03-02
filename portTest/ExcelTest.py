#! /usr/bin/ven python
# -*-coding:utf-8 -*-

from portTest.common import Common
from portTest.param import ParamFactory

import os

uri_selectEq = '/selectEq'
comm = Common('http://127.0.0.1:12356',api_type='http')
#获取当前的绝对路径
curPath = os.path.abspath('.')

#定义存储的参数excel文件路径
searchparamfile = curPath + '/Testexcel/liuyingTest.xlsx'

searchparam_dict = ParamFactory().chooseParam('xlsx',{'file':searchparamfile,'sheet':0}).paramAlllineDict()
print(searchparam_dict)
i = 0
while i < len(searchparam_dict):
    #通过读取参数类获取第i航的预期
    print(str(searchparam_dict[i]['equipmentid']))
    payload = 'equipmentid=' + searchparam_dict[i]['equipmentid']
    exp = searchparam_dict[i]['exp']
    #进行接口测试
    response_selectEq = comm.post(uri_selectEq,params=payload)
    print('Response内容：' + response_selectEq.text)
    i = i+1
