# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

'''简单阶跃函数
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
'''


def step_function(x):
    return np.array(x>0, dtype = np.int64)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):#线性整流函数，详见百度百科
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = ReLU(x)
plt.plot(x, y1, linestyle="--")
plt.plot(x, y2)
plt.plot(x, y3, linestyle="-.")
plt.ylim(-0.1, 1.1)
plt.show()


