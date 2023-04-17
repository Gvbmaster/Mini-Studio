import pygame

from player import player

class Shield():
    def __init__(self,x,y):
        self.imageShield = pygame.image.load("img/Shield.png").convert_alpha()
        self.imageWidth = 101.25
        self.imageHeight = 105.5
        self.imageShield = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
    