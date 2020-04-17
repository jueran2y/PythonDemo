import tushare as ts
import matplotlib.pyplot as plt
import time
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
list = []
flag = True
stockCode = ts.get_today_all()['code']
print()
for i,code in enumerate(stockCode):
    print('正在搜索第{}个数据...'.format(i))
    flag = True
    try:
        stock = ts.get_hist_data(code, start='2020-04-16', end='2020-04-17')
        preHigh = float(stock['high'][1])
        preLow = float(stock['low'][1])
        preOpen = float(stock['open'][1])
        preClose = float(stock['close'][1])
        StockHigh = float(stock['high'][0])
        StockLow = float(stock['low'][0])
        StockOpen = float(stock['open'][0])
        StockClose = float(stock['close'][0])
        #print(preOpen,preClose,StockHigh,StockLow,StockOpen,StockClose)
    except:
        print("获取第{}个数据失败{}".format(i,code))
        flag = False
    if flag:
        #子母线
        if preOpen > StockHigh and StockLow > preClose:  # 昨日开盘大于今日最高
            print("多头子母线：为你找到第{}个股票：{}".format(i, code))
            temp = '多头子母线'+code
            list.append(temp)
        if preClose > StockHigh and StockLow > preOpen:  # 昨日开盘大于今日最高
            print("多空子母线：为你找到第{}个股票：{}".format(i, code))
            temp = '多空子母线' + code
            list.append(temp)

        #锤子线
        if preOpen > StockHigh and StockLow > preClose:
            if 1.3*(preClose - preOpen) <= (preOpen - preLow) or 1.3*(preOpen - preClose) <= (preClose - preLow):
                if StockOpen >= preHigh:
                    print("锤子线：为你找到第{}个股票：{}".format(i, code))
                    temp = '锤子线' + code
                    list.append(temp)

file_handle = open('text.txt', mode='w',encoding='utf-8')
for i in list:
    file_handle.write('{}\n'.format(i))
file_handle.close()

