import pygame

# import setting


class Ship:
    """Manage class of ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set the initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the picture of ship and get it's rect
        self.image = pygame.image.load('飞机大战素材/10.1.jpg')
        self.rect = self.image.get_rect()

        # Put each new spaceship in the center of the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float in the attributes of ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Change the location of ship according the move sign"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom \
                < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # update rect according self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at the specified location """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底部居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
