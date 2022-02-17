# 题目2：（排序）对10个数进行排序。

# 方法一
# 这种方法通过使用列表的sort()方法（排序的方法）来实现
# 下面用了一个不定长参数，即*args，代表参数长度不确定，可输入的参数数量为 0~n
def px(*args):
    a2 = []
    for item in args:
        a2.append(item)
    a2.sort()
    print(a2)


px(2, 4, 5, 8, 2, 4, 3, 7, 1, 0, -1, -3, -4)


# 方法二
# 这个方法的思路很有意思，通过比较，先后确定列表下标0到9的数字，假设输入了4，3，2，1四个数字
# i = 0
# [4, 3, 2, 1]    # [3, 4, 2, 1]    #[2, 4, 3, 1]    #[1, 4, 3, 2]
# i = 1
# [1, 3, 4, 2]    # [1, 2, 4, 3]
# i = 2
# [1, 2, 3, 4]
raw = []
for i in range(10):
    x = int(input('int%d: ' % i))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]

print(raw)

