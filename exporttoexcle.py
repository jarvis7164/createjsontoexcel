# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 22:53
# @Author  : Jarvis
# @Email   : jiamiao12@qq.com
# @File    : exporttoexcle.py
# @Software: PyCharm
import openpyxl as op


# 导出数据到excel的类
class exporttoexcle:
    def exportoexcle(self,a, b,c):
        wb = op.Workbook()  # 创建工作簿对象
        ws = wb['Sheet']  # 创建sheet页
        ws.cell(row=1, column=1).value = a  # 第一行第一列赋值a
        ws.cell(row=1, column=2).value = b
        wb.save(c)  # 保存excle

a = exporttoexcle()
a.exportoexcle(1,2,'abc.xlsx')