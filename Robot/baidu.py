from selenium import webdriver
url='https://www.52pojie.cn/forum-2-1.html'
import time


# 创建一个浏览器
browser = webdriver.Chrome()


#while url != 'javascript:void(0)':
for page in range(5):
    print(url)
    browser.get(url)
    data=browser.find_element_by_id('threadlisttableid').find_elements_by_tag_name('tbody')

    for i in range(len(data)):
        # abc = data[i].find_element_by_xpath("//tbody[starts-with(@id,'normalthread_')]")
        # print(abc.text)
        tmp = data[i].get_attribute("id")
        if "normalthread_" in tmp:
            # print(tmp)
            title = data[i].find_element_by_class_name('xst').text
            mun = data[i].find_element_by_class_name('xi2').text

            if int(mun) > 1000:
                print(title + mun)

    url=browser.find_element_by_class_name('nxt').get_attribute('href')
# browser.find_element_by_id('kw').send_keys("牛逼")
# browser.find_element_by_id('su').click()


# browser.close()