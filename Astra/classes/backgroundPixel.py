import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load("img/Group 20.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.x = 0

    def update(self):
        self.x -= 1
        if self.x < -self.width:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.width, 0))