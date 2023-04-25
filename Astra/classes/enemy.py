import pygame
import random

from classes.values import *
from classes.projectileEn import *

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
        EnnemieStats.enemyAlive+=1
        self.last_shot_time = 0
        self.shoot_interval = 1000  # intervalle de temps entre chaque tir (en millisecondes)
        self.all_sprites_projectilesEn = pygame.sprite.Group() #liste de sprite pour les tir des ennemis 

                
    def move(self):
        if EnnemieStats.pattern==0:
            Enemy.pattern1(self)
        elif EnnemieStats.pattern==1:
            Enemy.pattern2(self)                     
            
    def shoot(self):
        self.shootEn = ProjectileEn(self.rect.centerx, self.rect.top, EnnemieStats.attackVelocity, "img/low poly/bullet.png", (100,90))

    
    def update(self):
        # Vérifier si suffisamment de temps s'est écoulé depuis le dernier tir
        now = pygame.time.get_ticks()
        time_since_last_shot = now - self.last_shot_time
        if time_since_last_shot > self.shoot_interval:
            # Créer un nouveau projectile et l'ajouter à la liste des sprites de projectiles
            self.shoot()
            self.all_sprites_projectilesEn.add(self.shootEn)

            # Réinitialiser le temps du dernier tir
            self.last_shot_time = now

    def pattern1(self):
        if (self.rect.x < 750 and self.rect.y < 350) or (self.rect.x==500 and self.rect.y==350):
            self.velocity = [1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > 750 and self.rect.y < 350) or (self.rect.x==750 and self.rect.y==100):
            self.velocity = [1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > 750 and self.rect.y > 350) or (self.rect.x==1000 and self.rect.y==350):
            self.velocity = [-1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x < 750 and self.rect.y > 350) or (self.rect.x==750 and self.rect.y==600):
            self.velocity = [-1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
    
    def pattern2(self):
        if (self.rect.x < 750 and self.rect.y < 350) or (self.rect.x==750 and self.rect.y==100):
            self.velocity = [-1, 1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > 750 and self.rect.y < 350) or (self.rect.x==1000 and self.rect.y==350):
            self.velocity = [-1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x > 750 and self.rect.y > 350) or (self.rect.x==750 and self.rect.y==600):
            self.velocity = [1, -1]
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        elif (self.rect.x < 750 and self.rect.y > 350) or (self.rect.x==500 and self.rect.y==350):
            self.velocity = [1, 1]
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
