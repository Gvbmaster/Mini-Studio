import pygame
import random
from classes.button import *
from classes.text import *
from pygame.locals import *
from classes.values import *

class Gameover():
    def __init__(self, screen):
        self.screen = screen
        self.casePlayer = pygame.image.load("img/player.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer, (395, 500))
        self.playerRect = self.casePlayer.get_rect(left=(202), top=(230))
        self.deathArea = pygame.image.load("img/deathRect.png").convert_alpha()
        self.deathAreaRect = self.deathArea.get_rect(left=(175), top=(175))

        self.area_color = "white"

        self.txtDeathScreen = [0, 1, 2, 3, 4]
        self.txtDeathScreen[0] = "Je n'aurais peut-être pas dû voler ce vaisseau… Mais je n'avais d'autres choix pour m'échapper."
        self.txtDeathScreen[1] = "Si seulement le transmutateur n'était pas endommagé… Quel était donc cet univers ? J'aurais dû être téléporté sur Avesia."
        self.txtDeathScreen[2] = "J'aurais pu les sauver… Je ne sais pas comment ils pourront survivre s'ils se font attaquer."
        self.txtDeathScreen[3] = "Ils comptaient tous sur moi. J'étais censé revenir avec assez d'informations pour nous permettre de survivre à leurs attaques."
        self.txtDeathScreen[4] = "Qui va pouvoir sauver Avesia ? Ils vont prendre tous nos cristaux de zorgonites et détruire la planète."
        self.font1 = pygame.font.Font('font/PlayfairDisplay-Regular.ttf', 60)
        # self.font2 = pygame.font.Font('font/DynaPuff-Regular.ttf', 60)
        # self.font3 = pygame.font.Font('font/ShareTechMono-Regular.ttf', 60)
        self.text = random.choice(self.txtDeathScreen)
                
    def update(self, screen):
        pygame.draw.rect(screen, "black", pygame.Rect(0,0,1920,1080))
        screen.blit(self.casePlayer, self.playerRect)
        screen.blit(self.deathArea, self.deathAreaRect)
        
        self.textArea = Text(self.font1, self.text, 900)
        self.textArea.drawText(screen, 700, 250)
        retryIMG = pygame.image.load("img/retry.png")
        retry = Button(retryIMG, 1000, 850)
        retry.update(screen)
        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry.checkingInput(playMousePos):
                    PlayerStats.currentHealth = 3
                    print("Passed Successfully !")
        pygame.display.update()
    def draw(screen):
        pass