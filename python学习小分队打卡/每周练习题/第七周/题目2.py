# 题目2：矩阵相加，计算两个矩阵相加。

# 方法一
a2 = [[12, 7, 3],
      [4, 5, 6],
      [7, 8, 9]]

b2 = [[5, 8, 1],
      [6, 7, 3],
      [4, 5, 9]]

c2 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
for i in range(len(c2)):
    for j in range(len(c2[0])):
        c2[i][j] = a2[i][j]+b2[i][j]
print(c2)
