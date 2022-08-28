# -*- coding: utf-8 -*-
# @Time    : 2022/8/27 23:42
# @Author  : Jarvis
# @Email   : jiamiao12@qq.com
# @File    : tojsondata.py
# @Software: PyCharm
import json

class tojsondata:
    def tojsondata(self, list_a):
        list = []
        for a in list_a:
            dict1 = {"barcode:":str(a)}
            # print(dict1)
            list.append(dict1)
            json_list = json.dumps(list)
            print(json_list)

a = tojsondata()
a.tojsondata([1,2,3,4])




