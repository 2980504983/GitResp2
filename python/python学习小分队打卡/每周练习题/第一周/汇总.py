# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

listA = [1, 2, 3, 4]
a, b, c, d = 0, 0, 0, 0

print(f'能组成 {4*3*2} 个不重复且不相同的三位数')
print(f'它们分别是:')
for a in listA:
    a *= 100
    for b in listA:
        b *= 10
        for c in listA:
            if a != 10*b and a != 100*c and b != 10*c:
                d = a + b + c
                print(d)

