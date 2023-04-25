import pygame
projectiles_group = pygame.sprite.Group()
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image_path, image_size):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, image_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        projectiles_group.add(self)  # Ajouter l'objet au groupe projectiles_group

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

