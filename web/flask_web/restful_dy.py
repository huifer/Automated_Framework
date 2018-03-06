#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful_dy.py
# @Author: huifer
# @Date  : 2018-3-6
# http://www.pythondoc.com/flask-restful/first.html
from flask import jsonify

R200 = {'code': 200, 'message': 'OK'}
R201 = {'code': 201, 'message': 'CREATED '}
R204 = {'code': 204, 'message': 'NO CONTENT'}
R400 = {'code': 400, 'message': 'INVALID REQUEST'}
R403 = {'code': 403, 'message': 'Forbidden '}
R404 = {'code': 404, 'message': 'NOT FOUND'}


def full_response(status, data):
    return jsonify({'status': status, 'data': data})


def status_response(status):
    return jsonify({'status': status})
