import pygame
from classes.button import *
from classes.text import *

screen = pygame.display.set_mode((1920, 1080))

class Gameover():
    def __init__(self):
        font = pygame.font.SysFont('Playfair Display Noir', 28)
        screen.fill("black")
        self.area_color = "white"

        self.imageWidth = 395
        self.imageHeight = 475
        self.casePlayer = pygame.image.load("img/player.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer,(int(self.imageWidth), int(self.imageHeight)))
        self.rectPlayer = self.casePlayer.get_rect(left=(200), top=(202))

        # self.textArea = pygame.draw.rect(screen, self.area_color, pygame.Rect(600,200,1120,480), 5)

        self.textArea = Text("bite", 20, "yellow", 'Playfair Display Noir')
        
        screen.blit(self.casePlayer, self.rectPlayer)

        retryIMG = pygame.image.load("img/retry.png")
        retry = Button(retryIMG, 1000, 800)
        retry.update(screen)

        playMousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry.checkingInput(playMousePos):
                    print("Passed Successfully !")
                        
        pygame.display.update()

    # def drawText():
    #     text = pygame.font.SysFont("Calibri", fSize, True).render(text, True, (0, 0, 0))
    #     rect = text.get_rect()
    #     rect.center = ((screen_side_length // 2) + x), ((screen_side_length // 2) + y)
    #     screen.blit(screen_text, rect)