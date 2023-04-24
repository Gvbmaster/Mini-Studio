import pygame
from pygame.locals import *
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.ath import ATH
from classes.backgroundPixel import Background
from classes.projectile import *
from classes.gameover import *
from classes.obstacle import *
from classes.values import *
from classes.warning import *
from classes.laser import *

from classes.enemy import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.ls = LifeSystem(self)
        self.gameover = GameoverLP(self)
        self.player = Player(50,500)
        self.buff = [Buff(750,450,2),Buff(850,450,2),Buff(950,450,2),Buff(1050,450,2)]
        self.buff1 =[Buff(750,550,1),Buff(850,550,1),Buff(950,550,1),Buff(1050,550,1)]
        self.buff2=[Buff(750,250,3),Buff(850,250,3),Buff(950,250,3),Buff(1050,250,3)]
        #####INTEGRATION LASER ET OBSTACLES###########
        self.obstacle = None                                    #|
        self.obstacles = []                                     #|
        self.obstacle_spawn_event = pygame.USEREVENT + 1        #|
        pygame.time.set_timer(self.obstacle_spawn_event, 2000)  #|innitialisation des obstacle et de leur event d'apparition
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
        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy=[Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])]
        
        EnnemieStats.enemyAlive=len(self.enemy)
        ###################################
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.buff, self.buff1,self.buff2, self.enemy)
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
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam.png", (100,90))
            self.all_sprites.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################
    def update(self):
        self.player.move()

        for buff in self.buff:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                PlayerStats.shield = True
                print("Buff catch and del")
                print(PlayerStats.shield)
        
        for buff in self.buff1:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                self.ls.healthPlayerUpdate(2)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        for buff in self.buff2:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                self.ls.healthPlayerUpdate(buff)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
            for obstacle in self.obstacles:
                if obstacle.collide_rect(self.player.rect):
                    self.ls.healthPlayerUpdate(obstacle)
                    print("Player take hit")
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
                    self.ls.healthPlayerUpdate(laser)
                    print("Player take hit")
                    print(PlayerStats.currentHealth)

        if EnnemieStats.enemyAlive==0:
            EnnemieStats.pattern=0
            EnnemieStats.pattern=random.randint(0,1)
            self.enemy=[Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][1][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][1][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][2][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][2][1]),
                        Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][3][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][3][1])]
            self.all_sprites.add(self.enemy)
            EnnemieStats.enemyAlive=len(self.enemy)
        
        for i in range (len(self.enemy)):
            if self.enemy[i].collide_rect(self.player.rect):
                self.enemy[i].kill()
                self.all_sprites.remove(self.enemy[i])
                self.ls.healthPlayerUpdate(3)
            if self.enemy[i].rect.x <= 200 - self.enemy[i].imageWidth:
                self.enemy[i].kill()
                self.all_sprites.remove(self.enemy[i])
            else:
                self.enemy[i].move()
            # print(EnnemieStats.enemyAlive)
    

    def display(self):
        if PlayerStats.currentHealth > 0:
            self.background.update()
            self.screen.fill("black")
            self.background.draw(self.screen)
            #pygame.draw.rect(self.screen, self.area_color, self.area)
            self.all_sprites.draw(self.screen)
            self.player.draw(self.screen)
            self.ath.draw(self.screen)
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

game = Game(screen)
game.run()

pygame.quit()
