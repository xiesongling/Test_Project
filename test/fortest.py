# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:52:59 2021

@author: admin
"""

data={
            "method":"post",
            "url":"https://test-calling-api.apyfc.com/calling/community/app/api/v3/login",
            "jason":{
            "loginType": "pwd",
            "loginWithPwdRequest": {
                  "mobile": "13545424538",
                  "pwd": "123456"} 
            }
            }

type(data)