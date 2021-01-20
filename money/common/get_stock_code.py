#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/29 16:02
# software: PyCharm

import pymysql


def get_stock_basic_code():
    # 打开数据库连接
    db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    listcode = []
    # SQL 查询语句
    sql = "SELECT symbol FROM stock_basic "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        for item in results:
            for i in item:
                # print(i)
                listcode.append(i)

    except:
        print("Error: unable to fecth data")

    # try:
    #        if cursor.execute(sql, tuple(data.values())):
    #            print("successful")
    #            db.commit()
    #    except:
    #            print("failed")
    #            db.rollback()

    # print(listcode)
    # 关闭数据库连接
    cursor.close()
    db.close()
    return listcode