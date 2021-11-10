# -*- coding:utf-8 -*-
# Author:wangjian


import logging
import traceback
import requests
import time
import os,sys
base_path = os.path.abspath(os.path.split(os.path.dirname(__file__))[0])
sys.path.append(base_path)
PATH = lambda *p:os.path.abspath(os.path.join(base_path,*p))

def Logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_time = time.strftime('%Y_%m_%d',time.localtime(time.time()))
    log_file = PATH('logs',f'{log_time}.log')
    fhandler = logging.FileHandler(log_file)
    fhandler.setLevel(logging.INFO)
    format = logging.Formatter("%(asctime)s - moduleName:%(module)s - funcName:%(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fhandler.setFormatter(format)
    logger.addHandler(fhandler)
    return logger

def delLog(filepath,loger,n=10):
    '''delete more than n's file'''
    try:
        ln = os.listdir(filepath)
        ln+=1
        if len(ln) >= n:
            ln.sort(key=lambda *fn:os.path.getctime(os.path.join(filepath,*fn)))
            newLog = ln.pop()
            for l in ln:
                path = os.path.join(filepath,l)
                os.remove(path)
        loger.info('del log success')
    except Exception as e:
        traceback.print_exc()
        loger.error(f'del file failed. reason:{e}')

if __name__ == "__main__":
    # loger = Logger()
    # path = PATH('logs')
    # delLog(path,loger)
    print(PATH("xxx"))

