#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pymongo

def get_data_from_db():

    word = []

    database = pymongo.MongoClient(host='localhost', port=27017)  # 连接到mongodb
    workdata = database['贴吧']  # 连接或者创建一个数据库
    collection = workdata['2019test2']  # 连接或者创建一个集合(collection)201900311 20190202
    database.close()
    n=0
    coll = collection.find()
    for i in coll:
        try:
            word.append([i['poster'],i['href']])
            n= n + 1
        except:
            pass
    # print(word)
    print('n:',n)
    return word

if __name__=='__main__':
    datas = get_data_from_db()
    print(type(datas))
    # [print(i) for i in datas]