# -*- codinf:utf-8 -*-
# author:wangjian

import sys,os
base_path = os.path.split(os.path.dirname(__file__))[0]
cpath = os.path.join(base_path,'utils')
sys.path.append(cpath)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.log import Logger
from time import sleep
import time


logger = Logger(base_path)

class ActPage(object):
    '''page action'''
    def __init__(self,driver):
        #driver = webdriver.Chrome()
        self.driver = driver

    
    def open_browser(self,url,time=30):
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

#**************************************==***************************************************

    
    def presenceEle(self,*args):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located(args))

    
    def preEleXP(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.XPATH,val)))

    
    def preEleID(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.ID,val)))

    
    def preEleName(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.NAME,val)))

    
    def preEleTag(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.TAG_NAME,val)))

    
    def preEleCls(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.CLASS_NAME,val)))

    
    def preEleCss(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR,val)))

    
    def preEleLink(self,val):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.LINK_TEXT,val)))

    
    def preElePLink(self,Text):
        '''
        Whether the element is presence
        '''
        return self.web_wait().until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,Text)))

#*******************************************************==*************************************************

    
    def visibilityEle(self,*args):
        '''
        Whether the element is displayed.
        '''
        return self.web_wait().until(EC.visibility_of_element_located(args))

    
    def visEleID(self,val):
        '''
        Whether the element is displayed.
        id.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.ID,val)))


    
    def visEleXP(self,val):
        '''
        Whether the element is displayed.
        xpath.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.XPATH,val)))

    
    def visEleName(self,val):
        '''
        Whether the element is displayed.
        name.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.NAME,val)))

    
    def visEleCls(self,val):
        '''
        Whether the element is displayed.
        class name.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.CLASS_NAME,val)))

    
    def visEleCss(self,val):
        '''
        Whether the element is displayed.
        css selector.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR,val)))

    
    def visEleTag(self,val):
        '''
        Whether the element is displayed.
        tag name.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.TAG_NAME,val)))

    
    def visEleLink(self,val):
        '''
        Whether the element is displayed.
        link text.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.LINK_TEXT,val)))

    
    def visElePLink(self,val):
        '''
        Whether the element is displayed.
        partial link text.
        '''
        return self.web_wait().until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,val)))

#*****************************************************==*****************************************************

    
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

#**********************************==*****************************************

    
    def unpresenceEle(self,*args):
        '''
        :param args:
        :return:
        '''
        return self.web_wait().until_not(EC.presence_of_element_located(args))

    
    def unpreEleXP(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.XPATH,val)))

    
    def unpreEleID(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.ID,val)))

    
    def unpreEleName(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.NAME,val)))

    
    def unpreEleTag(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.TAG_NAME,val)))

    
    def unpreEleCls(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.CLASS_NAME,val)))

    
    def unpreEleCss(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.CSS_SELECTOR,val)))

    
    def unpreEleLink(self,val):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.LINK_TEXT,val)))

    
    def unpreElePLink(self,Text):
        '''
        Whether the element is unpresence
        '''
        return self.web_wait().until_not(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,Text)))

#**************************************==*************************************

    
    def unvisibilityEle(self,*args):
        '''
        :param args:
        :return:
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located(args))

    
    def unvisEleID(self, val):
        '''
        Whether the element is undisplayed.
        id.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.ID, val)))

    
    def unvisEleXP(self, val):
        '''
        Whether the element is undisplayed.
        xpath.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.XPATH, val)))

    
    def unvisEleName(self, val):
        '''
        Whether the element is undisplayed.
        name.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.NAME, val)))

    
    def unvisEleCls(self, val):
        '''
        Whether the element is undisplayed.
        class name.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.CLASS_NAME, val)))

    
    def unvisEleCss(self, val):
        '''
        Whether the element is undisplayed.
        css selector.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, val)))

    
    def unvisEleTag(self, val):
        '''
        Whether the element is undisplayed.
        tag name.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.TAG_NAME, val)))

    
    def unvisEleLink(self, val):
        '''
        Whether the element is undisplayed.
        link text.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.LINK_TEXT, val)))

    
    def unvisElePLink(self, val):
        '''
        Whether the element is undisplayed.
        partial link text.
        '''
        return self.web_wait().until_not(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, val)))

#**************************************==*************************************


    
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

    # def locate_element(self,locator,value):
    #     '''
    #     :param locatetype:
    #       id,xpath,link text,partial link text,name,tag name,class name,css selector
    #     :param value:
    #     :return: ele or None
    #     '''
    #     return self.driver.find_element(by=locator,value=value)

    def locate_element(self,locator,val):
        '''
        :param loatetype:
          id,xpath,link text,partial link text,name,tag name,class name,css selector
        '''
        locator = locator.lower()
        if locator == 'xpath':
            return self.driver.find_element(by=By.XPATH,value=val)
        if locator == 'class':
            return self.driver.find_element(by=By.CLASS_NAME,value=val)
        if locator == 'id':
            return self.driver.find_element(by=By.ID,value=val)
        if locator == 'plinktext':
            return self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=val)
        if locator == 'linktext':
            return self.driver.find_element(by=By.LINK_TEXT,value=val)
        if locator == 'tag':
            return self.driver.find_element(by=By.TAG_NAME,value=val)
        if locator == 'name':
            return self.driver.find_element(by=By.NAME,value=val)
        if locator == 'css':
            return self.driver.find_element(by=By.CSS_SELECTOR,value=val)

    
    def locate_elements(self,locator,val):
        '''
        :param loatetype:
          id,xpath,link text,partial link text,name,tag name,class name,css selector
        '''
        locator = locator.lower()
        if locator == 'xpath':
            return self.driver.find_elements(by=By.XPATH, value=val)
        if locator == 'class':
            return self.driver.find_elements(by=By.CLASS_NAME, value=val)
        if locator == 'id':
            return self.driver.find_elements(by=By.ID, value=val)
        if locator == 'plinktext':
            return self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=val)
        if locator == 'linktext':
            return self.driver.find_elements(by=By.LINK_TEXT, value=val)
        if locator == 'tag':
            return self.driver.find_elements(by=By.TAG_NAME, value=val)
        if locator == 'name':
            return self.driver.find_elements(by=By.NAME, value=val)
        if locator == 'css':
            return self.driver.find_elements(by=By.CSS_SELECTOR, value=val)

    def clear(self,locator,val):
        self.locate_element(locator,val).clear()

    
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

    
    def getAttrVal(self,locator,val,attr):
        '''
        get element's attribute value.
        '''
        return self.locate_element(locator,val).get_attribute(attr)

    
    def input(self,locator,val,msg):
        self.locate_element(locator,val).send_keys(msg)

    def select(self,locator,val):
        return Select(self.locate_element(locator,val))

    
    def selectAll(self,locator,val):
        return self.select(locator,val).all_selected_options()

    
    def selectIndex(self,locator,val,content):
        return self.select(locator,val).select_by_index(content)

    
    def selectValue(self,locator,val,content):
        return self.select(locator,val).select_by_value(content)

    
    def selectText(self,locator,val,content):
        return self.select(locator,val).select_by_visible_text(content)

    
    def unselectAll(self,locator,val):
        return self.select(locator,val).deselect_all()

    
    def unselectIndex(self,locator,val,content):
        return self.select(locator,val).deselect_by_index(content)

    
    def unselectValue(self,locator,val,content):
        return self.select(locator,val).deselect_by_value(content)

    
    def unselectText(self,locator,val,content):
        return self.select(locator,val).deselect_by_visible_text(content)

    def action_chains(self):
        return ActionChains(self.driver)

    
    def click(self,locator,value):
        '''
        left click
        '''
        return self.locate_element(locator,value).click()

    
    def contextClick(self,locator,val):
        '''
        right click
        '''
        return self.action_chains().context_click(self.locate_element(locator,val)).perform()

    
    def moveToEle(self,locator,val):
        '''
        move to element
        '''
        return self.action_chains().move_to_element(self.locate_element(locator,val)).perform()

    
    def doubleClick(self,locator,val):
        '''
        Double click.
        '''
        return self.action_chains().double_click(self.locate_element(locator,val)).perform()

    
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

    
    def switchWindow(self,now_handle):
        '''
        Switch window.
        '''
        all_handles = self.allHandles()
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to_window(handle)

    
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

    
    def acceptAlert(self):
        '''
        Click alert's ok
        '''
        return self.alert().accept()

    
    def dismissAlert(self):
        '''
        Click alert's cancel.
        '''
        return self.alert().dismiss()

    
    def inputAlert(self,msg):
        '''
        Enter content in the alert.
        '''
        return self.alert().send_keys(msg)

    
    def forward(self):
        return self.driver.forward()

    
    def back(self):
        return self.driver.back()

    
    def getShot(self,func):
        '''
        screenshot and save file.
        :param base_path:
        :param func:
        :return:
        '''
        now_time = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
        fpath = os.path.join(base_path,'screenshot\{0}_{1}.png'.format(now_time,func))
        return self.driver.get_screenshot_as_file(fpath)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    print(base_path)
    ti = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
    path = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0],'screenshot\{0}.jpg'.format(ti))

