# 题目4：（有序列表插入元素）有一个已经排好序的数组。现输入一个数，
# 要求按原来的规律将他插入数组中。

# 方法一
# 1.append() 向列表末尾增加一个元素。
# 2.extend() 向列表末尾增加多个元素。
# 3.insert()在列表中的任意位置增加一个元素。格式：list.insert(索引, 要添加的元素)
# 这种方法可以检测列表是递增还是递减，在按规律插入数字

a4 = [2, 1, 1, 1]


def pd(s, a):
    if s[0] <= s[-1]:
        b = 0
        for s4 in s:
            if a <= s4:
                s.insert(b, a)
                break
            elif a > s[-1]:
                s.insert(len(s)+1, a)
                break
            b += 1
        print(s)

    elif s[0] > s[-1]:
        b = 0
        for s4 in s:
            if a >= s4:
                s.insert(b, a)
                break
            elif a < s[-1]:
                s.insert(len(s) + 1, a)
                break
            b += 1
        print(s)


pd(a4, 0)


# 方法二
# 这种方法的思路是先将要插入的元素直接添加进列表，然后在给列表排序
# 把元素a和列表里的元素从前往后比较，当发现某一元素大于或等于元素a，就从这个元素开始，将后面的
# 元素逐个往最后扔
lis = [1, 10, 100, 1000, 10000, 100000]
n = int(input('insert a number: '))
lis.append(n)
for i in range(len(lis)-1):
    if lis[i] >= n:
        # 这一步的意思是将列表的最后一个元素和第j个元素互换位置
        for j in range(i, len(lis)):
            lis[j], lis[-1] = lis[-1], lis[j]
        break
print(lis)

