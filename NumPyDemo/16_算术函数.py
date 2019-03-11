#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。

# 需要注意的是数组必须具有相同的形状或符合数组广播规则。

a = np.arange(9, dtype = np.float_).reshape(3,3)  
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([10,10,10])  
print (b)
print ('\n')
print ('两个数组相加：')
print (np.add(a,b))
print ('\n')
print ('两个数组相减：')
print (np.subtract(a,b))
print ('\n')
print ('两个数组相乘：')
print (np.multiply(a,b))
print ('\n')
print ('两个数组相除：')
print (np.divide(a,b))

# numpy.reciprocal()
# numpy.reciprocal() 函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。

# numpy.power()
# numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。

# numpy.mod()
# numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果。



