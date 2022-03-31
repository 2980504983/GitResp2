"""
    2048 控制台界面
"""
from bll import *
from model import *
import os


class GameConsoleView:

    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()
        pass

    def __start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()
        pass

    def __draw_map(self):
        os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__draw_map()
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    def __move_map_for_input(self):
        dir = input("请输入方向：")
        dict_dir = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])
            self.__controller.generate_new_number()

