# 题目4：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


# month=int(input('繁殖几个月？： '))
# month_1=1
# month_2=0
# month_3=0
# month_elder=0
# for i in range(month):
#     month_1,month_2,month_3,month_elder=month_elder+month_3, month_1,\
#                                         month_2, month_elder+month_3
#     print('第%d个月共'%(i+1), month_1+month_2+month_3+month_elder, '对兔子')
#     print('其中1月兔：', month_1)
#     print('其中2月兔：', month_2)
#     print('其中3月兔：', month_3)
#     print('其中成年兔：', month_elder)


month = int(input('繁殖第几个月?:'))
month1 = 1
month2 = 0
month3 = 0
month_e = 0
for i in range(1, month+1):
    month1, month2, month3, month_e = month_e + month3, month1, month2, \
                                       month_e + month3
    print(f'第{i}个月共, {month1 + month2 + month3 + month_e}, 对兔子')
