# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:35:39 2021

@author: admin
"""
import requests
from data.xlsdata import XlsData

class BaseApi:
    def send(self,**data):   #两个星（**）：表示接收的参数作为字典来处理
        return requests.request(**data).json()
    def get_xlsdata(self):
        xlsdata=XlsData()
        xlsdata.open_excel("../data/easycook.xlsx")
        sheet=xlsdata.get_sheet("首页")
        datas=xlsdata.get_content(sheet, 1, 0)
        return datas
