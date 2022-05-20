#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pymongo,pytest,json

@pytest.fixture()
def get_data_from_db(tmpdir):

    datas = []

    database = pymongo.MongoClient(host='localhost', port=27017)  # 连接到mongodb
    workdata = database['贴吧']  # 连接或者创建一个数据库
    collection = workdata['2019test2']  # 连接或者创建一个集合(collection)201900311 20190202
    database.close()
    n=0
    coll = collection.find()
    for i in coll:
        try:
            datas.append([i['poster'],i['href']])
            n= n + 1
        except:
            pass
    # print(word)
    print('n:',n)
    return datas

###为其他测试提供一个json文件数据源，scope=module
@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    python_author_data ={
        'ned':{'city':'chengdu'},
        'birr': {'city': 'shenzhen'},
        'ben': {'city': 'oulouba'}
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data,f)

    return file

###
# ###增加命令行选项
# def pytest_addoption(parser):
#     parser.addoption("--mycollect",action="store_ture",
#                      help="equal --collect-only"
#                      )