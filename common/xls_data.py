# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:06:43 2021

@author: admin
"""

import xlrd
class XlsData:
    def __init__(self,path,sheetname):
        self.workbook=xlrd.open_workbook(path)
        self.worksheet=self.workbook.sheet_by_name(sheetname)
        #获取第一行作为key值
        self.keys=self.worksheet.row_values(0)
        #获取总行数
        self.rownum=self.worksheet.nrows
        #获取总列数
        self.colnum=self.worksheet.ncols
        
    def dict_data(self):
        if self.rownum <=1:
            print("总行数小于等于1")
        else:
            r=[]
            j=1
            for i in range(self.rownum-1):
                s={}
                #从第二行取value值
                s["rownum"]=i+2
                values=self.worksheet.row_values(j)
                for x in range(self.colnum):
                    s[self.keys[x]]=values[x]
                r.append(s)
            return r    
if __name__ == "__main__":
    filepath = "../data/easycook.xlsx"
    sheetName = "首页"
    data = XlsData(filepath, sheetName)
    print(data.dict_data())
            