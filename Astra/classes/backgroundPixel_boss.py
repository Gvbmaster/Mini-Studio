import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load("img/pixel_art/background.png")
        self.rect = self.image.get_rect()
        self.height = self.rect.height
        self.y = 0

    def update(self):
        self.y += 10
        if self.y > self.height:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - self.height))