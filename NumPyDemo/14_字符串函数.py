#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作。 它们基于 Python 内置库中的标准字符串函数。

# 这些函数在字符数组类（numpy.char）中定义。

# 函数	描述
# add()	对两个数组的逐个字符串元素进行连接
# multiply()	返回按元素多重连接后的字符串
# center()	居中字符串
# capitalize()	将字符串第一个字母转换为大写
# title()	将字符串的每个单词的第一个字母转换为大写
# lower()	数组元素转换为小写
# upper()	数组元素转换为大写
# split()	指定分隔符对字符串进行分割，并返回数组列表
# splitlines()	返回元素中的行列表，以换行符分割
# strip()	移除元素开头或者结尾处的特定字符
# join()	通过指定分隔符来连接数组中的元素
# replace()	使用新字符串替换字符串中的所有子字符串
# decode()	数组元素依次调用str.decode
# encode()	数组元素依次调用str.encode

# add()	对两个数组的逐个字符串元素进行连接
print ('连接两个字符串：')
print (np.char.add('hello',' xyz'))
print ('\n')

print ('连接两个字符串：')
print (np.char.add(['hello'],[' xyz']))
print ('\n')
 
print ('连接示例：')
print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))

print (np.char.multiply('Runoob ',3))

# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))

print (np.char.title('ilikerunoob df'))
print ('ilikerunoob df'.title())

# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))

# 移除数组元素头尾的 a 字符
print (np.char.strip(['arunooba','admin','aajaava'],'a'))
