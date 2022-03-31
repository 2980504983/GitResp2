"""
    爬取斗鱼直播直播间信息
    unknow error 一般就是需要下拉
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class DouYu:
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def parse(self):
        # 这个很关键，要等待3秒，等信息加载完毕在获取，不然后面会报错
        time.sleep(3)

        room_list = self.driver.find_elements(By.XPATH, '//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        # print(len(room_list))

        data_list = []
        # 遍历房间列表，从每一个房间节点中获取数据
        for room in room_list:
            temp = {}
            # 这里xpath直接基于上次xpath写就行了
            temp['title'] = room.find_element(By.XPATH, './a[1]/div[2]/div[1]/h3').text
            temp['type'] = room.find_element(By.XPATH, './a[1]/div[2]/div[1]/span').text
            temp['owner'] = room.find_element(By.XPATH, './a[1]/div[2]/div[2]/h2').text
            temp['num'] = room.find_element(By.XPATH, './a[1]/div[2]/div[2]/span').text
            # 后面的图片定位不到
            # temp['img'] = room.find_element(By.XPATH,'./a/div[1]/div[1]/picture/img').get_attribute('src')
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            print(data)


    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)
        while True:
            # parse
            data_list = self.parse()
            # save
            self.save_data(data_list)

            # next
            try:
                el_next = self.driver.find_element(By.XPATH, '//*[contains(text(), "下一页")]')
                print(el_next)
                el_next.click()
            except:
                break


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()
