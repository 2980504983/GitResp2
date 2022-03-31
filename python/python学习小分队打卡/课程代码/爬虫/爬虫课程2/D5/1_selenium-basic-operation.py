"""
    selenium:
        安装:
            pip3 install selenium
            下载对应浏览器的启动程序,如果驱动程序的路径加到了环境变量中,就不需要在创建
            浏览器对象时指定驱动程序的地址

        selenium爬取动态加载的数据:
            使用page_source属性返回的就是渲染完毕后的页面源码

        动作链ActionChains:
            指的是一系列连续的动作(例如滑动动作)
            1 先导入动作链的包
                from selenium.webdriver import ActionChains

            2 创建一个动作链实例对象:
                action = ActionChains(浏览器对象)

            3 通过动作链实例对象对一个元素进行滑动操作
                action.click_and_hold(div_tag)  # 点击且长按
                # 偏移位置
                for i range (6):
                    # 还有其它移动函数,加上后面的perfrom()才会执行,perfrom()表示让动作链
                    立即执行
                    action.move_by_offset(10, 15).perfrom()

        如何让selenium规避检测:
            有些网站会检测请求是否是selenium发起的

            规避检测的方法:
                使用浏览器托管(使用selenium接管浏览器):
                实现步骤:
                    1 将浏览器驱动程序的目录添加到环境变量中
                    2 打开cmd,在命令行输入命令:
                        chrome.exe --remote-debugging-port=9222 --user-data-dir=
                        '一个空文件夹目录'
                        执行命令后,会打开本机安装好的真实的谷歌浏览器

                    3 执行如下代码
                        from selenium import webdriver
                        from selenium.webdriver.chrome.options import Options

                        chrome_options = Options()
                        chrome_options.add_experimental_option('debuggerAddress',
                        '127.0.0.1:9222')

                        chrome_driver = '驱动程序路径'

                        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
                        print(driver.title)

                        通过上面的代码就创建出了,上面真实浏览器的对象,在编写代码对其进行操作
                        就好了

    无头浏览器(无可视化界面的浏览器):
        1 谷歌无头浏览器(推荐,就是将谷歌浏览器设置无头)
        2 phantomJs




        iframe:
            标签定位时,如果标签存在与iframe下面,就会定位失败
            解决:
                使用switch_to
                eg1:
                    bro.switch_to.frame('iframe标签的id')
"""
from selenium.webdriver import ActionChains
from selenium import webdriver

# 1 实例化一个浏览器对象
bro = webdriver.Chrome()

# 发起请求
bro.get('https://www.baidu.com')

# 假装发起请求
bro.find_element('')

# 在搜索结果页面进行滚轮向下滑动的操作(执行js操作,js注入)
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 关闭浏览器
bro.quit()
