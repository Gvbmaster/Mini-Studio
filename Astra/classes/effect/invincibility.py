import pygame
from classes.values import PlayerStats

class Invicibility:
    def __init__(self):
        self.idEffect = 4
        PlayerStats.isPlayerHitable = False

    def Applyed():
        invicibilityFrame = pygame.USEREVENT + 1
        pygame.time.set_timer(invicibilityFrame, 3000)
        while True:
            for event in pygame.event.get():
                if event.type == invicibilityFrame:
                    PlayerStats.isPlayerHitable = False #joueur intouchable
            PlayerStats.isPlayerHitable = True 