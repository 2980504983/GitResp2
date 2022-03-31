import settings
import requests
import re
import ThirdWhistleblower


crawl_fail = []


# 通过举报标题列表的长度,获取向所有举报标题的url发起请求
def second_page(data):
    for i1 in range(len(data['title_url'])):

        # 清洗举报标题url
        url2 = 'https://service.account.weibo.com' + data['title_url'][i1]\
            .replace('\\', '')

        # 发送请求获取响应
        response = requests.get(url=url2, headers=settings.headers).content\
            .decode('unicode-escape')

        try:
            # 获取被举报人一共被多少人举报,并存储
            report_nums = re.findall(r'\(共(\d+)人举报\)', response)
            data['report_nums'] = report_nums
            # print(len(report_nums))
            # print(report_nums)
        except Exception as e:
            crawl_fail.append({'report_nums': url2})
            # print(e)

        try:
            # 获取详情文章的url
            article_url = re.findall(r'详情：*\s*<a .*? href="(.+?)"', response)[0]
            data['article_url'] = article_url
            # print(article_url)
            # print(len(article_url))
            # print(article_url)

        except Exception as e:
            crawl_fail.append({'article_url': url2})
            # print(e)
            # print(url2)
            # print(response)

        try:
            # 获取被举报人主页url
            url_by = data['by_url'][i1].replace('\\', '')
            data['url_by'] = url_by
            # print(len(url_by))
            print(url_by)

        except:
            crawl_fail.append({'url_by': url2})

        # 爬取第三页面数据
        ThirdWhistleblower.third_page(data)

    try:
        print(crawl_fail[0])
    except:
        print(f'第{data["page1"]+1}页，完美正确爬取')
    else:
        print('crawl-fail:', crawl_fail)
    print(data)
    return






