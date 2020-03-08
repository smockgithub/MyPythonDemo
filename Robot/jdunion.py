from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser=webdriver.Chrome()

url='https://union.jd.com/investment/groupList'

browser.get(url)

element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "accountingCenterRouterNewUser"))
    )

print('登入成功')

browser.get('https://union.jd.com/proManager/shopPromotion')

time.sleep(3)

tr=browser.find_elements_by_css_selector("tr.el-table__row")
#tr=tbody.find_element_by_tag_name("tr")

#tr=browser.find_element_by_class_name('el-table__row')


j=1#从第一页开始
k=100#到那一页结束
while j<=k:#从第一页开始到100页结束
    print('当前正在抓取第%s页' %j)

    #每一页从第一行到20行循环
    for i in range(len(tr)):


        name=tr[i].find_element_by_class_name("name").text
        #print(name)

        categories=tr[i].find_element_by_class_name('categories').get_attribute('title')
        #print(categories)

        self_operated="pop"
        try:
            tr[i].find_element_by_class_name('self-operated')
        except:
            #没有找到元素
            self_operated="pop"
        else:
            #找到了，没有异常
            self_operated="自营"


        #print(self_operated)

        佣金比例=tr[i].find_element_by_class_name("el-table_1_column_2").find_element_by_tag_name('span').text
        #print(佣金比例)

        pingfen=tr[i].find_element_by_class_name("el-table_1_column_3").find_element_by_tag_name('div').text
        #print(pingfen)

        dingdanliang=tr[i].find_element_by_class_name("el-table_1_column_4").find_element_by_tag_name('div').text
        #print(dingdanliang)

        jine=tr[i].find_element_by_class_name("el-table_1_column_5").find_element_by_tag_name('span').text
        #print(jine)

        #写入到文件
        
        msg="|".join([name,categories,self_operated,佣金比例,pingfen,dingdanliang,jine])
        print(msg)
        
        with open("D:\我的桌面\ppp.txt", 'a', encoding='utf-8') as f:
            f.write(msg + '\n')

    j=j+1 #标记为下一页

    #当前页20行循环结束后点击下一页
    if j<=k:
        nextpage=browser.find_elements_by_class_name('btn-next')[0]
        nextpage.click()

    




