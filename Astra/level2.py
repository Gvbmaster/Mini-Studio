import sys
import pygame
from pygame.locals import *
from classes.player import Player
# from classes.buff import Buff
from classes.lifesystem import *
from classes.ath_cartoon import ATH2
from classes.backgroundPixel import Background
from classes.projectile import *
from classes.effect.invicibility import *

from classes.obstacle import *
from classes.values import *
from classes.warning import *
from classes.laser2 import *
from classes.energy import *
from classes.projectileEn import *
from classes.enemy2 import *

import gameover

from level3 import *

class Level2:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background(image_path="img/old_cartoon/FOND/fond cartoon.png")
        self.ath = ATH2()
        self.ls = LifeSystem(self)
        self.gameover = gameover.GameoverLP(self)
        self.player = Player(0,500,image_path="img/old_cartoon/vaisseaux1__.png")
        # self.buff = [Buff(750,450,2),Buff(850,450,2),Buff(950,450,2),Buff(1050,450,2)]
        # self.buff1 =[Buff(750,550,1),Buff(850,550,1),Buff(950,550,1),Buff(1050,550,1)]
        # self.buff2=[Buff(750,250,3),Buff(850,250,3),Buff(950,250,3),Buff(1050,250,3)]
        #####INTEGRATION LASER ET OBSTACLES###########
        self.obstacle = None                                    #|
        self.obstacles = []                                     #|
        self.obstacle_spawn_event = pygame.USEREVENT + 1        #|
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)  #|innitialisation des obstacle et de leur event d'apparition
        self.energy_bar = Energy(650, 900, 600, 100, "img/old_cartoon/emptybar_old_cartoon.png", "img/old_cartoon/fullbar_old_cartoon.png")
        self.laser_position = [10, 280, 550, 820]               #|
        self.laserPosition1 = None                              #|
        self.laserPosition2 = None                              #|
        self.laser = None                                       #|
        self.warning1 = None                                    #|
        self.warning2 = None                                    #|
        self.lasers = []                                        #|
        self.laser_spawn_event = pygame.USEREVENT + 2           #|
        pygame.time.set_timer(self.laser_spawn_event, 15000)    #|initialisation des events de laser et de warning
        #####INTEGRATION ENNEMIS###########
        self.enemy = pygame.sprite.Group()
        print("ok")
        EnnemieStats.pattern=0
        EnnemieStats.pattern=random.randint(0,len(EnnemieStats.patternSpawn)-1)
        self.enemy1=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
        self.enemy2=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
        self.enemy3=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
        self.enemy4=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
        self.enemy5=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][4][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][4][1])
        self.enemy6=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][5][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][5][1])
        self.enemy7=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][6][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][6][1])
        self.enemy8=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][7][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][7][1])
        self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4,self.enemy5,self.enemy6,self.enemy7,self.enemy8)
        EnnemieStats.enemyAlive=len(self.enemy)
        ###################################
        self.sprite_player = pygame.sprite.Group()
        self.all_sprites_layer_1 = pygame.sprite.Group() #liste de sprite pour les lasers
        self.all_sprites_layer_2 = pygame.sprite.Group() #liste de sprite pour le joueur/ennemis/obstacles/buffs
        self.sprite_player.add(self.player)
        self.all_sprites_projectilesMC = pygame.sprite.Group() #liste de sprite pour les tir du MC
        self.all_sprites_projectilesEn = pygame.sprite.Group() #liste de sprite pour les tir du En
        self.all_sprites_layer_2.add(self.enemy)#,self.buff, self.buff1, self.buff2)
        
        
        
        self.space_pressed = False # Pour le tir auto
        self.energy_full = False
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto
        self.last_shot_timeEn = 0  # Initialiser à 0 pour le tir auto
        self.combo=0

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
#évènement d'apparition d'obtacle à des coordonées y aléatoire toutes les 2 sec
            if event.type == self.obstacle_spawn_event:
                obstacle = Obstacle(1920, random.randint(0, 1080),"img/old_cartoon/FOND/planet-{}.png".format(random.randint(1, 3)))
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
                if self.warning1 != None:
                    self.warning1.kill()
                if self.warning2 != None:
                    self.warning2.kill()
                self.all_sprites_layer_1.remove(self.warning1)
                self.all_sprites_layer_1.remove(self.warning2)
                if self.warning1 != None:
                    laser1 = Laser2(0, self.laserPosition1)
                    self.lasers.append(laser1)
                    self.all_sprites_layer_1.add(laser1)
                if self.warning2 != None:
                    laser2 = Laser2(0, self.laserPosition2)
                    self.lasers.append(laser2)
                    self.all_sprites_layer_1.add(laser2)
                pygame.time.set_timer(pygame.USEREVENT + 4, 3000)
    #disparition des lasers après 3 sec
            if event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)
                for sprite in self.all_sprites_layer_1:
                    if isinstance(sprite, Laser2):
                        sprite.kill()
                        self.lasers.remove(sprite)
            
