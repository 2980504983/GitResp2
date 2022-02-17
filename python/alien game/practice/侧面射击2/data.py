class Date:
    """游戏数据"""
    def __init__(self, ai_game):
        # 接入设置信息
        self.settings = ai_game.settings
        # 重置游戏数据
        self.reset_data()

    def reset_data(self):
        """重置游戏数据"""
        # 让玩家的飞船数量恢复
        self.ship_remain = self.settings.ship_limit
