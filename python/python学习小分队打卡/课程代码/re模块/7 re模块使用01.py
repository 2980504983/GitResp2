"""
    正则表达式匹配原则:
        正确性
        排他性(不多找)
        全面性(不遗漏)

    python re模块:
        regex = compile(pattern, flags = 0)
        功能: 产生正则表达式对象
        参数: pattern 正则表达式
             flags 功能标志位，扩展正则表达式匹配
        返回值: 正则表达式对象
    re模块有三层:
        re：
        regex:
        match:

    详细见re模块结构.jpg
"""

import re

# 目标字符串
s = "Alex:1994, Sunny:1996"
pattern = r'\w+:\d+'  # 正则表达式

# re模块调用findall, 如果正则表达式中有子组，则只能匹配子组中的内容
l = re.findall(pattern, s)
print(l)


# compile 对象调用findall,跟上面的findall没什么区别，但是多两个参数可以指定正则表达式在目标字符串上的作用范围
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)


# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]', s)
print(l)


# 替换目标字符串(将:替换为-，还可以指定最多替换几次)
s = re.sub(r":", '-', s)
print(l)


# 返回的是迭代对象,每个匹配结果，有一个match对象表示，match对象对匹配结果有更丰富的接口已经说明
it = re.finditer(r'\d+', s)
for i in it:
    print(i.group())  # 获取match对象的信息


# 完全匹配一个字符串,用fullmatch向当于在正则表达式前面加了一个^后面加了一个$
m = re.fullmatch(r'\w', s)
print(m.group())


# 匹配某个字符串的开始位置,相当于正则表达式前加一个^
m = re.match(r'\w+?', s)
print(m.group())


# 匹配目标字符串第一个符合内容
m = re.search(r'\d+', s)
print(m.group())


