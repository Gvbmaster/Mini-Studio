import sys
import pygame
from pygame.locals import *
from classes.player_boss import Player3
from classes.buff import Buff
from classes.lifesystem import *
from classes.ath_boss import ATH3
from classes.backgroundPixel_boss import Background3
from classes.projectile_boss import *
from classes.boss import *
from classes.effect.invicibility import *

from classes.obstacle import *
from classes.values import *
from classes.warning import *
from classes.laser_boss import *

from classes.enemy import *

import gameover

class Level3:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background3()
        self.ath = ATH3()
        self.ls = LifeSystem(self)
        self.gameover = gameover.GameoverLP(self)
        self.player = Player3(900,800)
        #####INTEGRATION LASER ET OBSTACLES###########
        self.laser_position = [10, 240, 480, 720, 960, 1200 ,1440, 1680 ]               #|
        self.laserPosition1 = None                              #|
        self.laserPosition2 = None                              #|
        self.laser = None                                       #|
        self.warning1 = None                                    #|
        self.warning2 = None                                    #|
        self.lasers = []                                        #|
        self.laser_spawn_event = pygame.USEREVENT + 2           #|
        pygame.time.set_timer(self.laser_spawn_event, 4000)    #|initialisation des events de laser et de warning

        self.boss = Boss("Astra 0.25", 20)
        self.all_sprites_layer_1 = pygame.sprite.Group() #liste de sprite pour les lasers
        self.all_sprites_layer_2 = pygame.sprite.Group() #liste de sprite pour le joueur/ennemis/obstacles/buffs
        self.all_sprites_projectilesMC = pygame.sprite.Group() #liste de sprite pour les tir du MC
        self.all_sprites_boss = pygame.sprite.Group() 
        self.all_sprites_boss.add(self.boss)
        self.all_sprites_layer_2.add()#self.buff, self.buff1, self.buff2)#, self.enemy)
        self.space_pressed = False # Pour le tir auto
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto
        self.boss_health_bar_rect = pygame.Rect(500, 1000, 800, 30) # Rectangle qui représente la barre de vie
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

#évènement d'apparition de laser avec warning avant
    #apparition des warnings
            if event.type == self.laser_spawn_event:
                self.laserPosition1 = random.choice(self.laser_position)
                self.laserPosition2 = random.choice(self.laser_position)
                self.laserPosition3 = random.choice(self.laser_position) 
                self.laserPosition4 = random.choice(self.laser_position)  
                while self.laserPosition2 == self.laserPosition1:
                    self.laserPosition2 = random.choice(self.laser_position)
                self.warning1 = WarningLogo(self.laserPosition1 , 0+ 310)
                self.warning2 = WarningLogo(self.laserPosition2 , 0+ 310)
                self.warning3 = WarningLogo(self.laserPosition3 , 0+ 310)
                self.warning4 = WarningLogo(self.laserPosition4 , 0+ 310)
                self.all_sprites_layer_1.add(self.warning1, self.warning2,self.warning3,self.warning4)
                pygame.time.set_timer(pygame.USEREVENT + 3, 2000)
    #disparition des warnings après 2 sec et apparition des laser aux mêmes positions
            if event.type == pygame.USEREVENT + 3:
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)
                self.warning1.kill()
                self.warning2.kill()
                self.warning3.kill()
                self.warning4.kill()
                self.all_sprites_layer_1.remove(self.warning1)
                self.all_sprites_layer_1.remove(self.warning2)
                self.all_sprites_layer_1.remove(self.warning3)
                self.all_sprites_layer_1.remove(self.warning4)
                laser1 = Laser3(self.laserPosition1, 0)
                laser2 = Laser3(self.laserPosition2, 0)
                laser3 = Laser3(self.laserPosition3, 0)
                laser4 = Laser3(self.laserPosition4, 0)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.lasers.append(laser3)
                self.lasers.append(laser4)
                self.all_sprites_layer_1.add(laser1, laser2, laser3, laser4)
                pygame.time.set_timer(pygame.USEREVENT + 4, 2000)
    #disparition des lasers après 2 sec
            if event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)
                for sprite in self.all_sprites_layer_1:
                    if isinstance(sprite, Laser3):
                        sprite.kill()
                        self.lasers.remove(sprite)

