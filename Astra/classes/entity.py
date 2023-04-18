import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Entity(Sprite):
    def __init__(self, x, y, speed, image_path, image_size):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, image_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide_with(self, other_entity):
        return self.rect.colliderect(other_entity.rect) and \
            self.mask.overlap_mask(other_entity.mask, (other_entity.rect.x - self.rect.x, other_entity.rect.y - self.rect.y))