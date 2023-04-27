import pygame, sys
from classes.button import Button
from pygame.locals import *
from tuto import Tuto
from level1 import Level1
from classes.pyvidplayer import *
from classes.enemy import *
from classes.enemy2 import *

screen = pygame.display.set_mode((0, 0),FULLSCREEN)
imgEnemy.Init()
imgEnemy2.Init()

class menu : 
    def play(self):
        while True:
            Tuto.run(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()

    def options(self):
        while True:
            optionsMousePos = pygame.mouse.get_pos()
            screen.fill("red")

            returnMainMenuIMG = pygame.image.load("img/ShipTest.png")
            returnMainMenu = Button(returnMainMenuIMG, 500, 500)
            returnMainMenu.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if returnMainMenu.checkingInput(optionsMousePos):
                        print("Passed Successfully !")
                        menu.mainMenu(self)
        
            pygame.display.update()

    def showCredits(self):
        vid = Video("video/outro1.mp4")
        vid.set_size((1920, 1080))
        end_video_event = pygame.USEREVENT + 1
        pygame.time.set_timer(end_video_event, 62000)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if event.type == end_video_event:
                    vid.close()
                    menu.mainMenu(self)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("la vidéo viens d'être skip")
                    vid.close()
                    menu.mainMenu(self)
                    
            vid.draw(screen, (0,0))
            pygame.display.update()

    def mainMenu(self):
        while True:
            menuMousePos = pygame.mouse.get_pos()
            screen.fill("black")

            playButtonIMG = pygame.image.load("img/menu/Nouvelle partie.png")
            playButtonIMG = pygame.transform.scale(playButtonIMG,(300,100))
            playButton = Button(playButtonIMG, 175, 370)
            if playButton.checkingInput(menuMousePos):
                playButtonIMGHover = pygame.image.load("img/menu/Nouvelle partie 2.png")
                playButtonIMGHover = pygame.transform.scale(playButtonIMGHover,(500,100))
                playButton = Button(playButtonIMGHover, 240, 370) #décallage ?
                playButton.update(screen)
            playButton.update(screen)

            optionsButtonIMG = pygame.image.load("img/menu/Options.png")
            optionsButtonIMG = pygame.transform.scale(optionsButtonIMG,(200,100))
            optionsButton = Button(optionsButtonIMG, 125, 470)
            if optionsButton.checkingInput(menuMousePos):
                optionsButtonIMGHover = pygame.image.load("img/menu/Options 2.png")
                optionsButtonIMGHover = pygame.transform.scale(optionsButtonIMGHover,(380,100))
                optionsButton = Button(optionsButtonIMGHover, 175, 470)
                optionsButton.update(screen)
            optionsButton.update(screen)

            showCreditsButtonIMG = pygame.image.load("img/menu/crédit.png")
            showCreditsButtonIMG = pygame.transform.scale(showCreditsButtonIMG,(200,100))
            showCreditsButton = Button(showCreditsButtonIMG, 125, 570)
            if showCreditsButton.checkingInput(menuMousePos):
                showCreditsButtonIMGHover = pygame.image.load("img/menu/crédit 2.png")
                showCreditsButtonIMGHover = pygame.transform.scale(showCreditsButtonIMGHover,(380,100))
                showCreditsButton = Button(showCreditsButtonIMGHover, 175, 570)
                showCreditsButton.update(screen)
            showCreditsButton.update(screen)

            quitButtonIMG = pygame.image.load("img/menu/Quitter.png")
            quitButtonIMG = pygame.transform.scale(quitButtonIMG,(200,100))
            quitButton = Button(quitButtonIMG, 125, 670)
            if quitButton.checkingInput(menuMousePos):
                quitButtonIMGHover = pygame.image.load("img/menu/Quitter 2.png")
                quitButtonIMGHover = pygame.transform.scale(quitButtonIMGHover,(380,100))
                quitButton = Button(quitButtonIMGHover, 175, 670)
                quitButton.update(screen)
            quitButton.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.checkingInput(menuMousePos):
                        print("Bouton cliqué ! Le jeu se lance !")
                        pygame.font.init()
                        tuto = Tuto(screen)
                        tuto.run()
                        pygame.quit()
                        sys.exit()
                    elif optionsButton.checkingInput(menuMousePos):
                        print("Bouton cliqué ! Les options s'affichent!")
                        menu.options(self)
                    elif showCreditsButton.checkingInput(menuMousePos):
                        print("Bouton cliqué ! Les crédits s'affichent !")
                        # pygame.display.set_mode((0, 0), FULLSCREEN)
                        menu.showCredits(self)
                    elif quitButton.checkingInput(menuMousePos):
                        print("Bouton cliqué ! Le jeu se ferme !")
                        pygame.quit()
                    else :
                        pass
            pygame.display.update()
menu.instance = menu()
menu.instance.mainMenu()