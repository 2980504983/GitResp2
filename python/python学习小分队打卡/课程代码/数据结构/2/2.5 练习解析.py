"""
    完成逆波兰表达式的实现

    1 3 + 4 * 5 -
    一加三 乘四 减五 = 11

    2 -
    十一减二 = 9 会保留上一次的最后结果
"""

# 约定俗成:
    # 单下划线表示，不希望别人在类外面使用，但是可以被继承(并不是语法要求)(江湖规矩)
    # 双下划线表示，即不希望在类外使用，也不可以被继承


class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 将列表的最后一个元素作为栈顶
        self._elems = []

    # 判断列表是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]


if __name__ == "__main__":
    st = SStack()
    while True:
        exp = input()
        temp = exp.split(" ")  # 按空格切割
        for item in temp:
            if item not in ["+", "-", "*", "/", "p"]:
                st.push(int(item))
            elif item == "+":
                y = st.pop()
                x = st.pop()
                st.push(x+y)
            elif item == "-":
                y = st.pop()
                x = st.pop()
                st.push(x-y)
            elif item == "*":
                y = st.pop()
                x = st.pop()
                st.push(x*y)
            elif item == "/":
                y = st.pop()
                x = st.pop()
                st.push(x/y)
            elif item == "p":
                print(st.top())

