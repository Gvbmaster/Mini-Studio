import pygame

from classes.projectile import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, name, damage):
        super().__init__()
        self.name = name
        self.health = 1000
        self.damage = damage
        self.image = pygame.image.load("img/boss.png")
        self.image = pygame.transform.scale(self.image, (1500, 300))
        self.rect = self.image.get_rect()
        self.rect.x = 210
        self.rect.y = -40
        self.projectiles = pygame.sprite.Group()  # Groupe de projectiles tirés par le boss
        self._kill = False

    def attack(self):
        print("Le boss", self.name, "attaque et inflige", self.damage, "points de dégâts !")

    def take_damage(self, amount):
        self.health -= amount
        print("Le boss", self.name, "subit", amount, "points de dégâts !")

    def update(self):
        self.projectiles.update()  # Mettre à jour les projectiles

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        # Créer un nouveau projectile à partir de la position du boss
        projectile = Projectile(self.rect.x, self.rect.y, 5, "img/laser_beam.png", (100, 90))
        self.projectiles.add(projectile)  # Ajouter le projectile au groupe de projectiles
    
    # def destroy(self):
    #     self.kill() # désactive le sprite
    #     self._kill = True
    #     self.groups().remove(self) # supprime le sprite du groupe