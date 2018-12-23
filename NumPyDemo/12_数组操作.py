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
# flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，变为一维
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
print (a.flatten())
print ('\n')
 
print ('以 F 风格顺序展开的数组：')
print (a.flatten(order = 'F'))



# numpy.ravel
# numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。

# 该函数接收两个参数：

# numpy.ravel(a, order='C')
# 参数说明：

# order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。

a = np.arange(8).reshape(2,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 ravel 函数之后：')
print (a.ravel()) # [0 1 2 3 4 5 6 7]
print ('\n')
 
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))


# 翻转数组
# 函数	描述
# transpose	对换数组的维度
# ndarray.T	和 self.transpose() 相同
# rollaxis	向后滚动指定的轴
# swapaxes	对换数组的两个轴
# numpy.transpose
# numpy.transpose 函数用于对换数组的维度，格式如下：



# numpy.transpose(arr, axes)
# 参数说明:

# arr：要操作的数组
# axes：整数列表，对应维度，通常所有维度都会对换。

a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a )
print ('\n')
 
print ('对换数组：')
print (np.transpose(a))


# numpy.ndarray.T 类似 numpy.transpose：
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)

# numpy.rollaxis
# numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：
# 向后滚动到0

# numpy.rollaxis(arr, axis, start)
# 参数说明：

# arr：数组
# axis：要向后滚动的轴，其它轴的相对位置不会改变
# start：默认为零，表示完整的滚动。会滚动到特定位置。

# 创建了三维的 ndarray
a = np.arange(24).reshape(2,3,4)
 
print ('np.arange(24).reshape(2,3,4)原数组：，2行 3行 4列')
print (a)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print ('\n')
 
print ('调用 rollaxis 函数：np.rollaxis(a,2,0)')
print (np.rollaxis(a,2,0))# 将轴 2 滚动到轴 0（宽度到深度） => 2 * 3 * 4 变更为 4*2*3
print ('\n')

print ('调用 rollaxis 函数：np.rollaxis(a,1,0)')
print (np.rollaxis(a,1,0))# 将轴 1 滚动到轴 0 => 2*3*4 变更为 3*2*4
print ('\n')
 
print ('调用 rollaxis 函数：np.rollaxis(a,2,1)')
print (np.rollaxis(a,2,1))# 将轴 2 滚动到轴 1：（宽度到高度）



# numpy.swapaxes
# numpy.swapaxes 函数用于交换数组的两个轴，格式如下：

# numpy.swapaxes(arr, axis1, axis2)
# arr：输入的数组
# axis1：对应第一个轴的整数
# axis2：对应第二个轴的整数

# 创建了三维的 ndarray
a = np.arange(24).reshape(2,3,4)
 
print ('原数组：')
print (a) # 2*3*4
print ('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
 
print ('调用 swapaxes 函数后的数组：')
print (np.swapaxes(a, 2, 0)) # 4*3*2