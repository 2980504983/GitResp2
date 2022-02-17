import pygame
import sys


class Bullet:
    """管理并创建子弹的游戏资源"""
    def __init__(self, x, y, screen):
        # 设置子弹的x y值
        self.x = x + 20
        self.y = y - 20
        # 接入外部屏幕信息
        self.screen = screen
        # 导入子弹图片
        self.image = pygame.image.load('E://python/ alien game/'
                                       '飞机大战素材/bullet2.png')

    def move(self):
        # 设置子弹的移动
        self.x += 0.1

    def display(self):
        # 显示子弹图片
        self.screen.blit(self.image, (self.x, self.y))


class Ship:
    """管理并创建ship的游戏资源"""
    def __init__(self, ai_game):
        # 接入外部屏幕信息
        self.screen = ai_game.screen

        # 设置飞船图片
        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")

        # 获取飞船的外接矩形
        self.rect = self.image.get_rect()

        # 给飞船的横纵坐标赋值
        self.x = self.rect.x
        self.y = self.rect.y

        # 设置飞船的初始位置
        self.rect.x = 0
        self.rect.y = 500

        # 飞船起飞标志
        self.moving_up = False
        self.moving_down = False

        # 存储飞机发射的所有子弹
        self.bulletList = []

    def fly(self):
        """让飞船上下飞"""

        # 飞船向上飞
        if self.moving_up and self.y > 0:
            self.y -= 1

        # 飞船向下飞
        if self.moving_down and self.y < 440:
            self.y += 1

        # 更新飞船坐标
        self.rect.y = self.y

    def display_ship(self):
        # 在屏幕上显示飞船图片
        self.screen.blit(self.image, self.rect)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def she_bullet(self):
        new_bullet = Bullet(self.rect.x, self.rect.y, self.screen)
        self.bulletList.append(new_bullet)


class ShipFire:
    """管理 ship fire 的主程序"""
    def __init__(self):
        """初始化pygame并创建游戏资源"""
        # 初始化Pygame
        pygame.init()
        # 设置屏幕信息
        self.screen = pygame.display.set_mode((500, 500))
        # 设置屏幕名称
        pygame.display.set_caption('冲吧！飞船')
        # 创建飞船实例
        self.ship = Ship(self)

    def key_control(self):
        # 按键管理
        for event in pygame.event.get():
            # 按键被按下时激活起飞标志
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    Ship.she_bullet()

            # 按键被松开时关闭起飞标志
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def main_loop(self):
        """游戏的主体循环"""
        while True:
            self.ship.fly()

            # 设置屏幕颜色 必须放在循环体中，否则颜色不会刷新
            self.screen.fill((100, 100, 100))

            # 显示飞船图片
            self.ship.display_ship()

            # 显示屏幕
            pygame.display.flip()


if __name__ == "__main__":
    do_it = ShipFire()
    do_it.main_loop()
