# 题目5：（杨辉三角）打印出杨辉三角形前十行

# 方法一
# 通过列表来实现，将第一行作为一个列表存储在一个列表中，然后再根据行数创建新的列表，每个列表的值
# 都是有前一个列表的前两个值相加得到。
def yang_hui(num=10):
    l = [[1]]
    for i in range(1, num):
        l.append([(0 if j == 0 else l[i-1][j-1]) + (0 if j == len(l[i-1])
                else l[i-1][j]) for j in range(i+1)])
    return l


print(yang_hui(10))


# 方法二
# map()接收一个函数，和n个列表，并将函数作用与所有列表
# 这题的思路是，通过将一行的前面加上一个零，在在后面加上一个零，并让两行相加。可以运行一下，我把
# 这两行的打印也加上了
def generate(numRows):
    r = [[1]]
    for i in range(1, numRows):
        r.append(list(map(lambda x, y: x+y, [0]+r[-1], r[-1]+[0])))
        # print((list(map(lambda x, y: x+y, [0]+r[-1], r[-1]+[0]))))
        print(r[-1]+[0])
        print([0]+r[-1])
    return r[:numRows]


a = generate(10)
for i in a:
    print(i)

