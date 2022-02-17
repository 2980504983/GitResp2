import pygame


class Screen:
    def __init__(self):
        # 初始化pygame
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
