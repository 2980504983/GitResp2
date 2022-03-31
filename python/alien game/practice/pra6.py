import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group

pygame.init()
bg_color = (20, 40, 50)
screen = pygame.display.set_mode((1200, 700))
random_number = randint(1, 1200)
dropspeed = 3
speed_factor = 5


class Doll(Sprite):
    """docstring for Doll"""

    def __init__(self, screen):
        super(Doll, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= speed_factor


class Water(Sprite):
    def __init__(self, screen, random_number):
        super(Water, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("E://python/ alien game/"
                                       "飞机大战素材/10.1.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = random_number
        self.rect.top = 0
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += dropspeed
        self.rect.y = self.y

    def fail(self):
        if self.rect.top >= self.screen_rect.bottom:
            print("no")
            waters.empty()
            random_number = randint(1, 1200)
            water = Water(screen, random_number)
            waters.add(water)


def catch_water(doll, water, waters):
    catch = pygame.sprite.spritecollide(doll, waters, True, collided=None)
    # 曾经前边有doll=Doll（）……导致在只有移动娃娃才能接到水珠的情况下，水珠不消失
    for water in waters:  # 之前丢了这句，就不是遍历了！！！！
        if water.rect.top >= water.screen_rect.bottom:
            waters.empty()

    if len(waters) == 0:
        random_number = randint(1, 1200)
        water = Water(screen, random_number)
        waters.add(water)


def check_keydown_events(event, doll):
    if event.key == pygame.K_RIGHT:
        doll.moving_right = True
    elif event.key == pygame.K_LEFT:
        doll.moving_left = True


def check_keyup_events(event, doll):
    if event.key == pygame.K_RIGHT:
        doll.moving_right = False
    elif event.key == pygame.K_LEFT:
        doll.moving_left = False


def event_check(doll):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, doll)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, doll)


def rungame():
    water = Water(screen, random_number)
    waters = Group()
    waters.add(water)
    doll = Doll(screen)
    while True:
        screen.fill(bg_color)  # 这一步很重要啊，要是挪到True以前，
        # 娃娃就会出现重影，擦掉背景色。
        doll.blitme()
        waters.draw(screen)
        pygame.display.flip()
        event_check(doll)
        doll.update()
        waters.update()
        catch_water(doll, water, waters)


rungame()
