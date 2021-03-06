#!/usr/bin/env python3
# -*- coding: utf-8 -*

from until.ObjectMap import *
from until.CliboardUnit import ClipBoard
from until.KeyBoardUnit import KeyBoard
from until.WaitUnit import WaitUnit
from until.DirAndTime import *
from selenium import webdriver

driver = None
waitUtil = None
# 打开浏览器
def open_browser(browser):#open_browser
    global driver, waitUtil
    try:
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            # driver = webdriver.Firefox(executable_path=fireFox)
            driver = webdriver.Firefox()
    except Exception as e:
        raise e
    else:
        waitUtil = WaitUnit(driver) # driver 创建之后， 创建等待类实例对象
# 浏览器窗口最大化
def maximize_browser():
    try:
        driver.maximize_window()
    except Exception as e:
        raise e
# 加载网址
def load_url(url):
    try:
        driver.get(url)
    except Exception as e:
        raise e
# 强制等待
def sleep(sleepSeconds):
    try:
        import time
        time.sleep(sleepSeconds)
    except Exception as e:
        raise e
# 清除输入框的内容
def clear(by, locator):
    try:
        getElement(driver, by, locator).clear()
    except Exception as e:
        raise e
# 输入框中输入内容
def input_value(by, locator, value):
    try:
        element = getElement(driver, by, locator)
        # element.click()
        element.send_keys(value)
    except Exception as e:
        raise e
# 点击操作
def click_btn(by, locator):
    try:
        getElement(driver, by, locator).click()
    except Exception as e:
        raise e
# 断言页面的title
def assert_title(titleStr):
    try:
        assert titleStr in driver.title, "%s not found in title!" % titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e
# 断言目标字符串是否包含在页面源码中
def assert_string_in_page_source(assertString):
    try:
        assert assertString in driver.page_source, "%s not found in page source!" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e
# 获取当前页面的title
def getTitle():
    try:
        return driver.title
    except Exception as e:
        raise e
# 获取页面源码
def getPageSource():
    try:
        return driver.page_source
    except Exception as e:
        raise e
# 切换到frame里面
def switchToFrame(by, locator):
    try:
        driver.switch_to.frame(getElement(driver, by, locator))
    except Exception as e:
        raise e
# 切换到frame里面
def wait_frame_to_be_available_and_switch_to_it(by, locator):
    try:
        driver.switch_to.frame(getElement(driver, by, locator))
    except Exception as e:
        raise e
# 跳到默认的frame
def switchToDefault():
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e
# 模拟ctrl+v键
def ctrlV(value):
    try:
        ClipBoard.setText(value)
        sleep(2)
        KeyBoard.onKey('ctrl', 'v')
    except Exception as e:
        raise e
# 模拟tab键
def tabKey():
    try:
        KeyBoard.onKey('tab')
    except Exception as e:
        raise e
# 模拟enter键
def enterKey():
    try:
        KeyBoard.onKey('enter')
    except Exception as e:
        raise e
# 屏幕截图
def saveScreenShot():
    pictureName = DirAndTime.CreatePicturePath() +'\\'+DirAndTime.getCurrentTime() + '.png'
    try:
        driver.get_screenshot_as_file(pictureName)
    except Exception as e:
        raise e
    else:
        return pictureName

def assert_error_info(by, locator, value):
    try:
        element = getElement(driver, by, locator)
        print(str(element.text))
        if value == element.text:
            print(99999999999999)
        else:
            print(000000000000000)
    except Exception as e:
        raise e


def waitPresenceOfElementLocated(by, locator):
    '''
    显示等待页面元素出现在DOM中，单并不一定可见
    :param by:
    :param locator:
    :return:
    '''
    waitUtil.presenceOfElementLocated(by, locator)
def waitFrameToBeAvailableAndSwitchToIt(by, locator):
    '''
    检查frame是否存在，存在就切换到frame中
    :param by:
    :param locator:
    :return:
    '''
    waitUtil.frameToBeAvailableAndSwtichToIt(by, locator)

def waitVisibiltyOfElementLocated(by, locator):
    '''
    显示等待页面元素出现在DOM中，并且可见
    :param by:
    :param locator:
    :return:
    '''
    waitUtil.visibiltyOfElementLocated(by, locator)

# 关闭浏览器
def quit_browser():
    try:
        driver.quit()
    except Exception as e:
        raise e
if __name__=='__main__':
    open_browser('chrome')
    load_url('http://www.baidu.com')
    # inputValue('id', 'kw','python')
    # clear('id', 'kw')
    # inputValue('id', 'kw', 'python')
    # clickBtn('id', 'su')
    # sleep(3)
    # title = getTitle()
    # print(title)
    # assertTitle('python')
    # assert_string_in_page_source('python')
    ctrlV('python')