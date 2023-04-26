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
from level1 import Level1

class Tuto:
    def __init__(self, screen):
#########################################################
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.ls = LifeSystem(self)
        self.player = Player(50,500)
        self.all_sprites_layer_2 = pygame.sprite.Group()
        self.tuto_fini = pygame.USEREVENT + 1000
###########################################################        

############## OBSTACLE INIT ###############
        self.obstacles = []
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_y = None
        self.obstacle = None
        self.obstacle_tuto_event = pygame.USEREVENT + 100
        self.all_sprites_layer_2.add(self.obstacle_group)
#####################################

############## TEXTE INIT ###################
        self.text_tuto_event_01 = pygame.USEREVENT + 1
        pygame.time.set_timer(self.text_tuto_event_01, 500)
        self.text_tuto_event_02 = pygame.USEREVENT + 2
        self.text_tuto_event_03 = pygame.USEREVENT + 3
        self.text_tuto_event_03_depop = pygame.USEREVENT + 33
        self.text_tuto_event_04 = pygame.USEREVENT + 4
        self.text_tuto_event_04_depop = pygame.USEREVENT + 44
        self.is_rect_drawable_01 = False
        self.is_rect_drawable_02 = False
        self.is_rect_drawable_03 = False
        self.is_rect_drawable_04 = False
        self.zoneTexte = Rectangle()
        self.zPress = False
        self.qPress = False
        self.sPress = False
        self.dPress = False
        self.spacePress = False
        self.text01 = "Pour vous déplacer, utilisez les touches Z Q S D !"
        self.text02 = "Pour tirer, utilisez la touche ESPACE. Détruisez cet ennemi !"
        self.text03 = "Attention !!!"
        self.text04 = "Les astéroïdes vous infligeront des dégâts, soyez vigilant !"
        self.text05 = "Pour vous soigner, récupérez des coeurs comme celui-ci !"
        self.font = pygame.font.Font('font/TurretRoad-Regular.ttf', 60)
        self.textDraw = None
#########################################

############# ENEMY INIT ##############################
        self.enemy_tuto_event = pygame.USEREVENT +200
        self.enemy = pygame.sprite.Group()
        self.enemyTuto = None
#######################################################

############# PLAYER INIT #########################
        self.sprite_player = pygame.sprite.Group()
        self.sprite_player.add(self.player)
###################################################
        
############# TIR INIT #################################
        self.all_sprites_projectilesMC = pygame.sprite.Group()
        self.spacePress = False
        self.last_shot_time = 0
        self.last_shot_timeEn = 0
