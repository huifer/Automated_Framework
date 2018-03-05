#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Time    : 2018-03-05 20:39
# @Author  : huifer
# @File    : yzm_result.py
# @Software: PyCharm
import easygui as g

def yzm(pic_path):
    yzm = g.enterbox(msg="输入验证码",title="验证码",image=pic_path)

    return yzm