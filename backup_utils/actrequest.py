# -*- coding:utf-8 -*-
# author:wangjian

import requests
import json
import numpy as np
import os,sys
try:
    import cookielib
except:
    import http.cookiejar as cookielib
from bs4 import BeautifulSoup
from abc import ABCMeta,abstractmethod


class Request(metaclass=ABCMeta):
    @abstractmethod
    def header(self):
        pass
    
    @abstractmethod
    def url(self):
        pass
    
    @abstractmethod
    def data(self):
        pass

class BaseRequest(object):
    def __init__(self,base_url):
        self.base_url = base_url
        self.header = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = self.base_url + url

    def set_headers(self,header):
        self.header = header

    def set_data(self,data):
        self.data = data

    def set_files(self,file):
        self.files = file

class ActRequest(BaseRequest):
    user_info = {}
    def __init__(self,base_url):
        super(ActRequest,self).__init__(base_url)
        self.session = requests.Session()
        self.session.post(url)



    def header_format(self,lenth,cookie,obj,modul):
        headers = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':f'{lenth}',
            'Content-Type':'application/json;charset=utf8',
            'Cookie':cookie,
            'expire':'OFF',
            'Host':'bkzx-dev.hzos.hzs.zj',
            'Origin':f'https://{obj}-dev.hzos.hzs.zj',
            'Referer':f'https://{obj}-dev.hzos.hzs.zj/{modul}',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        return headers

    def get(self,url,header):
        self.set_headers(header)
        r = self.session.get(url,header)
        return r

    def post(self,url,data=None,json=None,**kwargs):
        r = self.session.post(url,data=data,json=json,**kwargs)
        return r

    def save_cookie(self,filename):
        try:
            self.session.cookies = cookielib.MozillaCookieJar(filename=filename)
            self.session.cookies.save(filename=filename,ignore_discard=True, ignore_expires=True)
            result = True
        except Exception as e:
            result = False
        return result

    def load_cookie(self,filename):
        try:
            self.session.cookies = cookielib.MozillaCookieJar(filename=filename)
            self.session.cookies.load(filename=filename,ignore_discard=True,ignore_expires=True)
            result = True
        except Exception as e:
            result = False
        return result


if __name__ == "__main__":
    print(1)
