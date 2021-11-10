# -*- coding:utf-8 -*-
# -*- coding:gbk -*-


from abc import ABCMeta,abstractmethod
import configparser
import yaml
import sys
import os

PATH = lambda *p : os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),*p))

class Conf(metaclass=ABCMeta):
    # @abstractmethod
    # def get_sections(self):
    #     pass

    @abstractmethod
    def get_options(self):
        pass

    @abstractmethod
    def get_option_val(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

class ActConf(Conf):
    def __init__(self,confpath):
        self.conf = configparser.ConfigParser()
        self.conf.read(confpath,encoding='utf-8-sig')

    def get_sections(self):
        """get all section"""
        return self.conf.sections()

    def get_options(self,section):
        """get all option"""
        return self.conf.options(section)

    def get_option_val(self,section,option):
        """get value of option"""
        self.conf.get(section,option)

    def get_items(self,section):
        """get all option and value"""
        self.conf.items(section)

class ActYaml(Conf):
    def __init__(self,yamlpath):
        with open(yamlpath,'r',encoding='utf-8') as fp:
            self.cont = yaml.load(fp,Loader=yaml.FullLoader)  

    def get_options(self):
        return self.cont.keys()

    def get_option_val(self):
        return self.cont.values()

    def get_items(self):
        return self.cont.items()

if __name__ == "__main__":
    path = PATH('data','file','data_yaml','test_case.yaml')
    ay = ActYaml(path)
    data = ay.cont

    print(data[1])

    for d in data:
        dd = list(d.values())[0]
        for i in range(len(dd)):
            dd[i]['act']
            dd[i]['type']
            dd[i]['val']

