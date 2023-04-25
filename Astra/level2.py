import sys
import pygame
from pygame.locals import *
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.ath import ATH
from classes.backgroundPixel import Background
from classes.projectile import *

from classes.obstacle import *
from classes.values import *
from classes.warning import *
from classes.laser import *
from classes.energy import *
from classes.enemy import *

class Level2:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background(image_path="img/old_cartoon/fond/fond cartoon.png")
        self.ath = ATH()
        self.player = Player(0,500,image_path="img/old_cartoon/vaisseaux1__.png")
        self.buff = [Buff(750,450,2),Buff(850,450,2)]
        self.buff1 =[Buff(750,550,1),Buff(850,550,1)]
        self.buff2=[Buff(750,250,3),Buff(850,250,3)]
        #####INTEGRATION LASER ET OBSTACLES###########
        self.obstacle = None                                    #|
        self.obstacles = []                                     #|
        self.obstacle_spawn_event = pygame.USEREVENT + 1        #|
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)  #|innitialisation des obstacle et de leur event d'apparition
        self.energy_bar = Energy(750, 900, 600, 100, "img/emptybar.png", "img/fullbar.png")
        self.laser_position = [10, 280, 550, 820]               #|
        self.laserPosition1 = None                              #|
        self.laserPosition2 = None                              #|
        self.laser = None                                       #|
        self.warning1 = None                                    #|
        self.warning2 = None                                    #|
        self.lasers = []                                        #|
        self.laser_spawn_event = pygame.USEREVENT + 2           #|
        pygame.time.set_timer(self.laser_spawn_event, 15000)    #|initialisation des events de laser et de warning
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.buff, self.buff1,self.buff2)
        self.space_pressed = False # Pour le tir auto
        self.teleport = False
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
#évènement d'apparition d'obtacle à des coordonées y aléatoire toutes les 2 sec
            if event.type == self.obstacle_spawn_event:
                obstacle = Obstacle(1920, random.randint(0, 1080))
                self.obstacles.append(obstacle)
                self.all_sprites.add(obstacle) 

#évènement d'apparition de laser avec warning avant
    #apparition des warnings
            if event.type == self.laser_spawn_event:
                self.laserPosition1 = random.choice(self.laser_position)
                self.laserPosition2 = random.choice(self.laser_position) 
                while self.laserPosition2 == self.laserPosition1:
                    self.laserPosition2 = random.choice(self.laser_position)
                self.warning1 = WarningLogo(1825, self.laserPosition1 + 110)
                self.warning2 = WarningLogo(1825, self.laserPosition2 + 110)
                self.all_sprites.add(self.warning1, self.warning2)
                pygame.time.set_timer(pygame.USEREVENT + 3, 2000)
    #disparition des warnings après 2 sec et apparition des laser aux mêmes positions
            if event.type == pygame.USEREVENT + 3:
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)
                self.warning1.kill()
                self.warning2.kill()
                self.all_sprites.remove(self.warning1)
                self.all_sprites.remove(self.warning2)
                laser1 = Laser(0, self.laserPosition1)
                laser2 = Laser(0, self.laserPosition2)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.all_sprites.add(laser1, laser2)
                pygame.time.set_timer(pygame.USEREVENT + 4, 3000)
    #disparition des lasers après 3 sec
            if event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)
                for sprite in self.all_sprites:
                    if isinstance(sprite, Laser):
                        sprite.kill()
                        self.lasers.remove(sprite)

########################### Touches de mouvement ############################################################################################            
            keys = pygame.key.get_pressed() # Appel de la détection de touche préssé
            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                self.player.velocity[0] = -1 
                PlayerStats.attackSpeed = 75 # Regulation de la cadence de tir par rapport au fait qu'on recul
                print("left press")
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
                self.player.velocity[0] = 1
                PlayerStats.attackSpeed = 175 # Regulation de la cadence de tir par rapport au fait qu'on avance
                print("right press")
            else:
                self.player.velocity[0] = 0
                PlayerStats.attackSpeed = 100
                
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                self.player.velocity[1] = -1
                PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                print("up press")
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.velocity[1] = 1
                PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                print("down press")
            else:
                self.player.velocity[1] = 0
                PlayerStats.attackSpeed = 100
            
############################ Tir automatique du vaisseau ######################################################################################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Espace pressé")
                    self.space_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Espace relâché")
                    self.space_pressed = False
        self.all_sprites.update()
        current_time = pygame.time.get_ticks()  # Obtenir le temps actuel en millisecondes
        if self.space_pressed and current_time - self.last_shot_time >= PlayerStats.attackSpeed:  # Limiter le tir a la class PlayerStats qui est dans values qui est donc 250
            # Créer une instance de Projectile à la position du joueur
            projectile = Projectile(self.player.rect.right, self.player.rect.centery, PlayerStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (90,40))
            self.all_sprites.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
    def update(self):
        self.player.move()

        for buff in self.buff:
            if buff.collide_rect(self.player):
                buff.kill()
                self.all_sprites.remove(buff)
                PlayerStats.shield = True
                print("Buff catch and del")
                print(PlayerStats.shield)

        for buff in self.buff1:
            if buff.collide_rect(self.player):
                buff.kill()
                self.all_sprites.remove(buff)
                LifeSystem.healthPlayerUpdate(self, 2)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        for buff in self.buff2:
            if buff.collide_rect(self.player):
                buff.kill()
                self.all_sprites.remove(buff)
                LifeSystem.healthPlayerUpdate(self, buff)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
            for obstacle in self.obstacles:
                if pygame.sprite.collide_mask(obstacle, self.player):
                    LifeSystem.healthPlayerUpdate(self, obstacle)
                    print("Player take hit")
                    obstacle.kill()
                    print(PlayerStats.currentHealth)
                if obstacle.rect.x <= 0 - obstacle.imageWidth:
                    obstacle.kill()
                    self.all_sprites.remove(obstacle)
                    self.obstacles.remove(obstacle)
                else:
                    obstacle.move()

        #chaque laser provoque des dégâts
            for laser in self.lasers:
                if laser.collide_rect(self.player.rect):
                    LifeSystem.healthPlayerUpdate(self, laser)
                    print("Player take hit")
                    print(PlayerStats.currentHealth)

    def display(self):
        self.background.update()
        self.screen.fill("black")
        self.background.draw(self.screen)
        #pygame.draw.rect(self.screen, self.area_color, self.area)
        self.all_sprites.draw(self.screen)
        self.player.draw(self.screen)
        self.ath.draw(self.screen)
        self.energy_bar.update()
        self.energy_bar.fill_rect_rect.x = self.energy_bar.rect.x
        self.energy_bar.fill_rect_rect.y = self.energy_bar.rect.y
        self.screen.blit(self.energy_bar.image, self.energy_bar.rect)
        self.screen.blit(self.energy_bar.fill_rect, self.energy_bar.fill_rect_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
