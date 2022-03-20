import scrapy
import time
#             'timestamp_secret': timestamp_secret


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response, *args, **kwargs):
        # 从登录页面响应中解析出post请求中要提交的数据
        login = '2980504983'
        pwd = '22330989650w'
        timestamp = str(int(time.time()*1000))
        timestamp_secret = response.xpath('//*[@id="login"]/div[4]/form/div/input[11]/@value').extract_first()
        token = response.xpath('//*[@id="login"]/div[4]'
                               '/form/input[1]/@value').extract_first()
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'login': login,
            'password': pwd,
            'trusted_device': '',
            'webauthn - support': 'supported',
            'webauthn - iuvpaa - support': 'unsupported',
            'return_to': 'https://github.com/login',
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            'required_field_ad27': '',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret

        }
        print(post_data)

        # 针对登录url发送post请求
        print(3)
        yield scrapy.FormRequest(
            url='https://github.com/session',
            callback=self.after_login,
            formdata=post_data
        )

    def after_login(self, response):
        print(2)
        yield scrapy.Request('https://github.com/2980504983', callback=self.check_login)


    def check_login(self, response):
        print(2)
        print(response)
        print(response.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[2]/'
                             'div[2]/div/div[1]/div/ol/li[2]/div/div/div/a/span').extract_first())
