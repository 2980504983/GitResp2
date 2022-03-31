import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    """表示单个星星的类"""

    def __init__(self, ai_game):
        """初始化星星并设置初始位置"""
        # 继承超类
        super().__init__()
        # 接入屏幕信息
        self.screen = ai_game.screen

        # 加载星星图片并回去其外接矩形
        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")
        self.rect = self.image.get_rect()

        # 设置初始位置为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的精确水平位置
        self.x = float(self.rect.x)


class BackGround:
    """创建背景"""
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设置背景参数
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 设置背景名称
        pygame.display.set_caption("星星图像")

        # 导入星星组
        self.stars = pygame.sprite.Group()

        self.create()

    def create(self):
        """创建星星群"""
        # 创建一个星星并计算一行能容纳多少个星星
        star = Star(self)
        # 加入-10 到 10之间的随机整数
        random_number = randint(0, 10)
        random_number1 = randint(0, 10)

        # star_width, star_height = star.rect.size
        # star_width = star.rect.width
        # available_space_x = 1200 - (star_width * 2)
        # number_star_x = available_space_x // (star_width * 2)
        #
        # # 计算屏幕里可以容纳多少行星星
        # available_space_y = 750 - (star_height * 3)
        # number_rows = available_space_y // (star_height * 2)

        # 创建星星群
        for row_number in range(random_number):
            for star_number in range(random_number1):
                self.create_alien(star_number, row_number)

    def create_alien(self, star_number, row_number):
        # 创建一个外星人并加入当前行
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

    def run(self):
        """主循环"""
        while True:
            # 键盘检测
            self.key_control()

            # 填充背景颜色
            self.screen.fill((100, 100, 100))

            # 显示星星群
            self.stars.draw(self.screen)

            # 显示内容
            pygame.display.flip()


if __name__ == '__main__':
    ai = BackGround()
    ai.run()
