#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/12/2 6:37
# software: PyCharm
import pymysql
from itertools import chain
'''
从数据库获取到HSGTHDSTA表中的scode，目的是排除掉没有沪港通资金占比的scode，加快速度
'''


def select_HGTZJ_code():
    # 创建从数据库表中获取有效代码
    # 创建数据库连接
    db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
    cursor = db.cursor()
    # sql = 'insert IGNORE INTO HSGTHDSTA({keys}) VALUES ({values})'.format(keys=keys, values=values)
    sql = 'SELECT SCODE FROM HSGTHDSTA GROUP BY SCODE'
    try:
        cursor.execute(sql)
        elems = cursor.fetchall()
        # print(cursor.fetchall())
        # 将元组数据转为列表
        resultlist = list(chain.from_iterable(elems))
        # print(resultlist.__len__())
    except:
        print("failed")
    return resultlist


if __name__ == '__main__':
    select_HGTZJ_code()
    print(select_HGTZJ_code())
