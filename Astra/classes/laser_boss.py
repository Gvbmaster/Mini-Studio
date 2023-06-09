import pygame

from classes.values import *

class Laser3(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/big-laser-samere-boss.png").convert_alpha()
        self.imageWidth = 260
        self.imageHeight = 1080
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self._kill = False
        self.has_buff = False

    def collide_rect(self, rect):
        if self._kill:
            return False
        return self.rect.colliderect(rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def kill(self):
        super().kill()
        self._kill = True