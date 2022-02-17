# 每周练习题
# 题目1：作用域、类的方法与变量，模仿静态变量(static)另一案例（这一题需要去网上搜索，
# 理解静态变量）
# 题目2：矩阵相加，计算两个矩阵相加。
# 题目3：统计 1 到 100 之和。
# 题目4：打破循环，求输入数字的平方，如果平方运算后小于 50 则退出。
# 题目5：函数交换变量，两个变量值用函数互换。
# 题目6：数字比大小，数字比较。
# 题目7：使用lambda来创建匿名函数
# 爬虫学习
# 2.1 HTTP基本原理


# 题目一
# 题目1：作用域、类的方法与变量，模仿静态变量(static)另一案例（这一题需要去网上搜索，
# 理解静态变量）

# 方法一
# 这个方法里很明显可以看出全局变量和局部变量的区别，class dummy num 是局部变量，作用域仅限于这
# 这个类内，而global num 是全局变量作用域包括类内和类外
class Dummy:
    num = 1

    def num1(self):
        print('class dummy num:', self.num)
        print('global num: ', num)
        self.num += 1


n = Dummy()
num = 1
for i in range(5):
    num *= 10
    n.num1()


# 方法二
# 静态变量的定义：静态变量初始化只会被执行一次
# 在方法static里a就是一个静态变量，因为a的初始化只会被执行一次,而在no_static方法里a就不是一个
# 静态变量，因为每次遍历，a都会初始化
def static():
    a = 0
    for s in range(10):
        a += 1
    print(a)


def no_static():
    for s in range(10):
        a = 0
        a += 1
    print(a)


no_static()
static()
