# -*- coding:utf-8 -*-
__author__ = 'quanchimi'

#Numpy常用函数
import numpy as np

#1.读写CSV文件
#获取收盘价，成交量
close_price, volume = np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
#print('close_price:',close_price)
#获取开盘价
open_price = np.loadtxt('data.csv',delimiter=',',usecols=(3,),unpack=True)

#2/成交量加权平均数
vwap = np.average(close_price,weights=volume)
#时间加权平均数
twap = np.average(close_price,weights=(np.arange(len(close_price))))
#算数平均数
mean = np.mean(close_price)

#3.获取收盘价最高，最低价
h ,l = np.loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True)
hightest = np.max(h)
lowest = np.max(l)

#4.计算收盘价的中位数
median = np.median(close_price)

#排序(sort)
sorted_closing = np.msort(close_price)
#判断个数是奇数还是偶数
N = len(close_price)
median_ind =(N-1)/2
if(N&0x1):
    median_sorted_closing = sorted_closing[median_ind]
else:
    median_sorted_closing = (sorted_closing[median_ind]+sorted_closing[median_ind+1])/2

#5.计算方差
variance = np.var(close_price)

#手动求方差
variance_from_definition = np.mean((close_price-close_price.mean())**2)











