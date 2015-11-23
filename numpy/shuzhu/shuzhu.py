# -*-coding: utf-8 -*-
#numpy 数组的创建
__author__ = 'quanchimi'

import numpy as np

#创建数组ndarray
data1= [4,7,3,7,2,0]
arr1 = np.array(data1,dtype=np.float64)#利用array函数
print ('arr1:',arr1,arr1.dtype)
print

#创建多维数组 嵌套序列
data2 = [1,2,3,4.],[5,6,7,8]
arr2 = np.array(data2)
print('arr2:',arr2,arr2.dtype)
print
print('arr2\'s ndim:',arr2.ndim,arr2.shape)
print

#创建指定长度全为0或全为1的数组
arr3 = np.zeros(10)
print('arr3:',arr3,arr3.dtype)
print
arr4 = np.zeros((3,6))
print('arr4:',arr4)
print

#创建empty数组
arr5 = np.empty((4,3,2))#4个3x2的数组
print('arr5:',arr5)
print

#arrage数组
arr6 = np.arange(14)
print('arr6:',arr6)
print

#单位矩阵eye identity
arr7 = np.eye(3)
print('arr7:',arr7)
arr8 = np.identity(5)
print('arr8:',arr8)
print

#利用astype转换数据类型

arr9 =np.array([1,3,5,6,8,9],dtype=np.int32)
print('arr9:',arr9,arr9.dtype)
float_arr9 = arr9.astype(np.float64)
print('float_arr9:',float_arr9,float_arr9.dtype)
print

arr10 =np.array([1.5,4,6.2,0.1,6])
print('arr10:',arr10,arr10.dtype)
int_arr10 =arr10.astype(np.int32)
print('int_arr10:',int_arr10,int_arr10.dtype)
print
numeric_strings = np.array(['1.23','4','6.90','0.4'],dtype=np.string_)
print('numeric_strings:',numeric_strings,numeric_strings.dtype)
float_numeric_strings = numeric_strings.astype(float)
print('float_numeric_strings:',float_numeric_strings,float_arr9.dtype)