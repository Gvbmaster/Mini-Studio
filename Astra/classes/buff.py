import pygame

class Buff(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("img/Life.png").convert_alpha()
        # Redimensionner l'image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect(x=x, y=y)
        self._kill = False


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide_rect(self, rect):
        if self.rect.colliderect(rect):
            self.kill()
            return True
        else:
            return False