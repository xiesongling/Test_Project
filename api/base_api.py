# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:35:39 2021

@author: admin
"""
import requests


class BaseApi:
    def send(self,**data):   #两个星（**）：表示接收的参数作为字典来处理
        return requests.request(**data,verify=False).json()
    
