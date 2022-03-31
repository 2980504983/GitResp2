import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对子弹进行管理的类"""

    def __init__(self, settings, screen, ship):
        """在飞船出创建一个子弹对象"""

        # 继承父类的属性
        super().__init__()

        self.screen = screen

        # 在（0， 0）处创建一个子弹的矩形，再设置其准确位置
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """更新子弹位置"""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)