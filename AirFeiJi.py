#coding:utf-8
import pygame
from pygame.locals import *
import time
import random

class Base(object):

    def __init__(self, x, y, images, screen_temp):
        self.x = x
        self.y = y
        self.images = pygame.image.load(images)
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.images, (self.x, self.y))


class BasePlane(Base):

    def __init__(self,x,y,images,screen_temp):
        super().__init__(x,y,images,screen_temp)
        self.bullet_list = [] #存储发射进去的子弹

    def display(self):
        Base.display(self)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            bullet.judge()#判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet)
                # #列表元素删除部分优化


class BaseBullet(Base):

    def __init__(self,x,y,screen_temp,images):
        super().__init__(x,y,images,screen_temp)


class HeroPlane(BasePlane):

    def __init__(self,screen_temp):
        super().__init__(160,550,"./images/me1.png",screen_temp)
        #BasePlane.__init__(self,160,550,"./images/me1.png",screen_temp)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y +=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


class EnemyPlane(BasePlane):

    def __init__(self,screen_temp):
        super().__init__(0,0,"./images/enemy1.png",screen_temp)
        self.bianjie = "right"

    def move(self):
        if self.bianjie == "right":
            self.x += 5
        elif self.bianjie == "left":
            self.x -= 5
        if self.x > 426:
            self.bianjie = "left"
        elif self.x == 0:
            self.bianjie = "right"

    def fire(self):
        #self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
        random_num = random.randint(1,100)
        if random_num in (23,56,78):
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


class EnemyBullet(BaseBullet):

    def __init__(self,screen_temp,x,y):
        super().__init__(x+27.5,y+43,screen_temp,"./images/bullet1.png")

    def move(self):
        self.y += 20

    def judge(self):
        if self.y > 695:
            return True
        else:
            return False


class Bullet(BaseBullet):

    def __init__(self,screen_temp,x,y):
        super().__init__(x+48.5,y-20,screen_temp,"./images/bullet2.png")

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


def key_contorl(hero_temp):
    """键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                hero_temp.move_down()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():
    screen = pygame.display.set_mode((480,700),0,32)
    bg = pygame.image.load("./images/background.png")
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(bg,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_contorl(hero)


if __name__ == '__main__':
    main()