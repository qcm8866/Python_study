# -*- encoding:utf-8 -*-
__author__ = 'quanchimi'
# 股票分析例子学习numpy


import numpy as np

close_price = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
cp = close_price
# diff函数计算离散差分
cp_diff =np.diff(cp)
rate_of_returns = cp_diff/cp[:-1]
standard_deviation = np.std(rate_of_returns)
print(standard_deviation)
#对数收益指数