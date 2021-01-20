#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/12/2 19:48
# software: PyCharm
'''
主力排名数据，需每日更新插入
注意时间，这个接口没有时间数据，需要手动添加，需筛选时间数据
'''

import requests
import json
import pymysql

cookies = {
    'st_si': '82884447268291',
    'st_sn': '197',
    'st_psi': '20201202195249554-113300300814-4676961108',
    'st_asi': 'delete',
    'qgqp_b_id': '83b60a65c5c22972649fa86e1efda73a',
    'HAList': 'a-sz-000100-TCL%u79D1%u6280%2Ca-sz-300496-%u4E2D%u79D1%u521B%u8FBE%2Ca-sz-000400-%u8BB8%u7EE7%u7535%u6C14%2Ca-sz-002384-%u4E1C%u5C71%u7CBE%u5BC6%2Ca-sh-603786-%u79D1%u535A%u8FBE%2Ca-sh-601601-%u4E2D%u56FD%u592A%u4FDD%2Ca-sz-300733-%u897F%u83F1%u52A8%u529B',
    'em_hq_fls': 'js',
    'intellpositionL': '1215.35px',
    'intellpositionT': '2241.4px',
    'emshistory': '%5B%22%E6%B8%A4%E6%B5%B7%E7%A7%9F%E8%B5%81%22%2C%22%E8%8C%82%E5%8C%96%E5%AE%9E%E5%8D%8E%22%2C%22%E6%BA%A2%E5%A4%9A%E5%88%A9%22%2C%22%E7%9B%88%E5%BA%B7%E7%94%9F%E5%91%BD%22%2C%22%E5%85%89%E5%A4%A7%E9%93%B6%E8%A1%8C%22%2C%22%E9%87%91%E6%99%BA%E7%A7%91%E6%8A%80%22%2C%22%E9%82%AE%E5%82%A8%E9%93%B6%E8%A1%8C%22%5D',
    'cowCookie': 'true',
    'cowminicookie': 'true',
    'st_pvi': '69358380299554',
    'st_sp': '2020-11-26%2014%3A13%3A50',
    'st_inirUrl': 'https%3A%2F%2Fwww.eastmoney.com%2F',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://data.eastmoney.com/zjlx/list.html',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = (
    ('pn', '1'),
    ('pz', '5000'),
    ('po', '1'),
    ('np', '1'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5'),
    ('fltt', '2'),
    ('invt', '2'),
    ('fid', 'f184'),
    ('fid0', 'f4001'),
    ('fields', 'f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265'),
    ('fs', 'm:0 t:6 f:!2,m:0 t:13 f:!2,m:0 t:80 f:!2,m:1 t:2 f:!2,m:1 t:23 f:!2,m:0 t:7 f:!2,m:1 t:3 f:!2'),
    ('rt', '53563666'),
    # ('cb', 'jQuery18309522185650288084_1606909944323'),
    ('cb', ''),
    ('_', '1606909980656'),
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
    sql = 'INSERT IGNORE INTO ZL_ZJ_PM({keys}) VALUES ({values})'.format(keys=keys, values=values)
    # print(sql)
    # print(tuple(data.values()))
    try:
        if cursor.execute(sql, tuple(data.values())):
            print("successful")
            db.commit()
    except:
        print("failed")
        db.rollback()
db.close()