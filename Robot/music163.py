#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们这次的目标是爬取热门歌单(https://music.163.com/#/discover/playlist/)，比如网易云音乐中播放量大于 1000万 的歌单信息（歌单名称、链接）。

# Selenium with Python中文翻译文档 https://selenium-python-zh.readthedocs.io/en/latest/index.html

# how to use
# 1. pip install selenium
# 2. 安装ChromeDriver，https://sites.google.com/a/chromium.org/chromedriver/downloads
# 3. 以 Windows 为例，下载结束后，将 ChromeDriver 放置在 Python 安装目录下的 Scripts 文件夹即可

# <div class="bottom">
# <a class="icon-play f-fr" title="播放" href="javascript:;" data-res-type="13" data-res-id="2728824287" data-res-action="play"></a>
# <span class="icon-headset"></span>
# <span class="nb">17万</span>
# </div>

from selenium import webdriver #导入浏览器模块
import time #导入时间模块？好像没用用到
import os #os是用于操作文件的模块

url='https://music.163.com/#/discover/playlist/' #定义个变量url

browser = webdriver.Chrome() #启动一个浏览器窗口

#定义一个path参数，用于指定最终的文件存储的路径
path = os.environ['USERPROFILE']+"\\Documents\\python\\"
if os.path.exists(path) == False :
    os.makedirs(path)

while url != 'javascript:void(0)':
    print("url=",url)
    browser.get(url) #打开某个网址

    # time.sleep(1) #暂停1毫秒还是1秒

    # 切换到iframe,iframe name = contentFrame
    browser.switch_to.frame("contentFrame") #看要抓取的网页是否需要切换，主要看要抓取的页面是否在frame里，99%的网页都没有frame的

    #查找id=m-pl-container的元素，在这个元素里面查找所有<li>的元素，把查找到的所有li放到参数data里
    data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li") 
    
    # print(data[0].text) #输出data的内容到控制台

    for i in range(len(data)): #循环每一个<li>元素
        num = data[i].find_element_by_class_name("nb").text
        if '万' in num and int(num.split('万')[0]) > 1000: # 大于1千万
            msk = data[i].find_element_by_css_selector("a.msk")
            # print(msk)
            print(' '.join([msk.get_attribute('title'), num, msk.get_attribute("href")]) + '\n' + '=' * 50 + '\n')

            with open(path+"163playlist.txt", 'a', encoding='utf-8') as f:
                f.write(' '.join([msk.get_attribute('title'), num, msk.get_attribute("href")]) + '\n')
                
    url = browser.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")

print("文件已保存到",path+"163playlist.txt")
# 结束调用
browser.close()
