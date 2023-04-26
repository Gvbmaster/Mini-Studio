import pygame
from pygame.locals import *
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
<<<<<<< HEAD
from classes.ath_boss import ATH
from classes.backgroundPixel_boss import Background
from classes.projectile_boss import *
=======
from classes.ath import ATH
from classes.backgroundPixel import Background
from classes.projectile import *
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
from classes.boss import *
from classes.effect.invicibility import *

from classes.obstacle import *
from classes.values import *
from classes.warning import *
<<<<<<< HEAD
from classes.laser_boss import *
=======
from classes.laser import *
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b

from classes.enemy import *

from classes.gameover import *

<<<<<<< HEAD
class Level3:
=======
class Game:
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.ls = LifeSystem(self)
        self.gameover = Gameover(self)
<<<<<<< HEAD
        self.player = Player(900,800)
        # self.buff = [Buff(750,450,2),Buff(850,450,2),Buff(950,450,2),Buff(1050,450,2)]
        # self.buff1 =[Buff(750,550,1),Buff(850,550,1),Buff(950,550,1),Buff(1050,550,1)]
        # self.buff2=[Buff(750,250,3),Buff(850,250,3),Buff(950,250,3),Buff(1050,250,3)]
=======
        self.player = Player(0,0)
        self.buff = [Buff(750,450,2),Buff(850,450,2),Buff(950,450,2),Buff(1050,450,2)]
        self.buff1 =[Buff(750,550,1),Buff(850,550,1),Buff(950,550,1),Buff(1050,550,1)]
        self.buff2=[Buff(750,250,3),Buff(850,250,3),Buff(950,250,3),Buff(1050,250,3)]
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
        #####INTEGRATION LASER ET OBSTACLES###########
        self.obstacle = None                                    #|
        self.obstacles = []                                     #|
        self.obstacle_spawn_event = pygame.USEREVENT + 1        #|
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)  #|innitialisation des obstacle et de leur event d'apparition
<<<<<<< HEAD
        self.laser_position = [10, 240, 480, 720, 960, 1200 ,1440, 1680 ]               #|
=======
        self.laser_position = [10, 280, 550, 820]               #|
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
        self.laserPosition1 = None                              #|
        self.laserPosition2 = None                              #|
        self.laser = None                                       #|
        self.warning1 = None                                    #|
        self.warning2 = None                                    #|
        self.lasers = []                                        #|
        self.laser_spawn_event = pygame.USEREVENT + 2           #|
<<<<<<< HEAD
        pygame.time.set_timer(self.laser_spawn_event, 4000)    #|initialisation des events de laser et de warning
        #####INTEGRATION ENNEMIS###########
        # self.enemy = pygame.sprite.Group()
        # if EnnemieStats.enemyAlive==0:
        #     EnnemieStats.pattern=0
        #     EnnemieStats.pattern=random.randint(0,1)
        # self.enemy1=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
        # self.enemy2=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
        # self.enemy3=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
        # self.enemy4=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
        # self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4)
        # EnnemieStats.enemyAlive=len(self.enemy)
=======
        pygame.time.set_timer(self.laser_spawn_event, 15000)    #|initialisation des events de laser et de warning
        #####INTEGRATION ENNEMIS###########
        self.enemy = pygame.sprite.Group()
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
        self.enemy1=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
        self.enemy2=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
        self.enemy3=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
        self.enemy4=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
        self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4)
        EnnemieStats.enemyAlive=len(self.enemy)
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
        ###################################
        self.boss = Boss("Big Boss", 20)
        self.all_sprites_layer_1 = pygame.sprite.Group() #liste de sprite pour les lasers
        self.all_sprites_layer_2 = pygame.sprite.Group() #liste de sprite pour le joueur/ennemis/obstacles/buffs
        self.all_sprites_projectilesMC = pygame.sprite.Group() #liste de sprite pour les tir du MC
        self.all_sprites_boss = pygame.sprite.Group() 
        self.all_sprites_boss.add(self.boss)
<<<<<<< HEAD
        self.all_sprites_layer_2.add()#self.buff, self.buff1, self.buff2)#, self.enemy)
