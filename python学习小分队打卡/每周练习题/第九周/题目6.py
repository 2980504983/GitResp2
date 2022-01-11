# 题目6：（查找字符串）查找字符串

# 方法一
# 通过find()方法查找字符串， 并返回下标
str6 = input('情输入要查找的字符串：')
str6a = '爱国守法，爱岗敬业'


def find_str():
    a6 = str6a.find(str6)
    if a6 == -1:
        print('没有这个字符')
    else:
        print(f'你输入的字符的下标是{a6}')


find_str()
