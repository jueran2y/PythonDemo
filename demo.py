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
for i, code in enumerate(stockCode):
    print('正在搜索第{}个数据...'.format(i))
    flag = True
    try:
        stock = ts.get_hist_data(code, start='2020-04-15', end='2020-04-17')

        ppHigh = float(stock['high'][2])
        ppLow = float(stock['low'][2])
        ppOpen = float(stock['open'][2])
        ppClose = float(stock['close'][2])

        preHigh = float(stock['high'][1])
        preLow = float(stock['low'][1])
        preOpen = float(stock['open'][1])
        preClose = float(stock['close'][1])

        StockHigh = float(stock['high'][0])
        StockLow = float(stock['low'][0])
        StockOpen = float(stock['open'][0])
        StockClose = float(stock['close'][0])
        # print(preOpen,preClose,StockHigh,StockLow,StockOpen,StockClose)
    except:
        print("获取第{}个数据失败{}".format(i, code))
        flag = False

    # 都是在一段上涨或下跌的过程中出现才准确率比较大
    if flag:
        # 子母线
        if preOpen > StockHigh and StockLow > preClose:  # 昨日开盘大于今日最高
            print("多头子母线：为你找到第{}个股票：{}".format(i, code))
            temp = '多头子母线：' + code
            list.append(temp)
        if preClose > StockHigh and StockLow > preOpen:  # 昨日开盘大于今日最高
            print("多空子母线：为你找到第{}个股票：{}".format(i, code))
            temp = '多空子母线：' + code
            list.append(temp)

        human = False
        # 锤子线
        if preOpen == preHigh or preHigh < preOpen * 1.014 or preClose == preHigh or preHigh < preClose * 1.014:  # 保证锤子线的上阴线不超过实体太多
            # 锤子线阳线
            if preClose > preOpen:
                if preClose - preOpen <= 1.3 * (preOpen - preLow):# 锤子的下影线是否是实体的1.3倍长
                    human = True
            else:#锤子线阴线
                if preOpen - preClose <= 1.3 * (preClose - preLow):# 锤子的下影线是否是实体的1.3倍长
                    human = True
            if human:
                if StockLow >= preHigh:  # 如果最低大于前一天的最高价则有可能是会上涨的概率大
                    print("上涨锤子线：为你找到第{}个股票：{}".format(i, code))
                    temp = '上涨锤子线：' + code
                    list.append(temp)
                if StockHigh <= preClose:  # 如果最高价小于前一天的收盘价则可能是会下跌的概率大
                    print("下跌锤子线：为你找到第{}个股票：{}".format(i, code))
                    temp = '下跌锤子线：' + code
                    list.append(temp)

        # 启明星
        # 在下跌趋势中第一天是阴线
        if ppOpen > ppClose:
            # 然后在第二天出现了星线 可以是阴线也可以是阳线
            if preClose < ppClose and preOpen < ppClose:
                # 第三天出现了大阳线 要跳空
                if StockOpen > preClose and StockClose > preClose:
                    print("启明星：为你找到第{}个股票：{}".format(i, code))
                    temp = '启明星：' + code
                    list.append(temp)

        # 黄昏星
        # 在下跌趋势中第一天是阳线
        if ppClose > ppOpen:
            # 然后在第二天出现了星线 可以是阴线也可以是阳线
            if preClose > ppClose and preOpen > ppClose:
                # 第三天出现了大阴线 要跳空
                if StockOpen < preClose and StockClose < preClose:
                    print("黄昏星：为你找到第{}个股票：{}".format(i, code))
                    temp = '黄昏星：' + code
                    list.append(temp)

file_handle = open('text.txt', mode='w', encoding='utf-8')
for i in list:
    file_handle.write('{}\n'.format(i))
file_handle.close()