=======
        self.all_sprites_layer_2.add(self.buff, self.buff1, self.buff2, self.enemy)
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
        self.space_pressed = False # Pour le tir auto
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto
        self.boss_health_bar_rect = pygame.Rect(500, 1000, 800, 30) # Rectangle qui représente la barre de vie
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
<<<<<<< HEAD
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
=======
                self.laserPosition2 = random.choice(self.laser_position) 
                while self.laserPosition2 == self.laserPosition1:
                    self.laserPosition2 = random.choice(self.laser_position)
                self.warning1 = WarningLogo(1825, self.laserPosition1 + 110)
                self.warning2 = WarningLogo(1825, self.laserPosition2 + 110)
                self.all_sprites_layer_1.add(self.warning1, self.warning2)
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
                pygame.time.set_timer(pygame.USEREVENT + 3, 2000)
    #disparition des warnings après 2 sec et apparition des laser aux mêmes positions
            if event.type == pygame.USEREVENT + 3:
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)
                self.warning1.kill()
                self.warning2.kill()
<<<<<<< HEAD
                self.warning3.kill()
                self.warning4.kill()
                self.all_sprites_layer_1.remove(self.warning1)
                self.all_sprites_layer_1.remove(self.warning2)
                self.all_sprites_layer_1.remove(self.warning3)
                self.all_sprites_layer_1.remove(self.warning4)
                laser1 = Laser(self.laserPosition1, 0)
                laser2 = Laser(self.laserPosition2, 0)
                laser3 = Laser(self.laserPosition3, 0)
                laser4 = Laser(self.laserPosition4, 0)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.lasers.append(laser3)
                self.lasers.append(laser4)
                self.all_sprites_layer_1.add(laser1, laser2, laser3, laser4)
                pygame.time.set_timer(pygame.USEREVENT + 4, 2000)
    #disparition des lasers après 2 sec
=======
                self.all_sprites_layer_1.remove(self.warning1)
                self.all_sprites_layer_1.remove(self.warning2)
                laser1 = Laser(0, self.laserPosition1)
                laser2 = Laser(0, self.laserPosition2)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.all_sprites_layer_1.add(laser1, laser2)
                pygame.time.set_timer(pygame.USEREVENT + 4, 3000)
    #disparition des lasers après 3 sec
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
            if event.type == pygame.USEREVENT + 4:
                pygame.time.set_timer(pygame.USEREVENT + 4, 0)
                for sprite in self.all_sprites_layer_1:
                    if isinstance(sprite, Laser):
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
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam2.png", (90,110))
            self.all_sprites_projectilesMC.add(projectile)
            self.all_sprites_layer_2.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
    def update(self):
        self.player.move()

<<<<<<< HEAD
        # for buff in self.buff:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         PlayerStats.shield = True
        #         print("Buff catch and del")
        #         print(PlayerStats.shield)
        
        # for buff in self.buff1:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         self.ls.healthPlayerUpdate(2)
        #         print("Buff catch and del")
        #         print(PlayerStats.currentHealth)

        # for buff in self.buff2:
        #     if buff.collide_rect(self.player.rect):
        #         buff.kill()
        #         self.all_sprites_layer_2.remove(buff)
        #         self.ls.healthPlayerUpdate(buff)
        #         Invicibility.update(self)
        #         print("Buff catch and del")
        #         print(PlayerStats.currentHealth)

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
        # for obstacle in self.obstacles:
        #     if obstacle.collide_rect(self.player.rect):
        #         Invicibility.update(self)
        #         self.ls.healthPlayerUpdate(obstacle)
        #         print("Player take hit")
        #         print(PlayerStats.currentHealth)
        #     if obstacle.rect.x <= 0 - obstacle.imageWidth:
        #         obstacle.kill()
        #         self.all_sprites_layer_2.remove(obstacle)
        #         self.obstacles.remove(obstacle)
        #     else:
        #         obstacle.move()
=======
        for buff in self.buff:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites_layer_2.remove(buff)
                PlayerStats.shield = True
                print("Buff catch and del")
                print(PlayerStats.shield)
        
        for buff in self.buff1:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites_layer_2.remove(buff)
                self.ls.healthPlayerUpdate(2)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        for buff in self.buff2:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites_layer_2.remove(buff)
                self.ls.healthPlayerUpdate(buff)
                Invicibility.update(self)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
        for obstacle in self.obstacles:
            if obstacle.collide_rect(self.player.rect):
                Invicibility.update(self)
                self.ls.healthPlayerUpdate(obstacle)
                print("Player take hit")
                print(PlayerStats.currentHealth)
            if obstacle.rect.x <= 0 - obstacle.imageWidth:
                obstacle.kill()
                self.all_sprites_layer_2.remove(obstacle)
                self.obstacles.remove(obstacle)
            else:
                obstacle.move()
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b

        #chaque laser provoque des dégâts
        for laser in self.lasers:
            if laser.collide_rect(self.player.rect):
                Invicibility.update(self)
                self.ls.healthPlayerUpdate(laser)
                print("Player take hit")
                print(PlayerStats.currentHealth)

