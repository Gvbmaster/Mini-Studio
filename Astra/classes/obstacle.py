import pygame
import random

from classes.values import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y,image_path="img/Asteroid-{}.png".format(random.randint(1, 20))):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.imageWidth = 100
        self.imageHeight = 80
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ObstacleStats.speed
        self.velocity = [-1, 0]
        self._kill = False
        self.has_buff = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def collide_rect(self, rect):
        if self._kill:
            return False
        return self.mask.overlap(pygame.mask.from_surface(rect), (rect.left - self.rect.left, rect.top - self.rect.top)) is not None

    def draw(self, screen):
        screen.blit(self.mask.to_surface(), self.rect)
        
    def kill(self):
        super().kill()
        self._kill = True
