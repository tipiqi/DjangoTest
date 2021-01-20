
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/29 16:30
# software: PyCharm
from dongfang import df_HGT_ZJ
from common import get_HGTZJ_code_frommysql
import datetime
import time

# # 从tushare获取股票的所有代码
# print(stock_code.get_stock_basic_code())
# for stock_code_num in stock_code.get_stock_basic_code():
#     HGT_ZJ.insert_mysql_HSGTHDSTA(stock_code_num)
# # print(('filter', '(SCODE=\''+str(2222222)+'\')'))

# 创建从数据库表中获取有效代码
# print(get_HGTZJ_code_frommysql.select_HGTZJ_code())
for stock_code_num in get_HGTZJ_code_frommysql.select_HGTZJ_code():
    df_HGT_ZJ.insert_mysql_HSGTHDSTA(stock_code_num)
    # time.sleep(1)




