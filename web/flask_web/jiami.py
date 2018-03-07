#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : jiami.py
# @Author: huifer
# @Date  : 2018-3-7
from functools import wraps

from flask import request
from web.flask_web.restful_dy import *


def check_auth(username, password):
    """
    # TODO:用户认证 username password
    传入用户名以及密码
    :param username:用户名
    :param password:密码
    :return:
    """
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False


def authenticate():
    """
    验证信息头
    :return: 验证信息头部
    """
    message = {'message': "Authenticate."}
    response = jsonify(message)
    response.status_code = status_response(R401)
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return response


def requires_auth(f):
    """

    :param f:
    :return:
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
