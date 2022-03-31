"""
    selenium 常用配置:
        chrome设置无头模式:
            1 实例化配置对象
             options = webdriver.ChromeOptions()

            2 配置对象开启无界面模式的命令
            options.add_argument("--headless")

            3 配置对象添加禁用gpu命令
            options.add_argument(--disable-gpu)

            4 实例化带有配置对象的driver对象
            driver = webdriver.Chrome(options=options)

        设置代理:
            确定，更换ip代理，必须重新启动浏览器，也就是重新创建driver
            1 实例化配置对象:
                options = webdriver.ChromeOptions()
            2 配置对象添加使用代理ip的命令
                options.add_argument('--proxy-server=http://代理ip:代理端口')
            3 实例化带有配置对象的driver对象
                driver = webdriver.Chrome(options=options)

        selenium替换user-agent:
            1 实例化配置对象:
                options = webdriver.ChromeOptions()
            2 配置对象添加替换UA的命令
                options.add_argument('--user-agent="要更换的user-agent"')
            3 实例化带有配置对象的driver对象:
                driver = webdriver.Chrome(options=options)
"""
from selenium import webdriver

url = 'https://www.baidu.com'

# 设置chrome为无头模式
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=options)

# driver.get(url)
# driver.save_screenshot('百度到此一游.png')


# 设置代理ip
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://183.240.14.171:10011')
driver = webdriver.Chrome(options=options)

driver.get(url)
