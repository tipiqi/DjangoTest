#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/12/27 18:06
# software: PyCharm

'''

需每天下载更新数据
主要收集展示个股资金流，
展示数据：
代码、名称、最新价、今日涨跌幅、今日主力净流入（净额、净占比）、今日超大单净流入、今日大单净流入、今日中单、今日小单


'''


import requests
import json
import pymysql

cookies = {
    'st_si': '90333301217935',
    'st_sn': '23',
    'st_psi': '20201227180304925-113300300813-5517443214',
    'st_asi': 'delete',
    'waptgshowtime': '20201225',
    'qgqp_b_id': '41ace0e081c65173dbe7a427130119f9',
    'cowCookie': 'true',
    'intellpositionL': '1215.35px',
    'intellpositionT': '932.6px',
    'pgv_pvi': '6712911872',
    'pgv_si': 's5145225216',
    '_qddaz': 'QD.b5rgli.5goru2.kj6xg7dj',
    'st_pvi': '37914180003707',
    'st_sp': '2020-12-25%2009%3A08%3A56',
    'st_inirUrl': 'https%3A%2F%2Fwww.eastmoney.com%2F',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = (
    ('pn', '1'),
    ('pz', '50'),
    ('po', '1'),
    ('np', '1'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5'),
    ('fltt', '2'),
    ('invt', '2'),
    ('fid0', 'f4001'),
    ('fid', 'f62'),
    ('fs', 'm:0 t:6 f:!2,m:0 t:13 f:!2,m:0 t:80 f:!2,m:1 t:2 f:!2,m:1 t:23 f:!2,m:0 t:7 f:!2,m:1 t:3 f:!2'),
    ('stat', '1'),
    # ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f124'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124'),
    ('rt', '53635446'),
    # ('cb', 'jQuery18306748281684272909_1609063339692'),
    ('_', '1609063388525'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)
db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
cursor = db.cursor()
# print(json.loads(response.text).get('data').get('diff'))
for data in json.loads(response.text).get('data').get('diff'):
    print(data)
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    # sql = 'INSERT INTO{table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    sql = 'INSERT IGNORE INTO df_GGZJPM({keys}) VALUES ({values})'.format(keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print("successful")
            db.commit()
    except:
        print("failed")
        db.rollback()
db.close()