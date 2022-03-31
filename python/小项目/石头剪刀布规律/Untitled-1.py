"""
探究多人石头剪刀布的规律，寻找怎么出能赢的可能性最大

    1  5 人， 且有前一盘作为数据基础，1代表石头， 2代表剪刀， 3代表布

    2  做出假设，假设第一盘的数据，为11123， 下一盘出什么最可能赢呢？
       石头 剪刀 还是 布， 设计模型让这样的对局重复10000次，分别记录下一盘
       石头 剪刀 布的胜率

    3 写出 剪刀石头布的逻辑，让石头剪刀布重复进行，当有对局结果为11123，就记录下一局石头剪刀布的赢得情况，并分别记录

    4 模型设计：写一个剪刀石头布逻辑类(接收玩家对局信息，并返回结果) 写一个玩家生成类(接收玩家数量，随机生成各玩家的出手情况并生成列表)
                写一个数据限制类，只让11123下一局的数据传递给逻辑类，写一个结果存储与输出类(接收每局结果并记录，接收对局数量，最后返回结果)
"""
import random


class JianShiBu:
    def panduan(self, player_data):
        """
        判断胜负，并返回结果
        """
        if player_data:
            # 当对局信息中没有石头
            if 1 not in player_data:
                if 2 in player_data:
                    if 3 in player_data:
                        return 2
                    else:
                        return 0
                else:
                    return 0
            # 当对局信息中没有剪刀
            if 2 not in player_data:
                if 1 in player_data:
                    if 3 in player_data:
                        return 3
                    else:
                        return 0
                else:
                    return 0
            # 当对局信息中没有布
            if 3 not in player_data:
                if 2 in player_data:
                    if 1 in player_data:
                        return 1
                    else:
                        return 0
                else:
                    return 0
                pass
            # 当对局信息中剪刀石头布都有
            if 1 in player_data and 2 in player_data and 3 in player_data:
                return 0

class Data_bron:
    def __init__(self) -> None:
        self.data = []

    def data_get(self, player_num):
        for i in range(player_num):
            self.data.append(random.randint(1,3))
        return self.data
        pass

class Data_set:
    def __init__(self) -> None:
        self.flag = False
        pass
    def data_set(self, data, list):
        if self.flag:
            self.flag = False
            return data
        if data.sort() == list.sort():
            self.flag = True

class Ruselt:
    def __init__(self) -> None:
        self.data_maker = Data_bron()
        self.data_seter = Data_set()
        self.ruselt_helper = JianShiBu()

        self.shitou = 0
        self.jiandao = 0
        self.bu = 0
        self.pingju = 0

    def get_ruselt(self, nums, player_nums, list):
        for i in range(nums):
            self.data_maker.data = []
            data = self.data_maker.data_get(player_nums)
            result = self.ruselt_helper.panduan(self.data_seter.data_set(data, list))
            if result == 0:
                self.pingju += 1
            elif result == 1:
                self.shitou += 1
            elif result == 2:
                self.jiandao += 1
            elif result == 3:
                self.bu += 1
        print(f'平局 [{self.pingju}]\n石头赢 [{self.shitou}]\n剪刀赢 [{self.jiandao}]\n布赢 [{self.bu}]')
        pass


a = Ruselt()
a.get_ruselt(100, 5, [1,1,1,2,3])
