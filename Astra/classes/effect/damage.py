import pygame

class Damage():
    def __init__(self):
        self.idEffect = 3
        self.image = pygame.image.load("img/Damage.png").convert_alpha()
        self.imageWidth = 151.25
        self.imageHeight = 146.5
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        