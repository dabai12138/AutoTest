#! -*- codinf:utf-8 -*-
# author:wangjian

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import *
from utils.actpage import ActPage
from utils.log import Logger
from utils.decorator import verification
from utils.conf import readConf
from random import randint
from time import sleep
import win32gui
import win32con
import win32api
import pyautogui
import os,sys


base_path = os.path.split(os.path.dirname(__file__))[0]
cur_path = sys.argv[0]
kwconfpath = os.path.join(base_path,'conf/keyword.ini')
logger = Logger(base_path)


class KeyWords(ActPage):
    '''login bkzx'''
    def __init__(self,driver):
        super(KeyWords,self).__init__(driver)

    def conf(self,section,confpath=kwconfpath):
        '''
        get the values of section.
        :param section:
          section name
        :return:
          tuple values
        '''
        self.rc = readConf(confpath)
        clist = self.rc.get_items(section)
        if len(clist) > 1:
            values = []
            for conf in clist:
                values.append(conf[1])
        else:
            values = clist[0][1]
        return values

    def add_image(self, photeFrame, imagedir, imagelist, determine):
        '''add image'''
        for image in imagelist:
            imagepath = os.path.join(imagedir, image)
            res = self.presenceEle(By.XPATH,photeFrame)
            if res:
                res.click()
            sleep(5)
            self.upload(imagepath)
            sleep(5)
            self.exec_js(determine)

    @verification
    def login(self,user,password,time=30):
        self.open_browser(login_url)
        self.exec_js(login_js)
        self.exec_js(user_js.format(user))
        self.exec_js(passwd_js.format(password))
        self.exec_js(button_js)
        self.imp_wait(time)
        now_handle = self.curHandle()
        self.switchWindow(now_handle)
        res = True
        if self.titleIs(mh_title):
            now_handle = self.curHandle()
            res = self.presenceEle(By.CLASS_NAME,'app-item-name')
            #sleep(2)
            if res:
                self.exec_js(bkzx_js)
                self.switchWindow(now_handle)
                if self.titleIs(title):
                    logger.INFO('{0}:login successful.'.format(cur_path))
                else:
                    logger.INFO('{0}:login failed.'.format(cur_path))
        elif self.titleIs(title):
            logger.INFO('{0}:login successful.'.format(cur_path))
        else:
            logger.INFO('{0}:login failed.'.format(cur_path))
            res = False
        return res

    @verification
    def logout(self,time=30):
        self.moveToEle(By.XPATH,logout)
        self.click(By.XPATH,dropout)
        self.click(By.ID,logoutid)
        self.click(By.ID,dropoutid)
        self.imp_wait(time)
        res = True
        if self.urlIs(login_url):
            logger.INFO('{0}:logout sucessful.'.format(cur_path))
        else:
            logger.INFO('{0}:logout failed.'.format(cur_path))
            res = False
        return res

    @verification
    def upload(self,imagepath):
        '''upload image or video'''
        no1 = win32gui.FindWindow('#32770', '打开')
        comboboxex32 = win32gui.FindWindowEx(no1, 0, 'ComboBoxEx32', None)
        combobox = win32gui.FindWindowEx(comboboxex32, 0, 'ComboBox', None)
        edit = win32gui.FindWindowEx(combobox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(no1, 0, 'Button', '打开(&O)')
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None,imagepath)
        win32gui.SendMessage(no1, win32con.WM_COMMAND, 1, button)
        return

    def createVideoDir(self,level=1,testdir='testdir'):
        '''create video dir'''
        createdir_js, inputname_js, determine = self.conf('CREATEVIDEODIR')
        if level == 1:
            self.exec_js(createdir_js.format(level))
            self.exec_js(inputname_js.format(int(level)-1,testdir))
            self.exec_js(determine)
        #undo

    def exportFile(self):
        pass

    def _selectDate(self,date_cls,attr):
        '''
        Select date.
        '''
        eles = self.locate_elements(By.CLASS_NAME,date_cls)
        lists = []
        for ele in eles:
            value = ele.get_attribute(attr)
            if value == 'false':
                date = ele.text
                lists.append((int(date),ele))
        return lists

    @verification
    def selectTime(self,start=None,stop=None):
        '''
        Choose start and end time.
        :param start:
          start=1 Start date 1
        :param stop:
          stop=24 Stop date 24
        :return:
        '''
        start_stop, determine, date_cls, attr = self.conf('SELECTTIME')
        self.exec_js(start_stop)
        self.sleep(3)
        lists = self._selectDate(date_cls,attr)
        if start is None and stop is None:
            lists[0][1].click()
            lists[-1][1].click()
        else:
            lists[start][1].click()
            lists[stop][1].click()
        self.sleep(3)
        self.exec_js(determine)
        return

    def dateButton(self,n=0):
        '''
        click date button.
        :param n:
        :return:
        '''
        datebutton = self.conf('DATEBUTTON')
        datebutton = datebutton.format(n)
        self.exec_js(datebutton)
        return

    def selectTree(self,n=0):
        '''
        :param n:
          n=0 check all
          n=1 check first
          ...
        :return:
        '''
        selectionbox, showcheckbox, checkbox = self.conf('SELECTTREE')
        checkbox = checkbox.format(n)
        self.exec_js(selectionbox)
        self.sleep(1)
        try:
            self.exec_js(showcheckbox)
            self.sleep(1)
        except:
            self.sleep(1)
        self.exec_js(checkbox)
        self.sleep(1)
        return


    def selectPointR(self,x=950,y=500,time=2,button='left'):
        '''
        select range of point.
        :param x:
        :param y:
        :param time:
        :param button:
        :return:
        '''
        point_js = self.conf('RANGE')[0]
        self.exec_js(point_js)
        pyautogui.click(x,y,duration=time,button=button)
        self.sleep(2)
        return

    def selectCircle(self,x1=950,y1=500,x2=1350,y2=700,time=2,button='left'):
        '''
        select range of circle.
        :param x1 y1:
          x1 y2: Starting point coordinates
        :param x2 y2:
          x2 y2: End point coordinates
        :param time:
        :param button:
        :return:
        '''
        circle_js = self.conf('RANGE')[1]
        self.exec_js(circle_js)
        pyautogui.moveTo(x1,y1,duration=time)
        pyautogui.dragTo(x2,y2,duration=time,button=button)
        self.sleep(2)
        return

    def selectFrame(self,x=None,y=None):
        frame_js = self.conf('RANGE')[2]
        self.exec_js(frame_js)
        n = randint(3,9)
        for i in range(1,n+1):
            if not x and not y:
                x = randint(700, 1500)
                y = randint(300, 700)
            if i != n:
                pyautogui.click(x, y, duration=1, button='left')
            else:
                pyautogui.doubleClick(x, y)
            x = y = None
        self.sleep(2)

    def searchPoint(self,msg):
        selectpoint, searchKeyword, search = self.conf('SELECTEDPOINT')
        self.exec_js(selectpoint)
        self.exec_js(searchKeyword.format(msg))
        self.exec_js(search)

    def createDir(self,style=None):
        if style is None:
            dirname, newfolder = self.conf('CREATEDIR')[:2]
        else:
            dirname, newfolder = self.conf('CREATECOMMONDIR')
        self.exec_js(dirname)
        self.exec_js(newfolder)

    def selectCommonZone(self, n=None):
        lenth, commonzone, tick, determine = self.conf('SELECTCOMMONZONE')
        self.exec_js(commonzone)
        eles = self.locate_elements(By.CLASS_NAME,lenth)
        if n == None:
            n = randint(1,len(eles))
        for i in range(n):
            self.exec_js(tick.format(i))
        self.exec_js(determine)

    def alarmContact(self,tag='p',n=1):
        eles = self.locate_elements(By.TAG_NAME,tag)
        for ele in eles:
            if ele.get_attribute('title') == u"点击添加告警接收人":
                ele.click()
        if n == 1:
            pass
        #undo

if __name__ == "__main__":
    # pyautogui.typewrite()
    # pyautogui.screenshot()
    pass