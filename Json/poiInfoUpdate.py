#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def rewrite_json_file(filepath,json_data):
	with open(filepath, 'w') as f:
		json.dump(json_data,f)
	f.close()

jsonFile = input("请输入文件地址：")

with open(jsonFile, "r", encoding='utf-8') as f:
    src = json.loads(f.read())

pid = int(input("请输入PID："))
category_id = int(input("请输入category_id："))
y = int(input("请输入需要修改的y："))

print(type(src))

if isinstance(src,(list, tuple)):#如果是已知类型
    for item in src:
        if item["pid"] == pid and item["category_id"] == category_id:
            # print(item["pid"])
            item["y"] = y
    
    # 导出到文件
    # os.path.abspath(jsonFile) # 获取路径对象
    path = os.path.abspath(os.path.dirname(os.path.abspath(jsonFile)) + os.path.sep + ".")
    print("path=",path)
    rewrite_json_file(path+"\\poiInfo2.json",src)