############################ Tir automatique du vaisseau ######################################################################################
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    #print("Espace pressé")
                    self.space_pressed = True
            if event.type == pygame.KEYUP and event.key == K_SPACE:
                    #print("Espace relâché")
                    self.space_pressed = False
        self.all_sprites_layer_2.update()
        self.all_sprites_projectilesMC.update()
        current_time = pygame.time.get_ticks()  # Obtenir le temps actuel en millisecondes
        if self.space_pressed and current_time - self.last_shot_time >= PlayerStats.attackSpeed:  # Limiter le tir a la class PlayerStats qui est dans values qui est donc 250
            # Créer une instance de Projectile à la position du joueur
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam.png", (100,90))
            self.all_sprites_projectilesMC.add(projectile)
            self.all_sprites_layer_2.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
############################ Tir automatique du vaisseau ######################################################################################
        self.all_sprites_layer_2.update()
        self.all_sprites_projectilesEn.update() 
        current_timeEn = pygame.time.get_ticks()  # Obtenir le temps actuel en millisecondes
        if current_timeEn - self.last_shot_timeEn >= EnnemieStats.attackSpeed:  # Limiter le tir a la class EnnemieStats qui est dans values qui est donc 250
            # Créer une instance de Projectile à la position de l'ennemi
            if self.enemy1 in self.enemy:
                projectileEn1 = ProjectileEn(self.enemy1.rect.centerx, self.enemy1.rect.bottom , EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn1)
            if self.enemy2 in self.enemy:
                projectileEn2 = ProjectileEn(self.enemy2.rect.centerx, self.enemy2.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn2)
            if self.enemy3 in self.enemy:
                projectileEn3 = ProjectileEn(self.enemy3.rect.centerx, self.enemy3.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn3)
            if self.enemy4 in self.enemy:
                projectileEn4 = ProjectileEn(self.enemy4.rect.centerx, self.enemy4.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn4)
            if self.enemy5 in self.enemy:
                projectileEn5 = ProjectileEn(self.enemy5.rect.centerx, self.enemy5.rect.bottom , EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn5)
            if self.enemy6 in self.enemy:
                projectileEn6 = ProjectileEn(self.enemy6.rect.centerx, self.enemy6.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn6)
            if self.enemy7 in self.enemy:
                projectileEn7 = ProjectileEn(self.enemy7.rect.centerx, self.enemy7.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn7)
            if self.enemy8 in self.enemy:
                projectileEn8 = ProjectileEn(self.enemy8.rect.centerx, self.enemy8.rect.bottom, EnnemieStats.attackVelocity, "img/old_cartoon/balle cartoon.png", (60,20))
                self.all_sprites_projectilesEn.add(projectileEn8)
            self.all_sprites_layer_2.add(self.all_sprites_projectilesEn)#projectileEn1,projectileEn2,projectileEn3,projectileEn4)
            self.last_shot_timeEn = current_timeEn  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
    def update(self):
        keys = pygame.key.get_pressed() # Appel de la détection de touche préssé

        if keys[pygame.K_q] :
            if self.player.rect.x>0:
                self.player.velocity[0] = -1 
                PlayerStats.attackSpeed = 75 # Regulation de la cadence de tir par rapport au fait qu'on recul
                # #print("left press")
            else:
                PlayerStats.attackSpeed = 100
                self.player.velocity[0]=0
        elif keys[pygame.K_d] :
            if self.player.rect.x<1750:
                self.player.velocity[0] = 1
                PlayerStats.attackSpeed = 175 # Regulation de la cadence de tir par rapport au fait qu'on avance
                # #print("right press")
            else:
                PlayerStats.attackSpeed = 100
                self.player.velocity[0]=0
        else:
            self.player.velocity[0] = 0
            
            
        if keys[pygame.K_z] :
            if self.player.rect.y>0:
                self.player.velocity[1] = -1
                # #print("up press")
                PlayerStats.attackSpeed = 100
            else:
                self.player.velocity[1] = 0
        elif keys[pygame.K_s] :
            if self.player.rect.y<1000:
                self.player.velocity[1] = 1
                # #print("down press")
                PlayerStats.attackSpeed = 100
            else:
                self.player.velocity[1] = 0
        else:
            self.player.velocity[1] = 0

        self.player.move()

        # for buff in self.buff:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         PlayerStats.shield = True
        #         #print("Buff catch and del")
        #         #print(PlayerStats.shield)
        
        # for buff in self.buff1:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         self.ls.healthPlayerUpdate(2)
        #         #print("Buff catch and del")
        #         #print(PlayerStats.currentHealth)

        # for buff in self.buff2:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         self.ls.healthPlayerUpdate(buff)
        #         Invicibility.update()
        #         #print("Buff catch and del")
        #         #print(PlayerStats.currentHealth)


        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
        for obstacle in self.obstacles:
            if obstacle.collide_rect(self.player.rect):
                Invicibility.update()
                self.ls.healthPlayerUpdate(obstacle)
                self.combo=0
                #print("Player take hit")
                #print(PlayerStats.currentHealth)
            if obstacle.rect.x <= 0 - obstacle.imageWidth:
                obstacle.kill()
                self.all_sprites_layer_2.remove(obstacle)
                self.obstacles.remove(obstacle)
            else:
                obstacle.move()

        #chaque laser provoque des dégâts
        for laser in self.lasers:
            if laser.collide_rect(self.player.rect):
                Invicibility.update()
                self.ls.healthPlayerUpdate(laser)
                #print("Player take hit")
                #print(PlayerStats.currentHealth)

        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,len(EnnemieStats.patternSpawn)-1)
            self.enemy1=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
            self.enemy2=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
            self.enemy3=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
            self.enemy4=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
            self.enemy5=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][4][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][4][1])
            self.enemy6=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][5][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][5][1])
            self.enemy7=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][6][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][6][1])
            self.enemy8=Enemy2(EnnemieStats.patternSpawn[EnnemieStats.pattern][7][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][7][1])
            self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4,self.enemy5,self.enemy6,self.enemy7,self.enemy8)
            self.all_sprites_layer_2.add(self.enemy)
            EnnemieStats.enemyAlive=len(self.enemy)


        for enemy in self.enemy:
            if enemy.collide_rect(self.player.rect):
                self.ls.healthPlayerUpdate(3)
                Invicibility.update()
                self.combo=0

        self.enemy1.move()
        self.enemy2.move()
        self.enemy3.move()
        self.enemy4.move()
        self.enemy5.move()
        self.enemy6.move()
        self.enemy7.move()
        self.enemy8.move()

        for projectile in self.all_sprites_projectilesMC:
            if projectile.rect.left > 1920:
                projectile.kill()
                # #print("Tir sortie de l'ecran ")
            elif self.enemy1.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy1)
                # #print("Ennemi Toucher !!!")
            elif self.enemy2.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy2)
            elif self.enemy3.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy3)
            elif self.enemy4.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy4)
            elif self.enemy5.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy5)
            elif self.enemy6.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy6)
            elif self.enemy7.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy7)
            elif self.enemy8.collide_rect(projectile):
                projectile.kill()
                if self.energy_bar.energy < 100 :
                    self.energy_bar.set_energy(self.energy_bar.energy + 5)
                if self.combo<10:
                    self.combo+=1
                print(self.combo)
                Enemy2.healthEnemyUpdate(self.enemy8)

        for projectileEn1 in self.all_sprites_projectilesEn:
            if projectileEn1.rect.left < 0:
                projectileEn1.kill()
                #print("Tir sortie de l'ecran ")
            elif pygame.sprite.spritecollide(projectileEn1, self.sprite_player, False):
                projectileEn1.kill()
                self.combo=0
                self.ls.healthPlayerUpdate(3)
                Invicibility.update()
                #print("Allier Toucher !!!")

        keys = pygame.key.get_pressed()
        r_pressed = keys[pygame.K_r]
        
        if self.energy_bar.energy == 100:
            self.energy_full = True

        if self.energy_full and r_pressed:

            BLACK = (0, 0, 0)
            alpha = 0

            
            for i in range(255):
                alpha += 0.1
                black_screen = pygame.Surface(self.screen.get_size())
                black_screen.set_alpha(alpha)
                self.screen.blit(black_screen, (0, 0))
                black_screen.fill(BLACK)
                pygame.display.update()
                pygame.time.delay(1)

            
            level3 = Level3(self.screen)
            level3.run()
            pygame.quit()
            sys.exit()
            

    def display(self):
        if PlayerStats.currentHealth > 0:
            self.background.update()
            self.screen.fill("black")
            self.background.draw(self.screen)
            self.all_sprites_layer_1.draw(self.screen)
            self.all_sprites_layer_2.draw(self.screen)
            self.sprite_player.draw(self.screen)
            self.ath.draw(self.screen)
            self.energy_bar.update()
            self.energy_bar.fill_rect_rect.x = self.energy_bar.rect.x
            self.energy_bar.fill_rect_rect.y = self.energy_bar.rect.y
            self.screen.blit(self.energy_bar.image, self.energy_bar.rect)
            self.screen.blit(self.energy_bar.fill_rect, self.energy_bar.fill_rect_rect)
            self.energy_bar.update()
            self.energy_bar.fill_rect_rect.x = self.energy_bar.rect.x
            self.energy_bar.fill_rect_rect.y = self.energy_bar.rect.y
            self.screen.blit(self.energy_bar.image, self.energy_bar.rect)
            self.screen.blit(self.energy_bar.fill_rect, self.energy_bar.fill_rect_rect)
            pygame.display.flip()
        else:
            self.gameover.update(self.screen)

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)