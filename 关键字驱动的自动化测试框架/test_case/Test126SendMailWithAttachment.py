#!/usr/bin/env python3
# -*- coding: utf-8 -*

from until.ParseExcel import ParseExcel
from config.VarConfig import *
from action.PageAction import *
import traceback
from until.log import Logger
import logging

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
p = ParseExcel()
sheetName = p.wb.sheetnames #get excel all sheet name

def Test123MailSendWithAtt():
    try:
        testCasePassNumber = 0

        requiredCase = 0

        isExecuteColumnValues = p.getColumnValue(sheetName[0],testCase_testIsExecute)

        for index,value in enumerate(isExecuteColumnValues):
            #获取对应步骤的sheet名称
            stepSheetName = p.getCellOfValue(sheetName[0],index + 2,testCase_testStepName)

            print("now stepsheetname:",stepSheetName)
            if value.strip().lower() == 'y':
                requiredCase += 1
                testCasePassNumber = 0
                print("开始测试用例：{}".format(stepSheetName))
                log.logger.info("开始测试用例：{}".format(stepSheetName))
                #如果用例被标记为执行y，切换到对应的sheet页
                # 获取对应的sheet表中的总步骤数，关键字，定位方式，定位表达式，操作值
                #步骤总数
                values = p.getColumnValue(stepSheetName,testStep_testNum)#第一列的数据

                stepNum = len(values)
                print(stepNum)
                for step in range(2,stepNum+2):
                    rawValue = p.getRowValue(stepSheetName,step)
                    #step name
                    stepName = rawValue[testStep_testStepDescribe - 2]
                    #keyword
                    keyWord = rawValue[testStep_keyWord - 2]
                    #local method
                    by = rawValue[testStep_elementBy - 2]
                    #local expression
                    locator = rawValue[testStep_elementLocator - 2]
                    #operate value
                    operateValue = rawValue[testStep_operateValue - 2]

                    print("get value:{},{},{},{},{}".format(keyWord,by,locator,operateValue,type(operateValue)))

                    if keyWord and by and locator and operateValue:
                        func = keyWord + '(' + '"' + by + '"' + ',' + '"' + locator + '"' + ',' + '"' + str(operateValue) + '"' + ')'
                    elif keyWord and by and locator and operateValue is None:
                        func = keyWord + '(' + '"' + by + '"' + ',' + '"' + locator + '"' + ')'

                    elif keyWord and operateValue and type(operateValue) == str and by is None and locator is None:
                        func = keyWord + '(' + '"' + operateValue + '"' + ')'

                    elif keyWord and operateValue and type(operateValue) == int and by is None and locator is None:
                        func = keyWord + '(' + str(operateValue) + ')'

                    else:
                        func = keyWord + '(' + ')'

                    print(">>>>>>>>func:", func)

                    #########测试执行############
                    try:
                        # 执行测试步骤
                        eval(func)
                    except Exception:
                        # 截图
                        picPath = saveScreenShot()
                        # 写回测试结果
                        errorInfo = traceback.format_exc()
                        p.writeTestResult(stepSheetName, step, 'Failed', errorInfo, picPath)
                        print('步骤"{}"执行失败'.format(stepName))
                        log.logger.info('步骤"{}"执行失败'.format(stepName))
                        raise
                    else:
                        print('步骤"{}"执行通过'.format(stepName))
                        log.logger.info('步骤"{}"执行通过'.format(stepName))
                        # 标记测试步骤为pass
                        p.writeTestResult(stepSheetName, step, 'Pass')
                        testCasePassNumber += 1
                    # print('通过用例步数数:',testStepPassNum)
                if testCasePassNumber == stepNum:
                    # 标记测试用例sheet页的执行结果为pass
                    p.writeCell(sheetName[0], index + 2, testCase_testResult, 'Pass')
                    testCasePassNumber += 1
                else:
                    p.writeCell(sheetName[0], index + 2, testCase_testResult, 'Failed')
                print('共{}条用例，{}条需要被执行，本次执行通过{}条'.format(len(isExecuteColumnValues), requiredCase, testCasePassNumber))
                log.logger.info(
                    '共{}条用例，{}条需要被执行，本次执行通过{}条'.format(len(isExecuteColumnValues), requiredCase, testCasePassNumber))
    except Exception as e:
        print(traceback.format_exc(e))
        log.logger.info(traceback.format_exc(e))

if __name__ == '__main__':
    Test123MailSendWithAtt()

