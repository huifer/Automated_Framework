#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app.py
# @Author: huifer
# @Date  : 2018-3-6
from flask import Flask, request

from web.flask_web.restful_dy import *
from web.flask_web.jiami import *


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# 获取所有
@app.route("/api/v1.0/getall", methods=['GET'])
def get_all():
    return full_response(R200, tasks)


# 获取指定Id
@app.route("/api/v1.0/getid/<int:id>", methods=['GET'])
def get_id(id):
    result = [data for data in tasks if data['id'] == id]
    if len(result) == 0:
        return status_response(R404)
    return full_response(R200, result[0])


# 增加一条数据
@app.route('/api/v1.0/create', methods=['POST'])
def add_one():
    request_data = request.json
    if 'title' not in request_data.keys():
        return status_response(R404)
    else:

        title = request_data['title']
        tasks.append({'title': title})
        return full_response(R201, tasks)


# 删除一条数据
@app.route('/api/v1.0/delone/<int:id>', methods=['DELETE'])
def del_one(id):
    print(tasks)
    result = [data for data in tasks if data['id'] == id]
    if len(result) == 0:
        return status_response(R404)
    tasks.remove(result[0])
    print("shanchuhou", tasks)
    return status_response(R204)


@app.route("/api/v1.0/sec")
@requires_auth
def authenticate():
    return status_response(R200)

@app.route("/")
def index():
    return "hello"



if __name__ == '__main__':
    app.run(
        debug=True,
        port=8060
    )
