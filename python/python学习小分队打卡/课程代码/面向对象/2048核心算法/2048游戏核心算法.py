"""
    2048 游戏核心算法
"""
# 1
# 零元素移至末尾
# 示例：
# [2,0,2,0] --> [2,2,0,0]
# [2,4,0,2] --> [2,4,0,2]

# 2
# 相邻元素合并
# 示例：
# [2,2,0,0] --> [4,0,0,0]
# [2,2,4,0] --> [4,4,0,0]

# 3
# 地图向左移动
map_ = [
    [2, 0, 0, 2],
    [0, 2, 2, 4],
    [4, 4, 4, 4],
    [2, 0, 4, 4]
]

# 4
# 地图上移和下移


def zero_move(a):
    """
        零元素移至末尾
    """
    for i in range(-1, -len(a)-1, -1):
        if a[i] == 0:
            a.remove(a[i])
            a.append(0)


def merge_elements(a):
    # 将中间的零元素移到末尾
    zero_move(a)

    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            a[i] = a[i] + a[i+1]
            del a[i+1]
            a.append(0)


def map_left_move(a):
    for i in a:
        merge_elements(i)


def map_right_move(a):
    for i in a:
        merge_elements(i)
    for i in a:
        i.reverse()


def trans(a):
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]


def map_move_up(a):
    trans(a)
    map_left_move(a)
    trans(a)


def map_move_down(a):
    trans(a)
    map_right_move(a)
    trans(a)

