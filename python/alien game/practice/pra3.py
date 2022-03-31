import pygame

import sys


class DetectionButton:
    """键盘按键检测"""
    def __init__(self):
        # 初始化模块
        pygame.init()

        # 设置屏幕大小
        self.screen = pygame.display.set_mode((500, 500))

        # 设置屏幕名称
        pygame.display.set_caption("按键检测")

        # 设置屏幕颜色
        self.screen.fill((100, 10, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_q:
                        sys.exit()

            # 显示屏幕
            pygame.display.flip()


if __name__ == '__main__':
    ai = DetectionButton()
    ai.run()
