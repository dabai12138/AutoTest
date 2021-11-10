# -*- coding:utf-8 -*-
# -*- coding:gb2312 -*-
# author:wangjian

import csv
import xlrd
import xlwt
import sys,os
import yaml
import pandas as pd
import numpy as np
import datetime,time


basepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
yaml_path = os.path.join(basepath,'conf','test_search.yaml')

class readExcel(object):
    '''read excel file'''
    def __init__(self,file):
        self.filename = file
        self.file = os.path.join(basepath, r'data\filedata\data_excel\%s' % self.filename)
        self.data = xlrd.open_workbook(self.file)

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
    def __init__(self,filename):
        self.filename = filename
        self.file = os.path.join(basepath, r'data\file\data_excel\%s' % self.filename)
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
            print(data)
            for row,col,msg in data:
                print(row,col,msg)
                ws.write(row,col,msg,style)
            # self.wb.save(self.file)
        except Exception as e:
            result = False
        return result

    def save_excel(self):
        self.wb.save(self.file)

class actCsv(object):
    '''action csv file'''
    def __init__(self):
        pass

    def read_csv(self,filename):
        file = os.path.join(basepath, 'file\data_csv\%s' % filename)
        with open(file,'r') as fp:
            data = csv.reader(fp)
        return data

    def write_row(self,file,content):
        if not os.path.exists(file):
            with open(file,'w+') as fp:
                data = csv.writer(fp)
                data.writerow(content)
        else:
            with open(file,"a+") as fp:
                data = csv.writer(fp)
                data.writerow(content)
    def write_rows(self,file,content):
        if not os.path.exists(file):
            with open(file,'w+') as fp:
                data = csv.writer(fp)
                data.writerows(content)
        else:
            with open(file,'a+') as fp:
                data = csv.writer(fp)
                data.writerows(content)

def get_yaml_data(yaml_path=yaml_path):
    if os.path.exists(yaml_path):
        with open(yaml_path,encoding="UTF-8") as fp:
            data = fp.read()
            data = yaml.load(data,yaml.Loader)
            return data

if __name__ == "__main__":
    # rex = readExcel('test_spss.xls')
    # data = rex.get_rows('test_spss')
    # single_list = []
    # all_list = []
    # none_list = []
    # for j in range(len(data[0])):
    #     none_list.append('')
    # for i in data:
    #     if i != none_list:
    #         single_list.append(i)
    #     else:
    #         all_list.append(single_list)
    #         single_list = []
    # all_list.append(single_list)
    # for case in all_list:
    #     for step in case:
    #         for index in range(len(step) - 1, -1, -1):
    #             if step[index] == '':
    #                 step.pop(index)
    # case_name = []
    # for case in all_list:
    #     case_name.append(case[0][1])
    data = get_yaml_data()
    print(data)
