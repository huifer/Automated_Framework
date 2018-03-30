#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dbfCheck.py
# @Author: huifer
# @Date  : 2018-3-30
import os

from dbfread import DBF


def biaogekong(path):
    """
    检查dbf 空的文件
    :param path: file_path
    :return:
    """
    fil = set()
    for root, dirs, files in os.walk(path):
        for x in files:
            aa = x.split(".")
            fil.add(os.path.join(path, aa[0]) + ".dbf")

    wt = set()
    for tt in fil:
        table = DBF(tt)
        for record in table:
            a = dict(record)
            for k, v in a.items():
                if v == "":
                    wt.add(tt)

    print(wt.__len__()  ,"以下内容 shp中有空的内容")
    for i in wt:
        print(i)


def zpdbf(path):
    """
    检查dbf 中照片是正常连接的
    :param path:
    :return:
    """
    fil = set()
    for root, dirs, files in os.walk(path):
        for x in files:
            aa = x.split(".")
            fil.add(os.path.join(path, aa[0]) + ".dbf")

    wt = set()
    for tt in fil:
        table = DBF(tt)
        for record in table:
            a = dict(record)
            for k, v in a.items():
                if "\\" in str(v):
                    if os.path.exists(str(v)):
                        pass
                    else:
                        wt.add(v)

    print(wt.__len__()  ,"以下内容 shp中图片有问题")
    for x in wt:
        print(x)

if __name__ == '__main__':
    path = r"\\192.168.1.46\2018年河道地形测量\上交资料\总图"
    biaogekong(path=path)
    zpdbf(path=path)
