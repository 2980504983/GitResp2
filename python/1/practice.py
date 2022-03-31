# def spin_words(sentence):
#     a=len(sentence)
#     if a>=5:
#         print(sentence.(spin_words(sentence)))
#         pass
#     else:
#         print(sentence)
#         pass
#     pass
# spin_words('kasjdklasjd')



# def spin_words(sentence):
#     # 将句子中单词转化为序列，以空格分隔
#     s = sentence.split(' ')
#     #根据序列的索引，设定循环，range(len(s))获取的为序列的索引
#     for i in range(len(s)):
#         #获取到对应索引的字符串
#         t = s[i]
#         #判断字符长度是否大于5
#         if len(t) >= 5:
#             #将字符反向排列，得到新的字符串，t[::-1]是字符串切片功能逆转字符串
#             t1 = t[::-1]
#             #将序列中的原字符替换为新的字符
#             s[i] = t1
#     #组成新的句子
#     sentence = ' '.join(s)
#     print(sentence)
#     return sentence
# #调用方法
# spin_words('Welcome to here')



        # print(info1)
# info = ' '.join(info1)
# print(info)

# def spin_words(sentence):
#     a=sentence.split(' ')
#     b=len(a)
#     for i in range(b):
#         i1=a[i]
#         if len(i1)>=5:
#             i2=i1[::-1]
#             a[i]=i2
#             pass
#         pass
#     sentence=' '.join(a)
#     print(sentence)
#     pass
# spin_words("This is a testaskjdk")



def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
print(spin_words('abcdef'))


def asjd(sentence1):
    return ' '.join([x[::-1] if len(x) >=5 else x for x in sentence1.split(' ')])
