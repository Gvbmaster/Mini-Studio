import pygame

class Heal():
    def __init__(self):
        self.idEffect = 1
        self.image = pygame.image.load("img/Life.png").convert_alpha()
        self.imageWidth = 151.25
        self.imageHeight = 146.5
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        