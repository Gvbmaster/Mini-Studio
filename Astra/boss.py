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
        keys = pygame.key.get_pressed() # Appel de la détection de touche préssé
        if keys[pygame.K_q] :
            boss.kill()  # ou boss.remove(all_sprites_layer_1)

    # Mise à jour de l'écran
    screen.fill((255, 255, 255))
    boss.update()
    boss.draw(screen)
    pygame.display.flip()

    # Vérification si le boss est toujours en vie
    if boss._kill:
        print("Le boss", boss.name, "est mort !")
        break