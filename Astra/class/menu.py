import pygame, sys
from button import Button

screen = pygame.display.set_mode((1280, 720))

class menu : 

    def play(self):
        while True:
            playMousePos = pygame.mouse.get_pos()
            print(playMousePos)

            screen.fill("black")

            returnMainMenuIMG = pygame.image.load("img/ShipTest.png")
            returnMainMenu = Button(returnMainMenuIMG, 100, 100)
            returnMainMenu.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if returnMainMenu.checkingInput(playMousePos):
                        print("Passed Successfully !")
                        menu.mainMenu(self)
        
            pygame.display.update()

    def options(self):
        while True:
            optionsMousePos = pygame.mouse.get_pos()
            print(optionsMousePos)
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

    def mainMenu(self):
        while True:
            menuMousePos = pygame.mouse.get_pos()
            print(menuMousePos)
            screen.fill("red")

            playButtonIMG = pygame.image.load("img/LogoTest.PNG")
            playButton = Button(playButtonIMG, 400, 400)
            playButton.update(screen)

            #autres boutons
            #options
            #showCredits
            #quitGame

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.checkingInput(menuMousePos):
                        menu.play(self)
                    #autres boutons
                    #options
                    #showCredits
                    #quitGame
            pygame.display.update()

menu.instance = menu()
menu.instance.mainMenu()