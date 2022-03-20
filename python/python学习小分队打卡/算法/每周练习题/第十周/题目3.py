# 题目3：三数排序
# （ 输入3个数a,b,c，按大小顺序输出。）

# 方法一
a3 = int(input('请输入数字a：'))
b3 = int(input('请输入数字b：'))
c3 = int(input('请输入数字c：'))

d3 = [a3, b3, c3]
d3.sort(reverse=True)
for item in d3:
    print(item, end=',')


# 方法二
# 这种方法作者经常用，应该是一种比较经典的算法
raw = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)

raw2 = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw2.append(x)
print(sorted(raw2))
