# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:35:39 2021

@author: admin
"""
import requests
import json

'''
class BaseApi:
    def send(self,**data):   #两个星（**）：表示接收的参数作为字典来处理
        return requests.request(**data,verify=False).json()
'''
class BaseApi:
    def sen_request(self,testdata):
        '''封装request请求'''
        method=testdata["method"]
        url=testdata["url"]
        try:
            headers=eval(testdata["headers"])
        except:
            headers=None
        try:
            params=eval(testdata["params"])
        except:
            params=None
        try:
            bodydata=eval(testdata["body"])
        except:
            bodydata={}
        
        verify=False
        # 判断传data数据还是json   
        type=testdata["type"]
        if type=="data":
            body=bodydata
        elif type=="json":
            body=json.dumps(bodydata)
        else:
            body=bodydata
        try:
            r=requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=body,
                verify=verify
                )
            return r.json()
        except Exception as msg:
            msg=str(msg)
            return r.text

        
           
        
            
                
                
            
        
        
