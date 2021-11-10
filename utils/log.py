# -*- coding:utf-8 -*-
# Author:wangjian


import logging
import traceback
import requests
import time
import os,sys

base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

class Logger(object):
    def __init__(self,logpath):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)#set log level
        self.logpath = logpath

    def handler(self):
        log_time = time.strftime('%Y_%m_%d',time.localtime(time.time()))
        log_file = os.path.join(self.logpath,'logs\{0}.log'.format(log_time))
        self.fhandler = logging.FileHandler(log_file)
        self.fhandler.setLevel(logging.INFO)
        format = logging.Formatter("%(asctime)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        self.fhandler.setFormatter(format)
        self.logger.addHandler(self.fhandler)
        return self.logger

    def INFO(self,msg):
        return self.handler().info(msg)

    def WARN(self,msg):
        return self.handler().warning(msg)

    def ERROR(self,msg):
        return self.handler().error(msg)

class delfile(object):
    '''delete more than n's file'''
    def __init__(self):
        pass

    def __call__(self,filepath,n):
        try:
            ln = os.listdir(filepath)
            if len(ln) >= n:
                ln.sort(key=lambda fn:os.path.getctime(os.path.join(filepath,fn)))
                ln.pop()
                for l in ln:
                    path = os.path.join(filepath,l)
                    os.remove(path)
                msg = 'del log success'
                return msg
        except Exception as e:
            traceback.print_exc()
            msg = 'del file failed'
            return msg

if __name__ == "__main__":
    #loger = Logger(base_path)
    #loger.ERROR('xxx')
    path = os.path.join(base_path,'logs')
    dl = delfile()
    dl(path,10)