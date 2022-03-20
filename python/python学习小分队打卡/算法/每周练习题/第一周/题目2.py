# 题目2：输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入天数：'))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

# 判断月份和日期是否合理
if 0 < month <= 12 and day <= 31:
    sum1 = months[month - 1] + day
    # 判断闰年，平年
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # 如果月份大于2加一天
        if month > 2:
            sum1 += 1
    print(f'{year}年{month}月{day}号是一年的第{sum1}天')
else:
    print('请输入正确的天数或月份')
