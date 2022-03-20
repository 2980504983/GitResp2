# 题目6：（高空抛物）一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def high(x, y):
    if y > 0:
        y -= 1
        return high(float(x/2), y)
    else:
        return x


c = int(input("请输入反弹次数："))
h = int(input('请输入原高度：'))

answer = high(h, c)
an = str(answer)
print(f'第{c}次反弹{an}这么高')
