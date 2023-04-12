from cProfile import run
import pygame

#initialisation de pygame
pygame.init() 

#taille de la fenetre
screenWidth=1280
screenHeight=720

#couleur du background (R,G,B) (rouge,vert,bleu)
color=(0,0,0)

#vitesse de déplacement du vaisseau
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
#définition de la tailles de l'image
imageWidth=101.25
imageHeight=105.5

#initialisation de l'horloge interne
clock = pygame.time.Clock()

#Chargement des images
image = pygame.image.load("img/ShipTest.png").convert_alpha() #convert_alpha permet de garder la transparence d'un .png
logo = pygame.image.load("img/LogoTest.png").convert()
#resize des images
logo = pygame.transform.scale(logo, (32, 32))
image = pygame.transform.scale(image, (imageWidth, imageHeight)) 
#initialisation du logo (image en haut a gauche de la fenetre)
pygame.display.set_icon(logo)
#initialisation du titre de la fenetre
pygame.display.set_caption("Astra")

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
            
    #remplie le bachground avec la couleur choisi plus haut
    screen.fill((color))
    
    #affichage de l'image en x et y  ( donc x=,y=0(haut gauche)) sur le screen
    screen.blit(image, (x,y)) 
    
    #update de la fenetre
    pygame.display.flip() 

    #limite les fps du programme
    clock.tick(60)
    
#fermeture de pygame
pygame.quit() 

