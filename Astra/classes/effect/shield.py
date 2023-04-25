import pygame

class Shield():
    def __init__(self):
        self.idEffect = 2
        self.image = pygame.image.load("img/Shield.png").convert_alpha()
        self.imageWidth = 151.25
        self.imageHeight = 146.5
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))