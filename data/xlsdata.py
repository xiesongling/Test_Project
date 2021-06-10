# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 16:23:32 2021

@author: admin
"""
import xlrd
class XlsData:
    
    workbook = None
    def open_excel(self,path):
        """
        打开excel
        :param path: 打开excel文件的位置
        """
        
        if (self.workbook == None):
            self.workbook = xlrd.open_workbook(path)
    
    def get_sheet(self,sheetName):
         """
         获取页名
         :param sheetName: 页名
         :return: workbook
         """
       
         return self.workbook.sheet_by_name(sheetName)
    
    def get_rows(self,sheet):
        """
        获取行号
        :param sheet: sheet
        :return: 行数
        """
        return sheet.nrows
    
    def get_content(self,sheet, row, col):
        """
        获取表格中内容
        :param sheet: sheet
        :param row: 行
        :param col: 列
        :return:
        """
        return sheet.cell(row, col).value
    
    def release(path):
        """释放excel减少内存"""
        global workbook
        workbook.release_resources()
        del workbook
        # todo:没有验证是否可用






































