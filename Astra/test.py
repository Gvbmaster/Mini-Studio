import pygame
from pygame.locals import *
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.ath import ATH
from classes.backgroundPixel import Background
from classes.projectile import *

from classes.effect.invicibility import *

from classes.obstacle import *
from classes.values import *
from classes.warning import *
from classes.laser import *

from classes.enemy import *

from classes.gameover import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.ls = LifeSystem(self)
        self.gameover = Gameover(self)
        self.player = Player(0,0)

         ########INTEGRATION BUFF########################
        self.buff_drop = []
        # self.buff_group = pygame.sprite.Group()
        self.buff_id = None
        self.buff = None
        # self.buff_mouvement = False

        #####INTEGRATION LASER ET OBSTACLES###########
        self.obstacle = None
        self.obstacles = []
        self.obstacle_spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)
        self.laser_position = [10, 280, 550, 820]
        self.laserPosition1 = None
        self.laserPosition2 = None
        self.laser = None
        self.warning1 = None
        self.warning2 = None
        self.lasers = []
        self.laser_spawn_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.laser_spawn_event, 15000)

        #####INTEGRATION ENNEMIS###########
        self.enemy_group = pygame.sprite.Group()
        if EnnemieStats.enemyAlive == 0:
            EnnemieStats.pattern = 0
            EnnemieStats.pattern=random.randint(0,1)
        self.enemy1 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
        self.enemy2 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
        self.enemy3 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
        self.enemy4 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
        self.enemy_group.add(self.enemy1, self.enemy2, self.enemy3, self.enemy4)
        EnnemieStats.enemyAlive = len(self.enemy_group)

        ###################################
        self.all_sprites_layer_1 = pygame.sprite.Group() #liste de sprite pour les lasers
        self.all_sprites_layer_2 = pygame.sprite.Group() #liste de sprite pour le joueur/ennemis/obstacles/buffs
        self.all_sprites_projectilesMC = pygame.sprite.Group() #liste de sprite pour les tir du MC
        self.all_sprites_layer_2.add(self.enemy_group) #possible ajout : self.buff_group
        
        self.space_pressed = False # Pour le tir auto
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto

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

########################### Touches de mouvement ############################################################################################            
            keys = pygame.key.get_pressed() # Appel de la détection de touche préssé
            if keys[pygame.K_q] :
                self.player.velocity[0] = -1 
                PlayerStats.attackSpeed = 75 # Regulation de la cadence de tir par rapport au fait qu'on recul
                # print("left press")
            elif keys[pygame.K_d] : 
                self.player.velocity[0] = 1
                PlayerStats.attackSpeed = 175 # Regulation de la cadence de tir par rapport au fait qu'on avance
                # print("right press")
            else:
                self.player.velocity[0] = 0
                
                
            if keys[pygame.K_z] :
                self.player.velocity[1] = -1
                # print("up press")
                PlayerStats.attackSpeed = 100
            elif keys[pygame.K_s] :
                self.player.velocity[1] = 1
                # print("down press")
                PlayerStats.attackSpeed = 100
            else:
                self.player.velocity[1] = 0
            
############################ Tir automatique du vaisseau ######################################################################################
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    # print("Espace pressé")
                    self.space_pressed = True
            if event.type == pygame.KEYUP and event.key == K_SPACE:
                    # print("Espace relâché")
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


############################# Drop de buff à la mort d'un ennemi ################################################################################
    def drop(self, actual_x, actual_y):
        drop_rate = random.randint(1, 100)  #lance un pourcentage de drop

        if drop_rate > 95 : #10%
            self.buff_id = 2    #drop un shield
            self.buff = Buff(actual_x, actual_y, self.buff_id)
        elif drop_rate > 85 and drop_rate <= 95:    #15%
            self.buff_id = 1    #drop un heal
            self.buff = Buff(actual_x, actual_y, self.buff_id)
        else:
            None
        
        #si un buff est drop il est ajouté à la liste des sprites
        if self.buff_id != None :
            self.all_sprites_layer_2.add(self.buff)
            self.buff_drop.append(self.buff)

            # self.buff_mouvement = True
        # else:
        #     self.buff_mouvement = False

    # Pour un nouveau buff, il faut: 1. un taux de drop en pourcentage
    #                                2. une ID de buff qui correspond à "self.buff_id"
    #                                3. la création d'un Buff avec les coordonées d'apparition et une id
