# 题目6：（调用函数）练习函数调用。

# 创建一个屏幕
# 这里的函数用到了pygame, 如果要运行的化要先导入pygame模块，导入步骤，1点击File,
# 2点击settings, 3点击project: 项目名, 4点击python Interpreter, 5点击＋号
# 搜索并安装(install)pygame
import pygame


class Screen:
    def __init__(self):
        """创建屏幕所需的资源"""

        # 初始化pygame
        pygame.init()

        # 设置屏幕大小(改变数字可以改变屏幕的大小)
        self.screen = pygame.display.set_mode((1000, 500))

        # 设置屏幕名称
        pygame.display.set_caption('屏幕显示')

    def run(self):
        """显示屏幕"""
        while True:
            # 检测按键按Q退出
            self.keyboard()

            # 设置屏幕颜色(改变数字可以改变屏幕的颜色)
            self.screen.fill((50, 20, 20))

            # 显示屏幕
            pygame.display.flip()

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()


if __name__ == '__main__':
    A6 = Screen()
    A6.run()
