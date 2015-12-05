# -*- encoding:utf-8 -*-
__author__ = 'quanchimi'
# 股票分析例子学习numpy


import numpy as np
import datetime

close_price = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
cp = close_price
# diff函数计算离散差分
cp_diff =np.diff(cp)
rate_of_returns = cp_diff/cp[:-1]
standard_deviation = np.std(rate_of_returns)
# print(standard_deviation)

# 对数收益指数
log_rate_of_return = np.diff(np.log(cp))
# print(log_rate_of_return)

# where函数可以根据指定条件返回数组的索引值
pos_return_indices = np.where(log_rate_of_return > 0)


# 计算波动率 年波动率等于对数收益的标准差除以其均值，再除以交易日倒数的平方根
annual_volatility = (np.std(log_rate_of_return) / np.mean(log_rate_of_return)) / np.sqrt(1. / 252.)
# print(annual_volatility)

Monthly_Volatility = annual_volatility * np.sqrt(1. / 12.)


# 日期分析

def datestr2num(s):
    return datetime.datetime.strptime(s,"%d-%m-%Y").date().weekday()
dates = np.loadtxt('data.csv',delimiter=',',usecols=(1,),converters={1:datestr2num},unpack=True)
# 保存各工作日的平均收盘价
averages = np.zeros(5)
for i in xrange(5):
    indices = np.where(dates==i)
    price = np.take(cp,indices)
    avg =  price.mean()
    print ("date", i, "prices", price, "average", avg)
    averages[i] = avg

# 找出哪个工作日平均收盘价最高，哪个最低
top = averages.max()
bottom = averages.min()
print("Highest average",top)
print("Top day of the week",np.argmax(averages))
print("Lowest average",bottom)
print("Bottom day of the week",np.argmin(averages))