########################### Touches de mouvement ############################################################################################            
            keys = pygame.key.get_pressed() # Appel de la détection de touche préssé
            if keys[pygame.K_q] :
                self.player.velocity[0] = -1 
                PlayerStats.attackSpeed = 100
                # print("left press")
            elif keys[pygame.K_d] : 
                self.player.velocity[0] = 1
                PlayerStats.attackSpeed = 100
                # print("right press")
            else:
                self.player.velocity[0] = 0
                PlayerStats.attackSpeed = 100
                
            if keys[pygame.K_z] :
                self.player.velocity[1] = -1
                # print("up press")
                PlayerStats.attackSpeed = 175
            elif keys[pygame.K_s] :
                self.player.velocity[1] = 1
                # print("down press")
                PlayerStats.attackSpeed = 75
            else:
                self.player.velocity[1] = 0
                PlayerStats.attackSpeed = 100
############################ Tir automatique du vaisseau ######################################################################################
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    print("Espace pressé")
                    self.space_pressed = True
            if event.type == pygame.KEYUP and event.key == K_SPACE:
                    print("Espace relâché")
                    self.space_pressed = False
        self.all_sprites_layer_2.update()
        self.all_sprites_projectilesMC.update()
        current_time = pygame.time.get_ticks()  # Obtenir le temps actuel en millisecondes
        if self.space_pressed and current_time - self.last_shot_time >= PlayerStats.attackSpeed:  # Limiter le tir a la class PlayerStats qui est dans values qui est donc 250
            # Créer une instance de Projectile à la position du joueur
            projectile = Projectile3(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam2.png", (90,110))
            self.all_sprites_projectilesMC.add(projectile)
            self.all_sprites_layer_2.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
    def update(self):
        self.player.move()

        #chaque laser provoque des dégâts
        for laser in self.lasers:
            if laser.collide_rect(self.player.rect):
                Invicibility.update()
                self.ls.healthPlayerUpdate(laser)
                print("Player take hit")
                print(PlayerStats.currentHealth)

        for projectile in self.all_sprites_projectilesMC :
            if pygame.sprite.spritecollide(self.boss, self.all_sprites_projectilesMC, True):
                self.boss.take_damage(10)
                print(self.boss.health)
        if self.boss.health == 0:
            print("Le boss", self.boss.name, "a été vaincu !")
            self.boss.kill()
        if not self.boss.alive():
            print("Le boss", self.boss.name, "est mort !")
            self.all_sprites_boss.remove(self.boss)

    def display(self):
        if PlayerStats.currentHealth > 0:
            self.background.update()
            self.screen.fill("black")
            self.background.draw(self.screen)
            self.all_sprites_layer_1.draw(self.screen)
            self.all_sprites_layer_2.draw(self.screen)
            self.player.draw(self.screen)
            self.ath.draw(self.screen)
            self.all_sprites_boss.update()
            self.all_sprites_boss.draw(self.screen)
            if self.boss.health > 0:
                boss_health_bar_width = int(self.boss.health / 2000 * self.boss_health_bar_rect.width)
                boss_health_bar_green_rect = pygame.Rect(self.boss_health_bar_rect.left, self.boss_health_bar_rect.top, boss_health_bar_width, self.boss_health_bar_rect.height)
                boss_health_bar_red_rect = pygame.Rect(self.boss_health_bar_rect.left + boss_health_bar_width, self.boss_health_bar_rect.top, self.boss_health_bar_rect.width - boss_health_bar_width, self.boss_health_bar_rect.height)
                pygame.draw.rect(self.screen, (0, 255, 0), boss_health_bar_green_rect)
                pygame.draw.rect(self.screen, (255, 0, 0), boss_health_bar_red_rect)
            pygame.display.flip()
        else:
            self.gameover.update(self.screen)

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
