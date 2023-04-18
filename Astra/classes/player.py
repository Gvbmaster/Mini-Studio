import pygame
from classes.entity import *
from classes.values import *
from classes.projectile import*

class Player(Entity):
    def __init__(self, x, y, speed, image_path, image_size):
        super().__init__(x, y, speed, image_path, image_size)
        

    def update(self):
        # les mouvements
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # On l'emp�che de sortir de l'�cran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Param.screenWidth:
            self.rect.right = Param.screenWidth
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Param.screenHeight:
            self.rect.bottom = Param.screenHeight

    