# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:08:18 2021

@author: admin
测试用例
"""
import pytest

from api.topic import Topic
#from api.base_api import BaseApi
from common.xls_data import XlsData

class TestTopic:
    
    filepath = "../data/easycook.xlsx"
    sheetName = "首页"
    xlsdata=XlsData(filepath, sheetName)
    url=xlsdata.env_data()
    data = xlsdata.dict_data(url)
    
   
    def setup(self):
        self.topic=Topic()
        
        
    
    #数据驱动
    @pytest.mark.parametrize("data",[*data])    
    def test_get_topic(self,data):
          
          res=self.topic.get(data)
          print(res)
          #assert res["message"]=="业务成功"
          
   


if __name__=='__main__':
    
    
    pytest.main(['-s','-v'])
    
    