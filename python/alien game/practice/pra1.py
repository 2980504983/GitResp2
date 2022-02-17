import pygame
import sys


class Hero:
    """Manage Hero object"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load picture of hero and get it's rect
        self.image = pygame.image.load('E:/python/ alien game/飞机大战素材/'
                                       '10.1.jpg')
        self.rect = self.image.get_rect()

        # put the hero in the the center of bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class BackgroundWindow:
    """create background window"""
    def __init__(self):
        # Initialization and check all of module of pygame
        pygame.init()

        # create screen and set it
        self.screen = pygame.display.set_mode((1000, 600))

        # set the name of screen
        pygame.display.set_caption('Wow')

    def run_game(self):
        """Main loop"""

        # get info of mouse and keyboard
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # set color of background and update screen
            self.screen.fill((5, 39, 175))
            hero = Hero(self)
            hero.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    ai = BackgroundWindow()
    ai.run_game()
