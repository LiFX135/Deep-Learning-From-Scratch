# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

'''这是阶跃函数的最简单写法
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
'''


def step_function(x):
    return np.array(x>0, dtype = np.int64)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


