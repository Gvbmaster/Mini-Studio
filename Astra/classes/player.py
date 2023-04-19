import pygame
from classes.values import *

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/ShipTest.png").convert_alpha()
        self.imageWidth = 101.25
        self.imageHeight = 105.5
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.currentHealth = PlayerStats.currentHealth
        self.speed = PlayerStats.speed
        self.attack = PlayerStats.attackDamage
        self.attackSpeed = PlayerStats.attackSpeed
        self.velocity = [0, 0]
        self._kill = False
        self.has_shield = False
        self.shield_images = []

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if PlayerStats.shield == True:
            shield_image = pygame.image.load("img/Shield.png").convert_alpha()
            shield_rect = shield_image.get_rect(center=self.rect.center)
            screen.blit(shield_image, shield_rect)
            self.shield_images.append(shield_image)

        if self.has_shield==True:
            PlayerStats.shield=True
            
        else: 
            PlayerStats.shield = False
            if self.shield_images:
                for image in self.shield_images:
                    self.shield_images.remove(image)
