import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
driver = webdriver.Chrome()

# 发送请求
driver.get("http://www.baidu.com")
time.sleep(3)

# 在百度搜索框中搜索python
driver.find_element(By.ID, 'kw').send_keys('python')

# 点击百度搜索
driver.find_element(By.ID, 'su').click()

time.sleep(6)

# 退出浏览器
driver.quit()
