import pygame

class Heal():
    def __init__(self):
        self.idBuff = 1
        self.imageShield = pygame.image.load("img/Life.png").convert_alpha()
        self.imageWidth = 101.25
        self.imageHeight = 105.5
        self.imageShield = pygame.transform.scale(self.imageShield,(int(self.imageWidth), int(self.imageHeight)))
        