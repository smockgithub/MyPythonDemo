#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# NumPy 包含大量的各种数学运算的函数，包括三角函数，算术运算的函数，复数处理函数等。

# 三角函数
# NumPy 提供了标准的三角函数：sin()、cos()、tan()。

a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度  
print (np.sin(a*np.pi/180))
print ('\n')
print ('数组中角度的余弦值：')
print (np.cos(a*np.pi/180))
print ('\n')
print ('数组中角度的正切值：')
print (np.tan(a*np.pi/180))
