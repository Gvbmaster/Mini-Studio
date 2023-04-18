import pygame

from classes.player import *
from classes.enemy import *
from pattern.patternone import *
from classes.values import Param
from classes.projectile import *

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


#boolean running
running = True 

#initialisation de l'horloge interne
clock = pygame.time.Clock()
projectiles = pygame.sprite.Group()
player = Player(0, 0, 10, "Astra/img/ShipTest.png", (100,100))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espace pressé")
            # Créer une instance de Projectile à la position du joueur
                projectile = Projectile(player.rect.centerx, player.rect.top, 10, "Astra/img/pixel_laser_yellow.png", (100,90))
                projectiles.add(projectile)


    projectiles.update()  # Appel à la méthode update() des projectiles pour les déplacer

    enemy_image_path = "Astra/img/ennemyTest.png"
    enemy_image_size = (100, 100)
    enemy = Enemy(400, 300, 5, enemy_image_path, enemy_image_size)

    if pygame.sprite.collide_mask(player, enemy):
        print ("touché")
  
    screen.fill((0, 0, 0))  
    screen.blit(player.image, player.rect)
    projectiles.draw(screen)  # Appel à la méthode draw() des projectiles pour les afficher à l'écran
    player.update()
    player.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    pygame.display.update()

    #limite les fps du programme
    clock.tick(60)
    
pygame.quit()