import pygame

from classes.values import *

class WarningLogo(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/warning.png").convert_alpha()
        self.imageWidth = 85
        self.imageHeight = 85
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self._kill = False
        self.has_buff = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def kill(self):
        super().kill()
        self._kill = True
