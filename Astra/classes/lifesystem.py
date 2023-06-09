import pygame
from classes.values import *
from classes.buff import *
from classes.player import *

class LifeSystem :
    def __init__(self, game):
        super().__init__()
        self.game = game

    def healthPlayerUpdate(self, buff):
        if buff == 2 :
            if PlayerStats.currentHealth < PlayerStats.maxHealth:
                PlayerStats.currentHealth = PlayerStats.currentHealth+1
                #update le sprite de vie
            elif PlayerStats.currentHealth == PlayerStats.maxHealth:
                print("Vie maximale atteinte !")

        else:
            if PlayerStats.isPlayerHitable == True :
                if PlayerStats.shield == True:
                    PlayerStats.shield = False
                    Player.has_shield = False

                elif PlayerStats.currentHealth <= PlayerStats.maxHealth & PlayerStats.currentHealth > 0:
                    PlayerStats.currentHealth = PlayerStats.currentHealth -1
                    if PlayerStats.currentHealth == 0:
                        #kill player
                        #gameover.update()
                        print("Game Over !")
                    else :
                        pass
                else :
                    pass
            else :
                pass

    def healthEnemyUpdate(self):
        if EnnemieStats.currentHealth <= EnnemieStats.maxHealth:
            EnnemieStats.currentHealth = EnnemieStats.currentHealth - PlayerStats.attackDamage
            if EnnemieStats.currentHealth <= 0:
                #kill enemy
                print("Enemy killed !")

    def healthBossUpdate(self):
        if BossStats.currentHealth <= BossStats.maxHealth:
            BossStats.currentHealth = BossStats.currentHealth - PlayerStats.attackDamage
            if BossStats.currentHealth <= 0:
                #kill boss
                print("Boss killed !")
            else:
                print(f"Boss took {PlayerStats.attackDamage} damage")