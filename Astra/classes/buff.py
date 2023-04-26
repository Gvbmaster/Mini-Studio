import pygame
from classes.effect.shield import Shield
from classes.effect.heal import Heal
from classes.effect.damage import Damage
from classes.values import *

class Buff(pygame.sprite.Sprite):
    def __init__(self,x,y,idEffect):
        super().__init__()
        self.idEffect = 2
        self.image = self.get_effect_image(idEffect)
        # Redimensionner l'image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.rect = self.image.get_rect(x=x, y=y)
        # self.speed = BuffStats.speed
        # self.velocity = [-1, 0]
        self._kill = False

    def get_effect_image(self, idEffect):
        if idEffect == 2:
            return Shield().image
        elif idEffect == 1:
            return Heal().image
        elif idEffect == 3:
            return Damage().image
        
    # def move(self):
    #     self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collide_rect(self, rect):
        if self._kill:
            return False
        return self.rect.colliderect(rect)

    def kill(self):
        super().kill()
        self._kill = True