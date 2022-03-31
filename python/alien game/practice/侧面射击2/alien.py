import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """管理外星人资源的类"""
    def __init__(self, ai_game):
        """初始化资源"""
        # 继承超类
        super().__init__()

        # 初始化pygame
        pygame.init()

        # 接入屏幕信息
        self.screen = ai_game.screen

        # 接入设置信息
        self.settings = ai_game.settings

        # 导入外星人图片
        self.image = pygame.image.load('E://python/ alien game/'
                                       '飞机大战素材/20.1.jpg')

        # 获取外星人的外接矩形
        self.rect = self.image.get_rect()

        # 设置外星人的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 以小数形式存储外星人的纵坐标
        self.y = float(self.rect.x)

    def update(self):
        """上下移动的外星人"""
        self.y += self.settings.alien_speed * self.settings.direction

        # 更新纵坐标
        self.rect.y = self.y

    def edge_detection(self):
        """检测外星人是否碰到屏幕边缘，如果是返回Ture"""
        if self.rect.y >= 804 or self.rect.y <= \
                0:
            return True
