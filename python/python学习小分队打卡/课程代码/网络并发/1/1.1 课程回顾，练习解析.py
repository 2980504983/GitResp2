"""
    前情回顾

    1 二分查找
    2 IO操作: IO密集型(速度慢)， 计算密集型(快)
    3 文件读写操作:
        打开文件 open()
        读写文件 read() write()
        关闭文件 close()

"""

# 复制文件

filename = input("File:")

try:
    fr = open(filename, 'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open("file.jpg", 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()