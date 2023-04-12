from cProfile import run
import pygame

pygame.init() #initialisation de pygame

screen = pygame.display.set_mode((1280,720))#definition de screen avec un display de 1280 pixel sur 720

running = True #boolean running

x = 0
y = 0

clock = pygame.time.Clock()

image = pygame.image.load("img/ShipTest.png").convert() #definition de image avec le fichier ShipTest.png

while running: #tant que running égal True on reste dans cette boucle
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:#si l'event est égal à QUIT(alt+f4 ou fermeture)
            running = False #alors running devient False et on sors de la boucle

    #ATTENTION la méthode si dessous détecte l'input seulement une fois (au moment ou l'un appuie sur la touche) donc inutilsable pour le deplacement
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:
                #print("Gauche !")
            #if event.key == pygame.K_RIGHT:
                #print("Droite !")
            #if event.key == pygame.K_UP:
                #print("Haut !")
            #if event.key == pygame.K_DOWN:
                #print("Bas !")

    
    pressed = pygame.key.get_pressed()
    #Ici tant que nous appuyer sur la touche l'input est détecter
    if pressed[pygame.K_LEFT]:
        print("Gauche !")
        x -= 1
    if pressed[pygame.K_RIGHT]:
        print("Droite")
        x += 1
    if pressed[pygame.K_UP]:
        print("Haut !")
        y -= 1
    if pressed[pygame.K_DOWN]:
       print("Bas !")
       y += 1

    screen.fill((0, 0, 0,))#remplie de noir (code RGB) le screen

    screen.blit(image, (x,y)) #affichage de image en x et y  ( donc 0 0(haut gauche)) sur le screen

    pygame.display.flip() #maj du display

    clock.tick(1000)

pygame.quit() #fermeture de pygame

