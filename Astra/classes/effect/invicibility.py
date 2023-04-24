import pygame
import time
from classes.values import PlayerStats

class Invicibility:
    def __init__(self):
        self.end_invincibility_time = None

    def update(self):
        if PlayerStats.isPlayerHitable == True:
            self.end_invincibility_time = time.monotonic() + 3.0
            PlayerStats.isPlayerHitable = False
            print("Le joueur n'est désormais plus touchable !")
        elif PlayerStats.isPlayerHitable == False and self.end_invincibility_time is not None:
            if time.monotonic() >= self.end_invincibility_time:
                PlayerStats.isPlayerHitable = True
                self.end_invincibility_time = None
                print("Le joueur est désormais touchable !")

