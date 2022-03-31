# 题目6
# 递归输出,利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# 方法一
# 用reversed()方法翻转字符串，在遍历
text = 'YanQingYue'
for a in reversed(text):
    print(a, end='')

print(text[1:])


# 方法二
# 通过字符串的下标以及递归的方法来实现
def rec(string):
    if len(string) != 1:
        # 字符串下标是从零开始的，这里的意思是将去掉开头第一个字母的字符串作为下一次
        # 方法调用的字符串
        rec(string[1:])
    # 这里开始有些不理解，我觉得这里应该只输出一次，就是在输出字符串的最后一个字母的时候代码
    # 就应该结束，后面反应过来了，在输出第一个要打印字母后，代码只是完成了最后一个递归的方法，
    # 还要接着运行前面递归的代码，也就是前面剩下的print.
    print(string[0])


rec(input('string here:'))
