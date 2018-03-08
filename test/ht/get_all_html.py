#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_all_html.py
# @Author: huifer
# @Date  : 2018-3-8
import requests
import re
from lxml import etree

url = "http://localhost:8060/404"

r = requests.get(url=url)

html = etree.HTML(r.text)

CSS = html.xpath("/html/head/link/@href")
IMG = html.xpath("//img/@src")

# ra = re.findall("(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",r.text)

# with open('test.html','wb') as f:
#     f.write(r.content)


pass