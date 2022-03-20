import scrapy


class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/2980504983']

    def start_requests(self):
        url = self.start_urls[0]
        temp = 'has_recent_activity=1; path=/; expires=Tue, 15 Mar 2022 08:29:55 GMT; secure; HttpOnly; SameSite=Lax_gh_sess=7tBP7S0Or1J3XbnwrSvoxRj6eA0G95Iyr7KABgcv5UjAOE2833qmu8AVh8NRTpSdHr%2BayKVxApJPxSl%2FLPeNoUn5B4F7bp4O7r9MatO%2FhzUgcqhWTnjV18BbmYYw6lVGWc%2FYr3sdOulm6YevhKXzSvDsHNSfA1QELEQyE7wux%2F4DeVw4NIBMPO6kSn11ZlYuLRYuW7oxT9UtlK5wH%2FV9dIbie6x15A1cwYPwvJT7Um3a%2BIwRY3AHq1KMtoyeMqfyVP3FSdN%2BCofj4T883dK0vjZIOe%2F7knx2BP7j4KHgV7HHFVLrDdf0zVH%2FQSVjIv5g99F%2BdDdp3vs3S4xnJcAbzkKtoW4zlo0OdxeXB0KdU%2F3RT1l9JeRcjBcjrycdeYMRBGJ38VRU7LJBZ5W4ecqsSjkrOy4FwscFqB1XNfa7FyyfXMXMP40PzpFHC83v2Vg1Wqd%2B4RE%2B9pjSSk6nLmVP%2FsM2MYf5foytgPI93uT2BkloX7CioDD%2B%2F8YZHxxc7EqiXUoAjWqZhjVP2JHh0h5y07Pduv1WvVRLVj0drTNroQzUWScWQqqYo06xJ5AkHvw4Zd6P7kWbqi%2FlI3RwK25OiI1hQMtn5SUrU4vOtxwOJlsttLbHHIcITrq0uLoZZrBy8B1suo70WWsnNx21QG537v0Sds1eBCf%2Fj8G5ZIE2MY6Jngkx5WIY7VgW2VpVbj8OfkvhoubBaOMpQkozVZMXFiERvRA5Q3mciTczV8kIbK4C6kLOTGPJt4heN5thEs8p--2hMRFtBlFO0nW17V--RC4gRQuCyjCPBo3leoDJSA%3D%3D; path=/; secure; HttpOnly; SameSite=Lax'
        cookies = {data.split('=')[0]:data.split('=')[-1] for data in temp.split(';')}

        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response, *args, **kwargs):
        print(response.xpath('//*[@id="js-pjax-container"]/div[2]/div/div[2]/'
                             'div[2]/div/div[1]/div/ol/li[2]/div/div/div/a/span').extract_first())
        pass
