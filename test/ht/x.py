#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : x.py
# @Author: huifer
# @Date  : 2018-3-8
import difflib

hd = difflib.HtmlDiff()
loads = ""
with open("res.html", 'r', encoding='utf8') as load:
    loads = load.readlines()

mens = ""
with open("test.html", 'r', encoding='utf8') as men:
    mens = men.readlines()

with open("htmlout.html", "w", encoding="utf8") as fo:
    fo.write(hd.make_file(loads, mens))


class CheckFile(object):
    def __init__(self):
        self.hd = difflib.HtmlDiff()
        self.checked = None
        self.mems = None

    pass
