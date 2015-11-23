# -*- encoding:utf-8 -*-
#python Numpy库学习3
__author__ = 'quanchimi'
import numpy as np

#数组和标量之间的运算
arr1 = np.array([[1,2,3],[4,5,6]])
print('arr1:',arr1)
print
print(arr1*arr1)
print

arr2 =np.arange(15).reshape((3,5))
print(arr2)
#转置
print('transpose:',arr2.T)
print
#利用np.dot计算矩阵内积
arr3 = np.random.randn(6,3)
print(np.dot(arr3.T,arr3))
print

#高维数组转置
arr4 = np.arrange(16).reshap((2,3,4))

print(arr4)
print
print(arr4.transpose((1,0,2)))
