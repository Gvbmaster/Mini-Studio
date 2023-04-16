import pygame

#initialisation de pygame
pygame.init() 

import pygame
from pygame.locals import *

class Entity:
    def __init__(self, x, y, speed, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (75.5, 40.9))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

#taille de la fenetre
screenWidth=1280
screenHeight=720

pattern0x=[1480,1380,1280,1380,1480]
pattern0y=[522,422,322,222,122]
patternx=[pattern0x]
patterny=[pattern0y]
positionx=[patternx[0][0],patternx[0][1],patternx[0][2],patternx[0][3],patternx[0][4]]
positiony=[patterny[0][0],patterny[0][1],patterny[0][2],patterny[0][3],patterny[0][4]]

#couleur du background (R,G,B) (rouge,vert,bleu)
color=(0,0,0)

#vitesse de deplacement du vaisseau
speed=5

#creation de la fenetre
screen = pygame.display.set_mode((screenWidth,screenHeight))
screen.fill(color)
#update de la fenetre
pygame.display.flip()  

#boolean running
running = True 

#initialisation des coordonnees de spawn du vaisseau
x = 0
y = 0

#taille originale de l'image : Width=422 Height=405
#definition de la tailles de l'image
imageWidth=101.25
imageHeight=105.5

#taille originale de l'image : Width=755 Height=409

#initialisation de l'horloge interne
clock = pygame.time.Clock()

#Chargement des images
image = pygame.image.load("img/ShipTest.png").convert_alpha() #convert_alpha permet de garder la transparence d'un .png

logo = pygame.image.load("img/LogoTest.png").convert()
ennemySprite = pygame.image.load("img/ennemyTest.png").convert_alpha()
#resize des images
logo = pygame.transform.scale(logo, (32, 32))
image = pygame.transform.scale(image, (imageWidth, imageHeight))
#initialisation du logo (image en haut a gauche de la fenetre)
pygame.display.set_icon(logo)
#initialisation du titre de la fenetre
pygame.display.set_caption("Astra")

#eightbit_song = pygame.mixer.Sound("song/8bit.ogg")
#eightbit_song.play()


while running: #tant que running egal True on reste dans cette boucle
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:#si l'event est egal a QUIT(alt+f4 ou fermeture)
            running = False #alors running devient False et on sors de la boucle

    #ATTENTION la methode si dessous detecte l'input seulement une fois (au moment ou l'un appuie sur la touche) donc inutilsable pour le deplacement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                print("Gauche !")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print("Droite !")
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                print("Haut !")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print("Bas !")

    
    pressed = pygame.key.get_pressed()
    #Ici tant que nous appuyons sur la touche l'input est detecter
    if pressed[pygame.K_q] or pressed[pygame.K_LEFT]:#par exemple ici les input possible sont la touche q ou la touche fleche de gauche
        #verification de collision avec la bordure de la fenetre
        if (x>0):
            #decrementation de la vitesse sur x afin de faire aller le vaisseau vers la gauche
            x -= speed
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        if (x<screenWidth-imageWidth):
            x += speed
    if pressed[pygame.K_z] or pressed[pygame.K_UP]:
        if (y>0):
            y -= speed
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
       if (y<screenHeight-imageHeight):
            y += speed
            
    #remplie le background avec la couleur choisi plus haut
    screen.fill((color))
    
    #affichage de l'image en x et y  ( donc x=,y=0(haut gauche)) sur le screen
    screen.blit(image, (x,y)) 
    
    for i in range (5):
        ennemy0=Entity(positionx[i],positiony[i],2,'img/ennemyTest.png')
        positionx[i]-=2
        Entity.draw(ennemy0,screen)
    #ennemy0=Entity(position0x,position0y,2,'img/ennemyTest.png')
    #ennemy1=Entity(position1x,position1y,2,'img/ennemyTest.png')
    #ennemy2=Entity(position2x,position2y,2,'img/ennemyTest.png')
    #ennemy3=Entity(position3x,position3y,2,'img/ennemyTest.png')
    #ennemy4=Entity(position4x,position4y,2,'img/ennemyTest.png')
    #position0x-=2
    #position1x-=2
    #position2x-=2
    #position3x-=2
    #position4x-=2
    #Entity.draw(ennemy0,screen)
    #Entity.draw(ennemy1,screen)
    #Entity.draw(ennemy2,screen)
    #Entity.draw(ennemy3,screen)
    #Entity.draw(ennemy4,screen)

    #update de la fenetre
    pygame.display.flip() 

    #limite les fps du programme
    clock.tick(60)
    
#fermeture de pygame
pygame.quit()