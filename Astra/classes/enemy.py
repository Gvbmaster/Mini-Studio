import pygame
from classes.entity import *
from classes.values import *

class Enemy(Entity):
    def __init__(self, x, y, speed, image_path, image_size):
        super().__init__(x, y, speed, image_path, image_size)       

    def draw(self, screen):
        screen.blit(self.image, self.rect)