import pygame

class Shield():
    def __init__(self):
        self.idBuff = 2
        self.imageShield = pygame.image.load("img/Shield.png").convert_alpha()
        self.imageWidth = 101.25
        self.imageHeight = 105.5
        self.imageShield = pygame.transform.scale(self.imageShield,(int(self.imageWidth), int(self.imageHeight)))
        