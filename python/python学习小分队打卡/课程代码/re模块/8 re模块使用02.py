"""
    match 对象属性演示
"""
import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)  # 创建regex对象
obj = regex.search('abcdefghi')  # 创建match对象

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)  # 目标字符串结束位置
print(obj.re)  # 正则
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一个子组的组名
print(obj.lastindex)  # 最后一个子组的序列号

# 属性方法
print(obj.span())  # 匹配内容在字符串中的位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  # 生成捕获组字典
print(obj.groups)  # 获取子组对应内容元组
print(obj.group())  # 获取match对象对应内容

