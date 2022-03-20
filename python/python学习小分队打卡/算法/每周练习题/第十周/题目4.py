# 题目4：交换位置
# （输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。）

# 方法一
a4 = True
c4 = 1
d4 = []
while a4:
    b4 = input('请输入数组的第%d个数，输入q退出：' % c4)
    c4 += 1
    if b4 != 'q':
        d4.append(int(b4))
    else:
        a4 = False

"""
1.获取数组最大数和最小数在列表中的位置
2.将最大元素和最小元素分别与第一个和最后一个互换位置
"""
# 获取列表中最大值的位置
h4 = d4[:]
h4.sort()
f4 = h4[-1]
g4 = d4.index(f4)

# 获取列表中的最大值
f4 = h4[0]
i4 = d4.index(f4)

# 将最大元素和最小元素分别与第一个和最后一个互换位置
d4[g4], d4[0] = d4[0], d4[g4]
d4[i4], d4[-1] = d4[-1], d4[i4]
print(d4)


# 方法二
li = [3, 2, 5, 7, 8, 1, 5]

li[-1], li[li.index(min(li))] = li[li.index(min(li))], li[-1]

m = li[0]
ind = li.index(max(li))
li[0] = li[ind]
li[ind] = m

print(li)
