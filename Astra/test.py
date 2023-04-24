import pygame
from pygame.locals import *
import random
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.obstacle import *
from classes.enemy import *
from classes.values import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0,0)
        self.buff = Buff(750,450,2) #bouclier
        self.buff1 = Buff(850,550,1) #heal
        self.buff2 = Buff(750,250,3) #damage
        self.obstacle = Obstacle(1280, random.randint (0, 800))
        self.area = pygame.Rect(300,150,300,300)
        self.area_color = "red"
        self.all_sprites = pygame.sprite.Group()
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy=[Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])]
        
        EnnemieStats.enemyAlive=len(self.enemy)
        self.all_sprites.add(self.player, self.buff, self.buff1,self.buff2,self.obstacle,self.enemy)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

    def update(self,screen):
        
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

        if self.buff.collide_rect(self.player.rect):
            self.buff.kill()
            self.all_sprites.remove(self.buff)
            self.player.has_buff = True
            # print("Buff catch and del")
        
        if self.buff1.collide_rect(self.player.rect):
            self.buff1.kill()
            self.all_sprites.remove(self.buff1)
            LifeSystem.healthPlayerUpdate(self,2)
            # print("Buff catch and del1")
            # print(PlayerStats.currentHealth)

        if self.buff2.collide_rect(self.player.rect):
            self.buff2.kill()
            self.all_sprites.remove(self.buff2)
            LifeSystem.healthPlayerUpdate(self,3)
            # print("Buff catch and del")
            # print(PlayerStats.currentHealth)
            
        if self.obstacle.collide_rect(self.player.rect):
            LifeSystem.healthPlayerUpdate(self, self.obstacle)
            # print("Player take hit")
            # print(PlayerStats.currentHealth)

        
        if self.obstacle.rect.x <= 0 - self.obstacle.imageWidth:
            self.obstacle.kill()
            self.all_sprites.remove(self.obstacle)
        else:
            self.obstacle.move()
            
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy=[Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])]
            self.all_sprites.add(self.enemy)
        
        for i in range (len(self.enemy)):
            if self.enemy[i].collide_rect(self.player.rect):
                self.enemy[i].kill()
                self.all_sprites.remove(self.enemy[i])
                LifeSystem.healthPlayerUpdate(self,3)
                # print(PlayerStats.currentHealth)
                # #self.player.has_buff = True
                # print("ennemy hit")
                
            if self.enemy[i].rect.x <= 200 - self.enemy[i].imageWidth:
                self.enemy[i].kill()
                self.all_sprites.remove(self.enemy[i])
            else:
                self.enemy[i].move()
            # print(EnnemieStats.enemyAlive)
    

    def display(self):
        self.screen.fill("black")
        #pygame.draw.rect(self.screen, self.area_color, self.area)
        self.all_sprites.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self,screen):
        while self.running:
            self.handling_events()
            self.update(screen)
            self.display()
            self.clock.tick(60)
            


pygame.init()
screen = pygame.display.set_mode((0, 0),FULLSCREEN)#(1920, 1080))
game = Game(screen)
game.run(screen)
pygame.quit()
