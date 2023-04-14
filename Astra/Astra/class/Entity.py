import pygame
from pygame.locals import *

class Entity:
    def __init__(self, x, y, speed, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)