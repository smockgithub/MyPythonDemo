#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们这次的目标是爬取热门歌单(https://music.163.com/#/discover/playlist/)，比如网易云音乐中播放量大于 1000万 的歌单信息（歌单名称、链接）。

# how to use
# 1. pip install selenium
# 2. 安装ChromeDriver，https://sites.google.com/a/chromium.org/chromedriver/downloads
# 3. 以 Windows 为例，下载结束后，将 ChromeDriver 放置在 Python 安装目录下的 Scripts 文件夹即可

# <div class="bottom">
# <a class="icon-play f-fr" title="播放" href="javascript:;" data-res-type="13" data-res-id="2728824287" data-res-action="play"></a>
# <span class="icon-headset"></span>
# <span class="nb">17万</span>
# </div>

from selenium import webdriver
import time

url='https://music.163.com/#/discover/playlist/'

# 创建一个浏览器
browser = webdriver.Chrome()

while url != 'javacript:void(0)':

    browser.get(url)

    # time.sleep(1)

    # 切换到iframe,iframe name = contentFrame
    browser.switch_to.frame("contentFrame")

    # data = browser.find_element_by_id('m-pl-container').find_element_by_tag_name('li')
    data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    # print(data[0].text)
    # print(len(data))

    for i in range(len(data)):
        num = data[i].find_element_by_class_name("nb").text
        if '万' in num and int(num.split('万')[0]) > 1000: # 大于1千万
            msk = data[i].find_element_by_css_selector("a.msk")
            # print(msk)
            print(' '.join([msk.get_attribute('title'), num, msk.get_attribute("href")]) + '\n' + '=' * 50 + '\n')

            with open("F:\\Users\\smock\\Documents\\python\\163playlist.txt", 'a', encoding='utf-8') as f:
                f.write(' '.join([msk.get_attribute('title'), num, msk.get_attribute("href")]) + '\n')
                
    url = browser.find_element_by_css_selector("a.zbtn.znxt").get_attribute("href")

# 结束调用
browser.close()