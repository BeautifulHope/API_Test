#!/usr/bin/env python3
# -*- coding: utf-8 -*

import time

def count_running_time(mode):
    def decorate(func):
        def wrapper(*args,**kwargs):
            if mode == "time":
                start = time.time()
                func(*args)
                end = time.time()
                print("use time: ",end-start)
        return wrapper
    return decorate

if __name__ == '__main__':
    pass