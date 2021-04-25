# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:16:55 2021

@author: xie
"""

import requests
import pytest

#获取token
@pytest.fixture()
def get_token():
    url="https://test-calling-api.apyfc.com/calling/community/app/api/v3/login"
    data={
        "loginType": "pwd",
        "loginWithPwdRequest": {
              "mobile": "13545424538",
              "pwd": "123456"} 
        }

    res=requests.post(url, json=data)
    return(res.json()["data"]["token"])
    
#get_token()


#创建话题
def test_create_topic(token):
    headers = {'token': token}
    url="https://test-calling-api.apyfc.com/calling/community/app/api/v3/topic/publish"
    data={
      "appoint": "同意",
      
      "content": "测试11",
      "showOptions": "[支持,反对]",
      "title": "测试1",
     
     }
    res=requests.post(url,json=data,headers=headers)
    print(res.json())
    
    
test_create_topic(get_token)
