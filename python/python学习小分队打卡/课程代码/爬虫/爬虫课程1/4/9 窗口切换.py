"""
    有些时候，在一个页面的html文件中，会嵌套一个新的框架，也就是有一个新的html文件，
    这时候，我们的操作是停留在，外面的html中的，想要操作里面的html(点击，或是向框架里发送内容)
    就必须切换页面，不然是定位不到的
"""
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)


# 切换页面,里面输入，要切换框架的id,不过有时候id会没有，甚至可能有猫腻
# driver.switch_to.frame('login_frame')

# 可以先定位frame，也就是新的框架，然后再去切换
el_frame = driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]')
driver.switch_to.frame(el_frame)

driver.find_element(By.ID, "switcher_plogin").click()
driver.find_element(By.ID, "u").send_keys('2980504083')
driver.find_element(By.ID, "p").send_keys('12341234')
driver.find_element(By.ID, "login_button").click()



