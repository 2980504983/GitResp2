# 题目6：（做函数）
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…
# +1/n

# 方法一
def func6():
    a6 = int(input('请输入数字：'))
    s6 = 0
    d6 = 2
    if a6 % 2 == 0:
        for i6 in range(a6//2):
            s6 += 1/d6
            d6 += 2
        print(s6)
    else:
        for item in range(a6//2):
            s6 += 1/(d6-1)
            d6 += 2
        print(s6)


func6()


# 方法二
def peven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1.0 / i
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1.0 / i
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == '__main__':
    n = int(input('input a number: '))
    if n % 2 == 0:
        sum = dcall(peven, n)
    else:
        sum = dcall(podd, n)
    print(sum)
