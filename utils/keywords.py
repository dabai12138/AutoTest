#! -*- codinf:utf-8 -*-
# author:wangjian

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import *
from utils.actpage import ActPage
from utils.log import Logger
from utils.conf import readConf
from random import randint
from time import sleep
import win32gui
import win32con
import win32api
import pyautogui
import os,sys

class KeyWords(ActPage):
    '''login bkzx'''
    def __init__(self,driver):
        super(KeyWords,self).__init__(driver)

    def search(self,url):
        self.open_browser(url)
        self.input(By.ID,search_id,search_msg)
        self.click(By.ID,click_id)

if __name__ == "__main__":
    # pyautogui.typewrite()
    # pyautogui.screenshot()
    pass