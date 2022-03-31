import requests
import settings
import re

fail = []
crawl_fail = []

'https://weibo.com/ajax/profile/info?custom=jiangtianyi11'

def third_page(data):
    url_by = data['url_by']
    # print(url_by)
    url = None
    try:
        # 从被举报人url中获取uid
        url = "https://weibo.com/ajax/profile/info?uid=" + re.findall(r'/(\d+)',
                                                                      url_by)[0]
    except:
        url = 'https://weibo.com/ajax/profile/info?custom=' + \
              re.findall(r"[^/]/(.+)", url_by)[0]

    print(url)
    response = requests.get(url=url, headers=settings.headers).content.decode()
    # print(response)

    try:
        followers_count = re.findall(r'"followers_count_str":"(.*?)"', response)[0]
        data['followers_count'] = followers_count
        print(followers_count)
    except Exception as e:
        crawl_fail.append({'flowers_count': url_by})

    try:
        print(crawl_fail[0])
    except:
        print(f'第{data["page1"]+1}页，第三界面完美正确爬取')
    else:
        print('crawl-fail:', crawl_fail)
        fail.append(crawl_fail[0])
        del crawl_fail[0]
