"""
    1 用selenium访问目标url
    2 下滑,点击English
    3 下滑,点击全部语言
    4 等待一些时间，获取页面html
    5 从html中解析评论
    6 点击下一页
    7 重复4-6的过程,直至最后一页
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PingLun:
    def __init__(self):
        self.base_url = 'https://www.tripadvisor.ca/Attraction_Review-g1159661-d1824759-Reviews-or10-Hongcun_Ancient_Village-Yi_County_Anhui.html'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        time.sleep(5)
        temp_list = self.driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[2]/div/div/span/section[8]/div/div/span/section/section/div[1]/div/div[5]/div/span/div/div[5]/div[1]/div/span')
        for item in temp_list:
            print(item.text)

    def run(self):
        # 1 用selenium访问目标url
        self.driver.get(self.base_url)
        # 2 等待页面加载
        time.sleep(2)
        # 点击English,并点击
        down = self.driver.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[1]/span/div/div[2]/div/div/span[2]/span/div/div/button')
        down.click()
        all_language = self.driver.find_element(By.XPATH, '//span[contains(@id,"menu-item-all")]')
        all_language.click()
        # 提取数据
        for i in range(21):
            self.parse_data()
            self.driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[2]/div/div/span/section[8]/div/div/span/section/section/div[1]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div').click()


        # 滚动条的拖动
        # js = 'scrollTo(0, 500)'
        # # 执行js
        # self.driver.execute_script(js)


if __name__ == '__main__':
    a = PingLun()
    a.run()

