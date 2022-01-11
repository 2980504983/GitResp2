"""
    时间处理
"""
import time

# 1. 获取当前时间戳(从1970年1月1日到现在经过的秒数)
print(time.time())


# 2. 时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天)
# 注：时间元组实际上是一个类，只是支持像元组一样操作
print(time.localtime())

# 时间戳和时间元组的相互转换
# 戳转元
sjc = time.time()
sjyz = time.localtime(sjc)
print(sjyz)

# 元转戳
sjyz1 = time.localtime(sjc)
print(time.mktime(sjyz1))


# 时间元组和字符串相互转换
# 元转字
str_time = time.strftime("%Y / %m / %d / %H:%M:%S", sjyz)
print(str_time)

# 字转元
print(time.strptime(str_time, "%Y / %m / %d / %H:%M:%S"))
