#coding:utf-8
import pygame as py

#1、初始化部分：
import time
#初始化
#py.init()
#关闭
#print("游戏部分")
#py.quit()
#2、调试英雄位置部分验证：
#设置英雄尺寸位置信息，四个参数
# hero_rect = py.Rect(100,500,120,125)
# print("英雄原点信息%d %d"%(hero_rect.x,hero_rect.y))
# print("英雄尺寸信息%d %d"%(hero_rect.width,hero_rect.height))
# print("%d %d"%hero_rect.size)
#3、创建游戏窗口部分：
# py.init()
# #创建游戏窗口
# screen = py.display.set_mode((480,700))
# while True:
#     pass
# time.sleep(5)
#
# py.quit()

#4、绘制图像：
# py.init()
# #创建游戏窗口：
# screen = py.display.set_mode((480,700))
# #绘制背景图像加载图像：
# bg = py.image.load("./images/background.png")
# #绘制图像：
# screen.blit(bg,(0,0))
# py.display.update()
# time.sleep(10)
# #?背景图加载不明显
#5、绘制英雄图像：
# import pygame
# pygame.init()
# #绘制游戏窗口
# screen = pygame.display.set_mode((480,700))
# bg = pygame.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# pygame.display.update()
# #绘制英雄位置
# hero = pygame.image.load("./images/me1.png")
# #绘制在屏幕上：
# screen.blit(hero,(200,500))
# #更新显示
# pygame.display.update()
# i = 0
# while i<10:
#     i+=1
#     time.sleep(1)
# pygame.quit()
#?绘制内容会最后出现；
#6、调整为绘制后统一调用更新方法：
# py.init()
# screen = py.display.set_mode((480,700))
# bg = py.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# hero = py.image.load("./images/me1.png")
# screen.blit(hero,(150,500))
# py.display.update()
#7、创建时钟对象
# py.init()
# screen = py.display.set_mode((480,700))
# bg = py.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# hero = py.image.load("./images/me1.png")
# screen.blit(hero,(150,300))
# py.display.update()
# #创建时钟对象
# clock = py.time.Clock()
# #游戏循环
# i = 0
# while True:
#     #可以指定循环体内代码执行频率
#     clock.tick(1)
#     print(i)
#     i += 1
#     pass
# py.quit()
#8、更新英雄游戏位置：
# py.init()
# screen = py.display.set_mode((480,700))
# bg = py.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# hero = py.image.load("./images/me1.png")
# screen.blit(hero,(150,300))
# py.display.update()
# #创建时钟对象
# clock = py.time.Clock()
# #定义rect记录飞机的初始位置：
# hero_rect = py.Rect(150,300,102,126)
# #游戏循环
# while True:
#     #指定内部游戏代码执行频率
#     clock.tick(60)
#     #修改飞机飞行位置：
#     hero_rect.y -= 1
#     #3、调用bilt方法绘制图像
#     screen.blit(bg,(0,0))
#     screen.blit(hero,hero_rect)
#     py.display.update()
#
# py.quit()
#9、英雄循环飞行
# import pygame
# # 游戏的初始化
# pygame.init()
# # 创建游戏的窗口 480 * 700
# screen = pygame.display.set_mode((480, 700))
# # 绘制背景图像
# bg = pygame.image.load("./images/background.png")
# screen.blit(bg, (0, 0))
# # pygame.display.update()
# # 绘制英雄的飞机
# hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (150, 300))
# # 可以在所有绘制工作完成之后，统一调用update方法
# pygame.display.update()
# # 创建时钟对象
# clock = pygame.time.Clock()
# # 1. 定义rect记录飞机的初始位置
# hero_rect = pygame.Rect(150, 300, 102, 126)
# # 游戏循环 -> 意味着游戏的正式开始！
# while True:
#     # 可以指定循环体内部的代码执行的频率
#     # 捕获事件
#     event_list = pygame.event.get()
#     if len(event_list) > 0:
#         print(event_list)
#     # event = pygame.event.poll()
#     # if event.type == pygame.QUIT():
#     #      pygame.quit()
#     #      exit()
#     clock.tick(60)
#     # 2. 修改飞机的位置
#     hero_rect.y -= 1
#     # 判断飞机的位置
#     if hero_rect.y <= 0:
#         hero_rect.y = 700
#     # 3. 调用blit方法绘制图像
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     # 4. 调用update方法更新显示
#     pygame.display.update()
# pygame.quit()
#10、event事件：
# py.init()
# screen = py.display.set_mode((480,700))
# bg = py.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# hero = py.image.load("./images/me1.png")
# screen.blit(hero,(150,300))
# py.display.update()
# clock = py.time.Clock()
# hero_rect = py.Rect(150,300,102,126)
# while True:
#     clock.tick(60)
#     event_list = py.event.get()
#     if len(event_list) > 0:
#         print(event_list)
#     hero_rect.y -= 1
#     if hero_rect.y <= 0:
#         hero_rect.y =700
#     screen.blit(bg,(0,0))
#     screen.blit(hero,(hero_rect))
#     py.display.update()
# py.quit()
#11、监听事件的退出：
# py.init()
# screen = py.display.set_mode((480,700))
# bg = py.image.load("./images/background.png")
# screen.blit(bg,(0,0))
# hero = py.image.load("./images/me1.png")
# screen.blit(hero,(150,300))
# py.display.update()
# clock = py.time.Clock()
# hero_rect = py.Rect(150,300,102,126)
# while True:
#     clock.tick(60)
#     #event_list = py.event.get()
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             print("游戏退出。。。")
#             py.quit()
#             exit()
#     hero_rect.y -= 1
#     if hero_rect.y <= 0:
#         hero_rect.y =700
#     screen.blit(bg,(0,0))
#     screen.blit(hero,(hero_rect))
#     py.display.update()
# py.quit()
#演练精灵：
from plan_sprites import GameSprite
py.init()
screen = py.display.set_mode((480,700))
bg = py.image.load("./images/background.png")
screen.blit(bg,(0,0))
hero = py.image.load("./images/me1.png")
screen.blit(hero,(150,300))
py.display.update()
clock = py.time.Clock()
hero_rect = py.Rect(150,300,102,126)
#创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
enemy_group = py.sprite.Group(enemy,enemy1)
while True:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            print("退出游戏")
            py.quit()
            exit()
    #修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #让精灵组调用两个方法
    #让组中精灵更新位置
    enemy_group.update()
    #在屏幕上绘制所有精灵
    enemy_group.draw(screen)
    py.display.update()
py.quit()


