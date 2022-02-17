"""
    练习一：定义函数，根据年月日，返回星期数
    练习二： 定义函数，根据年月日，返回天数
    思路：获取生日和当前年月日
         将其全部转换成天数，相减
"""
import time


def day_of_week(year, month, day):
    """
    获取星期数
    :param year:年
    :param month: 月
    :param day: 日
    :return: 星期几
    """
    dict_week = {0: "星期一",
                 1: "星期二",
                 2: "星期三",
                 3: "星期四",
                 4: "星期五",
                 5: "星期六",
                 6: "星期天",
                 }
    time_tuple = time.strptime(f'{year} / {month} / {day}/ {0}:{0}:{0}',
                               "%Y / %m / %d/ %H:%M:%S")
    print(dict_week[time_tuple.tm_wday])


day_of_week(2021, 12, 27)


def get_day(year, month, day):
    time_tuple1 = time.strptime(f'{year} / {month} / {day}/', "%Y / %m / %d/")
    life_second = time.time() - time.mktime(time_tuple1)
    return life_second / 60 / 60 // 24


print(get_day(2003, 10, 4))

