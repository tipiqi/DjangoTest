#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/29 16:02
# software: PyCharm


import datetime
import tushare as ts
from common import get_stock_code_SZ
from sqlalchemy import create_engine

if __name__ == '__main__':

    # 设置tushare pro的token并获取连接
    ts.set_token('66958a31231d29b45d24c72e086097e1f080402ebf218757a7c2c5f5')
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。

    # 上次同步的时间为20190101——20201203
    start_dt = '20201207'
    # start_dt = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')
    print('开始时间:'+ start_dt)
    print('结束时间:'+ end_dt)

    # 建立数据库连接,剔除已入库的部分
    engine = create_engine('mysql+pymysql://root:Qi20200810@42.194.164.243/Stocks?charset=utf8')

    # 设定需要获取数据的股票池
    # stock_pool = ['603912.SH','300666.SZ','300618.SZ','002049.SZ','300672.SZ']
    stock_pool= get_stock_code_SZ.get_stock_basic_code()
    # print(stock_pool)
    print(len(stock_pool))
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
        print(i)
        # print(stock_pool[i])
        df.to_sql('stock_daily', con=engine, if_exists='append', index=False)
        print(stock_pool[i]+"插入完成")
    print('All Finished!')
