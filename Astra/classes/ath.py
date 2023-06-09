import pygame
from classes.values import *

class ATH():
    def __init__(self):
        self.healthBar = pygame.image.load("img/healthBarLowPoly.png").convert_alpha()
        self.rectHealthBar = self.healthBar.get_rect(x=25, y=25)
        self.lifePoint = pygame.image.load("img/lifePointLowPoly.png").convert_alpha()
        self.lifePoint = pygame.transform.scale(self.lifePoint,(169,124))

    def update(self):
        pass

    def draw(self, screen):
        if PlayerStats.currentHealth == 1:
            rectLifePoint1 = self.lifePoint.get_rect(x=75, y=93)
            screen.blit(self.lifePoint, rectLifePoint1)
        elif PlayerStats.currentHealth == 2:
            rectLifePoint1 = self.lifePoint.get_rect(x=75, y=93)
            rectLifePoint2 = self.lifePoint.get_rect(x=158,  y=92)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
        elif PlayerStats.currentHealth == 3:
            rectLifePoint1 = self.lifePoint.get_rect(x=75, y=93)
            rectLifePoint2 = self.lifePoint.get_rect(x=158,  y=92)
            rectLifePoint3 = self.lifePoint.get_rect(x=240, y=92)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
            screen.blit(self.lifePoint, rectLifePoint3)
        screen.blit(self.healthBar, self.rectHealthBar)

        