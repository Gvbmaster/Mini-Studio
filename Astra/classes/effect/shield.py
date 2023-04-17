import pygame

from player import player

class shield():
    def __init__(self,x,y):
        self.image = pygame.image.load("img/Shield.png").convert_alpha()
        
    