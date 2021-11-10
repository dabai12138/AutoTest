# -*- coding:utf-8 -*-
# -*- coding:gbk -*-

import configparser
import yaml
import pymysql
import sys
import os

base_path = os.path.abspath(os.path.split(os.path.dirname(__file__))[0])
sys.path.append(base_path)
PATH = lambda *p:os.path.abspath(os.path.join(base_path,*p))


class readConf(object):
    def __init__(self,confpath):
        self.config = configparser.ConfigParser()
        self.config.read(confpath,encoding='utf-8-sig')

    def get_option(self,section):
        return self.config.options(section)

    def get_items(self,section):
        return self.config.items(section)

if __name__ == "__main__":
    pass