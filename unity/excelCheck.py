#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : excelCheck.py
# @Author: huifer
# @Date  : 2018-3-23
import os

import xlrd

url = r"\\192.168.1.46\2018年河道地形测量\上交资料\excel\总表格\1.xlsx"  # excel 表格文件位置


def excelwt(url):
    workbook = xlrd.open_workbook(url)
    # 获取所有sheet
    get_sheet = workbook.sheet_names()

    zplist = []

    for x in get_sheet:
        # print(x)
        sheet1 = workbook.sheet_by_name(x)
        diyihang = sheet1.row(0)

        for i, zz in enumerate(diyihang):
            # print(i,zz)
            if "照片" in str(zz):
                ll = sheet1.col(i)
                # print(ll)
                zplist.append(ll)  # 获取所有照片

    # print(zplist)

    setzp = set()
    for x in zplist:
        # print(x)
        for y in x:
            xa = y.value
            # print(xa)
            setzp.add(xa)  # 去重复

    for x in setzp:  # 判断是否纯在
        if os.path.exists(str(x)):
            # print("OK")
            pass
        else:
            print(x)
if __name__ == '__main__':
    excelwt(url)
