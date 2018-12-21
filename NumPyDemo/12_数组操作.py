#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


# Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：

# 修改数组形状
# 翻转数组
# 修改数组维度
# 连接数组
# 分割数组
# 数组元素的添加与删除


# 修改数组形状
# 函数	描述
# reshape	不改变数据的条件下修改形状
# flat	数组元素迭代器
# flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# ravel	返回展开数组

# numpy.reshape
# numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： numpy.reshape(arr, newshape, order='C')
# arr：要修改形状的数组
# newshape：整数或者整数数组，新的形状应当兼容原有形状
# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。

a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)

# numpy.ndarray.flat
# numpy.ndarray.flat 是一个数组元素迭代器，实例如下:

a = np.arange(9).reshape(3,3) 
print ('原始数组：')
for row in a[1:]: # [3 4 5]
    print (row)
 
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print ('迭代后的数组：')
for element in a.flat:
    print (element)

# numpy.ndarray.flatten
# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：

# ndarray.flatten(order='C')
# 参数说明：

# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
# 默认按行
 
print ('展开的数组：')
print (a.flatten(order = 'C'))
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))

