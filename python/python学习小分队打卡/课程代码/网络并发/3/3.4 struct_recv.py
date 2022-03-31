from socket import *
import struct

# 和客户端一致
st = struct.Struct('i32sif')

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.213.1', 10325))

# 打开文件
f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)

    # (1, b'lily', 14, 92.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d  %-10s  %d  %.1f\n" % data  # 前面-10(左对齐占十个宽度)和.1(保留一位小数)是格式修饰符
    f.write(info)
    f.flush()  # 刷新缓冲区
