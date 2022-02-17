import pygame


class Ship:
    """飞船类"""
    def __init__(self, ai_game):
        """创建飞船的初始资源"""
        # 初始化pygame
        pygame.init()

        # 导入飞船图片
        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")
        # 接入屏幕信息
        self.screen = ai_game.screen

        # 接入设置
        self.settings = ai_game.settings

        # 获取飞船的外接矩形
        self.rect = self.image.get_rect()

        # 设置飞船的初始位置
        self.rect.x = 0
        self.rect.y = 0

        # 活动标志
        self.moving_up = False
        self.moving_down = False

    def display_ship(self):
        """显示飞船图片并传递其大小"""
        self.screen.blit(self.image, self.rect)

    def up_down(self):
        """控制飞船上下"""
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.settings.ship_speed

        if self.moving_down and self.rect.y < 804:
            self.rect.y += self.settings.ship_speed
