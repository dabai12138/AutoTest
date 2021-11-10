# -*- coding:utf-8 -*-
# -*- coding:gb2312 -*-
# author:wangjian

import csv
import xlrd
import xlwt
import sys,os
import xlsxwriter
import datetime,time


PATH = lambda *p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), *p)
)
print(PATH('../data','file','data_csv','test_csv'))
class Element(object):
    INFO_FILE = PATH("../logs/info.pickle")#记录结果
    REPORT_FILE = PATH("../report/Report.xlsx")#测试报告
    API_FILE = PATH("../report/api.xlsx")#用例文件
    PICT_PARAM = PATH("../logs/param.txt")#写入pict需要的参数
    PICT_PARAM_RESULT = PATH("../logs/param_result.txt")#pict生成的数据
    OPEN_PICT = PATH("../conf/Pict.ini")#pict配置器
    ERROR_EMPTY = "error_empty"
    ERROR_VALUE = "error_value"
    
class readExcel(object):
    '''read excel file'''
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = xlrd.open_workbook(self.filepath)

    #get all row data
    def get_rows(self,name='Sheet1'):
        table = self.data.sheet_by_name(name)
        nrows = table.nrows
        rows = []
        for row in range(nrows):
            data = table.row_values(row)
            rows.append(data)
        return rows

    #get one row data
    def get_row(self,row,name='Sheet1'):
        table = self.data.sheet_by_name(name)
        data = table.row_values(row)
        return data

     #get all col data
    def get_cols(self,name='Sheet1'):
        table = self.data.sheet_by_name(name)
        ncols = table.ncols
        cols = []
        for col in range(ncols):
            data = table.col_values(col)
            cols.append(data)
        return cols

    #get one col data
    def get_col(self,col,name='Sheet1'):
        table = self.data.sheet_by_name(name)
        data = table.col_values(col)
        return data

    #get cell data,row and col start from 0
    def get_cell(self,row,col,name='Sheet1'):
        table = self.data.sheet_by_name(name)
        data = table.cell_value(row,col)
        return data

class writeExcel(object):
    '''write excel file'''
    def __init__(self,filepath):
        self.filepath = filepath
        self.wb = xlwt.Workbook(encoding='ascii')

    def _create_sheet(self,name):
        ws = self.wb.add_sheet(name,cell_overwrite_ok=True)
        return ws

    def font_style(self,bold=False,underline=False,italic=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = "new font style"
        font.bold = bold#黑体
        font.underline = underline#下划线
        font.italic = italic#斜体
        style.font = font
        return style

    def write_excel(self,*data,name,bold=False,underline=False,italic=False):
        result = True
        ws = self._create_sheet(name)
        try:
            style = self.font_style(bold,underline,italic)
            for row,col,msg in data:
                ws.write(row,col,msg,style)
            # self.wb.save(self.file)
        except Exception as e:
            print(e)
            result = False
        return result

    def save_excel(self):
        self.wb.save(self.filepath)

class actCsv(object):
    '''action csv file'''
    def __init__(self,filepath):
        self.filepath = filepath

    def read_csv(self):
        with open(self.filepath,'r') as fp:
            data = csv.reader(fp)
        return data

    def write_row(self,content):
        with open(self.filepath,"a+") as fp:
            data = csv.writer(fp)
            data.writerow(content)
            
    def write_rows(self,content):
        with open(self.filepath,'a+') as fp:
            data = csv.writer(fp)
            data.writerows(content)


if __name__ == "__main__":
    pass