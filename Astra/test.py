import pygame
import random
import time as pytime
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.obstacle import *
from classes.laser import *
from classes.warning import *
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
        self.enemy=[Enemy(1380,160),Enemy(1280,260),Enemy(1180,360),Enemy(1280,460),Enemy(1380,560)]
        #initialisation des obstacles et de leur event d'apparition
        self.obstacle = None
        self.obstacles = []
        self.obstacle_spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)
        ########################################################################
        #initialisation des events de laser et de warning
        self.laser_position = [10, 280, 550, 820]
        self.laserPosition1 = None
        self.laserPosition2 = None
        self.laser = None
        self.warning1 = None
        self.warning2 = None
        self.lasers = []
        self.laser_spawn_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.laser_spawn_event, 15000)
        ########################################################################
        self.area = pygame.Rect(300,150,300,300)
        self.area_color = "red"
        self.all_sprites_layer_1 = pygame.sprite.Group() #liste de sprite pour les lasers
        self.all_sprites_layer_2 = pygame.sprite.Group() #liste de sprite pour le joueur/ennemis/obstacles/buffs
        self.all_sprites_layer_2.add(self.buff, self.buff1, self.buff2, self.enemy)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

#évènement d'apparition d'obtacle à des coordonées y aléatoire toutes les 2 sec
            if event.type == self.obstacle_spawn_event:
                obstacle = Obstacle(1920, random.randint(0, 1080))
                self.obstacles.append(obstacle)
                self.all_sprites_layer_2.add(obstacle) 

#évènement d'apparition de laser avec warning avant
    #apparition des warnings
            if event.type == self.laser_spawn_event:
                self.laserPosition1 = random.choice(self.laser_position)
                self.laserPosition2 = random.choice(self.laser_position) 
                while self.laserPosition2 == self.laserPosition1:
                    self.laserPosition2 = random.choice(self.laser_position)
                self.warning1 = WarningLogo(1825, self.laserPosition1 + 110)
                self.warning2 = WarningLogo(1825, self.laserPosition2 + 110)
                self.all_sprites_layer_1.add(self.warning1, self.warning2)
                pygame.time.set_timer(pygame.USEREVENT + 3, 2000)
    #disparition des warnings après 2 sec et apparition des laser aux mêmes positions
            if event.type == pygame.USEREVENT + 3:
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)
                self.warning1.kill()
                self.warning2.kill()
                self.all_sprites_layer_1.remove(self.warning1)
                self.all_sprites_layer_1.remove(self.warning2)
                laser1 = Laser(0, self.laserPosition1)
                laser2 = Laser(0, self.laserPosition2)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.all_sprites_layer_1.add(laser1, laser2)
                pygame.time.set_timer(pygame.USEREVENT + 4, 3000)
    #disparition des lasers après 3 sec
            if event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)
                for sprite in self.all_sprites_layer_1:
                    if isinstance(sprite, Laser):
                        sprite.kill()
                        self.lasers.remove(sprite)

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

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

        if self.buff.collide_rect(self.player.rect):
            self.buff.kill()
            self.all_sprites_layer_2.remove(self.buff)
            self.player.has_buff = True
            print("Buff catch and del")
        
        if self.buff1.collide_rect(self.player.rect):
            self.buff1.kill()
            self.all_sprites_layer_2.remove(self.buff1)
            LifeSystem.healthPlayerUpdate(self,2)
            print("Buff catch and del1")
            print(PlayerStats.currentHealth)


        if PlayerStats.isPlayerHitable == True:
            if self.buff2.collide_rect(self.player.rect):
                self.buff2.kill()
                self.all_sprites_layer_2.remove(self.buff2)
                LifeSystem.healthPlayerUpdate(self,3)
                print("Buff catch and del")
                print(PlayerStats.currentHealth) 
                
#chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
            for obstacle in self.obstacles:
                if obstacle.collide_rect(self.player.rect):
                    LifeSystem.healthPlayerUpdate(self, obstacle)
                    print("Player take hit")
                    print(PlayerStats.currentHealth)
                if obstacle.rect.x <= 0 - obstacle.imageWidth:
                    obstacle.kill()
                    self.all_sprites_layer_2.remove(obstacle)
                    self.obstacles.remove(obstacle)
                else:
                    obstacle.move()

#chaque laser provoque des dégâts
            for laser in self.lasers:
                if laser.collide_rect(self.player.rect):
                    LifeSystem.healthPlayerUpdate(self, laser)
                    print("Player take hit")
                    print(PlayerStats.currentHealth)


            for i in range (5):
                if self.enemy[i].collide_rect(self.player.rect):
                    self.enemy[i].kill()
                    self.all_sprites_layer_2.remove(self.enemy[i])
                    LifeSystem.healthPlayerUpdate(self,3)
                    print(PlayerStats.currentHealth)
                    print("ennemy hit")
                    
                if self.enemy[i].rect.x <= 0 - self.enemy[i].imageWidth:
                    self.enemy[i].kill()
                    self.all_sprites_layer_2.remove(self.enemy[i])
                else:
                    self.enemy[i].move()
        

    def display(self):
        self.screen.fill("black")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.all_sprites_layer_1.draw(self.screen)
        self.all_sprites_layer_2.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
            


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
game = Game(screen)
game.run()

pygame.quit()
