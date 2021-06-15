# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:08:18 2021

@author: admin
测试用例
"""
import pytest
import json
from api.topic import Topic
from api.base_api import BaseApi

class TestTopic:
    baseapi=BaseApi()
    data=json.loads(baseapi.get_xlsdata())
    def setup(self):
        self.topic=Topic()
        
        
    def test_token(self):
        print(self.topic.token)
    #数据驱动
    #@pytest.mark.parametrize("userId,type,communityCode,pageIndex,pageSize",[(1018,1,"4dd2457e322ce8b8",1,15)])    
    def test_get_topic(self):
          res=self.topic.get(self.data)
          print(res)
          assert res["message"]=="业务成功"
          
   


if __name__=='__main__':
    pytest.main(['-s','-v'])
    