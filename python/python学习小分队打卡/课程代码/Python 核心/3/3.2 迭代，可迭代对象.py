"""
    迭代:
        每一次对过程的重复称为一次"迭代"，每次迭代的结果，会作为下一次迭代的初始值。

    迭代原理:
        面试题:
            for循环的原理是什么?
            答: 1获取迭代器 2循环获取下一个元素 3遇到异常停止迭代

            可以被for的条件是什么?
            答: 能被for的对象必须具备__iter__方法，也就是必须有迭代器
            答: 能被for的对象是可迭代对象


        1 获取迭代器:
            iterator = list01.__iter__()

        2 循环获取下一个元素:
            while True:
                try:
                    item = iterator.__next__()
                    print(item)

            3 遇到异常停止迭代
            except StopIteration:
                break  # 退出循环

    可迭代对象:
        具有__iter__函数的对象，可以返回

"""

# 可迭代对象 -- 容器
list01 = [43, 45, 45, 1]
# 迭代过程
# for item in list01:
#    print(item)

# 上面过程的实质
iterator = list01.__iter__()  # 获取迭代器
print(iterator)

while True:  # 循环获取下一个元素
    try:
        item = iterator.__next__()
        print(item)

    except StopIteration:  # 遇到异常停止迭代
        break  # 退出循环
