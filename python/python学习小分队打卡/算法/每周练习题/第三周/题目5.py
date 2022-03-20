# 题目5：（完数）一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

# 方法一
# 遍历1000中的数
for a in range(1, 1000+1):
    # 在每次更换数字a时重置c
    c = 0
    # 在a-1的范围内寻找它的因子b
    for b in range(1, a):
        # 如果b是a的因子且b与a不相等，就让c加上该因子
        if a % b == 0:
            c += b
    # 当因子和c等于a时输出a或c
    if c == a:
        print(a)


# 方法二
# 该方法运用了集合去重的性质
def factor(num):
    # 将输入的值转化成int类型
    target = int(num)
    # 集合存储因子并对其进行去重
    res = set()
    # 寻找在target-1的范围内寻找因子
    for i in range(1, target):
        if target % i == 0:
            # 返回第一个因子
            res.add(i)
            # 返回第二个因子
            res.add(target/i)
    # 返回集合
    return res


# 遍历1000内的数并将其输入factor方法中
for b in range(1, 1001):
    # 如果b等于集合里各数之和减去b,输出b
    if b == sum(factor(b))-b:
        print(b)

