import pygame
import random
from classes.button import *
from classes.text import *
from pygame.locals import *
from classes.values import *

class GameoverLP():
    def __init__(self, screen):
        self.screen = screen
        self.casePlayer = pygame.image.load("img/playerLowPoly.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer, (250, 450))
        self.playerRect = self.casePlayer.get_rect(left=(280), top=(230))
        self.deathArea = pygame.image.load("img/deathRect.png").convert_alpha()
        self.deathAreaRect = self.deathArea.get_rect(left=(175), top=(175))

        self.area_color = "white"

        self.txtDeathScreen = [0, 1, 2, 3, 4]
        self.txtDeathScreen[0] = "Je n'aurais peut-être pas dû voler ce vaisseau… Mais je n'avais d'autres choix pour m'échapper."
        self.txtDeathScreen[1] = "Si seulement le transmutateur n'était pas endommagé… Quel était donc cet univers ? J'aurais dû être téléporté sur Avesia."
        self.txtDeathScreen[2] = "J'aurais pu les sauver… Je ne sais pas comment ils pourront survivre s'ils se font attaquer."
        self.txtDeathScreen[3] = "Ils comptaient tous sur moi. J'étais censé revenir avec assez d'informations pour nous permettre de survivre à leurs attaques."
        self.txtDeathScreen[4] = "Qui va pouvoir sauver Avesia ? Ils vont prendre tous nos cristaux de zorgonites et détruire la planète."
        self.font = pygame.font.Font('font/TurretRoad-Regular.ttf', 60)
        self.text = random.choice(self.txtDeathScreen)

        self.retryIMG = pygame.image.load("img/rejouerLowPoly.png")
        self.retry = Button(self.retryIMG, 967, 900)
                
    def update(self, screen):
        pygame.draw.rect(screen, "black", pygame.Rect(0,0,1920,1080))
        screen.blit(self.casePlayer, self.playerRect)
        screen.blit(self.deathArea, self.deathAreaRect)
        
        self.textArea = Text(self.font, self.text, 900)
        self.textArea.drawText(screen, 700, 250)
        
        self.retry.update(screen)
        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.retry.checkingInput(playMousePos):
                    PlayerStats.currentHealth = 3
                    print("Passed Successfully !")
        pygame.display.update()

class GameoverPA():
    def __init__(self, screen):
        self.screen = screen
        self.casePlayer = pygame.image.load("img/playerPixelArt.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer, (350, 450))
        self.playerRect = self.casePlayer.get_rect(left=(225), top=(230))
        self.deathArea = pygame.image.load("img/deathRect.png").convert_alpha()
        self.deathAreaRect = self.deathArea.get_rect(left=(175), top=(175))

        self.area_color = "white"

        self.txtDeathScreen = [0, 1, 2, 3, 4]
        self.txtDeathScreen[0] = "Je n'aurais peut-être pas dû voler ce vaisseau… Mais je n'avais d'autres choix pour m'échapper."
        self.txtDeathScreen[1] = "Si seulement le transmutateur n'était pas endommagé… Quel était donc cet univers ? J'aurais dû être téléporté sur Avesia."
        self.txtDeathScreen[2] = "J'aurais pu les sauver… Je ne sais pas comment ils pourront survivre s'ils se font attaquer."
        self.txtDeathScreen[3] = "Ils comptaient tous sur moi. J'étais censé revenir avec assez d'informations pour nous permettre de survivre à leurs attaques."
        self.txtDeathScreen[4] = "Qui va pouvoir sauver Avesia ? Ils vont prendre tous nos cristaux de zorgonites et détruire la planète."
        self.font = pygame.font.Font('font/ShareTechMono-Regular.ttf', 60)
        self.text = random.choice(self.txtDeathScreen)

        self.retryIMG = pygame.image.load("img/rejouerPixelArt.png")
        self.retry = Button(self.retryIMG, 967, 900)
                
    def update(self, screen):
        pygame.draw.rect(screen, "black", pygame.Rect(0,0,1920,1080))
        screen.blit(self.casePlayer, self.playerRect)
        screen.blit(self.deathArea, self.deathAreaRect)
        
        self.textArea = Text(self.font, self.text, 900)
        self.textArea.drawText(screen, 700, 250)

        self.retry.update(screen)
        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.retry.checkingInput(playMousePos):
                    PlayerStats.currentHealth = 3
                    print("Passed Successfully !")
        pygame.display.update()

class GameoverOC():
    def __init__(self, screen):
        self.screen = screen
        self.casePlayer = pygame.image.load("img/playerOldCartoon.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer, (400, 400))
        self.playerRect = self.casePlayer.get_rect(left=(210), top=(260))
        self.deathArea = pygame.image.load("img/deathRect.png").convert_alpha()
        self.deathAreaRect = self.deathArea.get_rect(left=(175), top=(175))

        self.area_color = "white"

        self.txtDeathScreen = [0, 1, 2, 3, 4]
        self.txtDeathScreen[0] = "Je n'aurais peut-être pas dû voler ce vaisseau… Mais je n'avais d'autres choix pour m'échapper."
        self.txtDeathScreen[1] = "Si seulement le transmutateur n'était pas endommagé… Quel était donc cet univers ? J'aurais dû être téléporté sur Avesia."
        self.txtDeathScreen[2] = "J'aurais pu les sauver… Je ne sais pas comment ils pourront survivre s'ils se font attaquer."
        self.txtDeathScreen[3] = "Ils comptaient tous sur moi. J'étais censé revenir avec assez d'informations pour nous permettre de survivre à leurs attaques."
        self.txtDeathScreen[4] = "Qui va pouvoir sauver Avesia ? Ils vont prendre tous nos cristaux de zorgonites et détruire la planète."
        self.font = pygame.font.Font('font/PlayfairDisplay-Regular.ttf', 60)
        self.text = random.choice(self.txtDeathScreen)

        self.retryIMG = pygame.image.load("img/rejouerOldCartoon.png")
        self.retry = Button(self.retryIMG, 967, 900)
                
    def update(self, screen):
        pygame.draw.rect(screen, "black", pygame.Rect(0,0,1920,1080))
        screen.blit(self.casePlayer, self.playerRect)
        screen.blit(self.deathArea, self.deathAreaRect)
        
        self.textArea = Text(self.font, self.text, 900)
        self.textArea.drawText(screen, 700, 250)
        
        self.retry.update(screen)
        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.retry.checkingInput(playMousePos):
                    PlayerStats.currentHealth = 3
                    print("Passed Successfully !")
        pygame.display.update()