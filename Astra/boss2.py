import pygame 
from classes.boss import *

pygame.init()

# Création d'une fenêtre de jeu
screen = pygame.display.set_mode((1920, 1080))

# Création d'un boss
boss = Boss("Big Boss", 100, 20)
all_sprites_layer_1 = pygame.sprite.Group()
all_sprites_layer_1.add(boss)

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # Vérification si la touche espace est enfoncée
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            boss.kill()
        
    # Mise à jour de l'écran
    screen.fill((255, 255, 255))
    
    # Vérification si le boss est toujours en vie
    if not boss.alive():
        print("Le boss", boss.name, "est mort !")
        all_sprites_layer_1.remove(boss)
        
    all_sprites_layer_1.update()
    all_sprites_layer_1.draw(screen)
    pygame.display.flip()
pygame.quit()