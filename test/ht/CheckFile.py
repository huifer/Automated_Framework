#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : CheckFile.py
# @Author: huifer
# @Date  : 2018-3-8
import difflib
from unity.Excel_utils import *


class CheckFile(object):
    def __init__(self):
        self.hd = difflib.HtmlDiff()
        # self.dd = difflib.ndiff()
        self.checked = None
        self.new = None

    def judgment(self, old_file, new_file):
        """
        新旧文件diff比对
        :param old_file: file_path
        :param new_file: file_path
        :return:result.html
        """
        with open(old_file, 'r', encoding='utf8') as check:
            self.checked = check.readlines()

        with open(new_file, 'r', encoding='utf8') as news:
            self.new = news.readlines()

        with open("result.html", "w", encoding="utf8") as f:
            f.write(self.hd.make_file(self.checked, self.new))

    def test(self, old_file, new_file):
        """
        difflib.SequenceMatcher(None, f1, f2)
        get_opcodes() => (tag,i1,i2,j1,j2)

        值	        含义
        'replace'	a[i1:i2]应该被替换 b[j1:j2]。
        'delete'	a[i1:i2]应该删除。请注意， 在这种情况下。j1 == j2
        'insert'	b[j1:j2]应插入 a[i1:i1]。请注意，在这种情况下。i1 == i2
        'equal'	    a[i1:i2] == b[j1:j2] （子序列相等）。

        :param old_file:file_path
        :param new_file:file_path
        :return:
        """
        f1 = open(old_file, 'r', encoding="utf8")
        f2 = open(new_file, 'r', encoding="utf8")
        f1 = f1.readlines()
        f2 = f2.readlines()
        result = difflib.SequenceMatcher(None, f1, f2)
        s = result.get_opcodes()
        for tag, i1, i2, j1, j2 in s:
            if tag != 'equal':
                print('{:7}   old[{}:{}] --> new[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, f1[i1:i2],
                                                                                 f2[j1:j2]))
        s.insert(0, ('对比结果', '旧文件行号1', '旧文件行号2', '新文件行号1', '新文件行号2'))
        write_row_excel(
            path='wenti.xls',
            sheet_name="wenti",
            row_context=s,
            row=0)


if __name__ == '__main__':
    CheckFile().judgment(old_file='test.html', new_file='res.html')
    CheckFile().test(old_file='test.html', new_file='res.html')
