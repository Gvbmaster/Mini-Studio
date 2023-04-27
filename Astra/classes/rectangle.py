import pygame

class Rectangle(pygame.sprite.Sprite):
    def draw(self):
        self.image = pygame.draw.rect(self.screen, "white", pygame.Rect(500,150,1000,300), 5, 25)