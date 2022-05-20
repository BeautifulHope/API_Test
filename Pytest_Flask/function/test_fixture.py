#!/usr/bin/env python3
# -*- coding: utf-8 -*
import time

import pymongo
import pytest
import requests

from temp_test import get_data_from_db

base_url = "http://127.0.0.1:5000/"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

###fixture
@pytest.fixture()
def some_data():
    return [42,32]

@pytest.mark.test_fixture
def test_some_data(some_data):
    assert [42,32] == some_data


######################################################################################从conftest.py获取fixture有点问题，
# 貌似新版的pytest不支持了
# 
# #从conftest中获取data
# 
# #测试数据
# test_datas = conftest.get_data_from_db()
# #测试id                                 ]
# test_ids = ['Test>>name:{},password:{}'.format(i[0],i[1]) for i in test_datas]
# 
# @pytest.mark.test_conftest_fixture
# @pytest.mark.parametrize('data',conftest.get_data_from_db,ids=test_ids)
# def test_get_id_data(data):
#     # param is list
#     url = base_url + 'parse'
#     param = {
#         'name': data[0],
#         'password': data[1]
#     }
# 
#     html = requests.get(url, headers=headers, params=param)
#     print(html.url)
#     print(html.text)
#     assert '200' == str(html.status_code)
#############################################################################################
#

############从数据库get数据############
test_datas = get_data_from_db()

print(type(test_datas))

test_ids = ['Test>>name:{},password:{}'.format(i[0],i[1]) for i in test_datas]

print('2222: ',type(test_datas))

@pytest.fixture(autouse = True)
def check_time():
    start_time = time.time()
    yield 
    end_time = time.time()
    print("test time:",end_time - start_time)

@pytest.mark.fixture_test
@pytest.mark.parametrize('data',test_datas,ids=test_ids)
def test_get_id_data(data):
    # param is list
    url = base_url + 'parse'
    param = {
        'name': data[0],
        'password': data[1]
    }

    html = requests.get(url, headers=headers, params=param)
    print(html.url)
    print(html.text)
    assert '200' == str(html.status_code)

