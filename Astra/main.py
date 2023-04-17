import pygame

from classes.player import *
from classes.enemy import *
from pattern.patternone import *
from classes.values import Param

#initialisation de pygame
pygame.init() 

#creation de la fenetre
screen = pygame.display.set_mode((Param.screenWidth,Param.screenHeight))

#Chargement des images
logo = pygame.image.load("Astra/img/LogoTest.png").convert()

#resize des images
logo = pygame.transform.scale(logo, (32, 32))

#Logo
pygame.display.set_icon(logo)

#Titre de la fenêtre
pygame.display.set_caption("Astra")

eightbit_song = pygame.mixer.Sound("Astra/song/8bit.ogg")
eightbit_song.play()

#boolean running
running = True 

#initialisation de l'horloge interne
clock = pygame.time.Clock()
player = Player(0, 0, 10, "Astra/img/ShipTest.png", (100,100))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    #for i in range (5):
     #   enemy=Entity(positionx[i],positiony[i],speedEnnemy[0],'img/ennemyTest.png')
     #   positionx[i]-=speedEnnemy[0]
     #   Entity.draw(ennemy,screen)
  
    screen.fill((0, 0, 0))  
    screen.blit(player.image, player.rect)
    pygame.display.flip()

    #limite les fps du programme
    clock.tick(60)
    
pygame.quit()