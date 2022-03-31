"""
    flags参数扩展
    1 使用re调用的匹配函数都有flags参数
    2 作用: 扩展丰富正则表达式的匹配功能
    3 常用flag：
        A == ASCII 元字符只能匹配ascii码(美式键盘能打印出来的，字母加一些特殊符号)
        I == I... 匹配忽略字母大小写
        S == DOTAll 使.可以匹配换行
        M == ... ^,$ 匹配每一行的开头和结尾
"""
import re

s = """Hello
北京
"""


# 只能匹配ascii码
# regex = re.compile(r"\w+", flags=re.A)

# 不区分大小写
# regex = re.compile(r"[a-z]+", flags=re.I)

# .可以匹配换行
# regex = re.compile(r'.+', flags=re.S)

# ^,$ 匹配每一行的开头和结尾
regex = re.compile(r'^北京', flags=re.M)

l = regex.findall(s)
print(l)

