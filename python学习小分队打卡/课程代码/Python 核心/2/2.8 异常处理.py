"""
异常：

    在Python中:
        各种异常的基类都是exception(错误)，所以在Python中异常就可以说是错误，但是在其他一些
        语言中这两个是完全不一样的概念

    定义:
        运行时检测到错误

    现象:
        当异常发生时，程序不会继续向下执行，而是会转到函数的调用语句

"""


def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数:"))
    # ZeroDivisionError
    res = apple_count / person_count
    print(f"每人{res}个苹果")


try:
    # 可能出错的代码
    div_apple(10)
except ValueError:
    print("输入的人数必须是整数")
except ZeroDivisionError:
    print("输入的人数不能是零")
except Exception:
    print("未知错误")

else:
    # 没有出错的代码，不能放在外面，因为放在外面，出错了错误被except后，代码也会执行
    print("没有出错")

finally:
    # 无论是否异常一定会执行的代码
    # 一般写了finally就不用写except和else
    # 作用：不能处理的错误，但是有一定要执行的代码，就定义到finally中
    print("finally")

print("后续逻辑......")
# -----------------------------------------------------------------------------


def get_score():
    while True:
        str_result = input("请输入成绩:")
        try:
            score = int(str_result)
        except:
            continue
        if 0 <= score <= 100:
            return score


print(get_score())
