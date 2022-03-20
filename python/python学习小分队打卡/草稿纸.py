import requests


url = 'https://hr.163.com/api/hr163/position/queryPage'
headers = {
    'cookie': '_ntes_nnid=bfb5c73e9506cc36a9e77cf266c28fd5,1636804873348; UM_distinctid=17d192c4f84382-0846b781c488c-57b1a33-144000-17d192c4f85c35; _ntes_nuid=bfb5c73e9506cc36a9e77cf266c28fd5; hb_MA-8E16-605C3AFFE11F_source=www.baidu.com; hb_MA-AC55-420C68F83864_source=www.baidu.com; HR163=0ef3cbbb5182c12805cf24829ed51ad791a5cc59; NTEShrSI=7D9551450A31E7E1CF99D76DB359EAB3.hzabj-new-rms4.server.163.org-8011; userName=; accountType=',
    'lang': 'zh',
    'origin': 'https://hr.163.com',
    'referer': 'https://hr.163.com/job-list.html?workType=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
data = {
    'currentPage': '2',
    'pageSize': '10'
}
response = requests.post(url, headers=headers, data=data)

print(response.content.decode())
