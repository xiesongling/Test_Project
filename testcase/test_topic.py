# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:08:18 2021

@author: admin
"""
import pytest
from api.topic import Topic

class TestTopic:
    
    def setup(self):
        self.topic=Topic()
        
    def test_token(self):
        print(self.topic.token())
    def test_get_topic(self):
        print(self.topic.get(1018, 1, "4dd2457e322ce8b8", 1, 15))
    

if __name__=='__main__':
    pytest.main(['-s','-v'])    