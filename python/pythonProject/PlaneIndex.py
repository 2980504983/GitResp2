import pygame #
import random
from pygame.locals import *
"""
1.Realize the display of aircraft,and control movement of aircraft
"""

class HeroPlane(object):
    def __init__(self,screen):
        # initial position of plane
        self.x=150
        self.y=420
        # Set up window of context displayed
        self.screen=screen
        # Generate picture of plane
        self.imageName='./飞机大战素材/10.1.jpg'
        self.image=pygame.image.load(self.imageName)
        # BulletList
        self.bulletList=[]
        pass
    def moveleft(self):
        if self.x>0:
            self.x-=10
        pass
    def moveright(self):
        if self.x<290:
            self.x+=10

    def moveup(self):
        if self.y>0:
            self.y-=10

    def MoveDown(self):
        if self.y<440:
            self.y+=10

        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        needDelitemList=[]
        for item in self.bulletList:
            if item.junge():
                needDelitemList.append(item)
                pass
            pass
        for i in needDelitemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

        pass
    def fire(self):
        # Create a new BulletObject
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x=x+13
        self.y=y-20
        self.screen=screen
        self.image=pygame.image.load('./飞机大战素材/bullet2.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)) # Display picture of bullet
        pass
    def move(self):
        self.y-=0.2
        pass
    def junge(self):
        if self.y<0:
            return True
        else:
            return False

    pass

class EnemyPlane:
    def __init__(self,screen):
        # Set up a direction
        self.direction='right'
        # initial position of plane
        self.x = 0
        self.y = 0
        # Set up window of context displayed
        self.screen = screen
        self.bulletList=[]
        # Generate picture of plane
        self.imageName = './飞机大战素材/20.1.jpg'
        self.image = pygame.image.load(self.imageName)
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        needDelitemList = []
        for item in self.bulletList:
            if item.junge():
                needDelitemList.append(item)
                pass
            pass
        for i in needDelitemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

        pass
    def fire(self):
        num=random.randint(1,1000)
        if num == 3:
            newBullet=EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)



        pass
    def move(self):
        if self.direction == 'right':
            self.x+=0.1
            pass
        elif self.direction == 'left':
            self.x-=0.1
            pass
        if self.x>330:
            self.direction='left'
            pass
        elif self.x<0:
            self.direction='right'


        pass

class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y+10
        self.screen=screen
        self.image=pygame.image.load('./飞机大战素材/bullet1.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)) # Display picture of bullet
        pass
    def move(self):
        self.y+=0.05
        pass
    def junge(self):
        if self.y>490:
            return True
        else:
            return False

    pass

def key_control(HeroObj):
    """
    Realize text of keyboard
    :param HeroObj:
    :return:
    """
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveleft() # Transfer function to move left
                pass
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveright() # Transfer function to move right
                pass
            elif event.key == K_w or event.key == K_UP:
                print('up')
                HeroObj.moveup()
                pass
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                HeroObj.MoveDown()

            elif event.key == K_SPACE:
                print('K_SPACE')
                HeroObj.fire()

def main():

    # First,create a screen display something
    screen=pygame.display.set_mode((350,500))

    # create a background
    background=pygame.image.load('./飞机大战素材/background.png')

    # set a title
    pygame.display.set_caption('阶段总结-飞机大战')

    # add background music
    pygame.mixer.init()
    pygame.mixer.music.load('./飞机大战素材/music.mp3.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) # cycles , -1 means infinite loop

    # create object of plane
    hero=HeroPlane(screen)

    # create object of enemyplane
    enemyplane=EnemyPlane(screen)

    # set context displayed
    while True:
        screen.blit(background,(0,0))
        # Display player's hero
        hero.display()
        enemyplane.display()
        enemyplane.move()
        enemyplane.fire()
        # get things about keyboard
        key_control(hero)

        # update context displayed
        pygame.display.update()
    pass
if __name__=='__main__':
    main()