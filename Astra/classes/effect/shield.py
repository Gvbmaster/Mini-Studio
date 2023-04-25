import pygame
class imgshield():
   def Init():
    imgshield.shield = pygame.image.load("img/Shield.png").convert_alpha()
    imageWidth = 151.25
    imageHeight = 146.5
    imgshield.shield = pygame.transform.scale(imgshield.shield,(int(imageWidth), int(imageHeight)))

class Shield():
    def __init__(self):
        self.idEffect = 2
        self.image = imgshield.shield
        
        