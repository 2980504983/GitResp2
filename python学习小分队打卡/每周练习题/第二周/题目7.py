# 题目7：将一个整数分解质因数。例如：输入90,打印出90=233*5。

target = int(input('输入一个整数：'))
# 该格式表示打印内容并不是完整的，后面还可以接同样的格式补充内容
print(target, ' = ', end='')

if target < 0:
    target = abs(target)
    print('-1*', end='')

flag = 0
if target <= 1:
    print(target)
    flag = 1


while True:
    if flag:
        break
    for i in range(2, int(target+1)):
        if target % i == 0:
            print("%d" % i, end='')
            if target == i:
                flag = 1
                break
            print('*', end='')
            target /= i
            # break
