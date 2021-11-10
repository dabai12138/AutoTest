# -*- codinf:utf-8 -*-
# author:wangjian

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt,unpack,data
from functools import wraps
import time
import os,sys
import win32gui
import win32con
import win32api
import pyautogui


PATH = lambda *p : os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),*p))

def reAct(func):
    @wraps(func)
    def wapper(*args,**kwargs):
        n = 0
        while n<3:
            try:
                rel = func(*args,**kwargs)
                break
            except:
                n+=1
                rel = "{} function is Execution exception".format(func.__name__)
                continue
        return rel
    return wapper

class ActPage(object):
    '''page action'''
    def __init__(self,driver):
        #driver = webdriver.Chrome()
        self.driver = driver

    def open_browser(self,url,time=40):
        '''
        open url step.
        :param url:
        :return:
        '''
        self.driver.maximize_window()
        self.driver.refresh()
        self.driver.get(url)
        self.imp_wait(time)

    
    def curl(self):
        '''
        get current's url.
        :return:
          current's url
        '''
        return self.driver.current_url

    def ctitle(self):
        '''
        get page title.
        :return:
          title's text
        '''
        return self.driver.title

    def getCookie(self):
        '''
        get all cookies.
        :return:
          cookies Dictionary's list
        '''
        return self.driver.get_cookies()

    def addCookie(self,**kwargs):
        '''
        add cookie.
        :param kwargs:
        :return:
        '''
        return self.driver.add_cookie(kwargs)

    def delCookie(self,name):
        '''
        delete cookie.
        :param name:
        :return:
        '''
        return self.driver.delete_cookie(name)

    def delCookies(self):
        '''
        del all cookies.
        '''
        return self.driver.delete_all_cookies()

    @reAct
    def exec_js(self,js):
        '''
        execute javascript code
        '''
        return self.driver.execute_script(js)

    def imp_wait(self,seconds=30):
        '''
        Implicit wait
        '''
        self.driver.implicitly_wait(seconds)

    def web_wait(self,seconds=30):
        return WebDriverWait(self.driver,seconds)

    def sleep(self,seconds=5):
        time.sleep(seconds)

    def titleIs(self,msg):
        '''
        Whether the title is as expected.
        :param msg:
          title's text
        :return:
          True or False
        '''
        return self.web_wait().until(EC.title_is(msg))

    def urlIs(self,url):
        '''
        Whether the url address is as expected.
        :param url:
        :return:
           True or False
        '''
        return self.web_wait().until(EC.url_to_be(url))

    def urlContains(self,url):
        '''
        Does the url address contain expectations.
        :param url:
        :return:
        '''
        return self.web_wait().until(EC.url_contains(url))

    def presenceEle(self,*args):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located(args))

    def visibilityEle(self,*args):
        '''
        Whether the element is displayed.
        '''
        return self.web_wait().until(EC.visibility_of_element_located(args))

    def presenceAlert(self):
        '''
        Whether the alert is present.
        :return:
          alert or None
        '''
        return self.web_wait().until(EC.alert_is_present())

    def unpresenceAlert(self):
        return self.web_wait().until_not(EC.alert_is_present())

    def titleNotIs(self,msg):
        '''
        :param msg:
        :return:
          True or False
        '''
        return self.web_wait().until_not(EC.title_is(msg))

    def urlNotIs(self,url):
        '''
        :param url:
        :return:
           True or False
        '''
        return self.web_wait().until_not(EC.url_to_be(url))

    def urlNotContains(self,url):
        '''
        :param url:
        :return:
          True or False
        '''
        return self.web_wait().until_not(EC.url_contains(url))

    def unpresenceEle(self,*args):
        '''
        :param args:
        :return:
        '''
        return self.web_wait().until_not(EC.presence_of_element_located(args))

    def unvisibilityEle(self,*args):
        '''
        :param args:
        :return:
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located(args))
    
    @reAct
    def displayed(self,locator,value):
        '''
        Whether the element is displayed.
        '''
        self.locate_element(locator,value).is_displayed()

    def enabled(self,locator,value):
        '''
        Whether the element can be used.
        :param locator:
        :param value:
        :return:
        '''
        self.locate_element(locator,value).is_enabled()

    def selected(self,locator,value):
        '''
        Whether the element is selected.
        :param locator:
        :param value:
        :return:
        '''
        self.locate_element(locator,value).is_selected()

    def locate_element(self,locator,value):
        '''
        :param locatetype:
          id,xpath,link text,partial link text,name,tag name,class name,css selector
        :param value:
        :return: ele or None
        '''
        return self.driver.find_element(by=locator,value=value)

    def locate_elements(self,locator,val):
        return self.driver.find_elements(by=locator,value=val)

    def clear(self,locator,val):
        self.locate_element(locator,val).clear()

    @reAct
    def getText(self,locator,val):
        '''
        get element's text
        '''
        return self.locate_element(locator,val).text

    def getSize(self,locator,val):
        '''
        get element's size
        '''
        return self.locate_element(locator,val).size
    
    @reAct
    def getAttrVal(self,locator,val,attr):
        '''
        get element's attribute value.
        '''
        return self.locate_element(locator,val).get_attribute(attr)

    def input(self,locator,val,msg):
        self.locate_element(locator,val).send_keys(msg)

    def select(self,locator,val):
        return Select(self.locate_element(locator,val))

    @reAct
    def selectValue(self,locator,val,content):
        return self.select(locator,val).select_by_value(content)

    @reAct
    def selectText(self,locator,val,content):
        return self.select(locator,val).select_by_visible_text(content)

    @reAct
    def unselectAll(self,locator,val):
        return self.select(locator,val).deselect_all()

    @reAct
    def unselectIndex(self,locator,val,content):
        return self.select(locator,val).deselect_by_index(content)

    @reAct
    def unselectValue(self,locator,val,content):
        return self.select(locator,val).deselect_by_value(content)

    @reAct
    def unselectText(self,locator,val,content):
        return self.select(locator,val).deselect_by_visible_text(content)

    @reAct
    def click(self,locator,value):
        '''
        left click
        '''
        return self.locate_element(locator,value).click()

    def action_chains(self):
        return ActionChains(self.driver)

    @reAct
    def contClick(self,locator,val):
        '''
        right click
        '''
        return self.action_chains().context_click(self.locate_element(locator,val)).perform()

    @reAct
    def moveToEle(self,locator,val):
        '''
        move to element
        '''
        return self.action_chains().move_to_element(self.locate_element(locator,val)).perform()

    @reAct
    def doubleClick(self,locator,val):
        '''
        Double click.
        '''
        return self.action_chains().double_click(self.locate_element(locator,val)).perform()

    @reAct
    def dragAndDrop(self,s_locator,s_val,t_locater,t_val):
        '''
        Drag an element to another element.
        :param args:
          sour,s_value,target,t_value
        :return:
        '''
        sour = self.locate_element(s_locator,s_val)
        target = self.locate_element(t_locater,t_val)
        return self.action_chains().drag_and_drop(sour,target).perform()

    def allHandles(self):
        '''
        get all window handles.
        '''
        return self.driver.window_handles

    def curHandle(self):
        '''
        get current window handle.
        '''
        return self.driver.current_window_handle

    @reAct
    def switchWindow(self,now_handle):
        '''
        Switch window.
        '''
        all_handles = self.allHandles()
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to_window(handle)
                
    @reAct
    def switchFrame(self,locator,val):
        '''
        Switch frame.
        '''
        iframe = self.locate_element(locator,val)
        return self.driver.switch_to_frame(iframe)

    def reSwitchFrame(self):
        '''
        return initial frame.
        '''
        return self.driver.switch_to.default_content

    def alert(self):
        '''
        switch alert.
        '''
        return self.driver.switch_to_alert()

    @reAct
    def acceptAlert(self):
        '''
        Click alert's ok
        '''
        return self.alert().accept()

    @reAct
    def dismissAlert(self):
        '''
        Click alert's cancel.
        '''
        return self.alert().dismiss()

    @reAct
    def inputAlert(self,msg):
        '''
        Enter content in the alert.
        '''
        return self.alert().send_keys(msg)

    @reAct
    def forward(self):
        return self.driver.forward()

    @reAct
    def back(self):
        return self.driver.back()

    @reAct
    def getShot(self,path,func):
        '''
        screenshot and save file.
        :param base_path:
        :param func:
        :return:
        '''
        now_time = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
        fpath = os.path.abspath(os.path.join(path,f'screenshot{now_time}_{func}.png'))
        return self.driver.get_screenshot_as_file(fpath)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

class KeyWords(ActPage):
    def __init__(self,driver):
        super().__init__(driver)

    def login(self,url,user,passwd):
        self.open_browser(url)
        self.click(By.XPATH,'/html/body/div[2]/div/p/span')
        self.clear(By.ID,'ITaccount')
        self.input(By.ID,'ITaccount',user)
        self.clear(By.ID,'ITpassword')
        self.input(By.ID,'ITpassword',passwd)
        self.click(By.ID,'UPLoginBtn')
        self.presenceEle((By.XPATH,'//*[@id="root"]/section/header/div[1]/div[1]/a[1]/span[1]'))
        
    def logout(self):
        pass
    
    def upload(self,imagepath):
        path = PATH('scripts','upload.exe')
        os.system(path)
        

if __name__ == "__main__":
    path = PATH('scripts','upload.exe')
    os.system(path)

