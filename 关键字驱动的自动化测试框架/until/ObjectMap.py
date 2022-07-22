#!/usr/bin/env python3
# -*- coding: utf-8 -*
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def getElement(driver, by, locator):
    '''
    查找单一元素
    :param driver:
    :param by:
    :param locator:
    :return: 元素对象
    '''
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return element

def getElements(driver, by, locator):
    '''
    查找一组元素
    :param driver:
    :param by:
    :param locator:
    :return: 元素对象
    '''
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return elements


if __name__ == '__main__':
    #birr_li
    #lly+.13……

    browser = webdriver.Chrome()

    browser.get('https://mail.126.com')
    time.sleep(5)
    browser.switch_to.frame(getElement(browser, 'xpath', "//div[@id='loginDiv']/iframe"))
    username = getElement(browser, 'xpath', "//input[@name='email']")
    username.send_keys('birr_li')
    # driver.switch_to.default_content()

    password = getElement(browser, 'xpath', "//input[@name='password']")
    password.send_keys('lly+.13191243969')

    browser.find_element_by_id("dologin").click()

    # browser.find_element_by_name("email").send_keys("selenium")

    # driver.quit()