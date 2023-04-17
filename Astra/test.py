import pygame

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
size = (800, 600)
screen = pygame.display.set_mode(size)

# Couleur
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

# Définir la classe RectangleSprite qui hérite de la classe Sprite
class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect

# Définir les sprites
rect1 = RectangleSprite(pygame.Rect(100, 100, 50, 50))
rect2 = RectangleSprite(pygame.Rect(200, 200, 50, 50))
sprites = pygame.sprite.Group(rect1, rect2)

# Boucle principale
done = False
while not done:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Déplacer le rectangle 1 avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.rect.move_ip(-1, 0)
    if keys[pygame.K_RIGHT]:
        rect1.rect.move_ip(1, 0)
    if keys[pygame.K_UP]:
        rect1.rect.move_ip(0, -1)
    if keys[pygame.K_DOWN]:
        rect1.rect.move_ip(0, 1)

    # Vérifier si les rectangles se touchent
    if pygame.sprite.collide_rect(rect1, rect2):
        rect2.kill()  # Supprimer le rectangle 2 et son sprite associé

    # Afficher les rectangles
    screen.fill(white)
    for sprite in sprites:
        pygame.draw.rect(screen, black, sprite.rect)
    pygame.display.flip()

clock.tick(60)
# Quitter Pygame
pygame.quit()