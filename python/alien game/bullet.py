import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manage bullet of ship"""

    def __init__(self, ai_game):
        """create a bullet object in the location of ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create rect symbol of bullet in the (0,0),then create
        # Correct location
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self
                                .settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the location of bullet by float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up"""
        # Update float value that change the location of bullet
        self.y -= self.settings.bullet_speed
        # Update location of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
