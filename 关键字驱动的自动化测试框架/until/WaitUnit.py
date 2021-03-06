#!/usr/bin/env python3
# -*- coding: utf-8 -*

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUnit(object):
    def __init__(self,driver):
        self.byDic = {
            'id':By.ID,
            'name':By.NAME,
            'class_name':By.CLASS_NAME,
            'xpath':By.XPATH,
            'link_text':By.LINK_TEXT
        }

        self.driver = driver
        self.wait = WebDriverWait(self.driver,50)

    def presenceOfElementLocated(self,by,locator):
        '''
        显示等待某个元素出现在dom中，不一定可见，存在返回元素对象
        :param by:
        :param locator:
        :return:
        '''
        try:
            if by.lower() in self.byDic:
                self.wait.until(EC.presence_of_element_located((self.byDic[by.lower()],locator)))
            else:
                raise TypeError("未找到定位方式，请确保定位方式正确！")
        except Exception as e:
            raise e

    def frameToBeAvaliableAndSwitchToIt(self,by,locator):
        '''
        检查frame是否存在，存在就切换到frame中
        :param by:
        :param locator:
        :return:
        '''
        try:
            if by.lower() in self.byDic:
                self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.byDic[by.lower()],locator)))
            else:
                raise TypeError("未找到定位方式，请确保定位方式正确！")
        except Exception as e:
            raise e

    def visibiltyOfElementLocater(self,by,locator):
        '''
        显示等待页面元素出现在dom中， 并且可见， 存在则返回该元素对象
        :param by:
        :param locator:
        :return:
        '''
        try:
            if by.lower() in self.byDic:
                self.wait.until(EC.visibility_of_element_located((self.byDic[by.lower()],locator)))
            else:
                raise TypeError("未找到定位方式，请确保定位方式正确！")
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    from until.ObjectMap import *

    browser = webdriver.Chrome()
    browser.get('https://mail.126.com')
    # time.sleep(5)

    wait = WaitUnit(browser)
    wait.frameToBeAvaliableAndSwitchToIt('xpath',"//div[@id='loginDiv']/iframe")
    wait.visibiltyOfElementLocater('xpath',"//input[@name='email']")
    username = getElement(browser,'xpath',"//input[@name='email']")
    username.send_keys("2333333")

    # browser.quit()