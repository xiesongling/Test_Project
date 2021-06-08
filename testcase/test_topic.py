# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:08:18 2021

@author: admin
测试用例
"""
import pytest
from api.topic import Topic

class TestTopic:
    
    def setup(self):
        self.topic=Topic()
        
    def test_token(self):
        print(self.topic.token)
    #数据驱动
    @pytest.mark.parametrize("userId,type,communityCode,pageIndex,pageSize",[(1018, 1, "4dd2457e322ce8b8", 1, 15)])    
    def test_get_topic(self,userId,type,communityCode,pageIndex,pageSize):
          print(self.topic.get(userId,type,communityCode,pageIndex,pageSize))
   


if __name__=='__main__':
    pytest.main(['-s','-v'])
    