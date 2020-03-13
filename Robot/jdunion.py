from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import traceback

#定义了一个方法
def getContent(fileName,p:bool):
    print("getContent 被执行了")
    #tr=browser.find_elements_by_css_selector("tr.el-table__row")
    

    j=1#从第一页开始
    k=100#到那一页结束
    while j<=k:#从第一页开始到100页结束
        print('当前正在抓取第%s页' %j)

        #是否还登录着？如果还登录着就继续抓，如果没有登录了，就提示并且等待人工登录继续
        try:
            tr=browser.find_elements_by_class_name("el-table__row")

            browser.find_elements_by_class_name("accountingCenterRouterNewUser")

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
                #print(msg)
                
                with open("D:\\花木兰\\ppp"+fileName+".txt", 'a', encoding='utf-8') as f:
                    f.write(msg + '\n')

            j=j+1 #标记为下一页

            #当前页20行循环结束后点击下一页
            if j<=k:
                nextpage=browser.find_elements_by_class_name('btn-next')[0]
                #time.sleep(random.randint(1,3))
                nextpage.click()
        except Exception as e:
            #没有找到登录标记
            print("异常信息:",e)
            traceback.print_exc()
            print("当前第几页=",j,";排序方式=",fileName,";是不是pop=",p)
            key=input("登录失败了，请人工登录后并调整好参数后按任意键继续")
            
        
        
# 方法定义结束

def setDesc(p:bool):
    #选择佣金比例，倒序
    #browser.find_element_by_css_selector("th.el-table_1_column_2").find_element_by_css_selector("i.sort-caret.descending").click()
    #getContent("佣金倒序",p)
    #选择30天引入单量
    #browser.find_element_by_css_selector("th.el-table_1_column_4").find_element_by_css_selector("i.sort-caret.descending").click()
    #getContent("引入单量",p)
    #选择30累计金额
    browser.find_element_by_css_selector("th.el-table_1_column_5").find_element_by_css_selector("i.sort-caret.descending").click()
    getContent("累计金额",p)

browser=webdriver.Chrome()

url='https://union.jd.com/investment/groupList'

browser.get(url)

element = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "accountingCenterRouterNewUser"))
    )

print('登入成功')

browser.get('https://union.jd.com/proManager/shopPromotion')

time.sleep(3)

# 30天有效订单量

#选中店铺类型
shopType = browser.find_element_by_css_selector("input.el-input__inner")
shopType.click()#点击店铺类型
time.sleep(2)
#选中自营 el-select-dropdown__item
g = browser.find_elements_by_css_selector("li.el-select-dropdown__item")[5]
g.click()

# 输入关键词
shopInput=browser.find_elements_by_css_selector("input.el-input__inner")[1]
shopInput.send_keys("生鲜")

#点击查询
browser.find_element_by_css_selector("[class='el-button el-button--primary el-button--small']").click()

#setDesc(False)

shopType = browser.find_element_by_css_selector("input.el-input__inner")
shopType.click()#点击店铺类型
time.sleep(2)
p = browser.find_elements_by_css_selector("li.el-select-dropdown__item")[6]
p.click() #非自营

# 输入关键词
shopInput=browser.find_elements_by_css_selector("input.el-input__inner")[1]
shopInput.send_keys("生鲜")

#点击查询
browser.find_element_by_css_selector("[class='el-button el-button--primary el-button--small']").click()

setDesc(True)

# 输入关键词
#shopInput=browser.find_elements_by_css_selector("input.el-input__inner")[1]
#shopInput.send_keys("生鲜")

#点击查询
#browser.find_element_by_css_selector("[class='el-button el-button--primary el-button--small']").click()








    




