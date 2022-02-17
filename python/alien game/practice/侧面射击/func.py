import pygame

import sys

from ship import Ship

from bullet import Bullet


def check_keys(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keys_down(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keys_up(event, ship)


def check_keys_down(event, settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并加入到Group编组中
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keys_up(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()