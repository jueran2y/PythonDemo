import tushare as ts
import matplotlib.pyplot as plt
import time
myStocks = {'002324','002503','002973','159995','002415','000100'}
name = ['name','open','pre_close','price','high','low','bid','ask','volume','amount']
ja = [[{'name': '侨银环保'}, {'open': '20.750'}, {'pre_close': '20.430'}, {'price': '22.470'}, {'high': '22.470'}, {'low': '20.720'}, {'bid': '22.470'}, {'ask': '0.000'}, {'volume': '3593744'}, {'amount': '78085391.320'}], [{'name': '芯片ETF'}, {'open': '0.920'}, {'pre_close': '0.910'}, {'price': '0.945'}, {'high': '0.947'}, {'low': '0.915'}, {'bid': '0.944'}, {'ask': '0.945'}, {'volume': '1187546563'}, {'amount': '1101717838.971'}], [{'name': '搜于特'}, {'open': '4.060'}, {'pre_close': '3.980'}, {'price': '3.990'}, {'high': '4.090'}, {'low': '3.820'}, {'bid': '3.990'}, {'ask': '4.000'}, {'volume': '296651645'}, {'amount': '1169383588.450'}], [{'name': '普利特'}, {'open': '20.400'}, {'pre_close': '20.600'}, {'price': '21.180'}, {'high': '21.320'}, {'low': '20.000'}, {'bid': '21.170'}, {'ask': '21.180'}, {'volume': '14947370'}, {'amount': '309661443.490'}], [{'name': 'TCL科技'}, {'open': '4.350'}, {'pre_close': '4.300'}, {'price': '4.470'}, {'high': '4.470'}, {'low': '4.320'}, {'bid': '4.460'}, {'ask': '4.470'}, {'volume': '367613155'}, {'amount': '1612744533.190'}], [{'name': '海康威视'}, {'open': '29.540'}, {'pre_close': '29.160'}, {'price': '30.220'}, {'high': '30.230'}, {'low': '29.490'}, {'bid': '30.220'}, {'ask': '30.230'}, {'volume': '53863033'}, {'amount': '1611108375.110'}]]

# name
# open
# pre_close
# price
# high
# low
# bid
# ask
# volume
# amount

# bigStock = []
# for myStock in myStocks:#编号
#     stock = ts.get_realtime_quotes(myStock)#获取个股数据
#     jsonlist = []
#     for i in range(len(name)):
#         dict = {}
#         dict[name[i]] = stock[name[i]][0]
#         jsonlist.append(dict)
#     bigStock.append(jsonlist)
# for i in range(6):
#     #涨跌幅
#     t = round((float(bigStock[i][3]['price']) - float(bigStock[i][2]['pre_close'])) / float(bigStock[i][2]['pre_close'])*100,2)
#     print(bigStock[i][0]['name'],round(float(bigStock[i][3]['price'])-float(bigStock[i][2]['pre_close']),3),t)

# tcl = ts.get_hist_data("002415")
# pic = []
# cnt = 0.0
# top = 0
# for i in range(len(tcl['close'])):
#     pic.append(float(tcl['close'][i]))
#     if top < float(tcl['close'][i]):
#         top = float(tcl['close'][i])
#     cnt += float(tcl['close'][i])
# print(round(cnt / len(tcl['close']),3))
# print(top)
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# pic.reverse()
# ax.plot(pic)
# plt.show()

# t = ts.get_hist_data('000100',start='2019-01-01',end='2020-01-01')
#
# print(t)

#             open  high  close   low  ...   ma20       v_ma5      v_ma10      v_ma20
# date                                 ...
# 2020-04-16  4.39  4.47   4.45  4.32  ...  4.531  3472386.35  4671006.35  5556972.13

# list = []
# flag = True
# stockCode = ts.get_today_all()['code']
# print()
# for i,code in enumerate(stockCode):
#     print('正在搜索第{}个数据...'.format(i))
#     flag = True
#     try:
#         stock = ts.get_hist_data(code, start='2020-04-16', end='2020-04-17')
#         preHigh = float(stock['high'][1])
#         preLow = float(stock['low'][1])
#         preOpen = float(stock['open'][1])
#         preClose = float(stock['close'][1])
#         StockHigh = float(stock['high'][0])
#         StockLow = float(stock['low'][0])
#         StockOpen = float(stock['open'][0])
#         StockClose = float(stock['close'][0])
#         #print(preOpen,preClose,StockHigh,StockLow,StockOpen,StockClose)
#     except:
#         print("获取第{}个数据失败{}".format(i,code))
#         flag = False
#     if flag:
#         #子母线
#         if preOpen > StockHigh and StockLow > preClose:  # 昨日开盘大于今日最高
#             print("多头子母线：为你找到第{}个股票：{}".format(i, code))
#             temp = '多头子母线'+code
#             list.append(temp)
#         if preClose > StockHigh and StockLow > preOpen:  # 昨日开盘大于今日最高
#             print("多空子母线：为你找到第{}个股票：{}".format(i, code))
#             temp = '多空子母线' + code
#             list.append(temp)
#
#         #锤子线
#         if preOpen > StockHigh and StockLow > preClose:
#             if 1.3*(preClose - preOpen) <= (preOpen - preLow) or 1.3*(preOpen - preClose) <= (preClose - preLow):
#                 if StockOpen >= preHigh:
#                     print("锤子线：为你找到第{}个股票：{}".format(i, code))
#                     temp = '锤子线' + code
#                     list.append(temp)
#
# file_handle = open('text.txt', mode='w',encoding='utf-8')
# for i in list:
#     file_handle.write('{}\n'.format(i))
# file_handle.close()

ts.set_token('3d2f1416ad3f285c244c15cb802ecfa40851d83cfc19939b670eb68b')
pro = ts.pro_api()
df = pro.daily(ts_code='000100.SZ', start_date='20200401', end_date='20200416')
print(df)

