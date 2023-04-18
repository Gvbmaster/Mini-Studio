import pygame
from classes.entity import *
from classes.values import *
from classes.projectile import*

class Player(Entity):
    def __init__(self, x, y, speed, image_path, image_size):
        super().__init__(x, y, speed, image_path, image_size)
        self.projectiles = pygame.sprite.Group()  # Créer un groupe de projectiles pour le joueur
    
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

        # On l'empêche de sortir de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Param.screenWidth:
            self.rect.right = Param.screenWidth
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Param.screenHeight:
            self.rect.bottom = Param.screenHeight
    
    def fire_projectile(self):
        projectile = Projectile(self.rect.centerx, self.rect.top, 10, "Astra/img/pixel_laser_yellow.png", (100, 90))
        self.projectiles.add(projectile)