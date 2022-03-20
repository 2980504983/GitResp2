# 题目3
# 斐波那契数列II, 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和

# 方法一
items = 20
re = 0
mo = 1
de = 2
for item in range(1, items+1):
    re += de/mo
    de, mo = de + mo, de
    # de = de + mo
    # mo = de - mo
    print(re)
