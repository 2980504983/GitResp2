# 题目3：暂停一秒输出，并格式化当前时间。（与上周稍微有差别，这个要格式化哈）
# import time
# import datetime

# 方法一
# a = 0
# while a <= 10:
#     """利用time模块中的方法实现格式化本地时间"""
#     print(time.strftime('%Y-%m-%d, %H:%m:%S', time.localtime()))
#     a += 1
#     # 每输出一次数据暂停一秒
#     time.sleep(1)

# 方法二
# a = 0
# while a <= 10:
#     """利用datetime模块可以省去格式化的功夫，但是后面有一串意义不明的小尾巴"""
#     print(datetime.datetime.now())
#     a += 1
#     time.sleep(1)
