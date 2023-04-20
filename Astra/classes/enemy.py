import pygame

from classes.values import *

class Enemy(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/EnemyTest.png").convert_alpha()
        self.imageWidth = 75.5
        self.imageHeight = 40.9
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.image = pygame.transform.rotate(self.image,90)
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