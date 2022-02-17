"""
    装饰器
        定义:
            在不改变原函数的调用以及内部代码的情况下，为期添加新功能

        作用: 拦截函数
        装饰器链: 一个方法可以有多个装饰器,顺序由近到远

        好处: 装他就有，不装就没有，装卸非常方便

"""


"""
# 缺点: 增加新功能要改变原有功能，违反开闭原则

# 需要增加的功能
def verify_permissions():
    print("权限验证")


# 已有功能
def enter_background():
    verify_permissions()
    print("进入后台")


def delete_order():
    verify_permissions()
    print("删除订单")
"""


"""
# 函数式编程中的闭包体现开闭原则
# 需要增加的功能
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper


# 已有功能
def enter_background():
    print("进入后台")


def delete_order():
    print("删除订单")


enter_background = verify_permissions(enter_background)
delete_order = verify_permissions(delete_order)

enter_background()
delete_order()

缺点: 每次拦截对已有功能的调用，不科学
"""


"""
def verify_permissions(func):
    def wrapper():
        print("权限验证")
        func()
    return wrapper


# 已有功能
# enter_background = verify_permissions(enter_background)
@ verify_permissions  # 作用和上面一样，拦截对下面方法的调用
def enter_background():
    print("进入后台")


@ verify_permissions
def delete_order():
    print("删除订单")
缺点：如果已有功能参数不统一，就会报错
"""


def verify_permissions(func):
    def wrapper(*args, **kwargs):  # 形参的星号是让多个参数合并为一个元组
        print("权限验证")
        func(*args, **kwargs)  # 实参的星号是让一个元组拆成一个个参数
    return wrapper


# 已有功能
@ verify_permissions
def enter_background(login_id, pwd):
    print("进入后台")


@ verify_permissions
def delete_order():
    print("删除订单")
