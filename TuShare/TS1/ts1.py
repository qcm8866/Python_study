# -*- coding:utf-8 -*-
__author__ = 'quanchimi'
#你好
import tushare as ts
_600011 = ts.get_hist_data('600011',start='2015-11-21',end='2015-11-30')
print(_600011)
