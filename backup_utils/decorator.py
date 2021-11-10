#author:wangjian
#-*- coding:utf-8 -*-

import sys,os
import traceback
import functools

def verification(func):
    @functools.wraps(func)
    def wapper(*args,**kwargs):
        try:
            res = func(*args,**kwargs)
            return res
        except Exception as e:
            print(e)
    return wapper

if __name__ == "__main__":
    pass