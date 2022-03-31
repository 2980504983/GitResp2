import pygame


class Screen:
    """
    创建界面
    """
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设置屏幕信息
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 设置屏幕名称
        pygame.display.set_caption('射击练习')

    def display_screen(self, color=(230, 230, 230)):
        # 设置屏幕颜色
        self.screen.fill(color)

        # 显示屏幕
        pygame.display.flip()


class Main:
    """
        初始化游戏，并开始游戏
    """
    def __init__(self):
        # 初始化屏幕资源
        self.screen = Screen()

    def main(self):
        """
            开始游戏
        """
        while True:
            self.screen.display_screen()


if __name__ == "__main__":
    do_it = Main()
    do_it.main()
