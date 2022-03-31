import requests
from lxml import etree
import time
import os


class DouBan:
    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250?start=%d&filter='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.'
                          '0.4844.82 Safari/537.36',
            'Cookie': 'viewed="3345554"; bid=lqLi7fK3SEs; gr_user_id=d4c5fe95-3dbc-4f51-9db7-68e2d63fc5aa; __gads=ID=c73563aecd00a46d-22fe81be79d000a8:T=1644129187:RT=1644129187:S=ALNI_MZNnku6ml_BtHPWqbbLhKN9boHagA; ll="118219"; douban-fav-remind=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1648109282%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2gVHLjemlqgDe3kTgOFNN2u8h1tufSrquY5ZswpHO7S-slAxcq_Bv8D4-Zit6Cm-%26wd%3D%26eqid%3D8404a174000023b100000006623c26dd%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1832319861.1644129188.1647496007.1648109282.6; __utmz=30149280.1648109282.6.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1648109282.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=223695111.0.10.1648109282; __utma=223695111.781375509.1647496110.1647496110.1648109282.2; ap_v=0,6.0; _vwo_uuid_v2=DF3922C7F4199B699CC1AEC9606E32E15|135cd1432ea7be8abd81c3c33b63cd64; __yadk_uid=D6RFP7E9IJhQgsfmkV07a6KftNNfS0VN; __utmc=30149280; __utmc=223695111; __utmb=30149280.4.10.1648109282; dbcl2="255321595:BKpTkkCZPnE"; ck=isEN; push_noty_num=0; push_doumail_num=0; ct=y; _pk_id.100001.4cf6=305f3bccb2a7c9d0.1647496110.2.1648113431.1647496135.'
        }

    def run(self):
        # 持久化存储
        dir_filename = f'./douban'
        if not os.path.exists(f'{dir_filename}'):
            os.mkdir(f'{dir_filename}')

        # 1 获取top250的信息节点
        for i in range(0, 1):
            url = f'https://movie.douban.com/top250?start={i*25}&filter='
            print(url)
            response = requests.get(url=url, headers=self.headers).content.decode()
            tree = etree.HTML(response)
            temp = tree.xpath('//ol/li//div[@class="info"]/div/a/@href')
            name_list = tree.xpath('//ol/li/div/div[1]/a/img/@alt')
            # print(name_list)

            # 取出电影id号并获取短评
            for item in range(len(temp)):
                nums = 0
                with open('./douban/short.txt', 'a', encoding='gb18030') as f:
                    f.write(f'\n\n-------------{name_list[item]}------------\n\n')
                print(f'开始爬取{name_list[item]}')

                for i1 in range(100):
                    if nums >2000:
                        break
                    url1 = temp[item] + f'comments?start={i1*20}&limit=20'
                    print(url1)
                    response = requests.get(url=url1, headers=self.headers).content.decode()
                    tree1 = etree.HTML(response)
                    short = tree1.xpath('//div[@id="comments"]//span[@class="short"]/text()')
                    for item1 in short:
                        nums += 1
                        with open('./douban/short.txt', 'a', encoding='gb18030') as f:
                            f.write(f'\n{nums}\n{item1}\n')
                        print(f'{name_list[item]}已经爬取{nums}条')
                    time.sleep(0.5)


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
