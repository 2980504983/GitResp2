# 题目2：（输出日期）输出指定格式的日期。
import time
import datetime

# 改变h,m,d等的大小写会有不同的输出效果
print(time.strftime('%Y-%m-%d, %H:%m:%S', time.localtime()))

# 输出今天的时间
print(datetime.date.today())

# 自己设定时间，自动以时间格式输出
print(datetime.date(2333, 2, 3))

# 时间的格式化输出，后面的年月日可更改
print(datetime.date.today().strftime('%d/%m/%Y'))

# 先设定一个时间，在通过函数将其更改在输出
day = datetime.date(1111, 2, 3)
day = day.replace(year=day.year+22)
print(day)
