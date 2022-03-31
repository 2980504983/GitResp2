# 练习：定义my_zip实现下列功能
list02 = ["孙悟空", "猪八戒", "唐僧", '沙僧']
list03 = [101, 102, 103, 104, ]
for item in zip(list02, list03):
    print(item)


def my_zip(*args):
    for i in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[i])
        yield tuple(list_result)


for item2 in my_zip(list02, list03):
    print(item2)
