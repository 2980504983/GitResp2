import settings
import requests
import re
import SecondReportTitle

# 管理中心url
url = 'https://service.account.weibo.com/index?type=5&status=0&page=%d'


def first_page():
    for i in range(0, 5):
        # 拼接翻页url
        url1 = url % i
        # 向管理中心发起请求获取响应
        response1 = requests.get(url=url1, headers=settings.headers).content\
            .decode('unicode-escape')

        # 提取管理中心里每个被举报人的拜访数
        visit_counts = re.findall(r'<td>(\d+)<\\/td>', response1)

        # 获取所有被举报人的url
        by_url = re.findall(r'a href="(.+)"\starget="_blank".+\n\s\s<td>\d+',
                            response1)

        # 获取所有被举报时间
        report_time = re.findall(r'<td>(.+)<\\/td>\n\t<\\/tr>', response1)

        # 获取所有举报标题url
        title_url = re.findall(r'class="m_table_tit"\s*><a\s*href="(.+)"+?\s',
                               response1)

        data_dict = {'visit_counts': visit_counts,
                     'by_url': by_url,
                     'report_time': report_time,
                     'title_url': title_url,
                     'page1': i
                     }

        # print(response1)
        #
        # print(len(by_url))
        # print(by_url)
        #
        # print(len(visit_counts))
        # print(visit_counts)
        #
        # print(len(report_time))
        # print(report_time)
        #
        # print(len(title_url))
        # print(title_url)

        # 举报标题界面数据爬取
        SecondReportTitle.second_page(data_dict)


if __name__ == "__main__":
    first_page()
