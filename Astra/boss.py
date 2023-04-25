import pygame 
from classes.boss import *
pygame.init()

# Création d'une fenêtre de jeu
screen = pygame.display.set_mode((1920, 1080))

# Création d'un boss
boss = Boss("Big Boss", 100, 20)

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



 

 

    # Mise à jour de l'écran
    screen.fill((255, 255, 255))
    boss.update()
    boss.draw(screen)
    pygame.display.flip()

    # Vérification si le boss est toujours en vie
    