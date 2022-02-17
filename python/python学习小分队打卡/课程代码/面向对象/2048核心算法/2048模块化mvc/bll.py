"""
    游戏逻辑控制器
"""
from model import *
import random


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map1 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map1

    def __zero_to_end(self):
        """
            零元素移至末尾
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        # 将中间的零元素移到末尾
        self.__zero_to_end()

        for i in range(len(self.__list_merge)-1):
            if self.__list_merge[i] == self.__list_merge[i+1]:
                self.__list_merge[i] += self.__list_merge[i+1]
                del self.__list_merge[i+1]
                self.__list_merge.append(0)

    def __move_left(self):
        for line in self.__map1:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for line in self.__map1:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __move_up(self):
        self.__spuare_matrix_transpose()
        self.__move_left()
        self.__spuare_matrix_transpose()

    def __move_down(self):
        self.__spuare_matrix_transpose()
        self.__move_right()
        self.__spuare_matrix_transpose()

    def __spuare_matrix_transpose(self):
        for c in range(1, len(self.__map1)):
            for r in range(c, len(self.__map1)):
                self.__map1[r][c-1], self.__map1[c-1][r] = self.__map1[c-1][r], self.__map1[r][c-1]

    def move(self, dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    def generate_new_number(self):
        # 获取所有空白位置
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return

        loc = random.choice(self.__list_empty_location)
        self.__map1[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(loc)

    def __get_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map1)):
            for c in range(len(self.__map1[r])):
                if self.__map1[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map1)):
            for c in range(len(self.__map1[r])-1):
                if self.__map1[r][c] == self.__map1[r][c+1] or self.__map1[c][r] == self.__map1[c+1][r]:
                    return False
        return True


# ----------------------------------测试代码--------------------
if __name__ == "__main__":
    controller = GameCoreController()
    print(controller.map)
