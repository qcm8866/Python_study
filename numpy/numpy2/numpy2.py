# -*- coding:utf-8 -*-
#Numpy索引切片
__author__ = 'quanchimi'

import numpy as np

arr = np.arange(10)
print('arr:',arr)
print('arr[0]:',arr[0],'arr[5]:',arr[5])
print('arr[5:8]',arr[5:8])
print(arr)
print
#多维数组

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[2])
print(arr2d[0,2])
print

arr3d =np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])

