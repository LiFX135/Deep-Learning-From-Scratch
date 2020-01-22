# -*- coding: utf-8 -*-
import numpy as np


'''   softmax函数的原始定义   '''
def softmax_prime(a):
    exp_a = exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
''' 这个函数运算时如果输入过大，那么很容易出现数据溢出  '''


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)   #溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)


