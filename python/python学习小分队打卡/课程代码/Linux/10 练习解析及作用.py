"""
    写入文件:

"""

# 打开文件
f = open("0 被操作的文件.py", 'w')


# 写操作
f.write("hello\n")  # 要换行要自己加\n
f.write("world")


# 将列表写入
l = ['hello world\n', 'hhh']
f.writelines(l)


# 关闭文件
f.close()
