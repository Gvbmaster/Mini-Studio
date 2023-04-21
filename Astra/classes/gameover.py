import pygame
from classes.button import *
from classes.text import *

screen = pygame.display.set_mode((1920, 1080))

class Gameover():
    def __init__(self):
        screen.fill("black")
        self.area_color = "white"

        self.imageWidth = 395
        self.imageHeight = 475
        self.casePlayer = pygame.image.load("img/player.png").convert_alpha()
        self.casePlayer = pygame.transform.scale(self.casePlayer,(int(self.imageWidth), int(self.imageHeight)))
        self.rectPlayer = self.casePlayer.get_rect(left=(200), top=(202))

        self.textAreaRect = pygame.draw.rect(screen, self.area_color, pygame.Rect(600,200,1120,480), 5)

        font = pygame.font.SysFont('Playfair Display', 40)
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit."
        self.textArea = Text(font, text, 900)
        self.textArea.draw(screen, 700, 220)
        
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