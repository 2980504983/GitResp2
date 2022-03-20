# 题目7：暂停一秒输出。 程序分析：使用 time 模块的 sleep() 函数

import time

for item in range(10):
    print(item)
    time.sleep(0.5)
