#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/29 10:26
# software: PyCharm

import tushare as ts
from sqlalchemy import create_engine  # 可将pandas的数据直接存到表中
import pymysql

'''
获取所有stock的基本信息

通过tushare获取所有code的基本信息，返回的数据为pandas
用sqlalchemy 下的create_engine 链接数据库，用to_sql 控制是否新建表，或者直接插入到当前表中，会自动创建表字段
'''

pro = ts.pro_api('66958a31231d29b45d24c72e086097e1f080402ebf218757a7c2c5f5')
# #查询当前所有正常上市交易的股票列表
#
datas = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date,market,is_hs')
# data = pro.stock_basic(exchange='', list_status='L')
print(datas)
# 因为mysqldb在python3中不支持，需要用pymysql替换
# engine = create_engine('mysql://root:Qi20200810@142.194.164.243/Stocks?charset=utf8')
engine = create_engine('mysql+pymysql://root:Qi20200810@42.194.164.243/Stocks?charset=utf8')
datas.to_sql('stock_basic', con=engine, if_exists='append', index=False)
