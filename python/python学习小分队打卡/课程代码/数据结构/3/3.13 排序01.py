"""
    各种排序放方法:
        冒泡排序:
        选择排序:
        插入排序:
        快排:

"""


# 冒泡排序
def bubble(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n


def sub_sort(n, low, high):  # 选定数组中的一个基准，将比他小的都甩到左边，比他大的都甩到右边
    # 选定基准
    x = n[low]
    # low 向后， high向前
    while low < high:
        # 后面的输往前放
        while n[high] >= x and high > low:
            high -= 1
        n[low] = n[high]
        # 前面的数往后放
        while n[low] < x and low < high:
            low += 1
        n[high] = n[low]
    n[low] = x
    return low


def quick(n, low, high):
    if low < high:
        key = sub_sort(n, low, high)
        quick(n, low, key-1)
        quick(n, key+1, high)


l=[5,7,4,3,2,1]
quick(l, 0, 5)

print(l)
