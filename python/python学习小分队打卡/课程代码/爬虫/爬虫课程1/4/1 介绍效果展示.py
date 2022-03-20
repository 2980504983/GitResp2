"""
    selenium:
        selenium是一个wed自动化测试工具
        selenium可以简化爬虫的操作，但是效率会大大降低，因此不到万不得已不会使用
        selenium应用范围很广，还可以用作自动化测试等方向
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 如果driver没有添加到环境变量，则需要用driver的绝对路径创建Service对象，再传给service参数
# s = Service(r'D:\软件\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
# driver = webdriver.Chrome(service=s)

# 如果driver添加了环境变量则不需要设置executable_path
driver = webdriver.Chrome()

# 向一个url发起请求
driver.get("http://www.baidu.com/")

# 把页面保存为图片，69版本以上的谷歌浏览器将无法使用截图功能
# driver.save_screenshot("itcast.png")

print(driver.title)  # 打印页面标题

# 退出模拟浏览器
driver.quit()  # 一定要退出，不然会残留进程


# phantomjs无界面浏览器，selenium支持大多数一线主流浏览器，例如谷歌，火狐。360等不支持

# 无头浏览器(无界面浏览器)和有头浏览器(有界面浏览器)
# 通常在开发过程中我们需要查看运行过程中的各种情况所以通常使用有头浏览器(开发有头浏览器)
# 而在项目完成进行部署时，平台采用服务器版操作系统，只有无头浏览器才能正常运行(部署无头浏览器)
