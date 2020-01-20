# -*- coding: utf-8 -*-
import numpy as np
A = np.array([1, 2, 3, 4])
print(A)
np.ndim(A)  #显示维度
np.shape(A) #显示形状
'''也可以用A.shape'''


A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

np.dot(A,B)#进行AB间的矩阵乘法运算


'''下面是神经网络内容'''
'''3.3.3 神经网络的内积'''
X = np.array([1,2])
W = np.array([[1,3,5], [2,4,6]])
