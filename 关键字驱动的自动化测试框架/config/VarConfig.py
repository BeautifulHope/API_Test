#!/usr/bin/env python3
# -*- coding: utf-8 -*

basePath = "G:\\0.ReadMe"

exceptionPath = basePath + "\\123"
excelPath = basePath +"\\456"

#存储全局的变量
import os

# 项目根目录
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 截图目录
exceptionPath = projectPath +r'\exceptionpictures'

# 驱动存放路径， 需要自己根据自己电脑的驱动为止修改
iePath = ''
chromePath = ''
fireFox = ''

# excel文件存放路径
excelPath = projectPath + r'\test_data\126mailSend.xlsx'
# loh文件存放路径
logPath = projectPath + '\\log\\'
# 测试用例部分列对应的列号
testCase_testCaseName = 2
testCase_testStepName = 4
testCase_testIsExecute = 5
testCase_testRunEndTime = 6
testCase_testResult = 7

# 用例步骤对应的列号
testStep_testNum = 1
testStep_testStepDescribe = 2
testStep_keyWord = 3
testStep_elementBy = 4
testStep_elementLocator = 5
testStep_operateValue = 6
testStep_testRunTime = 7
testStep_testResult = 8
testStep_testErrorInfo = 9
testStep_testErrorPic = 10


if __name__=='__main__':

    print(projectPath)
    print(exceptionPath)
    print(excelPath)