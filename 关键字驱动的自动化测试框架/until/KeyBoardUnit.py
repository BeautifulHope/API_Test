#!/usr/bin/env python3
# -*- coding: utf-8 -*

import win32api
import win32con

class KeyBoard(object):
    '''
    模拟键盘
    '''
    vk_code = {
        'enter': 0x0D,
        'tab': 0x09,
        'ctrl': 0x11,
        'v': 0x56
    }

    @staticmethod
    def keyDown(keyname):
        try:
            win32api.keybd_event(KeyBoard.vk_code[keyname],0,0,0)
        except Exception as e:
            raise e

    @staticmethod
    def keyUp(keyname):
        try:
            win32api.keybd_event(KeyBoard.vk_code[keyname],0,win32con.KEYEVENTF_KEYUP,0)
        except Exception as e:
            raise e

    @staticmethod
    def onKey(key1,key2):
        try:
            KeyBoard.keyDown(key1)
            KeyBoard.keyDown(key2)
            KeyBoard.keyUp(key1)
            KeyBoard.keyUp(key2)
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver

    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")
    keyword = browser.find_element_by_id("kw")
    keyword.send_keys('fc2')
    simulation_key = KeyBoard()
    simulation_key.keyDown('enter')

