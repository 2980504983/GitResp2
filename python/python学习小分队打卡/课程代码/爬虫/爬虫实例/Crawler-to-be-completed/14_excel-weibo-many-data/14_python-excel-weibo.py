import requests
from lxml import etree
from openpyxl import workbook
import re
from jsonpath import jsonpath



# 别这样写
url =


# 创建一个excel文件
wb = workbook.Workbook()






    # 第界面




        # 举报人界面获取粉丝数
        uid = re.findall(r'\d+', url_by)[0]
        print(uid)
        url_by = 'https://weibo.com/ajax/profile/info?uid=' + uid
            # print(url_by)
        # print(url_by)
        response3 = requests.get(url=url_by, headers=headers).content.decode()
        # print(response3)
        followers_count = re.findall(r'"followers_count_str":"(.*?)"', response3)[0]
        print(followers_count)

        # 文章界面获取相关文章信息
        article_id = re.findall(r'\d+/(.+)', article_url[0].replace('\\',''))
        print(article_url[0])
        print(article_id)
        try:
            response4 = requests.get(url=f'https://weibo.com/ajax/statuses/show?id={article_id[0]}', headers=headers).content.decode()
            article_title = re.findall(r'"text_raw":"#(.*?)#', response4)[0]
            # 如果没有匹配到则没有视频
            article_visit = re.findall(r'"online_users":\s*"(.+?)"', response4)
            article_forward = re.findall(r'"reposts_count":\s*(.+?),', response4)[0]
            article_comments_nums = re.findall(r'"comments_count":\s*(.+?),', response4)[0]
            print(article_comments_nums)
            print(article_forward)
            print(article_visit)
            # print(article_title)
        except Exception as e:
            print(e, '当前请求url无法建构')



