import pygame
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.projectile import*
from classes.values import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0,0)
        self.buff = Buff(750,450,2)
        self.buff1 = Buff(850,550,1)
        self.buff2 = Buff(750,250,3)
        self.area = pygame.Rect(300,150,300,300)
        self.area_color = "red"
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.buff, self.buff1,self.buff2)
        self.space_pressed = False # Pour le tir auto
        self.last_shot_time = 0  # Initialiser à 0 pour le tir auto

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
############################ Tir automatique du vaisseau ######################################################################################
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Espace pressé")
                    self.space_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Espace relâché")
                    self.space_pressed = False
        self.all_sprites.update()
        current_time = pygame.time.get_ticks()  # Obtenir le temps actuel en millisecondes
        if self.space_pressed and current_time - self.last_shot_time >= PlayerStats.attackSpeed:  # Limiter le tir a la class PlayerStats qui est dans values qui est donc 250
            # Créer une instance de Projectile à la position du joueur
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.speed, "img/pixel_laser_yellow.png", (100,90))
            self.all_sprites.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

        if self.buff.collide_rect(self.player.rect):
            self.buff.kill()
            self.all_sprites.remove(self.buff)
            self.player.has_buff = True
            print("Buff catch and del")
        
        if self.buff1.collide_rect(self.player.rect):
            self.buff1.kill()
            self.all_sprites.remove(self.buff1)
            LifeSystem.healthPlayerUpdate(self,2)
            print("Buff catch and del")
            print(PlayerStats.currentHealth)

        if self.buff2.collide_rect(self.player.rect):
            self.buff2.kill()
            self.all_sprites.remove(self.buff2)
            LifeSystem.healthPlayerUpdate(self,self.buff2)
            print("Buff catch and del")
            print(PlayerStats.currentHealth)

    

    def display(self):
        self.screen.fill("black")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.all_sprites.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

game = Game(screen)
game.run()

pygame.quit()
