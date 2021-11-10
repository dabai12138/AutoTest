# -*- coding:utf-8 -*-
# author:wangjian

import os,sys
base_path = os.path.abspath(os.path.split(os.path.dirname(__file__))[0])
sys.path.append(base_path)
PATH = lambda *p:os.path.abspath(os.path.join(base_path,*p))
