"""
    http响应(response)
        1 响应格式:
            响应行，响应头，空行，响应体

            响应行:
                反馈的响应情况 (HTTP/1.1响应版本，200响应码，ok附加信息)

                    响应码:
                        1xx 提示信息，表示请求被接收
                        2xx 响应成功
                        3xx 响应需要进一步操作，重定向
                        4xx 客户端错误
                        5xx 服务器错误
            响应头:
                对响应内容的描述， 也是一个个键值对

            空行:

            响应体:
                响应的主体内容
"""

# 使一个服务器的信息能够被浏览器解析，发送的信息就要遵循http协议
from socket import *

s = socket()
s.bind(('192.168.213.1', 10325))
s.listen(3)

c, addr = s.accept()

print(f"Connect from {addr}")
data = c.recv(1024)
print(data)

# 响应行， 响应头， 空行， 响应体
response = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""
c.send(response.encode())  # 发送响应内容
c.close()

# 在浏览器的网址中输入 192.168.213.1:10325 即可连接服务器
