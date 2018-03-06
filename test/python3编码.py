#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Time    : 2018-03-06 18:57
# @Author  : huifer
# @File    : python3编码.py
# @Software: PyCharm
import chardet

for i in ['abc123', '中国']:
    print(i, chardet.detect(i))
