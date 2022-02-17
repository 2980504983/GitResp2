import pygame

import sys


class Hero:
    """飞船属性"""
    def __init__(self, ai_game):
        # 实例接入设置
        self.screen = ai_game.screen
        # self.screen_rect = ai_game.screen.get_rect()

        # 设置飞船的图片并获取飞船的外接矩形
        self.image = pygame.image.load('飞机大战素材/10.1.jpg')
        self.rect = self.image.get_rect()

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 给飞船坐标赋值
        self.x = self.rect.x
        self.y = self.rect.y

    def fly(self):
        if self.moving_right and self.x < 440:
            self.x += 0.1

        if self.moving_left and self.x > 0:
            self.x -= 0.1

        if self.moving_up and self.y > 0:
            self.y -= 0.1

        if self.moving_down and self.y < 440:
            self.y += 0.1

        # 更新坐标
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """显示飞船图片"""
        self.screen.blit(self.image, self.rect)


class Main:
    def __init__(self):

        # 初始化pygame
        pygame.init()

        # 创建并设置屏幕
        self.screen = pygame.display.set_mode((500, 500))

        # 设置屏幕名称
        pygame.display.set_caption('火箭')

        # 创建飞船实例
        self.ship = Hero(self)

    def main_loop(self):
        """主循环"""
        while True:
            # 获取鼠标和键盘的信息
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                    elif event.key == pygame.K_q:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.moving_down = False

                    pass

            # 刷新飞船所在位置
            self.ship.fly()

            # 设置背景颜色
            self.screen.fill((51, 2, 3))
            # 显示飞船图片
            self.ship.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    AI = Main()
    AI.main_loop()
