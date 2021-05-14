# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:16:12 2021

@author: admin
"""
from string import Template
import yaml
from api.base_api import BaseApi
class WeWork(BaseApi):
    mobile="13545424538"
    pwd="123456"
    #获取token
    def template(self):
        with open("../api/get_token.yaml") as f:
            #完成模板替换（替换了yaml里面的变量）
           re=Template(f.read()).substitute(mobile=self.mobile,pwd=self.pwd) 
           #re是字符串对象，转换成python对象:字典或列表
           return yaml.safe_load(re)
    def token(self):
        req=self.template()
        res=self.send(**req)
        return res["data"]["token"]#**data解字
