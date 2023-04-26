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
from classes.rectangle import *
from classes.text import *

class Tuto:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.ls = LifeSystem(self)
        self.player = Player(50,500)

######### OBSTACLE INIT ###############
        self.obstacles = []
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_y = None
        self.obstacle = None
        self.obstacle_tuto_event = pygame.USEREVENT + 100
#####################################

######### TEXTE INIT ###################
        self.isRectDrawable = True
        self.zoneTexte = Rectangle()
        self.zPress = False
        self.qPress = False
        self.sPress = False
        self.dPress = False
        self.spacePress = False
        self.text = "Pour vous déplacer, utilisez les touches Z Q S D !"
        self.font = pygame.font.Font('font/TurretRoad-Regular.ttf', 60)
        self.textDraw = Text(self.font, self.text, 800)
#########################################

############# ENEMY INIT ##############################
        self.enemy_group = pygame.sprite.Group()
#######################################################

        self.all_sprites_layer_2 = pygame.sprite.Group()
        self.all_sprites_layer_2.add(self.obstacle_group)



    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        #event d'apparition des obstacles
            if event.type == self.obstacle_tuto_event :
                # print("ça fontionne walla")
                pygame.time.set_timer(self.obstacle_tuto_event, 0)
                self.obstacle_y = 0
                while self.obstacle_y < 1080:
                    print("new obstacle")
                    obstacle = Obstacle(1920, self.obstacle_y)
                    self.obstacles.append(obstacle)
                    # self.obstacle_group.add(obstacle)
                    self.all_sprites_layer_2.add(obstacle)
                    self.obstacle_y = self.obstacle_y + 100

        #touches de déplacement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] :
                self.qPress = True
                self.player.velocity[0] = -1 
                PlayerStats.attackSpeed = 75
            elif keys[pygame.K_d] :
                self.dPress = True
                self.player.velocity[0] = 1
                PlayerStats.attackSpeed = 175
            else:
                self.player.velocity[0] = 0
                    
            if keys[pygame.K_z] :
                self.zPress = True
                self.player.velocity[1] = -1
                PlayerStats.attackSpeed = 100
            elif keys[pygame.K_s] :
                self.sPress = True
                self.player.velocity[1] = 1
                PlayerStats.attackSpeed = 100
            else:
                self.player.velocity[1] = 0

        self.obstacle_group.update()
        self.all_sprites_layer_2.update()


    def update(self):
        self.player.move()

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
        for obstacle in self.obstacles:
            if pygame.sprite.spritecollide(obstacle, self.player, False):
                Invicibility.update(self)
                self.ls.healthPlayerUpdate(obstacle)
                print("Player take hit")
                print(PlayerStats.currentHealth)
            if obstacle.rect.x <= 0 - obstacle.imageWidth:
                obstacle.kill()
                self.obstacle_group.remove(obstacle)
                self.obstacles.remove(obstacle)
            else:
                obstacle.move()


    def display(self):
        self.background.update()
        self.screen.fill("black")
        self.background.draw(self.screen)
        if self.isRectDrawable == True :
            Rectangle.draw(self)
            self.textDraw.drawText(self.screen, 550, 180)
            if self.zPress == self.qPress == self.sPress == self.dPress == True:
                self.isRectDrawable = False
                pygame.time.set_timer(self.obstacle_tuto_event, 2000)
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