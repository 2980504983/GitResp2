"""
    模拟登录流程:
        1 对点击登录按钮对应的请求进行发送(post请求)
        2 处理请求参数:
            用户名
            密码
            验证码
            其它的防伪参数

    处理动态变化的参数:
        1 去前台页面源码中寻找
        2 如果前台页面没有的话,我们可以基于抓包工具进行全局搜索

    基于百度AI实现爬虫的功能:
        1 图像识别(识别图片)
        2 语音识别/合成(将语音转换成文字/将字符串转换成语音)
        3 自然语言处理(对数据进行特殊处理,例如情感分析,挺强大的)

        使用流程:
            1 登录百度ai
            2 选择想要实现的功能
            3 在实现功能下创建一个app
            4 选择对应的pythonSDK文档进行代码实现

        试一试:
            url = https://duanziwang.com/
            将段子网中的段子内容爬取到本地,然后基于语音合成将段子合成为mp3的音频文件,然后可以自己
            搭建一个web服务器,线上实时播放音频文件

    作业:
        url = https://www.pearyvideo.com/category
        爬取梨视频中最热板块下的短视频数据
"""
from lxml import etree
import requests
from chaojiying import tranformImgCode

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

# 创建一个session对象
session = requests.Session()

# 这里是对主页发请求,猜测这里产生了cookie,因此用session来访问,如果有cookie就会自动存到session
# 对象中
page_text = session.get(url=url, headers=headers).content.decode()

# 解析验证码图片地址
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.cn/'+tree.xpath('//*[@id="imgCode"]/@src')[0]

# 将图片验证码存到本地，这里也发了请求,因此可以也用session对象捕获
img_data = session.get(img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)

# 识别验证码
code_text = tranformImgCode('./code.jpg', 1902)
print(code_text['pic_str'])




login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data = {
    '__VIEWSTATE': 'kbuzDCH8KSRuTenzU/dqrz4oJ+vyAtBC9o2+SuAXrslOsG17mOBbGY32GrW4SJX2JTH'
                   'rP7vbSPL7n8KMiXNhsx3MYq2V6+hvJyLI0fI+O1LVyafUY6tA1mVCazk=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13237038763',
    'pwd': '22330989650',
    'code': code_text['pic_str'],
    'denglu': '登录'
}
print(data)

# 对点击登录按钮发起请求
page_text_login = requests.post(url=login_url, headers=headers, data=data).content.decode()
with open('./gushi.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text_login)



