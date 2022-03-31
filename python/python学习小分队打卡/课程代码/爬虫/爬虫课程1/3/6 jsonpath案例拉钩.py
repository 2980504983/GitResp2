"""
    拉钩网jsonpath实例
"""

import jsonpath
import requests
import json

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

response = requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json',
                        headers=headers)
# 将字符串json转化成json
dict_data = json.loads(response.content)

# 打印a开头的城市名
print(jsonpath.jsonpath(dict_data, "$..A..name"))

# 打印所有城市名
print(jsonpath.jsonpath(dict_data,"$..name"))