##################################################################################################################################################
        

    def update(self):
        self.player.move()

    # Pour chaque buff il faut créer un if qui vérifie le buff_id qui est drop par l'ennemi et lui assigner le code de collision du buff comme pour les buffs suivants
        for self.buff in self.buff_drop:
            # self.buff_mouvement = False
            if self.buff_id == 2 : #and buff.collide_rect(self.player.rect)
                if self.buff.collide_rect(self.player.rect):
                    self.buff.kill()
                    self.all_sprites_layer_2.remove(self.buff)
                    self.buff_drop.remove(self.buff)
                    PlayerStats.shield = True
                    print("Buff catch and del")
                    print(PlayerStats.shield)
                # if  buff.rect.x <= -200:
                #     buff.kill()
                #     self.all_sprites_layer_2.remove(buff)
                # else:
                #     self.buff_mouvement = True
                # self.buff_mouvement = False
            elif self.buff_id == 1 : #and buff.collide_rect(self.player.rect)
                if self.buff.collide_rect(self.player.rect):
                    self.buff.kill()
                    self.all_sprites_layer_2.remove(self.buff)
                    self.buff_drop.remove(self.buff)
                    self.ls.healthPlayerUpdate(2)
                    print("Buff catch and del")
                    print(PlayerStats.currentHealth)
                # if  buff.rect.x <= -200:
                #     buff.kill()
                #     self.all_sprites_layer_2.remove(buff)
                # else:
                #     self.buff_mouvement = True
                # self.buff_mouvement = False
            # else:
            #     self.buff_mouvement = True

            # if self.buff_mouvement == True :
            #     buff.move()

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

        #chaque laser provoque des dégâts
        for laser in self.lasers:
            if laser.collide_rect(self.player.rect):
                Invicibility.update(self)
                self.ls.healthPlayerUpdate(laser)
                print("Player take hit")
                print(PlayerStats.currentHealth)

        if EnnemieStats.enemyAlive == 0:
            EnnemieStats.pattern = 0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy1 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
            self.enemy2 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1])
            self.enemy3 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1])
            self.enemy4 = Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0], EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])
            self.enemy_group.add(self.enemy1, self.enemy2, self.enemy3, self.enemy4)
            self.all_sprites_layer_2.add(self.enemy_group)
            EnnemieStats.enemyAlive = len(self.enemy_group)

        #pour chaque ennemi il faut récup sa dernière position et l'attribué au drop
        if self.enemy1.collide_rect(self.player.rect):
            #récupération de la dernière position de l'ennemi
            actual_x = self.enemy1.rect.x
            actual_y = self.enemy1.rect.y
            self.enemy1.kill()
            #drop d'un buff avec les coordonées récup
            self.drop(actual_x, actual_y)
            self.enemy_group.remove(self.enemy1)
            self.ls.healthPlayerUpdate(3)
            
            
        if self.enemy2.collide_rect(self.player.rect):
            actual_x = self.enemy2.rect.x
            actual_y = self.enemy2.rect.y
            self.enemy2.kill()
            self.drop(actual_x, actual_y)
            self.enemy_group.remove(self.enemy2)
            self.ls.healthPlayerUpdate(3)
            
        if self.enemy3.collide_rect(self.player.rect):
            actual_x = self.enemy3.rect.x
            actual_y = self.enemy3.rect.y
            self.enemy3.kill()
            self.drop(actual_x, actual_y)
            self.enemy_group.remove(self.enemy3)
            self.ls.healthPlayerUpdate(3)
            
        if self.enemy4.collide_rect(self.player.rect):
            actual_x = self.enemy4.rect.x
            actual_y = self.enemy4.rect.y
            self.enemy4.kill()
            self.drop(actual_x, actual_y)
            self.enemy_group.remove(self.enemy4)
            self.ls.healthPlayerUpdate(3)

        self.enemy1.move()
        self.enemy2.move()
        self.enemy3.move()
        self.enemy4.move()

        for projectile in self.all_sprites_projectilesMC:
            if projectile.rect.left > 1920:
                projectile.kill()
                # print("Tir sortie de l'ecran ")
            elif pygame.sprite.spritecollide(projectile, self.enemy_group, True):
                actual_x = projectile.rect.x
                actual_y = projectile.rect.y
                projectile.kill()
                self.drop(actual_x, actual_y)
                # print("Ennemi Toucher !!!")

    def display(self):
   
            self.background.update()
            self.screen.fill("black")
            self.background.draw(self.screen)
            self.all_sprites_layer_1.draw(self.screen)
            self.all_sprites_layer_2.draw(self.screen)
            self.player.draw(self.screen)
            self.ath.draw(self.screen)
            pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)

game = Game(screen)
game.run()

pygame.quit()
