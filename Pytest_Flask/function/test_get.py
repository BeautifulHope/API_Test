#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pytest
import requests


base_url = "http://127.0.0.1:5000/"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
}

def test_hello_world():
    url = base_url

    html = requests.get(url, headers=headers)

    print("status code:",html.status_code)

    assert '200' == str(html.status_code)


@pytest.mark.list_param
@pytest.mark.parametrize('data',[
    ['birr',123414],
    ['ben',233],
    ['benson',344],
                                 ])
def test_get_data(data):
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

@pytest.mark.dict_param
@pytest.mark.parametrize('name,password',[
    ('birr','123414'),
    ('ben','233'),
    ('benson','344'),
                                 ])
def test_get_data_2(name,password):
    # param is key-value
    url = base_url + 'parse'
    param = {
        'name':name,
        'password':password
    }
    
    html = requests.get(url,headers=headers,params=param)
    print(html.url)
    print(html.text)
    assert '200' == str(html.status_code)

#修改数据格式，使其在log中打印标签头

#测试数据
test_datas = [
    ['birr',123414],
    ['ben',233],
    ['benson',344]
]
#测试id                                 ]
test_ids = ['Test>>name:{},password:{}'.format(i[0],i[1]) for i in test_datas]

@pytest.mark.list_id_param
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



#########################POST的解析测试############################
test_datas = [
    ['birr',123414],
    ['ben',233],
    ['benson',344]
]
#测试id                                 ]
test_ids = ['Test>>name:{},password:{}'.format(i[0],i[1]) for i in test_datas]

@pytest.mark.post_test
@pytest.mark.parametrize('data', test_datas, ids=test_ids)
def test_get_id_data(data):
    # param is list
    url = base_url + 'parse'
    param = {
        'name': data[0],
        'password': data[1]
    }

    html = requests.post(url, headers=headers, json=param)
    print(html.url)
    print(html.text)
    assert '200' == str(html.status_code)
