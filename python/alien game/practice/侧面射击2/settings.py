class Settings:
    """侧面射击游戏设置"""
    def __init__(self):
        # 屏幕设置
        self.screen_color = (100, 100, 100)

        # 飞船设置
        self.ship_speed = 5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_speed = 1.5
        self.bullet_number_allowed = 3
        self.bullet_color = (150, 200, 150)

        # 外星人设置
        self.alien_speed = 1.5
        self.drop_speed = 120
        self.direction = 1
        self.alien_range1 = 10
        self.alien_range2 = 15
