#coding:utf-8
import pygame
from pygame.locals import *
import time
import random

class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 160
        self.y = 550
        self.hero = pygame.image.load("./images/me1.png")
        self.screen = screen_temp
        self.bullet_list = [] #存储发射进去的子弹
        self.bullet_list_remove = []

    def display(self):
        self.screen.blit(self.hero,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            bullet.judge()#判断子弹是否越界
            if bullet.judge():
                #self.bullet_list_remove.append(bullet)
                self.bullet_list.remove(bullet)
                # #列表元素删除部分优化
    # def remove(self):
    #     for bullet_remove in self.bullet_list_remove:
    #         print(bullet_remove)
    #         self.bullet_list.remove(bullet_remove)

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


class EnemyPlane(object):
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.enemy = pygame.image.load("./images/enemy1.png")
        self.screen = screen_temp
        self.bullet_list = [] #存储发射进去的子弹
        self.bianjie = "right"

    def display(self):
        self.screen.blit(self.enemy,(self.x,self.y))
        for bullit in self.bullet_list:
            bullit.display()
            bullit.move()
            bullit.judge()
            if bullit.judge():
                 self.bullet_list.remove(bullit)


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
        self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
        # random_num = random.randint(1,100)
        # if random_num in (23,56,78):
        #     self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))




class EnemyBullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+27.5
        self.y = y+43
        self.screen = screen_temp
        self.bullet = pygame.image.load("./images/bullet1.png")

    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))

    def move(self):
        self.y += 20

    def judge(self):
        if self.y > 695:
            return True
        else:
            return False

class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x = x+48.5
        self.y = y-20
        self.screen = screen_temp
        self.bullet = pygame.image.load("./images/bullet2.png")

    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))

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
        print(event.type)
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up')
                #hero_temp.y -= 4
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                hero_temp.move_down()
            elif event.key == K_SPACE:
                print('space')
                #hero_temp.fire()
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
        #time.sleep(0.1)


if __name__ == '__main__':
    main()