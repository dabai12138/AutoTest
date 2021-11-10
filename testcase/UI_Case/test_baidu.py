#! -*- codinf:utf-8 -*-
# author:wangjian

from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep
from utils import *
from utils import actpage,actfile
import unittest
import win32gui
import win32con
import win32api
import pyautogui
import os,sys
import inspect

driver_path = PATH("../tools/chromedriver.exe")
yaml_path = PATH("../conf/test_search.yaml")
yaml_data = actfile.get_yaml_data(yaml_path)

class test_search(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(driver_path,options=options)
        #driver = webdriver.Chrome()
        self.AP = actpage.ActPage(driver)
        self.AP.open_browser(yaml_data['url']['new_url'])

    def tearDown(self) -> None:
        self.AP.quit()

    def get_modul_name(self):
        import inspect
        modul_name = (str(inspect.stack()[0]).split(',')[6]).split("=")[1]
        return modul_name

    def test_search_01(self,yaml_data=yaml_data):
        yaml_data = yaml_data['search1']
        self.AP.input(By.ID,yaml_data['search_id'],yaml_data['search_msg'])
        self.AP.click(By.ID,yaml_data['click_id'])
        title = self.AP.ctitle()
        self.assertEqual(title,"百度资讯搜索_热门")

    def test_search_02(self,yaml_data=yaml_data):
        yaml_data = yaml_data['search2']
        self.AP.input(By.ID,yaml_data['search_id'],yaml_data['search_msg'])
        self.AP.click(By.ID,yaml_data['click_id'])
        title = self.AP.ctitle()
        try:
            self.assertEqual(title,"百度资讯搜索_冷门")
        except:
            modul_name = eval((str(inspect.stack()[0]).split(',')[6]).split("=")[1])
            self.AP.getShot(modul_name)

    def test_search_03(self,yaml_data=yaml_data):
        yaml_data = yaml_data['search3']
        self.AP.input(By.ID,yaml_data['search_id'],yaml_data['search_msg'])
        self.AP.click(By.ID,yaml_data['click_id'])
        title = self.AP.ctitle()
        try:
            self.assertEqual(title,"百度资讯搜索_水门")
        except:
            modul_name = eval((str(inspect.stack()[0]).split(',')[6]).split("=")[1])
            self.AP.getShot(modul_name)

if __name__ == "__main__":
    unittest.main()