# 题目3：（字符串构成）输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

string = input('请输入字符串：')
alp = 0
num = 0
spa = 0
oth = 0
for item in range(len(string)):
    # 判断字符中遍历的值是否符合条件
    if string[item].isalpha():
        alp += 1
    elif string[item].isalnum():
        num += 1
    elif string[item].isspace():
        spa += 1
    else:
        oth += 1
print('英文字母: {}'.format(alp))
print(f'数字: {num}')
print('空格: %d' % spa)
print('其它: %r' % oth)
