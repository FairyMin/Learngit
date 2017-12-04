# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random


class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 700
        self.screen=screen_temp
        self.image = pygame.image.load("F:\\pyscript\\feiji\\hero1.png")
        self.bullet_list = [] #存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10


    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


class EnermyPlane(object):

    '''敌机类'''
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.screen=screen_temp
        self.image = pygame.image.load("F:\\pyscript\\feiji\\enemy0.png")
        self.bullet_list = [] #存储发射出去的子弹对象引用
        self.direction = "right"  #用来存储飞机的运动方向

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x >440:
            self.direction = "left"           
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,70)
        if random_num == 15 or random_num == 35 or random_num == 60:
            self.bullet_list.append(Enermy_Bullet(self.screen,self.x,self.y))



class Bullet(object):
    """子弹类"""
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y - 20
        self.screen=screen_temp
        self.image = pygame.image.load("F:\\pyscript\\feiji\\bullet.png")
    
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))   


    def move(self):
        self.y -=5

    def judge(self):
        if self.y<0:
            return True
        else:
            return False


class Enermy_Bullet(object):
    """子弹类"""
    def __init__(self,screen_temp,x,y):
        self.x = x + 25  
        self.y = y + 40
        self.screen=screen_temp
        self.image = pygame.image.load("F:\\pyscript\\feiji\\bullet1.png")
    
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))   


    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 850:
            return True
        else:
            return False

def key_control(hero_temp):
    #获取时间，比如按键等
    for event in pygame.event.get():
        #判断是否点击了退出按钮
        if event.type ==QUIT:
            print("exit")
            exit()

        #判断是否按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()

            #检测按键是否是空格
            elif event.key == K_SPACE:
                hero_temp.fire()




def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852),0,32)

    #2.创建一个背景图片
    background = pygame.image.load("F:\\pyscript\\feiji\\background.png")
    
    #3.创建一个飞机对象
    hero = HeroPlane(screen)

    #4.床架敌机
    enermy = EnermyPlane(screen)
    while True:
        
        screen.blit(background,(0,0))
        hero.display()
        enermy.display()
        enermy.move()  #调用敌机移动方法
        enermy.fire() #敌机开火
        pygame.display.update()
        key_control(hero)

        time.sleep(0.01)




if __name__ == '__main__':
    main()