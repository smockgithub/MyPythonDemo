# -*- coding: utf-8 -*-



# 声明方法用def
def printStr(str):
    print(str)

printStr("ABCDEFG")

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

print(power(10))
print(power(99,50))