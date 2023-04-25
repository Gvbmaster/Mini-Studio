import pygame
import random

from classes.values import *

class Enemy(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()
        self.ship=["img/low poly/enemyShip1.png","img/low poly/enemyShip2.png","img/low poly/enemyShip3.png"]
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.type=random.choice(self.ship)
        self.image = pygame.image.load(EnnemieStats.type).convert_alpha()
        self.imageWidth = 76
        self.imageHeight = 41
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = EnnemieStats.speed
        self.velocity = [0, 0]
        self._kill = False
        self.has_buff = False
        self.up=False
        self.left=False
        EnnemieStats.enemyAlive+=1
                
        
    def move(self):
        if EnnemieStats.pattern==0:
            Enemy.pattern1(self)
        elif EnnemieStats.pattern==1:
            Enemy.pattern2(self)
        elif EnnemieStats.pattern==2:
            Enemy.pattern3(self)
        elif EnnemieStats.pattern==3:
            Enemy.pattern4(self)
            
            
    def pattern1(self):
        if (self.rect.x < EnnemieStats.meanP1[0] and self.rect.y < EnnemieStats.meanP1[1]) or (self.rect.x==EnnemieStats.pattern1[0][0] and self.rect.y==EnnemieStats.pattern1[0][1]):
            self.velocity = [1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > EnnemieStats.meanP1[0] and self.rect.y < EnnemieStats.meanP1[1]) or (self.rect.x==EnnemieStats.pattern1[1][0] and self.rect.y==EnnemieStats.pattern1[1][1]):
            self.velocity = [1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > EnnemieStats.meanP1[0] and self.rect.y > EnnemieStats.meanP1[1]) or (self.rect.x==EnnemieStats.pattern1[2][0] and self.rect.y==EnnemieStats.pattern1[2][1]):
            self.velocity = [-1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x < EnnemieStats.meanP1[0] and self.rect.y > EnnemieStats.meanP1[1]) or (self.rect.x==EnnemieStats.pattern1[3][0] and self.rect.y==EnnemieStats.pattern1[3][1]):
            self.velocity = [-1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
    
    def pattern2(self):
        if (self.rect.x < EnnemieStats.meanP2[0] and self.rect.y < EnnemieStats.meanP2[1]) or (self.rect.x==EnnemieStats.pattern2[0][0] and self.rect.y==EnnemieStats.pattern2[0][1]):
            self.velocity = [-1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > EnnemieStats.meanP2[0] and self.rect.y < EnnemieStats.meanP2[1]) or (self.rect.x==EnnemieStats.pattern2[1][0] and self.rect.y==EnnemieStats.pattern2[1][1]):
            self.velocity = [-1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > EnnemieStats.meanP2[0] and self.rect.y > EnnemieStats.meanP2[1]) or (self.rect.x==EnnemieStats.pattern2[2][0] and self.rect.y==EnnemieStats.pattern2[2][1]):
            self.velocity = [1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x < EnnemieStats.meanP2[0] and self.rect.y > EnnemieStats.meanP2[1]) or (self.rect.x==EnnemieStats.pattern2[3][0] and self.rect.y==EnnemieStats.pattern2[3][1]):
            self.velocity = [1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
            
    def pattern3(self):
        if (self.rect.y==EnnemieStats.pattern3[0][1]) or (self.rect.y==EnnemieStats.pattern3[1][1]):
            self.up = False
        if (self.rect.y==EnnemieStats.pattern3[2][1]) or (self.rect.y==EnnemieStats.pattern3[3][1]):
            self.up = True
            
        if(self.up):
            self.velocity[1] = -1
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        else:
            self.velocity[1] = 1
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
    
    def pattern4(self):
        if (self.rect.y == 100) or (self.rect.y==541):
            self.up=False
            print("ok")
        elif (self.rect.y == 540) or (self.rect.y==981):
            print("ok1")
            self.up=True
        
        if (self.rect.x == 1720):
            self.left=True
        elif (self.rect.x == 1280):
            self.left=False
        
        if (self.left):
            self.velocity[0] = -1
        else:
            self.velocity[0] = 1
            
        if(self.up):
            self.velocity[1] = -1
        else:
            self.velocity[1] = 1
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
            

    def collide_rect(self, rect):
        if self._kill:
            return False
        return self.rect.colliderect(rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def kill(self):
        super().kill()
        self._kill = True
        EnnemieStats.killCount+=1
        EnnemieStats.enemyAlive-=1
        # print(EnnemieStats.killCount)
