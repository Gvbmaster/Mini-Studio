import pygame

class Rectangle:
    def draw(self):
        pygame.draw.rect(self.screen, "white", pygame.Rect(500,150,1000,300), 5, 25)