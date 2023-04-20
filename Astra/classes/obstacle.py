import pygame
import random

from classes.values import *

class Obstacle(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/Asteroid-00{}.png".format(random.randint(1, 6))).convert_alpha()
        self.imageWidth = 100
        self.imageHeight = 80
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ObstacleStats.speed
        self.velocity = [-1, 0]
        self._kill = False
        self.has_buff = False

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def collide_rect(self, rect):
        if self._kill:
            return False
        return self.rect.colliderect(rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def kill(self):
        super().kill()
        self._kill = True
