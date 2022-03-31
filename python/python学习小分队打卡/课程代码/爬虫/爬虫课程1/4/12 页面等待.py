"""
    页面等待
        页面在加载过程中需要花费时间等待网站服务器的响应，在这个过程中，标签元素可能还没有加载出来，
        是不可见的，如何处理这种情况呢

        页面等待分类:
            强制等待:
                time,sleep()
                缺点: 不智能，
            隐式等待:
                隐式等待时针对元素定位，饮食等待设置了一个时间，在一段时间内判断元素是否定位
                成功，如果成功了，就直接进入下一步，不会再继续等待，但是如果在设置的时间内没有定位
                成功，就会报错，只要设置一次，后面都会启用(较为常用)

            显示等待:
                明确等待某一个元素(没经过多少秒就查看等待条件是否达成，一般用于软件测试)，
                超过时间，会报错
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.baidu.com'

driver = webdriver.Chrome()
# 设置隐式等待之后的所有元素定位操作都有最大等待时间十秒，在十秒内会定期进行元素定位，超过设置时间就会报错
driver.implicitly_wait(10)
driver.get(url)

el = driver.find_element(By.XPATH, '//*[@id="lg"]/map/area')
print(el)

