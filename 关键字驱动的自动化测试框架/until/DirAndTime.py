#!/usr/bin/env python3
# -*- coding: utf-8 -*
import os
from datetime import datetime,date
from config.VarConfig import *

class DirAndTime(object):
    @staticmethod
    def getCurrentDate():
        try:
            currentDate = date.today()
        except Exception as e:
            raise e
        else:
            return str(currentDate)

    @staticmethod
    def getCurrentTime():
        try:
            Time = datetime.now()
            currentTime = Time.strftime('%H_%M_%S')
        except Exception as e:
            raise e
        else:
            return currentTime

    @staticmethod
    def CreatePicturePath():
        try:
            picturePath = os.path.join(exceptionPath,DirAndTime.getCurrentDate())

            if not os.path.exists(picturePath):
                os.mkdir(picturePath)
        except Exception as e:
            raise e
        else:
            return picturePath

if __name__ == '__main__':
    print(DirAndTime.getCurrentDate())
    print(DirAndTime.getCurrentTime())
    print(DirAndTime.CreatePicturePath())