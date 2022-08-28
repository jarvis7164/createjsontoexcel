# -*- coding: utf-8 -*-
# @Time    : 2022/8/28 0:10
# @Author  : Jarvis
# @Email   : jiamiao12@qq.com
# @File    : getdata.py
# @Software: PyCharm
import pymysql

class getdata:
    def getdata(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='test',
                             charset='utf8mb4',#mysql字符格式
                             cursorclass=pymysql.cursors.DictCursor)

        try:
            cursor = db.cursor();

            sql = """SELECT distinct test.order.order FROM test.order """

            cursor.execute(sql)

            results = cursor.fetchall()
            order_list = []
            for row in results:
                order = row['order']
                sql1 = """SELECT * FROM test.order where test.order.order = '{order}' """.format(order=order)
                cursor.execute(sql1)
                results_barcode = cursor.fetchall()
                barcode_list = []
                for row in results_barcode:
                    barcode = row['barcode']
                    barcode_list.append(barcode)
                a = (order, barcode_list)
                order_list.append(a)
            print(order_list)

        except pymysql.Error as err:
            print(err)

        finally:
            cursor.close()

a = getdata()
a.getdata()