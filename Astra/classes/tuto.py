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
        # self.all_sprites_layer_2 = pygame.sprite.Group()

        self.enemy = pygame.sprite.Group()


    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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
            
            if keys[pygame.K_z] :
                self.isRectDrawable = False

    def update(self):
        self.player.move()


    def display(self):
        self.background.update()
        self.screen.fill("black")
        self.background.draw(self.screen)
        # Rectangle.draw(self)
        if self.isRectDrawable == True :
            Rectangle.draw(self)
            self.textDraw.drawText(self.screen, 550, 180)
            if self.zPress == True and self.qPress == True and self.sPress == True and self.dPress == True:
                pass
        self.player.draw(self.screen)
        self.ath.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)