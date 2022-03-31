from socket import *
import struct


# 定义数据格式
st = struct.Struct('i32sif')  # i表示整形

# udp套接字
s = socket(AF_INET, SOCK_DGRAM)
addr = ('192.168.213.1', 10325)

while True:
    print('==================================')
    id_ = int(input('ID:'))
    name = input('name:').encode()
    age = int(input("Age:"))
    score = float(input("Score:"))

    # 打包数据并发送
    data = st.pack(id_, name, age, score)
    s.sendto(data, addr)