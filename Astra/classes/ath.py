import pygame
from classes.values import *

class ATH():
    def __init__(self):
        self.healthBar = pygame.image.load("img/healthBar.png").convert_alpha()
        self.rectHealthBar = self.healthBar.get_rect(x=0, y=0)
        self.lifePoint = pygame.image.load("img/lifePoint.png").convert_alpha()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.healthBar, self.rectHealthBar)

        if PlayerStats.currentHealth == 1:
            rectLifePoint1 = self.lifePoint.get_rect(x=50, y=150)
            screen.blit(self.lifePoint, rectLifePoint1)
        elif PlayerStats.currentHealth == 2:
            rectLifePoint1 = self.lifePoint.get_rect(x=50, y=150)
            rectLifePoint2 = self.lifePoint.get_rect(x=50, y=250)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
        elif PlayerStats.currentHealth == 3:
            rectLifePoint1 = self.lifePoint.get_rect(x=50, y=150)
            rectLifePoint2 = self.lifePoint.get_rect(x=50, y=250)
            rectLifePoint3 = self.lifePoint.get_rect(x=50, y=350)
            screen.blit(self.lifePoint, rectLifePoint1)
            screen.blit(self.lifePoint, rectLifePoint2)
            screen.blit(self.lifePoint, rectLifePoint3)