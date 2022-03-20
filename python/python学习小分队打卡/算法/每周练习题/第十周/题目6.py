# 题目6：报数
# （有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，
# 问最后留下的是原来第几号的那位。）

# 方法一
# 这个方法没写好，写到后面发现把题目搞错了
"""
1.input n的值
2.根据n创建一个1到n的序数列表
3.弹出报到三的元素，重复此操作
4.输出最后留下的数
"""

# n = int(input('请输入n的值：'))
#
# a6 = []
# for i in range(1, n+1):
#     a6.append(i)
#
#
# def fun6(a=1):
#     for s in range(1, len(a6)+1):
#         if s % 3 == 0:
#             print(a6)
#             a6.remove(a6[s-a])
#             a += 1
#     if len(a6) >= 3:
#         fun6()
#
#
# fun6()


# 方法二
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0: k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n: i = 0

    i = 0
    while num[i] == 0: i += 1
    print(num[i])
