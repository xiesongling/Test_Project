# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:16:12 2021

@author: admin
"""
from string import Template
import pytest
import yaml
from api.base_api import BaseApi
class WeWork(BaseApi):
    #mobile="13545424538"
    #pwd="123456"
    token_data=yaml.safe_load(open("../data/get_token_data.yaml",encoding='utf-8'))["data"]
   
    #获取token
    pytest.mark.parametrize("data",token_data)
    def template(self):
        with open("../api/get_token.yaml",encoding='utf-8') as f:
# =============================================================================
#             data={
#                 "mobile":self.mobile,
#                 "pwd":self.pwd
#                 }
# =============================================================================
            #完成模板替换（替换了yaml里面的变量）           
            re=Template(f.read()).substitute(self.token_data) 
           #re是字符串对象，转换成python对象:字典或列表
            return yaml.safe_load(re)
    def token(self):
        req=self.template()
        res=self.send(**req)
        return res["data"]["token"]#**data解字
