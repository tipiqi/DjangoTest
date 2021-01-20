#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/11/5 19:50
# software: PyCharm

import requests
import json

cookies = {
    'waptgshowtime': '2020115',
    'st_si': '68932914331287',
    'st_sn': '12',
    'st_psi': '20201105195821338-113300300813-3894495425',
    'st_asi': 'delete',
    'qgqp_b_id': '83b60a65c5c22972649fa86e1efda73a',
    'cowCookie': 'true',
    'intellpositionL': '1215.35px',
    'intellpositionT': '829.4px',
    'st_pvi': '86855102282273',
    'st_sp': '2020-11-05%2019%3A51%3A19',
    'st_inirUrl': 'https%3A%2F%2Fwww.eastmoney.com%2F',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
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
    ('pz', '1000'),  # 获取的数据条数
    ('po', '1'),  # 按照资金流入净额 1 正  0 负
    ('np', '1'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5'),
    ('fltt', '2'),
    ('invt', '2'),
    ('fid0', 'f4001'),
    ('fid', 'f62'),  # 今日的 f62   3日的 f267   5日的 f164  10日的  f174
    #   当日 fields  f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124
    #   3日  fields  f12,f14,f2,f127,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f257,f258,f124
    #   5日  fields  f12,f14,f2,f109,f164,f165,f166,f167,f168,f169,f170,f171,f172,f173,f257,f258,f124
    #   10日 fields  f12,f14,f2,f160,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183,f260,f261,f124
    ('fs', 'm:0 t:6 f:!2,m:0 t:13 f:!2,m:0 t:80 f:!2,m:1 t:2 f:!2,m:1 t:23 f:!2,m:0 t:7 f:!2,m:1 t:3 f:!2'),
    ('stat', '1'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124,f127,f267,f268,f269,f270,f271,f272,f273,f274,f275,f276,f109,f164,f165,f166,f167,f168,f169,f170,f171,f172,f173,f160,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183'),
    # ('fields','f116,f117,f12,f14,f2'),
    # ('rt', '53485916'),
    ('rt', '53488238'),
    # ('cb', 'jQuery183010560113351676459_1604577195795'),
    ('_', '1604577503807'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)

# print(requests.content)
resp_dict = json.loads(response.text)
print(resp_dict)
datas = resp_dict.get('data').get('diff')
# print(datas)

companyname = []

for data in datas:
    # print(data)
    # 股票代码
    symbol = data.get('f12')
    # 股票名称、公司名称
    company = data.get('f14')
    # 最新价格
    last_trade = data.get('f2')

    # 今日涨跌幅度   3日涨跌幅度 5 10
    change = data.get('f3')
    change_day3 = data.get('f127')
    change_day5 = data.get('f109')
    change_day10 = data.get('f173')

    # 主力净流入  3日主力净流入 5 10
    master_come = data.get('f62')
    master_come_day3 = data.get('f267')
    master_come_day5 = data.get('f164')
    master_come_day10 = data.get('f174')
    # 主力净流入占比   3日主力净流入占比
    master_come_num = data.get('f184')
    master_come_num_day3 = data.get('f268')
    master_come_num_day5 = data.get('f165')
    master_come_num_day10 = data.get('f175')

    # 超大单净流入   3日
    super_big_come = data.get('f66')
    super_big_come_day3 = data.get('f269')
    super_big_come_day5 = data.get('f166')
    super_big_come_day10 = data.get('f176')
    # 超大单净流入占比    3日
    super_big_come_num = data.get('f69')
    super_big_come_num_day3 = data.get('f270')
    super_big_come_num_day5 = data.get('f167')
    super_big_come_num_day10 = data.get('f177')

    # 大单净流入   3日   5
    big_come = data.get('f72')
    big_come_day3 = data.get('f271')
    big_come_day5 = data.get('f168')
    big_come_day10 = data.get('f178')
    # 大单净流入占比
    big_come_num = data.get('f75')
    big_come_num_day3 = data.get('f272')
    big_come_num_day5 = data.get('f169')
    big_come_num_day10 = data.get('f179')

    # 中单净流入
    middle_come = data.get('f78')
    middle_come_day3 = data.get('f273')
    middle_come_day5 = data.get('f170')
    middle_come_day10 = data.get('f180')
    # 中单净流入占比
    middle_come_num = data.get('f81')
    middle_come_num_day3 = data.get('f274')
    middle_come_num_day5 = data.get('f171')
    middle_come_num_day10 = data.get('f181')

    # 小单净流入
    small_come = data.get('f84')
    small_come_day3 = data.get('f275')
    small_come_day5 = data.get('f172')
    small_come_day10 = data.get('f182')
    # 小单净流入占比
    small_come_num = data.get('f87')
    small_come_num_day3 = data.get('f276')
    small_come_num_day5 = data.get('f173')
    small_come_num_day10 = data.get('f183')
    #
    # 汇总占比  当天资金流入占比，3日内资金流入占比，5日内资金流入占比，10日内资金流入占比
    sum_today = master_come_num + super_big_come_num + big_come_num + middle_come_num + small_come_num
    sum_day3 = master_come_num_day3 + super_big_come_num_day3 + big_come_num_day3 + middle_come_num_day3 + small_come_num_day3
    sum_day5 = master_come_num_day5 + super_big_come_num_day5 + big_come_num_day5 + middle_come_num_day5 + small_come_num_day5
    sum_day10 = master_come_num_day10 + super_big_come_num_day10 + big_come_num_day10 + middle_come_num_day10 + small_come_num_day10
    # 汇总   单天所有的流入资金，3日内所有的流入资金，5日内所有的流入资金，10日内所有的流入资金
    sum_num_today = master_come + super_big_come + big_come + middle_come + small_come
    sum_num_day3 = master_come_day3 + super_big_come_day3 + big_come_day3 + middle_come_day3 + small_come_day3
    sum_num_day5 = master_come_day5 + super_big_come_day5 + big_come_day5 + middle_come_day5 + small_come_day5
    sum_num_day10 = master_come_day10 + super_big_come_day10 + big_come_day10 + middle_come_day10 + small_come_day10
    # 差额比值  *天的流入资金-今日流入资金
    chg_day3 = (sum_num_day3 - sum_num_today)/sum_num_day3
    chg_day5 = (sum_num_day5 - sum_num_today)/sum_num_day5
    chg_day10 = (sum_num_day10 - sum_num_today)/sum_num_day10

    #  某只股票的最近的资金情况




# 市值：将几天内净流入的金额除以市值，计算比例，
    # if chg_day10 > 0.8 and sum_day10 > 10:
    if chg_day3 > 0.7 and sum_day3 > 10 and change_day3 < 5:
        # 11月23号 早上筛选出：['光大银行', '盈康生命', '溢多利', '茂化实华', '渤海租赁'] 记得回归复盘  预计100亿以下市值不考虑
        #1126   ['邮储银行', '金智科技', '南纺股份', '爱丽家居']
    # if change_day3 < 5:
          companyname.append(company)
# （10天所有的流入加流出- （当天流入+流出） ） / 10天所有的流入加流出

    # 模型1 近三天涨幅小于5  and  近5天的净流入占比大于10
    # if change_day3 < 5 and (sum_day5) > 10:
    #     companyname.append(company)

    # 模型2 当天净流入>5  and 近3天净流入占比大于10 and 近5天净流入大于10   and 近10天净流入占比大于15
    # if sum_today > 5  and sum_day3 > 10 and sum_day5 > 10 and sum_day10 > 15:
    # if sum_today > 5 and sum_day5 > 10 and sum_day10 > 15:
    # if sum_day5 > 10 and sum_day10 > 15:
    #     companyname.append(company)

    # 模型3 近三天涨幅小于5    最近3天净流入大于10
    # if change_day3 < 5 and sum_day3 > 10:
    #     companyname.append(company)

    # 模型4 近三天涨幅小于5    最近10天净流入大于10
    # if change_day3 < 5 and sum_day10 > 10:
    #     companyname.append(company)
    #
    # 模型5 近10天净流入大于15
    # if sum_day10 > 10:
    #     companyname.append(company)

    # 模型6 近10点净流入大于10    近5天涨幅小于5     偏向稳定形
    # if change_day5 < 5 and sum_day10 > 8:
    #     companyname.append(company)


print(companyname)