<<<<<<< HEAD
        # if EnnemieStats.enemyAlive==0:
        #     EnnemieStats.pattern=0
        #     EnnemieStats.pattern=random.randint(0,1)
        #     self.enemy1=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
        #     self.enemy2=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
        #     self.enemy3=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
        #     self.enemy4=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
        #     self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4)
        #     self.all_sprites_layer_2.add(self.enemy)
        #     EnnemieStats.enemyAlive=len(self.enemy)

        # if self.enemy1.collide_rect(self.player.rect):
        #     self.enemy1.kill()
        #     self.enemy.remove(self.enemy1)
        #     self.ls.healthPlayerUpdate(3)
            
        # if self.enemy2.collide_rect(self.player.rect):
        #     self.enemy2.kill()
        #     self.enemy.remove(self.enemy2)
        #     self.ls.healthPlayerUpdate(3)
            
        # if self.enemy3.collide_rect(self.player.rect):
        #     self.enemy3.kill()
        #     self.enemy.remove(self.enemy3)
        #     self.ls.healthPlayerUpdate(3)
            
        # if self.enemy4.collide_rect(self.player.rect):
        #     self.enemy4.kill()
        #     self.enemy.remove(self.enemy4)
        #     self.ls.healthPlayerUpdate(3)

        # self.enemy1.move()
        # self.enemy2.move()
        # self.enemy3.move()
        # self.enemy4.move()

        for projectile in self.all_sprites_projectilesMC :
            # if projectile.rect.left > 1920:
            #     projectile.kill()
            #     print("Tir sortie de l'ecran ")
            # elif pygame.sprite.spritecollide(projectile, self.enemy, True):
            #     projectile.kill()
            #     print("Ennemi Toucher !!!")
            if pygame.sprite.spritecollide(self.boss, self.all_sprites_projectilesMC, True):
=======
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy1=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
            self.enemy2=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
            self.enemy3=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
            self.enemy4=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
            self.enemy.add(self.enemy1,self.enemy2,self.enemy3,self.enemy4)
            self.all_sprites_layer_2.add(self.enemy)
            EnnemieStats.enemyAlive=len(self.enemy)

        if self.enemy1.collide_rect(self.player.rect):
            self.enemy1.kill()
            self.enemy.remove(self.enemy1)
            self.ls.healthPlayerUpdate(3)
            
        if self.enemy2.collide_rect(self.player.rect):
            self.enemy2.kill()
            self.enemy.remove(self.enemy2)
            self.ls.healthPlayerUpdate(3)
            
        if self.enemy3.collide_rect(self.player.rect):
            self.enemy3.kill()
            self.enemy.remove(self.enemy3)
            self.ls.healthPlayerUpdate(3)
            
        if self.enemy4.collide_rect(self.player.rect):
            self.enemy4.kill()
            self.enemy.remove(self.enemy4)
            self.ls.healthPlayerUpdate(3)

        self.enemy1.move()
        self.enemy2.move()
        self.enemy3.move()
        self.enemy4.move()

        for projectile in self.all_sprites_projectilesMC :
            if projectile.rect.left > 1920:
                projectile.kill()
                print("Tir sortie de l'ecran ")
            elif pygame.sprite.spritecollide(projectile, self.enemy, True):
                projectile.kill()
                print("Ennemi Toucher !!!")
            elif pygame.sprite.spritecollide(self.boss, self.all_sprites_projectilesMC, True):
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
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
            #pygame.draw.rect(self.screen, self.area_color, self.area)
            self.all_sprites_layer_1.draw(self.screen)
            self.all_sprites_layer_2.draw(self.screen)
            self.player.draw(self.screen)
            self.ath.draw(self.screen)
            self.all_sprites_boss.update()
            self.all_sprites_boss.draw(screen)
            if self.boss.health > 0:
<<<<<<< HEAD
                boss_health_bar_width = int(self.boss.health / 2000 * self.boss_health_bar_rect.width)
=======
                boss_health_bar_width = int(self.boss.health / 1000 * self.boss_health_bar_rect.width)
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
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

pygame.init()
screen = pygame.display.set_mode((0, 0),FULLSCREEN)

<<<<<<< HEAD
game = Level3(screen)
=======
game = Game(screen)
>>>>>>> b8ac95a69d2859da793dec1c3ba3d5bef6a6261b
game.run()

pygame.quit()
