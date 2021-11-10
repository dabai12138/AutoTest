# -*- coding:utf-8 -*-
# -*- coding:gbk -*-

import configparser
import yaml
import pymysql
import sys
import os
path = os.path.join(os.path.split(os.getcwd())[0],'conf\keyword.ini')


class readConf(object):
    def __init__(self,confpath):
        self.config = configparser.ConfigParser()
        self.config.read(confpath,encoding='utf-8-sig')

    def get_option(self,section):
        return self.config.options(section)

    def get_items(self,section):
        return self.config.items(section)

if __name__ == "__main__":
    rc = readConf(path)
    rr = rc.get_items('Stttt')
    print(type(rr[0][1]),type(eval(rr[0][1])))