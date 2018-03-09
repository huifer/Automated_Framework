#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Excel_utils.py
# @Author: huifer
# @Date  : 2018-3-9
import xlrd
import xlwt


def read_excel(path, index=None, sheet_name=None, row=None, col=None):
    """
    index sheet_name 选一个
    :param path: str
    :param index: int
    :param sheet_name: str
    :param row: int
    :param col: int
    :return:dict()
    """
    workbook = xlrd.open_workbook(path)
    # 获取所有sheet
    get_sheet = workbook.sheet_names()
    if index is not None:
        # 索引获取方式
        try:
            sheet1 = workbook.sheet_by_index(index)
        except Exception as e:
            return e
        else:
            if row is not None:
                rows = sheet1.row_values(row)
            else:
                rows = []
            if col is not None:
                cols = sheet1.col_values(col)
            else:
                cols = []
            if row is not None and col is not None:
                val = sheet1.cell(row, col).value
            else:
                val = None
            return {
                'rows': rows,
                'cols': cols,
                'val': val}
    elif sheet_name:
        # 名称获取方式
        try:
            sheet1 = workbook.sheet_by_name(sheet_name)
        except Exception as e:
            return e
        else:
            if row is not None:
                rows = sheet1.row_values(row)
            else:
                rows = []
            if col is not None:
                cols = sheet1.col_values(col)
            else:
                cols = []
            if row is not None and col is not None:
                val = sheet1.cell(row, col).value
            else:
                val = None
            return {
                'rows': rows,
                'cols': cols,
                'val': val}

    """
    # 获取所有合并单元格内容
    merge = []
    for (rlow, rhigh, clow, chigh) in sheet2.merged_cells:
        merge.append([rlow, clow])
    for index in merge:
        print(sheet2.cell_value(index[0], index[1]))
    """


def excel_style(name, height, bold=False):
    """

    :param name:str 字体
    :param height:int 宽
    :param bold: bool 是否夹菜
    :return: xlwt.XFStyle()
    """
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.col = 0
    font.height = height
    style.font = font
    return style


def write_row_excel(path, sheet_name=None, row_context=None, row=None):
    """
    逐行写入
    :param path: str
    :param sheet_name: str
    :param row_context:[[],[]...]
    :param row:int
    :return: true or false
    """
    if sheet_name is not None and row_context is not None and row is not None:
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(sheet_name, cell_overwrite_ok=True)
        row = row
        for x in row_context:
            for i in range(len(x)):
                sheet1.write(row, i, x[i], excel_style("微软雅黑", 220, True))

            row += 1
        try:
            f.save(path)
        except Exception as e:
            return e
        else:
            return True
    else:
        return "参数错误"


def write_col_excel(path, sheet_name=None, col_context=None, col=None):
    """

    :param path: str
    :param sheet_name:str
    :param col_context:[[],[]...]
    :param col:int
    :return:True of false
    """
    if sheet_name is not None and col_context is not None and col is not None:
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(sheet_name, cell_overwrite_ok=True)
        col = col
        for x in col_context:
            for i in range(len(x)):
                sheet1.write(i, col, x[i], excel_style("微软雅黑", 220, True))
            col += 1
        try:
            f.save(path)
        except Exception as e:
            return e
        else:
            return True
    else:
        return "参数错误"


if __name__ == '__main__':
    test1 = read_excel(r"read_test.xlsx", index=0, row=2, col=1)
    print(test1)
    test2 = write_row_excel(
        path="123.xls",
        sheet_name="tt1",
        row_context=[['a', 'b', 'c'], ['aa', 'bb', 'cc'], ['aaa', 'bbb', 'ccc']],
        row=0,
    )
    print(test2)
    test3 = write_col_excel(
        path='456.xls',
        sheet_name="tt2",
        col_context=[['a', 1, 2, 3], ['b', 11, 22, 33], ['c', 111, 222, 333]],
        col=0
    )
    print(test3)
