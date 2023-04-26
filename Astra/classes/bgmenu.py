import pygame 

class Background:
    def __init__(self):
        self.image = pygame.image.load("img/mainmenu.png")

    def draw(self, screen):
        screen.blit(self.image, (50, 0))