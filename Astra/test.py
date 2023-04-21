import pygame
from classes.player import Player
from classes.buff import Buff
from classes.lifesystem import *
from classes.ath import ATH
from classes.backgroundPixel import Background
from classes.projectile import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = Background()
        self.ath = ATH()
        self.player = Player(0,0)
        self.buff = [Buff(750,450,2),Buff(850,450,2),Buff(950,450,2),Buff(1050,450,2)]
        self.buff1 =[Buff(750,550,1),Buff(850,550,1),Buff(950,550,1),Buff(1050,550,1)]
        self.buff2=[Buff(750,250,3),Buff(850,250,3),Buff(950,250,3),Buff(1050,250,3)]
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

########################### Touches de mouvement ############################################################################################            
            if event.type == pygame.KEYDOWN: # Appel de la constante KEYDOWN
                if event.key == pygame.K_LEFT : 
                    self.player.velocity[0] = -1 
                    PlayerStats.attackSpeed = 75 # Regulation de la cadence de tir par rapport au fait qu'on recul
                    print("left press")
                elif event.key == pygame.K_RIGHT : 
                    self.player.velocity[0] = 1
                    PlayerStats.attackSpeed = 175 # Regulation de la cadence de tir par rapport au fait qu'on avance
                    print("right press")
                elif event.key == pygame.K_UP : 
                    self.player.velocity[1] = -1
                    PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                    print("up press")
                elif event.key == pygame.K_DOWN :
                    self.player.velocity[1] = 1
                    PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                    print("down press")
        
            elif event.type == pygame.KEYUP: # Appel de la constante KEYUP
                if event.key == pygame.K_LEFT and self.player.velocity[0] == -1:
                    self.player.velocity[0] = 0
                    PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                    print("left up")
                elif event.key == pygame.K_RIGHT and self.player.velocity[0] == 1:
                    self.player.velocity[0] = 0
                    PlayerStats.attackSpeed = 100 # Regulation de la cadence de tir a la base 10 tirs/s
                    print("right up")
                elif event.key == pygame.K_UP and self.player.velocity[1] == -1:
                    self.player.velocity[1] = 0
                    print("up up")
                elif event.key == pygame.K_DOWN and self.player.velocity[1] == 1:
                    self.player.velocity[1] = 0
                    print("down up")
            
############################ Tir automatique du vaisseau ######################################################################################
            if event.type == pygame.KEYDOWN:
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
            projectile = Projectile(self.player.rect.centerx, self.player.rect.top, PlayerStats.attackVelocity, "img/laser_beam.png", (100,90))
            self.all_sprites.add(projectile)
            self.last_shot_time = current_time  # Mettre à jour le temps du dernier tir
#################################################################################################################################################

        

     

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

        for buff in self.buff:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                PlayerStats.shield = True
                print("Buff catch and del")
                print(PlayerStats.shield)
        
        for buff in self.buff1:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                LifeSystem.healthPlayerUpdate(self,2)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)

        for buff in self.buff2:
            if buff.collide_rect(self.player.rect):
                buff.kill()
                self.all_sprites.remove(buff)
                LifeSystem.healthPlayerUpdate(self,buff)
                print("Buff catch and del")
                print(PlayerStats.currentHealth)
    

    def display(self):
        self.background.update()
        self.screen.fill("black")
        self.background.draw(self.screen)
        #pygame.draw.rect(self.screen, self.area_color, self.area)
        self.all_sprites.draw(self.screen)
        self.player.draw(self.screen)
        self.ath.draw(self.screen)
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
