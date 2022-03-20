# 题目7
# 递归求等差数列，有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
# 他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？

# 方法一
# 方法接收第一个人的年龄，第几个人，年龄差，三个参数
def year(first, people_nums, age_cha):
    first += age_cha
    if people_nums > 2:
        year(first, people_nums-1, age_cha)
    else:
        print(first)


year(10, 5, 2)


# 方法二
def age(n):
    if n == 1:
        return 10
    return 2+age(n-1)


print(age(5))
