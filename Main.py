from cProfile import run
import pygame

pygame.init() #initialisation de pygame

screenWidth=1280
screenHeight=720

color=(0,255,0)

speed=5

screen = pygame.display.set_mode((screenWidth,screenHeight))#definition de screen avec un display de 1280 pixel sur 720
screen.fill(color)
pygame.display.flip()  

running = True #boolean running

x = 0
y = 0

#Originale image size : Width=422 Height=405
imageWidth=101.25
imageHeight=105.5
clock = pygame.time.Clock()

image = pygame.image.load("Mini-Studio/img/ShipTest.png").convert_alpha() #definition de image avec le fichier ShipTest.png
logo = pygame.image.load("Mini-Studio/img/LogoTest.png").convert()
logo = pygame.transform.scale(logo, (32, 32))
image = pygame.transform.scale(image, (imageWidth, imageHeight)) 
pygame.display.set_icon(logo)
pygame.display.set_caption("Astra")

while running: #tant que running �gal True on reste dans cette boucle
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:#si l'event est �gal � QUIT(alt+f4 ou fermeture)
            running = False #alors running devient False et on sors de la boucle

    #ATTENTION la m�thode si dessous d�tecte l'input seulement une fois (au moment ou l'un appuie sur la touche) donc inutilsable pour le deplacement
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
    #Ici tant que nous appuyer sur la touche l'input est d�tecter
    if pressed[pygame.K_q] or pressed[pygame.K_LEFT]:
        if (x>0):
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

    screen.fill((color))#remplie de noir (code RGB) le screen

    screen.blit(image, (x,y)) #affichage de image en x et y  ( donc 0 0(haut gauche)) sur le screen

    pygame.display.flip() #maj du display

    clock.tick(60)#limite les fps du programme

pygame.quit() #fermeture de pygame

