# 第一章 Python入门

### 1.5 NumPy

#### 1.5.2 NumPy数组

```python
x = np.array([1.0,2.0,3.0])		#使用np.array(<列表参数>)生成数组
print(x)

>>> [1.0,2.0,3.0]

type(x)

>>> <class 'numpy.ndarray'>		#数组类型为'numpy.ndarray'
```



#### 1.5.3 算术运算

```python
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y
>>> array([3., 6., 9.])

x - y
>>> array([-1., -2., -3.])

x * y
>>> array([2., 8., 18.])	
```

##### NumPy对大部分数组算术运算要求元素个数相同，不然会报错



#### 1.5.4 N维数组

```python
A = np.array([[1, 2], [3, 4]])

>>>print(A)
[[1 2]
 [3 4]]

>>>A.shape			#.shape 方法查看矩阵形状
Out[13]: (2, 2)

>>>A.dtype			#.dtype 方法查看矩阵的数据类型
dtype('int32')

>>>B = np.array([[3, 0], [0, 6]])

>>>A + B 			#矩阵加减法是正常的
array([[ 4,  2],
       [ 3, 10]])

>>>A * B 			#矩阵乘法和数学上不同
array([[ 3,  0],
       [ 0, 24]])

```



#### 1.5.5 广播

numpy能将形状不同的数组自动拓展

![image-20191215202411241](C:\Users\11058\AppData\Roaming\Typora\typora-user-images\image-20191215202411241.png)

![image-20191215202516158](C:\Users\11058\AppData\Roaming\Typora\typora-user-images\image-20191215202516158.png)



#### 1.5.6 访问元素

暂时不管









### 1.6 Matplotlib

#### 1.6.1 绘制简单图形



