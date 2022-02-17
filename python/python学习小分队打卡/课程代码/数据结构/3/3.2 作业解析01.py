"""
    在一段文字中有各种括号，编写一个接口程序去判断括号是否匹配

    else可以跟for， while， 等搭配，当for执行完后没有遇到break就会执行else的内容，遇到了
    就不会执行
"""


class StackError(Exception):
    pass


# 顺序栈类
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


def match(s):
    st = SStack()
    error = []
    for item in s:
        if item in ("(", "{", "["):
            st.push(item)
        if item in (")", "]", "}"):
            if not st.is_empty():
                temp = st.pop()
                if item == ")" and temp == "(":
                    pass
                elif item == "]" and temp == "[":
                    pass
                elif item == "}" and temp == "{":
                    pass
                else:
                    error.append(temp)
                    error.append(item)
            else:
                error.append(item)
    while not st.is_empty():
        error.append(st.pop())
    return error


def parent(text):
    parens = "()[]{}"
    i, text_len = 0, len(text)

    while True:
        while i < text_len and text[i] not in parens:  # 如果while中有and要判断哪个条件为假
            i += 1

        if i >= text_len:
            return
        else:
            yield text[i], [i]
            i += 1


def ver(text):
    left_parens = "([{"
    opposite = {'}': '}', ']': '[', ')': '('}
    ls = SStack()
    for pr, i in parent(text):
        if pr in left_parens:
            ls.push((pr, i))
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print(f"Unmatching is found at {i} for {pr}")
            break

    else:  # else也可以和for或者while等进行组合使用，当for执行完后没有遇到break就会执行else的内容，遇到了就不会执行
        if ls.is_empty():
            print("All parentheses are matched")

        else:
            d = ls.pop()
            print(f"Umatching is found at {d[1]} for {d[0]}")


