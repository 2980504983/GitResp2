# def line(long):
#     c1 = 1
#     for a1 in range(long, 0, -1):
#         print(' '*a1, end='')
#         print('*'*c1)
#         c1 += 2
#     for b1 in range(0, long+1):
#         print(' '*b1, end='')
#         print('*'*c1)
#         c1 -= 2
#
#
# line(75)
#
#
# def lx(length):
#     c = 1
#     for a in range(length, 0, -1):  # 打印上半部分的三角形
#         print(' '*a, end="")
#         print('*', end="")
#         print(' '*(c-1), end="")
#         if a != length:
#             print('*')
#         else:
#             print("")
#         c += 2
#     c -= 4
#     for b in range(2, length+1, 1):  # 打印下半部分的倒三角形
#         print(' ' * b, end="")
#         print('*', end="")
#         print(" "*(c-1), end="")
#         if b != length:
#             print("*")
#         else:
#             print("")
#         c -= 2
#
#
# lx(10)
