"""
    爬取微博热搜50条
"""
import requests
import json
from jsonpath import jsonpath
import re
from lxml import etree
import pymysql


class WeiBoHotSearch:
    def __init__(self):
        self.base_url = 'https://weibo.com/ajax/statuses/hot_band'
        self.headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53'
                '7.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'cookie': 'XSRF-TOKEN=dX3vfh1t3LC5iR5YyK2eKn-G; SUB=_2AkMVRFb9f8NxqwJRmP0dz2rjZY5yygjEieKjGKcmJRMxHRl-yT9jqlMZtRB6PsR4ErlKjinFysL7du5bdm5rk80gNnB7; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFpzJ55kj15F0Txa3TCNWE.; WBPSESS=a_YZA6I5qCR3U8i3Rfvlpp4O4vRhTMjBcq8WcoQvWqRO8rFMkJ_G8S20IWv9zbw7vKyKRaI6yv8xUYw0khtj9QU9GH2zq7uRNck-szWd-HSppd2RcFYqKqaBkCjW2RRr'
        }

    def get_response(self):
        response = requests.get(self.base_url, headers=self.headers)
        return response.content

    def parse_data(self, response):
        # 将json字符串转化为json对象
        data = json.loads(response)

        # 提取标题
        title = jsonpath(data, '$..band_list..word_scheme')

        # 提取url
        url_temp = jsonpath(data, '$..mblog.text')
        url = []
        print(url_temp)

        for item in url_temp:
            try:
                url.append(re.findall(r'<a href=\\?"(.*?)\\?" target', item)[0])
            except:
                print('--------------------------------------')
                print(item)
        url.pop()

        # 提取热度
        raw_hot = jsonpath(data, '$..band_list..num')

        return [title, url, raw_hot]

    def get_read_talk_from_response(self, url_list):
        read_talk_data = []
        # 遍历url获取热搜今日讨论量和今日阅读量
        for url in url_list:
            response = requests.get('https:'+url, headers=self.headers)
            html = etree.HTML(response.content.decode('utf-8'))
            read_talk_data.append(html.xpath('//*[@id="pl_topic_header"]/div[1]/div[2]/div/div[2]/span/text()'))

        return read_talk_data

    def save_to_mysql(self, title, url, raw_hot, read_talk):
        # 连接数据库
        db = pymysql.connect(host="localhost",
                             port=3306,
                             user='qyzw',
                             password='223309',
                             database='WeiBo',
                             charset='utf8')
        # 获取游标
        cur = db.cursor()

        # 执行sql语句,存入按热度顺序存入标题，热度值，url
        # for i in range(0, 50):
        #     try:
        #         sql = "insert into hot_search (title, hot_nums, url) values(%s, %s, %s);"
        #         cur.execute(sql, [title[i], raw_hot[i], url[i]]) # 执行语句
        #         db.commit()  # 提交操作
        #     except Exception as e:
        #         # 出现异常回滚
        #         print(e)
        #         db.rollback()

        # 执行sql语句，存入阅读量，与讨论量

        for j in range(1, 51):
                try:
                    sql = f"update hot_search set read_values=%s, talk_values=%s where id={j};"
                    cur.execute(sql, [read_talk[j][0], read_talk[j][1]])
                    db.commit()
                except Exception as e:
                    print(e)
                    db.rollback()

    def run(self):
        # 创建热搜榜单url
        # 创建headers
        # 发送请求获取响应
        response = self.get_response()

        # 从响应中获取url,标题,热度值
        data = self.parse_data(response)

        # 遍历url，获取响应
        # 从新的响应中获取今日阅读量和今日讨论量
        read_talk_data = self.get_read_talk_from_response(data[1])

        # 在mysql中创建weibo库，建立hot_search表
        # 将数据传入数据库中
        # self.save_to_mysql(data[0], data[1], data[2], read_talk_data)
        # 显示数据
        for i in range(0, 50):
            print(i)
            print(data[0][i], data[1][i], data[2][i], read_talk_data[i][0], read_talk_data[i][1])


if __name__ == '__main__':
    a = WeiBoHotSearch()
    a.run()
