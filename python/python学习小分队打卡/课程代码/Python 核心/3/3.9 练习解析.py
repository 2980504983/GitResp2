"""
    练习1:
        从列表[4,5,566,7,8,10]中选出所有偶数
        结果存入另外一个列表
        使用生成器实现
"""
list01 = [4, 5, 566, 7, 8, 10]


def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


re = get_even01()  # 函数会执行，将所有满足的数据存在result中在返回(数据一大就很占内存)
for item in re:
    print(item)


def get_even():
    for item1 in list01:
        if item1 % 2 == 0:
            yield item1


g01 = get_even()  # 函数不执行，生成生成器对象，调用next方法才执行函数里面的代码
                  # 这种方法不占内存，每次获取一个数据就掉一次next方法，满足就返回，下一次返回
                  # 的数据会覆盖上一次的，这种操作也就叫延迟操作或惰性操作

for item in g01:
    print(item)

