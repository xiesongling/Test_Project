# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:16:12 2021

@author: admin
"""
from api.base_api import BaseApi
class WeWork(BaseApi):
    #获取token
    def token(self):
            
            data={
                "method":"post",
                "url":"https://test-calling-api.apyfc.com/calling/community/app/api/v3/login",
                "json":{
                "loginType": "pwd",
                "loginWithPwdRequest": {
                      "mobile": "13545424538",
                      "pwd": "123456"} 
                }
                }
            res=self.send(**data)
            return res["data"]["token"]#**data解字典