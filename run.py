# -*- codinf:utf-8 -*-
# author:wangjian

from threading import Thread
from tools.HTMLTestRunner import HTMLTestRunner
from utils import *
from utils.smtp import Smtp
from utils.actfile import readExcel,get_yaml_data
from utils.log import Logger,delLog
import unittest
import sys,os
import time

base_path = PATH("..")
conf_path = PATH("..\conf\keywords.json")
report_path = PATH("..\\report")
email_yaml_path = PATH("..\conf\email.yaml")

class RunCase(object):

    def __init__(self,caseDir=r'testcase\UI_Case'):
        self.caseDir = caseDir
        self.loger = Logger()
        self.case_path = os.path.join(base_path, self.caseDir)

    def _add_case(self,rule):
        if not os.path.exists(self.case_path):os.mkdir(self.case_path)
        discover = unittest.defaultTestLoader.discover(start_dir=self.case_path,
                                                       pattern=rule,
                                                       top_level_dir=None)
        return discover

    def testname(self,rule):
        discover = self._add_case(rule)
        data = discover.__str__()[99:-6]
        n_list = data.split(',')
        name_list = []
        for n in n_list:
            l = n.split('=')
            name_list.append(l[-1][:-1])
        return name_list

    def run_case(self,name,rule):
        testtime = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
        filepath = os.path.join(base_path, 'report\{0}_AutoTestReport.html'.format(testtime))
        discover = self._add_case(rule)
        with open(filepath, 'wb') as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title="测试报告",
                                    description=u'{0}自动化测试报告'.format(name))
            runner.run(discover)
        self.send_email()

    def readCaseInfo(self,filename,sheetname):
        rex = readExcel(filename)
        data = rex.get_rows(sheetname)
        single_list = []
        all_list = []
        none_list = []
        case_name = []
        for j in range(len(data[0])):
            none_list.append('')
        #cut all testcase
        for i in data:
            if i != none_list:
                single_list.append(i)
            else:
                all_list.append(single_list)
                single_list = []
        all_list.append(single_list)
        #delete null obj
        for case in all_list:
            for step in case:
                for index in range(len(step) - 1, -1, -1):
                    if step[index] == '':
                        step.pop(index)
        #get testcase name list
        for case in all_list:
            case_name.append(case[0][1])
        return all_list,case_name

    #write excel testcase to code.
    def write_testcase(self,caselist,casepath):
        with open(conf_path, 'r+') as fp:
            kw_dict = eval(fp.read())
        if len(caselist) != 0:
            with open(casepath,'a+') as fp:
                for case in caselist:
                    name = case[0][1]
                    fp.write('\n    {0} {1}(self):\n'.format('def',name))
                    for step in case[1:]:
                        kw = step[1]
                        para = step[2:]
                        if len(para) == 0:
                            msg = kw_dict[kw].format('self.kw')
                        if len(para) == 1:
                            if type(para[0]) == str and '.' in para[0]:
                                #undo
                                para[0] = int(float(para[0]))
                            msg = kw_dict[kw].format('self.kw',para[0])
                        if len(para) == 2:
                            msg = kw_dict[kw].format('self.kw',para[0],para[1])
                        if len(para) == 3:
                            msg = kw_dict[kw].format('self.kw',para[0],para[1],para[2])
                        if len(para) == 4:
                            msg = kw_dict[kw].format('self.kw',para[0],para[1],para[2],para[3])
                        fp.write('        {0}\n'.format(msg))
                        #fp.write('{0}\n'.format(msg).rjust(8))
                fp.flush()

    def run(self,rule):
        name_list = self.testname(rule)
        sheetname = rule[:-4]
        filename = sheetname + '.xls'
        casefile = sheetname + '.py'
        casepath = os.path.join(self.case_path,casefile)
        add_list = []
        add_case = []
        step_list = []
        all_case,case_name = self.readCaseInfo(filename,sheetname)
        for case in case_name:
            if case not in name_list:
                add_list.append(case)
        for case in all_case:
            if case[0][1] in add_list:
                add_case.append(case)
        self.write_testcase(add_case,casepath)
        self.run_case(u'TEST',rule)
        logpath = os.path.join(base_path,'logs')
        screenshotpath = os.path.join(base_path,'screenshot')
        delLog(logpath,self.loger)
        delLog(screenshotpath,self.loger)

    def send_email(self):
        yaml_data = get_yaml_data(email_yaml_path)
        sm = Smtp(yaml_data["smtp_server"])
        sm.send_email(yaml_data['for_email'],yaml_data['passwd'],yaml_data['to_email'],report_path)

def thread_run(rules,func):
    threads = []
    for rule in rules:
        t = Thread(target=func,args=(rule,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    #rules = ['test_spss*.py','test_qybk*.py','test_spzz*.py','test_zsxr*.py','test_lxfx*.py','test_jbtx*.py','test_ycrl*.py']
    #rules = ['test_*.py']
    # thread_run(rules,rc.run())
    rc = RunCase()
    rc.run_case("测试百度","test_*.py")
    #thread_run(rules,rc.run)
    #rc.send_email()


