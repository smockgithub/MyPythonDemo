#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# NumPy "bitwise_" 开头的函数是位运算函数。

# NumPy 位运算包括以下几个函数：

# 函数	描述
# bitwise_and	对数组元素执行位与操作
# bitwise_or	对数组元素执行位或操作
# invert	按位取反
# left_shift	向左移动二进制表示的位
# right_shift	向右移动二进制表示的位
# 注：也可以使用 "&"、 "~"、 "|" 和 "^" 等操作符进行计算。

print ('13 和 17 的二进制形式：')
a,b = 13,17
print (bin(a), bin(b))
print ('\n')
 
print ('13 和 17 的位与：')
print (np.bitwise_and(13, 17))
print (13&17)
# 01101 = 13 
# 01110
# 01111
# 10000
# 10001 = 17
# 01101 = 13 
# 13与17
# 00001

print ('13 和 17 的位或：')
print (np.bitwise_or(13, 17))
print (13|17)
# 13或17
# 10001 = 17
# 01101 = 13 
# 11101 = 29

# invert() 函数对数组中整数进行位取反运算，即 0 变成 1，1 变成 0。
# 对于有符号整数，取该二进制数的补码，然后 +1。二进制数，最高位为0表示正数，最高位为 1 表示负数。
print ('13 invert：')
print (np.invert(13))
# 01101 = 13 
# 32位 00000000 00000000 00000000 00001101 = 13

print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print (np.invert(np.array([13], dtype = np.uint8)))
print ('\n')
# 比较 13 和 242 的二进制表示，我们发现了位的反转
 
print ('13 的二进制表示：')
print (np.binary_repr(13, width = 8))
print ('\n')
 
print ('242 的二进制表示：')
print (np.binary_repr(242, width = 8))
