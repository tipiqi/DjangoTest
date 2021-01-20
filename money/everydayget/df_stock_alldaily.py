#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2021/1/14 17:43
# software: PyCharm


import requests
import json
import pymysql
from itertools import chain

def get_stock_code_frommysql_stock_basic():
    # 创建从数据库表中获取有效代码
    # 创建数据库连接
    db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
    cursor = db.cursor()
    # sql = 'insert IGNORE INTO HSGTHDSTA({keys}) VALUES ({values})'.format(keys=keys, values=values)
    sql = 'SELECT symbol FROM stock_basic GROUP BY symbol'
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

def fix_stock_code():
    # 根据不同的接口需求，对stock进行调整优化
    resultlist = get_stock_code_frommysql_stock_basic()
    resultlist_fix = []
    # print(resultlist_fix)
    # 0和3开头的前缀带0.   6开头的前缀待1.
    for scode in resultlist:
        # print(scode[0])   # 需要转换类型
        if int(scode[0]) == 0:
            scode = '0.'+str(scode)
            resultlist_fix.append(scode)
        elif int(scode[0]) == 3:
            scode = '0.' + str(scode)
            resultlist_fix.append(scode)
        elif int(scode[0]) == 6:
            scode = '1.' + str(scode)
            resultlist_fix.append(scode)
    print(resultlist_fix)
    return resultlist_fix
    # ('filter', '(SCODE=\'' + str(stock_code_num) + '\')'),


def df_stock_alldaily(ts_code):
# 从东财根据ts_code，爬每个数据的当日所有数据
    cookies = {
        'st_si': '77193428594074',
        'st_sn': '19',
        'st_psi': '20210114173319535-113200301324-9882013413',
        'st_asi': 'delete',
        'waptgshowtime': '2021114',
        'qgqp_b_id': '8d3c8ee415d91e2ea6d80d9c0bf3970e',
        'HAList': 'f-0-000001-%u4E0A%u8BC1%u6307%u6570%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC',
        'em_hq_fls': 'js',
        'em-quote-version': 'topspeed',
        'cowCookie': 'true',
        'intellpositionL': '1010.13px',
        'intellpositionT': '1075px',
        'st_pvi': '77348267980400',
        'st_sp': '2021-01-14%2016%3A26%3A19',
        'st_inirUrl': 'https%3A%2F%2Fwww.eastmoney.com%2F',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'http://quote.eastmoney.com/kcb/688656.html',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
        ('fltt', '2'),
        ('invt', '2'),
        ('volt', '2'),
        ('fields', 'f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f198,f259,f260,f261,f171,f277,f278,f279,f288,f292,f182'),
        # ('secid', '1.300331'),
        # ('secid', '1.688139'),  # 0和3开头的前缀带0.   6开头的前缀待1.
        ('secid', ts_code),  # 0和3开头的前缀带0.   6开头的前缀待1.

        # ('cb', 'jQuery11240604972193327871_1610616878666'),
        ('_', '1610616878668'),
    )

    response = requests.get('http://push2.eastmoney.com/api/qt/stock/get', headers=headers, params=params, cookies=cookies)
    resp_dict = json.loads(response.text)
    datas = resp_dict.get('data')
    print(datas)

    # 创建数据库连接
    db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
    cursor = db.cursor()

    # 将数据批量插入数据库中

    # 将每条数据都插入到数据库中
    # table = 'HSGTHDSTA'
    # bianma =  data.get("SNAME")
    # print(bianma)
    keys = ','.join(datas.keys())
    values = ','.join(['%s'] * len(datas))
    # print(keys)
    # print(values)
    # sql = 'INSERT INTO{table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    sql = 'INSERT IGNORE INTO df_alldaily({keys}) VALUES ({values})'.format(keys=keys, values=values)
    # print(sql)
    # print(tuple(data.values()))
    try:
        if cursor.execute(sql, tuple(datas.values())):
            print("successful")
            db.commit()
    except:
        print("failed")
        db.rollback()
    db.close()

def insert_mysql():
    for ts_code in fix_stock_code():
        print(ts_code)
        df_stock_alldaily(ts_code)

# def update_mysql_UNIXTIME():
#     # 创建数据库连接
#     db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
#     cursor = db.cursor()
#     sql = 'update df_alldaily set f86 = FROM_UNIXTIME(f86,'%Y%m%d')'


if __name__ == '__main__':
    # get_stock_code_frommysql_stock_basic()
    # print(get_stock_code_frommysql_stock_basic())
    insert_mysql()