"""
    driver对象的常用属性和方法:
        1 driver.page_source 当前浏览器渲染之后的网页源代码
        2 driver.current_url 当前标签页的url
        3 driver.close() 关闭当前页面，如果只有一个页面则关闭整个浏览器
        4 driver.quit() 关闭浏览器
        5 driver.forward 页面前进
        6 driver.back() 页面后退
        7 driver.screen_shot(img_name) 页面截图
"""
import time
from time import sleep
from selenium import webdriver

url = "http://www.baidu.com"

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址
driver.get(url)

# # 显示源码
# print(driver.page_source)
#
# # 显示响应对应的url
# print(driver.current_url)
#
# # 页面标题
# print(driver.title)
#
# time.sleep(2)
# driver.get('http://www.douban.com')
#
# time.sleep(2)
# driver.back()
#
# time.sleep(2)
# driver.forward()
#
# time.sleep(2)
# driver.close()


# 截图,遇到要输入验证码，并且每次获取验证码图片，图片都会改变时，就需要截图，截图后在处理
driver.save_screenshot('baidu.png')
# 退出
driver.quit()

