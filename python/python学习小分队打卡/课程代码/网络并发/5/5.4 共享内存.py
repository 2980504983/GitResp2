"""
    共享内存:
        1 通信原理:
            在内存中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容，
            会覆盖之前的内容
        2 实现方法:
            两种Value(存放单一数值，整数，字符串等) 和 Array(存放一组数值，列表等)
            from multiprocessing import Value,Array
            obj = Value(ctype, data)
            功能: 开辟共享内存
            参数: ctype 表示 共享内存类型(对应C语言)
                 data 共享内存空间初始数据
            obj.value 对该属性的查看和修改就是对共享内存的读写

            obj = Array(ctype, data)  # 数组中的数据必须是一种数据类型(前面ctype的数据类型)
            obj 可迭代
"""