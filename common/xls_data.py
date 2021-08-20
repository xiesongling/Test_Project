# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:06:43 2021

@author: admin
"""
import json
import xlrd
class XlsData:
    def __init__(self,path,sheetname):
        self.workbook=xlrd.open_workbook(path)
        self.worksheet=self.workbook.sheet_by_name(sheetname)
        #获取第二行作为key值
        self.keys=self.worksheet.row_values(1)
        #获取总行数
        self.rownum=self.worksheet.nrows
        #获取总列数
        self.colnum=self.worksheet.ncols
    def env_data(self):
        
        e=self.worksheet.row_values(0)[0]
        env=json.loads(e)
        self.url=env["testing-status"][env["default"]]
        return self.url
    
    def variable_redata(self):
        r=self.worksheet.row_values(0)[1]
        redata=json.loads(r)
        print(type(r))
        return redata
        
    def dict_data(self,url):
        if self.rownum <=1:
            print("总行数小于等于1")
        else:
            r=[]
            j=2
            for i in list(range(self.rownum-2)):
                s={}
                #从第三行取value值
                values=self.worksheet.row_values(j)
                for x in list(range(self.colnum)):
                    
                    s[self.keys[x]]=values[x].replace("\n","")
                
                #print(type[s[self.keys[1]]])
                s["url"]=url+s["url"]
                raw=json.dumps(s)
                redata=self.variable_redata()
                for key,value in redata.items():
                   raw=raw.replace(f'${{{key}}}', value)
                s=json.loads(raw)
                r.append(s)#append()在列表末尾添加新的对象
                j+=1
            return r    
'''
if __name__ == "__main__":
    filepath = "../data/easycook.xlsx"
    sheetName = "首页"
    data = XlsData(filepath, sheetName)
    env=XlsData(filepath, sheetName).env_data()
    a=data.dict_data(env)
    #a=json.loads(a)
    print(a)
    #print(type(a))
'''    
          