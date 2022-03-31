import pygame


class Ship():

    def __init__(self, screen):
        """设置飞船的属性"""
        self.screen = screen  # EEEE:忘记写

        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")  # 读取飞船图片
        self.image = pygame.transform.rotate(self.image, -90)  # 将飞船顺时针旋转90°
        self.rect = self.image.get_rect()  # 获取飞船图片外接矩形
        self.screen_rect = screen.get_rect()  # 获取屏幕的外接矩形

        # 设置飞船的位置，将飞船放置在屏幕左侧中间
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # 初始化飞船上下移动属性
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """更新飞船位置"""
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)


