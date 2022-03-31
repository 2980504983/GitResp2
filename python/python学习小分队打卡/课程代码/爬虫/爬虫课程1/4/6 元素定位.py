"""
    driver对象定位标签元素，获取标签对象的方法
        from selenium.webdriver.common.by import By

        By类的可用属性如下：
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag_name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"


        1 driver.find_element(By.ID, 'kw') 定位一个元素，定位不到，会报错
        2 driver.find_elements(By.ID, 'kw') 定位多个元素，返回列表，没有元素，返回空列表
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# url = 'http://www.baidu.com'
#
# driver = webdriver.Chrome()
#
# driver.get(url)

# 通过xpath进行元素定位
# 只要定位到节点就行，不需要对节点进行操作，webdriver有自己的接口
# driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python3')

# css选择器
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('python3')

# 通过标签中name属性的值进行元素定位
# driver.find_element(By.NAME, 'wd').send_keys('python3')

# 通过class属性值进行元素定位
# driver.find_element(By.CLASS_NAME, 'wd').send_keys('python3')

# 通过链接文本进行元素定位，必须是全部文本
# driver.find_element(By.LINK_TEXT, '百度一下').send_keys('python3')

# 部分文本就行
# driver.find_element(By.PARTIAL_LINK_TEXT, '百度一下').send_keys('python3')

# 通过标签名进行元素定位,有多个标签，只返回第一个
# driver.find_element(By.TAG_NAME, 'title')

# 通过id进行元素定位,输入id对应的值即可
# driver.find_element(By.ID, 'su').click()


# 多个元素定位-------------------------------------------------------


url ='https://bj.58.com/hezu/?PGTID=0d100000-0000-1706-51cd-3b447b28fc77&ClickID=2'

driver = webdriver.Chrome()

driver.get(url)

el_list = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')

for el in el_list:
    print(el.text, el.get_attribute('href'))
