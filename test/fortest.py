# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:52:59 2021

@author: admin
"""
import json
from common.xls_data import XlsData

filepath = "../data/easycook.xlsx"
sheetName = "首页"
data = XlsData(filepath, sheetName)
env=XlsData(filepath, sheetName).env_data()
f=data.dict_data(env)[0]["headers"]

a='{"token":"tk58721f7ac15c420a8270128d3b0302f5","clientType":"100","content-type":"application/json"}'
b=json.loads(a)
#print(a)

c={'method': 'get', 'url': 'http://test-calling-api.apyfc.com/calling/travel/applet/api/travel/search/travelList', 'headers': '{"token":"tk58721f7ac15c420a8270128d3b0302f5","clientType":"100","content-type":"application/json"}', 'params': '{"categoryCode":"","contentIds":"","flagNew":0,"flagHot":0,"flagPrice":0,"keyword":"门票","page":1,"pageSize":10}'}
f=json.loads(f)
print(type(f))
print(f)

if f==a:
    print("相同")
else:
    print("不相同")