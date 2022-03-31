import pygame


class Settings():
    """所有设置的类"""

    def __init__(self):
        # 设置屏幕的属性
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 设置子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = 0, 0, 0