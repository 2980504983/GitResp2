# 题目2：题目 一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？

# # 网上看的做法
# for i in range(1, 1000):
#     for j in range(1, 1000):
#         for k in range(1, 1000):
#             if (i+100) == j*j and (i+268) == k*k:
#                 print(i)

# # 发现网上的做法显示的很慢，而且貌似要占用很多资源，于是改进
# for A in range(1, 1000):
#     for a in range(1, 1000):
#         if A + 100 == a * a:
#             for b in range(1, 1000):
#                 if A + 268 == b * b:
#                     print(A)

# # 老刘的做法
# jieguo=[]
# for i in range(1000):
#     flag1 = 0
#     f2 = 0
#     x1 = i+100
#     x2 = x1 + 168
#     for m in range(1000):
#         if x1 == m * m:
#             flag1 = 1
#             break
#     for n in range(10):
#         if x2 == (m+n) * (m+n):
#             f2 = 1
#             break
#     if flag1 == 1 and f2 == 1:
#         jieguo.append(i)
# print(f"这个数字是{jieguo}")

# # 看了老刘的做法，发现,如果：a * a == x + 100, b * b == x + 268, 那么(b * b) -
# # (a * a) == 168, 从这里发现，a与b的差值并不大，而且因为b平方数更大，所以当a,b的值改变时,
# # b的数值变化是小于a的，b-a会随着a的增大而减小，而根据a * a == x + 100可以得出a的范围,
# # a至少应该大于或等于10，所以在带入a = 10 得到b * b == 268 b大概等于17 差值为7，
# # 所以不需要遍历一千次去寻找第二个平方数，只需要将前一个平方数加上7的范围内寻找即可。
for A in range(1, 1000):
    for a in range(1, 1000):
        if A + 100 == a * a:
            for b in range(1, 7):
                if A + 268 == (a+b) * (a+b):
                    print(A)

