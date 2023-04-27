import pygame
import time
from classes.values import PlayerStats

class Invicibility:
    end_invincibility_time = None

    def update():
        if PlayerStats.isPlayerHitable == True:
            Invicibility.end_invincibility_time = time.monotonic() + 2
            PlayerStats.isPlayerHitable = False
            print("Le joueur n'est désormais plus touchable !")
        elif PlayerStats.isPlayerHitable == False and Invicibility.end_invincibility_time is not None:
            if time.monotonic() >= Invicibility.end_invincibility_time:
                PlayerStats.isPlayerHitable = True
                Invicibility.end_invincibility_time = None
                print("Le joueur est désormais touchable !")