#########################################################

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        #event d'apparition de la zone de text n°01
            if event.type == self.text_tuto_event_01:
                pygame.time.set_timer(self.text_tuto_event_01, 0)
                self.is_rect_drawable_01 = True

        #event d'apparition de la zone de text n°02
            if event.type == self.text_tuto_event_02:
                pygame.time.set_timer(self.text_tuto_event_02, 0)
                self.is_rect_drawable_02 = True

        #event d'apparition d'un ennemi
            if event.type == self.enemy_tuto_event :
                self.enemyTuto=Enemy(EnnemieStats.patternSpawn[EnnemieStats.pattern][0][0],EnnemieStats.patternSpawn[EnnemieStats.pattern][0][1])
                self.enemy.add(self.enemyTuto)
                self.all_sprites_layer_2.add(self.enemy)
                pygame.time.set_timer(self.enemy_tuto_event, 0)                
            
        #event d'apparition de la zone de texte n°03
            if event.type == self.text_tuto_event_03 :
                pygame.time.set_timer(self.text_tuto_event_03, 0)
                self.is_rect_drawable_03 = True
                pygame.time.set_timer(self.text_tuto_event_03_depop, 2000)

        #event de disparition de la zone de texte n°03
            if event.type == self.text_tuto_event_03_depop :
                pygame.time.set_timer(self.text_tuto_event_03_depop, 0)
                self.is_rect_drawable_03 = False

        #event d'apparition des obstacles
            if event.type == self.obstacle_tuto_event :
                pygame.time.set_timer(self.obstacle_tuto_event, 0)
                self.obstacle_y = 0
                while self.obstacle_y < 1080:
                    obstacle = Obstacle(1920, self.obstacle_y)
                    self.obstacles.append(obstacle)
                    self.all_sprites_layer_2.add(obstacle)
                    self.obstacle_y = self.obstacle_y + 100

        #event d'apparition de la zone de texte n°04
            if event.type == self.text_tuto_event_04 :
                pygame.time.set_timer(self.text_tuto_event_04, 0)
                self.is_rect_drawable_04 = True

        #event de disparition de la zone de texte n°04
            if event.type == self.text_tuto_event_04_depop :
                pygame.time.set_timer(self.text_tuto_event_04_depop, 0)
                self.is_rect_drawable_04 = False
                pygame.time.set_timer(self.tuto_fini, 3000)

        #event de lancement du niveau 1
            if event.type == self.tuto_fini :
                pass

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

            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                    self.spacePress = True
            if event.type == pygame.KEYUP and event.key == K_SPACE:
                    self.spacePress = False
        self.all_sprites_layer_2.update()
        self.all_sprites_projectilesMC.update()
        current_time = pygame.time.get_ticks()
        if self.spacePress and current_time - self.last_shot_time >= PlayerStats.attackSpeed:
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam.png", (100,90))
            self.all_sprites_projectilesMC.add(projectile)
            self.all_sprites_layer_2.add(projectile)
            self.last_shot_time = current_time

        self.obstacle_group.update()
        self.all_sprites_layer_2.update()
        
        for projectile in self.all_sprites_projectilesMC:
            if projectile.rect.left > 1920:
                projectile.kill()
            elif pygame.sprite.spritecollide(projectile, self.enemy, True):
                projectile.kill()
                pygame.time.set_timer(self.text_tuto_event_03, 2000)

    def update(self):
        self.player.move()

        #chaque obstacle provoque des dégâts et disparait une fois sorti de l'écran
        for obstacle in self.obstacles:
            if pygame.sprite.spritecollide(obstacle, self.sprite_player, False):
                self.ls.healthPlayerUpdate(obstacle)
                Invicibility.update()
                obstacle.kill()
            if obstacle.rect.x <= 0 - obstacle.imageWidth:
                obstacle.kill()
                self.obstacle_group.remove(obstacle)
                self.obstacles.remove(obstacle)
                pygame.time.set_timer(self.text_tuto_event_04, 2000)
            else:
                obstacle.move()              

        if self.enemyTuto!=None:
            print('zrazdaz')
            self.enemyTuto.move()

    def display(self):
        self.background.update()
        self.screen.fill("black")
        self.background.draw(self.screen)
        if self.is_rect_drawable_01 == True :
            Rectangle.draw(self)
            self.textDraw = Text(self.font, self.text01, 800)
            self.textDraw.drawText(self.screen, 550, 180)
            if self.zPress == self.qPress == self.sPress == self.dPress == True:
                self.is_rect_drawable_01 = False
                pygame.time.set_timer(self.text_tuto_event_02, 2000)
                pygame.time.set_timer(self.enemy_tuto_event, 2500)
        if self.is_rect_drawable_02 == True :
            self.textDraw = Text(self.font, self.text02, 800)
            Rectangle.draw(self)
            self.textDraw.drawText(self.screen, 550, 180)
            if self.spacePress == True:
                self.is_rect_drawable_02 = False
        if self.is_rect_drawable_03 == True:
            self.textDraw = Text(self.font, self.text03, 800)
            Rectangle.draw(self)
            self.textDraw.drawText(self.screen, 550, 180)
            pygame.time.set_timer(self.obstacle_tuto_event, 2000)
        if self.is_rect_drawable_04 == True:
            self.textDraw = Text(self.font, self.text04, 800)
            Rectangle.draw(self)
            self.textDraw.drawText(self.screen, 550, 180)
            pygame.time.set_timer(self.text_tuto_event_04_depop, 2000)
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