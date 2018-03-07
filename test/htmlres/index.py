#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Time    : 2018-03-06 20:02
# @Author  : huifer
# @File    : index.py
# @Software: PyCharm
import requests

header = {
    'Host': "www.zhihuihedao.cn",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # 'cookies': '143A4DB21A6D4E87EC33285956934DCF'
}
r = requests.get("http://www.zhihuihedao.cn",headers=header)

pass