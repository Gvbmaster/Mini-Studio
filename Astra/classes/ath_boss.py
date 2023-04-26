import pygame
from classes.values import *

class ATH():
    def __init__(self):
        self.healthBar = pygame.image.load("img/pixel_art/lifebare.png").convert_alpha()
        self.rectHealthBar = self.healthBar.get_rect(x=25, y=850)
        self.lifePoint = pygame.image.load("img/pixel_art/life.png").convert_alpha()
        self.lifePoint = pygame.transform.scale(self.lifePoint,(80,65))

    def update(self):
        pass

    def draw(self, screen):
        if PlayerStats.currentHealth == 1:
            rectLifePoint1 = self.lifePoint.get_rect(x=205, y=900)
            screen.blit(self.lifePoint, rectLifePoint1)
        elif PlayerStats.currentHealth == 2:
            rectLifePoint1 = self.lifePoint.get_rect(x=205, y=900)
            rectLifePoint2 = self.lifePoint.get_rect(x=283,  y=900)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
        elif PlayerStats.currentHealth == 3:
            rectLifePoint1 = self.lifePoint.get_rect(x=205, y=900)
            rectLifePoint2 = self.lifePoint.get_rect(x=283,  y=900)
            rectLifePoint3 = self.lifePoint.get_rect(x=360, y=900)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
            screen.blit(self.lifePoint, rectLifePoint3)
        screen.blit(self.healthBar, self.rectHealthBar)

        