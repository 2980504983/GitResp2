# 题目3：输入三个整数x,y,z，请把这三个数由小到大输出。

x = int(input("请输入x的值："))
y = int(input('请输入y的值：'))
z = int(input('请输入z的值：'))

listA = [x, y, z]
listA.sort()
print(listA)
