import pygame
from ship import Ship
from settings import Settings
from bullets import Bullet
from alien import Alien
from random import randint
from data import Date
from time import sleep


class SideShit:
    """侧面射击的主程序"""
    def __init__(self):
        """创建初始化资源"""

        # 初始化pygame
        pygame.init()

        # 创建设置信息
        self.settings = Settings()

        # 创建屏幕信息
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 获取屏幕外接矩形
        self.screen_rect = self.screen.get_rect()

        # 创建屏幕名称
        pygame.display.set_caption('侧面射击')

        # 创建飞船实例
        self.ship = Ship(self)

        # 创建子弹编组
        self.bullets = pygame.sprite.Group()

        # 创建外星人编组
        self.aliens = pygame.sprite.Group()

        # 创建外星人
        self.create_aliens()

        # 创建游戏数据实例
        self.data = Date(self)

    def run_game(self):
        """启动游戏"""
        while True:
            # 按键检测并更新飞船坐标
            self.keyboard_detection()

            self.update_aliens()

            # 更新屏幕内容
            self.update_screen()

    def keyboard_detection(self):
        """按键检测并更新飞船坐标"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def fire_bullet(self):
        """发射子弹"""
        # 限制子弹的数量
        if len(self.bullets) < self.settings.bullet_number_allowed:
            # 创建子弹实例
            new_bullet = Bullet(self)
            # 将新创建的子弹添加到子弹编组中
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """更新子弹的位置信息并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.x >= 1550:
                self.bullets.remove(bullet)

        self.bullet_alien_collisions()

    def create_alien(self):
        """创建单个外星人"""
        # 创建外星人实例
        alien = Alien(self)
        # 设置外星人的横坐标
        alien.rect.x = randint(600, 1550)
        # 设置外星人的纵坐标
        alien.rect.y = randint(0, 804)
        # 将外星人添加到外星人编组
        self.aliens.add(alien)

    def create_aliens(self):
        """创建多个外星人"""
        # 随机生成一个外星人数量
        alien_number = randint(self.settings.alien_range1,
                               self.settings.alien_range2)
        for item in range(alien_number):
            self.create_alien()

    def change(self):
        """当外星人碰到屏幕边缘时改变方向"""
        for alien in self.aliens.sprites():
            if alien.edge_detection():
                self.change_direction()
                break

    def change_direction(self):
        """将外星人下移并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.drop_speed
        self.settings.direction *= -1

    def update_aliens(self):
        """更新所有外星人的位置"""
        self.change()
        self.aliens.update()

        # 响应外星人与飞船碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_alien_collisions()
        # 响应外星人到达屏幕底部
        self.alien_get_bottom()

    def bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 检查是否有子弹撞到了外星人
        # 如果是就删除外星人
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # 删除现有的外星人并新建一组外星人
            self.bullets.empty()
            self.create_aliens()

    def ship_alien_collisions(self):
        """响应外星人和飞船碰撞"""
        # 飞船数量减一
        self.data.ship_remain -= 1
        # 清空屏幕上的子弹和外星人
        self.bullets.empty()
        self.aliens.empty()
        # 创建一群新的外星人
        self.create_aliens()
        # 停顿一下，让玩家知道撞到外星人了
        sleep(0.25)

    def alien_get_bottom(self):
        """响应外星人到达底部"""
        for alien in self.aliens.sprites():
            if alien.rect.left < self.screen_rect.left:
                # 像飞船被撞到一样处理
                self.ship_alien_collisions()

    def update_screen(self):
        """更新屏幕内容"""
        # 设置屏幕颜色
        self.screen.fill(self.settings.screen_color)

        # 更新子弹坐标并删除消失的子弹
        self.update_bullets()

        # 显示外星人图片
        self.aliens.draw(self.screen)

        # 显示子弹图片
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 显示飞船图片
        self.ship.display_ship()

        # 更新飞船坐标
        self.ship.up_down()

        # 显示屏幕信息
        pygame.display.flip()


if __name__ == '__main__':
    game = SideShit()
    game.run_game()
