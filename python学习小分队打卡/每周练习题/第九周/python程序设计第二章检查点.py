# 2.1 程序员的客户是谁？
"""给程序员钱的人"""
# 2.2 什么是软件需求？
"""就是指软件需要实现什么样的功能，有什么要求"""
# 2.3 什么是算法？
"""把需求按照逻辑顺序排好"""
# 2.4 什么是伪码？
"""伪码并不是真实的代码，往往是对需求实现的概括"""
# 2.5 什么是流程图？
"""流程图是用于设计程序的，是以图形的方式来表示程序中应该完成的处理步骤的手段"""
# 2.6 椭圆，平行四边形，矩形在流程图中表示什么意思？
"""椭圆是启动符和终止符，平行四边形是输入符和输出符， 矩形是处理符"""


# 2.7 编写一条显示你姓名的语句
print("YanQingYue")
# 2.8 编写一条显示下列文本的语句(python's the best)
print("python's the best")
# 2.9 编写一条显示下列文本的语句(The cat said "meow")
print('The cat said "meow"')


# 2.10 什么是变量？
"""变量是代表存储在计算机存储器中某个数值的名字"""
# 2.11 在python语言中，下列变量名那些是非法的，为什么？
""" x 合法
    99bottles 非法 第一个字符只能是字母或下划线
    july2009 合法
    theSales 合法
    r&d 非法 不能使用python中的关键字
    grade_report 合法
"""
# 2.12 变量名Sales 和 sales 是指同一个变量吗？为什么是或为什么不是？
"""不是，python中的变量名是区分大小写的，这是两个不同的变量"""
# 2.13 下面这条赋值语句是有效的还是无效的，为什么？(72 = amount)
"""无效的，变量要在左边"""
# 2.14下列代码将显示出什么？(val = 99 /print('The value is', 'val'))
"""显示The value is val"""
# 2.15 判断变量的类型 (value1 = 99， value2 = 45.9)
"""value1 是 int类型， value2 是 float类型"""
# 2.16 请问下列程序将显示什么内容？(val = 99 / val = 0 / print(val))
"""0"""


# 2.22 怎样才能抑制print函数输出结束是的换行？
"""将print中的end参数改为空格"""
# 2.23 如何改变在传给print函数的各个输出项之间自动显示的字符？
"""可以修改print的sep参数"""
# 2.24 转义字符\n的含义是什么？
"""换行符"""
# 2.25 运算符+被用于两个字符串之间时的功能是什么？
"""将两个字符串相连"""
# 2.26 语句显示的结果是什么？(print(format(65.4321, '.2f')))
"""65.43  其中2表示精确的位数，f表示前面数字的类型"""


# 2.27 什么是有名常量？
"""有名常量指的是一个在程序执行过程中数值恒定不变的名字,通常字母都是大写"""
# 2.28 采用有名常量的三个好处是什么？
"""1增强程序的自解释性，2易于程序的大面积修改，3消除点击错误 """
# 2.29 请编写一条python语句来为10%的折扣定义一个有名常量
"""MM = 0.1"""

# 机器龟的猎户座星群程序代码

# 创建伪码
# 第一步 创建一个界面作为猎户座星系
# 第二步 确定猎户座星系上每颗星的名字和对应的坐标
# 第三步 在每个坐标上创建一个点并显示其名字来代表该星
# 第四步 按照一定顺序将每颗星用线连起来


# 代码实现
# 导入机器龟库
import turtle

# 设置界面的大小为500,600
turtle.setup(500, 600)

# 隐藏海龟的路线
turtle.penup()
# 隐藏海龟本体
turtle.hideturtle()

# 设定各星星的坐标(用的是有名常量)

BETE_X = -70
BETE_Y = 200

SAI_X = -90
SAI_Y = -180

TAK_X = -40
TAK_Y = -20

LAM_X = 0
LAM_Y = 0

MINT_X = 40
MINT_Y = 20

MEI_X = 80
MEI_Y = 180

RIGEL_X = 120
RIGEL_Y = -140

# 把星星画出来并显示名字

# 让海龟去到这个坐标
turtle.goto(BETE_X, BETE_Y)
# 生成一个点
turtle.dot()
# 创建名字
turtle.write('Betegeuse')

turtle.goto(SAI_X, SAI_Y)
turtle.dot()
turtle.write('Saiph')
turtle.goto(TAK_X, TAK_Y)
turtle.dot()
turtle.write('Alnitak')
turtle.goto(LAM_X, LAM_Y)
turtle.dot()
turtle.write('Alnilam')
turtle.goto(MINT_X, MINT_Y)
turtle.dot()
turtle.write('Mintaka')
turtle.goto(MEI_X, MEI_Y)
turtle.dot()
turtle.write('Meissa')
turtle.goto(RIGEL_X, RIGEL_Y)
turtle.dot()
turtle.write('Rigel')

# 连线
turtle.pendown()
turtle.goto(MINT_X, MINT_Y)
turtle.goto(MEI_X, MEI_Y)
turtle.penup()
turtle.goto(MINT_X, MINT_Y)
turtle.pendown()
turtle.goto(TAK_X, TAK_Y)
turtle.goto(SAI_X, SAI_Y)
turtle.penup()
turtle.goto(TAK_X, TAK_Y)
turtle.pendown()
turtle.goto(BETE_X, BETE_Y)

# 保持界面(意义相当于mainloop)
turtle.done()
