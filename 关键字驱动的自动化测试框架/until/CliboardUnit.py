#!/usr/bin/env python3
# -*- coding: utf-8 -*

import win32con
import win32clipboard as W

class ClipBoard(object):

    @staticmethod
    def getText():
        '''
        获取剪切板内容
        :return:
        '''

        try:
            #open clipboard
            W.OpenClipboard()

            #get value from clipboard
            value = W.GetClipboardData(win32con.CF_TEXT)

            #close clipboard
            W.CloseClipboard()
        except Exception as e:
            raise e
        else:
            return value

    @staticmethod
    def setText(value):
        try:
            # open clipboard
            W.OpenClipboard()
            #clear clipboard
            W.EmptyClipboard()

            # get value from clipboard
            value = W.SetClipboardData(win32con.CF_UNICODETEXT,value)

            # close clipboard
            W.CloseClipboard()
        except Exception as e:
            raise e
        else:
            return value

if __name__ == '__main__':
    from selenium import webdriver

    value = "python"

    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")
    keyword = browser.find_element_by_id("kw")

    useclipboard = ClipBoard()
    useclipboard.setText(value)

    kw_value = useclipboard.getText()

    print(kw_value)

    keyword.send_keys(kw_value.decode('utf-8'))

    # browser.find_element_by_id("su").click()