"""
    selenium控制标签页的切换:
        (句柄就是指向标签对象的标识)
        1 获取所有标签页的窗口句柄列表
        2 利用窗口句柄切换到句柄指向的标签页

        具体方法:
            1 获取当前所有标签页句柄构成的列表:
                current_windows = driver.window_handles
            2 根据标签页句柄列表索引下标进行切换:
                driver.switch_to.window(current_windows[0])

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://jn.58.com/'

driver = webdriver.Chrome()

driver.get(url)

print(driver.current_url)
print(driver.window_handles)

# 定位并点击租房按钮
el = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div'
                         '[1]/div[1]/span[1]/a')
el.click()

# 虽然点击并创建了新的页面，但是当前url还是在首页，也就是控制权还在首页
print(driver.current_url)
print(driver.window_handles)


# 切换标签页
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_url)

el_list = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/ul/li[1]/div[2]/h2/a')
print(len(el_list))
