import pygame

from classes.values import *

class Laser(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/big-laser-samere.png").convert_alpha()
        self.imageWidth = 1920
        self.imageHeight = 260
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.mask = pygame.mask.from_surface(self.image)
        self._kill = False
        self.has_buff = False

    def collide_mask(self, sprite):
        if self._kill:
            return False
        offset = (sprite.rect.x - self.rect.x, sprite.rect.y - self.rect.y)
        return self.mask.overlap(sprite.mask, offset)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def kill(self):
        super().kill()
        self._kill = True