# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:08:18 2021

@author: admin
测试用例
"""
import pytest
import json
import re

from api.topic import Topic
from api.base_api import BaseApi
from common.xls_data import XlsData

class TestTopic:
    
    filepath = "../data/easycook.xlsx"
    sheetName = "首页"
    xlsdata=XlsData(filepath, sheetName)
    url=xlsdata.env_data()
    data = xlsdata.dict_data(url)
    
    
   
    def setup(self):
        self.baseapi=BaseApi()
        
        
    
    #数据驱动
    @pytest.mark.parametrize("data",[*data])    
    def test_get_topic(self,data):
          
          res=self.baseapi.sen_request(data).json()
          print(type(res))
          res=json.dumps(res, ensure_ascii=False)
          check=data["checkpoint"]
          #返回结果
          
         
          print(res)
          #断言
          ru=r'\".*?\":( )*\".*?\"'
          it = re.finditer(ru,check) 
          for i in it:
              item=i.group()
              assert item in res
          
          
   


if __name__=='__main__':
    
    
    pytest.main(['-s','-v'])
    
    