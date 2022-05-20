#!/usr/bin/env python3
# -*- coding: utf-8 -*

from flask import Flask, render_template, jsonify, request, redirect, url_for
import time


app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
    agent = request.headers.get('User-Agent', None)  # 获取浏览器的ua
    return 'Hello, World!'

@app.route('/date', methods=["POST"])
def overview_app():
    """
    折线图数据发送
    """
    if request.method == "POST":
        return jsonify(data=[[320, 332, 301, 334, 390, 330, 320,18], [19,520, 132, 101, 134, 90, 230, 210]])

# http://127.0.0.1:5000/searcg?name=birr&age=213213
@app.route("/parse_get",methods=["GET","POST"])
def parse_geturl():
    name = request.args.get("name")
    age = request.args.get("age")
    timestamp = str(int(time.time()))

    response_data = {
        "name": name,
        "age" : age,
        "timestamp" : timestamp
    }
    return jsonify(response_data)

def request_parse(request_data):
    '''解析请求数据并以json形式返回'''

    name = ''
    password =  ''

    if request_data.method == 'POST':
        data = request_data.json
        print("josn data:",data,'  ',type(data))

        if type(data) == dict:
            name = data['name']
            password = data['password']
        else:
            name = request_data.form['name']
            password = request_data.form['password']
            print("data data:", name,'  ',password)

    elif request_data.method == 'GET':
        data = request_data.args
        name = data.get("name")
        password = data.get("password")

    return name,password

@app.route('/parse', methods = ["GET","POST"]) # GET 和 POST 都可以
def get_data():
    name,password = request_parse(request)
    # 假设有如下 URL
    # http://10.8.54.48:5000/index?name=john&password=20
    if name:
        # name = data.get("name")
        # password = data.get("password")

        response_data = {
            "name": name,
            "password" : password,
            "timestamp" : str(int(time.time())),
            "method": request.method
        }
        if name == "birr" :
            if password == "123414":
                response_data["login_status"] = "SUCCESS"
            else:
                response_data["login_status"] = "pasword Error：" + str(password)
        else:
            response_data["login_status"] = "name Error"
    else:
        response_data = {
            "login_status":"parse data is null!"
        }

    return jsonify(response_data)

@app.route("/head/")
def heade():
    headers = request.headers
    response = {}
    for k,v in headers.items():
        response[k] = v
    return jsonify(response)
    #因为协议头 headsers 是一个字典 所以遍历字典以展示出来

@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    method = request.method

    data= {
        'ip':ip,
        'url': url,
        'method':method,
        'headers':request.headers,
    }
    print(data)


if __name__ == "__main__":
    # app.run(host='0.0.0.0',port=5001)
    app.run()