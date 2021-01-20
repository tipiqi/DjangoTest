#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/29 10:26
# software: PyCharm
import tushare as ts
from sqlalchemy import create_engine  # 无法使用
import time
import pymysql

import datetime
# print(datetime.datetime.now().strftime('%Y%m%d'))
'''
通过tushare 获取沪港通资金数据
1：先获取到当前设置时间段内的交易日，生成list返回
# 获取到pandas数据转换为list  用for循环取到每条数据的值
# print(df.values.tolist())
# for i in df.values.tolist():
#     print(i[0])
# print(df)
2：链接数据库，将查询到的交易日的数据，存到数据库表中
'''

# 1：先获取到当前设置时间段内的交易日，生成list返回
pro = ts.pro_api('66958a31231d29b45d24c72e086097e1f080402ebf218757a7c2c5f5')
# #查询当前所有正常上市交易的股票列表
# 截取交易时间段
# df = pro.trade_cal(exchange='SSE', is_open='1',
#                             start_date=(datetime.datetime.now() + datetime.timedelta(days=-1)).date().strftime('%Y%m%d'),
#                             end_date=(datetime.datetime.now() + datetime.timedelta(days=-1)).date().strftime('%Y%m%d'),
#                             fields='cal_date')

df = pro.trade_cal(exchange='SSE', is_open='1',
                            start_date='20210115',
                            end_date='20210118',
                            fields='cal_date')
# 2：链接数据库，将查询到的交易日的数据，存到数据库表中
engine = create_engine('mysql+pymysql://root:Qi20200810@42.194.164.243/Stocks?charset=utf8')
for i in df.values.tolist():
    print(i[0]+"正在查询")
    df2 = pro.hk_hold(trade_date=i[0])
    print(df2)
    df2.to_sql('stock_HGT_ZJ', con=engine,if_exists='append')
    # df2.to_sql('stock_HGT_ZJ', con=engine, if_exists='append', index=False)
    # 存储成功，因为数据原因，需等待80s
    time.sleep(30)
    print(i[0]+"插入成功")



