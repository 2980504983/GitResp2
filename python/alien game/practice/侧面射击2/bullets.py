import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, ai_game):
        """初始化子弹信息"""
        # 继承超类
        super().__init__()

        # 接入屏幕信息
        self.screen = ai_game.screen

        # 接入设置信息
        self.settings = ai_game.settings

        # 在坐标（0， 0）处创建子弹外接矩形实例
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        # 设置正确的子弹位置
        self.rect.midright = ai_game.ship.rect.midright

        # 设置子弹颜色
        self.color = self.settings.bullet_color

        # 以小数方式存储子弹的很坐标
        self.x = float(self.rect.x)

    def update(self):
        """让子弹飞"""
        self.x += self.settings.bullet_speed
        # 更新子弹的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """显示子弹图像"""
        pygame.draw.rect(self.screen, self.color, self.rect)
