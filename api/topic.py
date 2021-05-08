# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:59:04 2021

@author: admin
"""
import requests
from api.base_api import BaseApi
from api.wework import WeWork

#继承为BaseApi
class Topic(BaseApi):
 
    def __init__(self):  #__init__函数：创建一个对象时默认被调用
        self.token=WeWork().token()
        
    #获取话题列表
    def get(self,userId,type,communityCode,pageIndex,pageSize):
        
        data={
              "method":"get",
              "url":"https://test-calling-api.apyfc.com/calling/community/app/api/v3/topic/list",
              "params":{
                  "userId":userId,
                  "type":type,
                  "communityCode":communityCode,
                  "pageIndex":pageIndex,
                  "pageSize":pageSize}
              }
        res=self.send(**data)
        return res