"""
    js2py的使用
"""

import js2py
import requests


# 创建js执行环境
context = js2py.EvalJs()

# 加载js文件,将要用到的js文件爬取下来,并加载到js执行环境中,内容要转成字符串,如果少的话,也可以复制粘贴
headers = {
}
big_js = requests.get('url', headers=headers).content.decode('utf-8')
context.execute(big_js)

# 向js环境中添加变量
context.n = {'text': 'python'}
print(type(context.n))
