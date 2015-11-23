# -*-coding: utf-8 -*-
#数组
__author__ = 'quanchimi'
from pandas import Series,DataFrame
import pandas as pd

# obj = Series([4,7,-7],index=['c','a','b'])
#
# print(obj[['c','a']])

data = {
    'state':['01','02','04'],
    'year':[2001,2002,2003],
    'pop':[1.5,1.7,1.8]
}

frame = DataFrame(data)

print(frame)