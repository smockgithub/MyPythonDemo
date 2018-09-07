#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32clipboard as w

# 写入剪切板方法
def settext(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(aString)
    w.CloseClipboard()

print('请输入一个字符串')
s= input() #等待输入字符串
result = s.title().replace('.','') #对字符串进行处理
print(result) #输出到cmd里
settext(result) #调用写入剪切板方法
print('已复制到剪切板')