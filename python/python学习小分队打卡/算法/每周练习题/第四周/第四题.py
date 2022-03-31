# 题目4
# 阶乘求和,求1+2!+3!+…+20!的和。

# 方法一
# 用遍历的方法求解，思路是：先将每个数自己的阶乘求出来，再把它们相加
# 遍历1到nums，在将数值num0再次遍历，求出num0的阶乘，在将其全部相加
def sum1(nums):
    b = 1
    a = 0
    for num0 in range(1, nums+1):
        for num1 in range(1, num0+1):
            b *= num1
        a += b
        b = 1
    print(a)


sum1(3)


# 方法二
# 用递归的方法来实现
# def sum2(nums):
#     b = 1
#     a = 0
#     for num0 in range(1, nums+1):
#         b *= num0
#     a += b
#     if nums-1 > 0:
#         sum2(nums-1)
#     print(a)
#
#
# sum2(3)


# 方法三
# 思路很好，先把阶乘化简在求值（有点难理解）
res = 1
for i in range(3, 1, -1):
    res = i * res+1
    print(res)
