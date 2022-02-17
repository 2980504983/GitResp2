"""
    文件读操作
    当文件很大时，一次读取会占用大量内存，可以分块读取(循环读)
"""

# 打开文件
f = open("0 被操作的文件.py", "r")


while True:
    data = f.read(2)  # 每次最多读2个字符
    if not data:  # 当文件读完后，会返回空，如果不跳出循环，会死循环，什么都看不到
        break
    print(data)


# 关闭文件
f.close()
