#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# NumPy 提供了很多统计函数，用于从数组中查找最小元素，最大元素，百分位标准差和方差等。 函数说明如下：

# numpy.amin() 和 numpy.amax()
# numpy.amin() 用于计算数组中的元素沿指定轴的最小值。

# numpy.amax() 用于计算数组中的元素沿指定轴的最大值。

# numpy.ptp()
# numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。

# numpy.percentile()
# 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。 函数numpy.percentile()接受以下参数。



a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 amin(a,1) 函数：axis=1')
print (np.amin(a,1))
print ('\n')
print ('再次调用 amin(a,0) 函数：axis=0')
print (np.amin(a,0))
print ('\n')
print ('调用 amax() 函数：')
print (np.amax(a))
print ('\n')
print ('再次调用 amax() 函数：')
print (np.amax(a, axis =  0))

a = np.array([[10, 7, 4], [3, 2, 1]])
print ('我们的数组是：')
print (a)
 
print ('调用 percentile() 函数：')
q:float = 70
# 50% 的分位数，就是 a 里排序之后的中位数
print (np.percentile(a, q)) 
 
# axis 为 0，在纵列上求
print (np.percentile(a, q, axis=0)) 
 
# axis 为 1，在横行上求
print (np.percentile(a, q, axis=1)) 
 
# 保持维度不变
print (np.percentile(a, q, axis=1, keepdims=True))


a = np.array([[30,65,70],[80,95,10],[50,90,60]])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 median() 函数：')
print (np.median(a))
print ('\n')
print ('沿轴 0 调用 median() 函数：')
print (np.median(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 median() 函数：')
print (np.median(a, axis =  1))

# 加权平均值
# numpy.average()
# numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。

# 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。

# 加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。

# 考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。

# 加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)=2
print ('# 加权平均值=========')
a = np.array([1,2,3,4])  
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 average() 函数：')
print (np.average(a))
print ('\n')
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])  
print ('再次调用 average() 函数：')
print (np.average(a,weights = wts))
print ('\n')
# 如果 returned 参数设为 true，则返回权重的和  
print ('权重的和：')
print (np.average([1,2,3,4],weights =  [4,3,2,1], returned =  True))


