import pygame
<<<<<<< Updated upstream
from classes.values import *

class Obstacle(pygame.sprite.Sprite): 
=======
from pygame.locals import *
from classes.entity import*

class Obstacle(pygame.sprite.Sprite):
>>>>>>> Stashed changes
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/banana.png").convert_alpha()
        self.imageWidth = 100
<<<<<<< Updated upstream
        self.imageHeight = 80
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = ObstacleStats.speed
        self.velocity = [-1, 0]
        self._kill = False
        self.has_buff = False

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
=======
        self.imageHeight = 90
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 0
        self.velocity = [0, 0]
        self._kill = False
>>>>>>> Stashed changes

    def draw(self, screen):
        screen.blit(self.image, self.rect)
