# 题目4：斐波那契数列。
# 0,1,1,2,3,

z = int(input('请输入数列的项数：'))


def sum1(n):
    """返回项数所对应的值"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sum1(n-1) + sum1(n-2)


print(sum1(z))


def sum2(n):
    """返回n项斐波那契数"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 定义斐波那契数列前两个的值
    a = [0, 1]
    # 将数列末尾两个数相加，并将该值返回到列表
    # b 为相加的次数
    for b in range(2, n+1):
        a.append(a[-1] + a[-2])
    return a


print(sum2(z))
