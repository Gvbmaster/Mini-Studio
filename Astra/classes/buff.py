import pygame

from effect.shield import Shield

class Buff(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = Shield().imageShield
        # Redimensionner l'image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect(x=x, y=y)
        self._kill = False


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide_rect(self, rect):
        return self.rect.colliderect(rect)