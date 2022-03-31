"""
    url去重:
        hash的运用:
                当我有很多url时,如果直接存储是很浪费空间的，因为url往往非常长,这时，我们可以用hash
                对url进行加密,来减小浪费的空间
        布隆过滤器:
            比hash更省空间

    文本内容去重:
        编辑距离:

        simhash:
            模糊hash

"""

import hashlib


data = 'python'
# 创建hash对象
md5 = hashlib.md5()
# 向hash对象中添加需要做hash运算的字符串
md5.update(data.encode())
# 获取字符串的hash值，16位
res = md5.hexdigest()
print(res)
