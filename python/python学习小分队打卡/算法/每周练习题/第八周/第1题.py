# 第八周
# 题目1：（随机数）输出一个随机数。
# 题目2：（按位与）学习使用按位与 & 。
# 题目3：（按位或）学习使用按位或 | 。
# 题目4：（按位异或）学习使用按位异或 ^ 。
# 题目5：（位取反、位移动）取一个整数a从右端开始的4〜7位。
# 题目6：（按位取反）学习使用按位取反~。
# 题目7：（画圈）画图，学用circle画圆形。

# python基础学习
# 看完第一章并完成第一章的检查点

# 爬虫学习
# 看完第一，二章


# 题目1：（随机数）输出一个随机数。

# 方法一
# random 模块中的 randint 方法
# 格式 random.randint(a, b)
import random
print(random.randint(1, 100))


# 方法二
# random.random()括号里不需要填入参数，返回一个大于等于0小于1的浮点数
print(random.random())


# 方法三
# random.uniform(a, b)返回a与b之间的一个浮点数
print(random.uniform(1, 100))
