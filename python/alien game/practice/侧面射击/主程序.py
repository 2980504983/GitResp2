import pygame

from settings import Settings

import func as f

from ship import Ship

from bullet import Bullet

from pygame.sprite import Group


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Side Shoot")

    ship = Ship(screen)

    bullets = Group()

    while True:

        f.check_keys(settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.left > screen.get_rect().right:
                bullets.remove(bullet)

        f.update_screen(settings, screen, ship, bullets)


run_game()
