#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义3开始的所有单数的生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#n求余，为true，返回的是一个lamdba
def _not_devisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n=next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_devisible(n),it)

for n in primes():
    if n<10000:
        print(n)
        
    else:
        break


