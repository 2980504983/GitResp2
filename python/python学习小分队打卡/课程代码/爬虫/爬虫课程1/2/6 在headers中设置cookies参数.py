"""
    在headers中设置cookies:
        1 从浏览器中复制user-agent和cookie
        2 浏览器中的请求头字段和值与headers参数中必须一致
        3 headers请求参数字典中的cookie键对应字符串
    判断带了cookie，和没有带cookie的区别，可以将url复制到无痕浏览中查看，无痕浏览不带cookie，
    发现，不带cookie的标题多了一个.github因此我们只要看标题差异就行了
"""

import requests

url = 'https://github.com/2980504983'

# 构建请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3'
 '6 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',

    "cookie": "_octo=GH1.1.1541760497.1633338056; _device_id=06f4ecc67369ed9c8a31ba99a9664f57; tz=Asia%2FShanghai; has_recent_activity=1; user_session=DAL6cxL-UTxTLTmhhMwT-gO0PnKczvNgr2TMVaKyyPa5Oa31; __Host-user_session_same_site=DAL6cxL-UTxTLTmhhMwT-gO0PnKczvNgr2TMVaKyyPa5Oa31; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=2980504983; _gh_sess=qFdZmxrbqJ3%2FkCoTiaxG1xGSVyops5nzICoX3ZxutyZJjDmAtVOmUTcYVCGvN4Iwt7KWUvOhpiQ%2BXV59sQXPhXzBJtc7F6GoJXzBKaJba264x7s3wgsy%2Bd5%2FzdWi6IG4U1Q8TpdLuEKo%2BA6Uo5V8KQ4kqONZJTnNWfvhQ%2BF17qjLHPPCXklyXCL4tqyHq8sHJWDenptFnhAAvhVyIzS5t%2FG77qYNojaBnBMjwVRI6NVVwKOOAHnnQgwicxkQYTJ%2BykRgLzP7VM814iYrl5hZstGFO9E54tkwVK3VJPu7KMxn785pTh9y%2FV7uFBwQiXGGhHJvc2VVZv43Tah8anNmZ7N8vBHPaf9dQ7HXAp%2BkDeIIr82NPSDEKYeRtg2Wsosfu%2Fw4sZL2ST0ZQKrGLX%2BxzJ5OWpCwZRBCN2YXdbQBTv80ORR6nLNYQ26PVKe9xLLAkGDPamxRSB1YCn2CH739CiOPbI%2BoTAz%2F7h1G0sUwgOJhk4SNH588zyL90yZPWmB3U4X3Tqa0l%2FFqI2XcQcv3gI0zzjdH4s2jSZ82pJNr973rQog0suiHZ%2BbJySFLHpHlYzMaolT45zfdf4gfUMMbVgQNPeafIwo4DvGlpztiLuRcWwFjaEnpiAVH5eYmmLEmQPZwbKZorTLaw9QBSGSWL7eejY6G3w5MKYUEAXQnUAhAyAKGpRh6Cp47E5P2MDyKO1LaEn%2FoyRsmhbw2vIWuFwmTrYzDkMLaDJLjKtAAP6xyNOSrO0qXeE5ALKdD6jeWUG4IGR%2FO4JdkMwC%2FFw8xdX06n20bZOMPZZyeMzMTmKlTecYgprpXN5itCHw%2B9o1JzNhgpF5AAd6Pr2NYGqXiiWuMakl%2BQolya29Axxogmbb3PK4EzLszEJIqD9OPZpfmPIcrVw2wbihuCY3zhP21E5EyrrUGbJA5--lewak8WAPJBkUznN--rQbLU9tJtQ5tl0piJj0JCw%3D%3D"
}

response = requests.get(url, headers=headers)

with open('github_cookies.html', 'wb') as f:
    f.write(response.content)
