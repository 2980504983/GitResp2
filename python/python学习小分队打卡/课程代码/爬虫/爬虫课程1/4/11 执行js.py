"""
    selenium控制浏览器执行js代码:
        有些时候，要点击的按钮不在视野中，就有可能点击失败
        有些网页的数据并不是一下就全部加载好的，而是触发式的(例如，你下滑，浏览器会不断的向服务器
        发起请求获取新的数据)，而selenium是不能直接下滑的，因此我们就可以通过执行js语句，来实现
        下拉的操作
"""
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://jn.lianjia.com'

driver = webdriver.Chrome()

driver.get(url)

# 滚动条的拖动
js = 'scrollTo(0, 500)'
# 执行js
driver.execute_script(js)

el_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[3]/div/div[1]/ul/li[2]')
el_button.click()
search_button = driver.find_element(By.XPATH, '//*[@id="keyword-box"]')
search_button.click()
search_button.send_keys('hhhjh')



