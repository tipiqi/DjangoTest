#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/27 13:52
# software: PyCharm

import requests
import json
import pymysql
import datetime
# print(datetime.datetime.now().strftime('%Y%m%d'))

'''
10个左右工作日更新一次，已用tushare_HGT_ZJ.py 代替
从dongfang 获取数据，存入到mysql 中的HSGTHDSTA 表
'''

def insert_mysql_HSGTHDSTA(stock_code_num):

    cookies = {
        'st_si': '82884447268291',
        'st_sn': '44',
        'st_psi': '20201127135128619-113300302016-7798844501',
        'st_asi': 'delete',
        'waptgshowtime': '20201126',
        'qgqp_b_id': '83b60a65c5c22972649fa86e1efda73a',
        'HAList': 'a-sh-603786-%u79D1%u535A%u8FBE%2Ca-sh-601601-%u4E2D%u56FD%u592A%u4FDD%2Ca-sz-300733-%u897F%u83F1%u52A8%u529B',
        'em_hq_fls': 'js',
        'cowCookie': 'true',
        'intellpositionL': '1215.35px',
        'intellpositionT': '704.6px',
        'emshistory': '%5B%22%E6%B8%A4%E6%B5%B7%E7%A7%9F%E8%B5%81%22%2C%22%E8%8C%82%E5%8C%96%E5%AE%9E%E5%8D%8E%22%2C%22%E6%BA%A2%E5%A4%9A%E5%88%A9%22%2C%22%E7%9B%88%E5%BA%B7%E7%94%9F%E5%91%BD%22%2C%22%E5%85%89%E5%A4%A7%E9%93%B6%E8%A1%8C%22%2C%22%E9%87%91%E6%99%BA%E7%A7%91%E6%8A%80%22%2C%22%E9%82%AE%E5%82%A8%E9%93%B6%E8%A1%8C%22%5D',
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
        'Referer': 'http://data.eastmoney.com/hsgtcg/StockHdStatistics.aspx?stock=603786',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('type', 'HSGTHDSTA'),
        ('token', '70f12f2f4f091e459a279469fe49eca5'),
        # ('filter', '(SCODE=\'603786\')'),
        # ('filter', '(SCODE=\'000400\')'),
        ('filter', '(SCODE=\''+str(stock_code_num)+'\')'),
        ('st', 'HDDATE'),
        ('sr', '-1'),
        ('p', '1'),
        ('ps', '150'),
        # ('js', '{"data":(x)}'),
        ('js', '(x)'),
        # ('js', 'var qxHGFkXi={"pages":(tp),"data":(x)}'),
        ('rt', '53548543'),
    )

    rs = requests.get('http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get', headers=headers, params=params,
                      cookies=cookies)
    # print(rs)
    print(rs.text)
    # for xx in eval(rs.text):
    #     print(xx)


    # 创建数据库连接
    db = pymysql.connect(host='42.194.164.243', user='root', password='Qi20200810', port=3306, db='Stocks')
    cursor = db.cursor()


# #  批量插入数据，初始的时候拉所有的数据
#     for data in eval(rs.text):
#         # 将每条数据都插入到数据库中
#         print(data)
#         # table = 'HSGTHDSTA'
#         # bianma =  data.get("SNAME")
#         # print(bianma)
#         keys = ','.join(data.keys())
#         values = ','.join(['%s']*len(data))
#         # sql = 'INSERT INTO{table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
#         sql = 'INSERT IGNORE INTO HSGTHDSTA({keys}) VALUES ({values})'.format( keys=keys, values=values)
#         try:
#             if cursor.execute(sql, tuple(data.values())):
#                 print("successful")
#                 db.commit()
#         except:
#                 print("failed")
#                 db.rollback()

#
    for data in eval(rs.text):
        # 将每条数据都插入到数据库中
        print(data)
        # table = 'HSGTHDSTA'
        # bianma =  data.get("SNAME")
        # print(bianma)
        keys = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        print(keys)
        print(values)
        # sql = 'INSERT INTO{table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
        sql = 'INSERT IGNORE INTO HSGTHDSTA({keys}) VALUES ({values})'.format(keys=keys, values=values)
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