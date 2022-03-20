# 题目5
# 递归求阶乘,利用递归方法求5!。

# 方法一
# 普通形式
def sum3(nums):
    if nums > 0:
        return nums * sum3(nums-1)
    else:
        return 1


print(sum3(5))


# 方法二
# 特殊的格式实现(三元运算)
#
def factorial(n):
    return n*factorial(n-1) if n > 1 else 1


print(factorial(5))


# 三元运算的一些格式
# def aa():
#     a = 0
#     b = 1
#     c = 2
#     if a > b:
#         print(a)
#     else:
#         return c
# 转化成三元运算的格式(return可以省略)
a = 0
b = 1
c = 2
print(a) if a > b else c

# 三元运算的嵌套
if a > b:
    print(a)
else:
    if b > c:
        print(b)
    else:
        print(c)


print(a) if a > b else print(b) if b > c else print(c)
