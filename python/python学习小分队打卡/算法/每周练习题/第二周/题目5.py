# 题目5：判断101-200之间有多少个素数，输出所有素数。
a = 0
listA = []
listB = list(range(101, 201))
for i in range(101, 201):
    for b in range(1, 201):
        if i % b == 0:
            if b != i and b != 1:
                listA.append(i)
                a += 1
print(set(listA))
# c = list(set(listB) - (set(listA)))
# print(c)
