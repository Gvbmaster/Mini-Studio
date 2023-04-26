import pygame

class Transition:
    def __init__(self, screen, fade_speed=5):
        self.screen = screen
        self.width, self.height = screen.get_width(), screen.get_height()
        self.fade_surface = pygame.Surface((self.width, self.height))
        self.fade_surface.fill((0, 0, 0))
        self.alpha = 255
        self.fade_dir = -1 # Set to -1 for fade in and 1 for fade out
        self.fade_speed = fade_speed
    
    def fade_in(self):
        self.alpha += self.fade_speed * self.fade_dir
        self.alpha = max(0, min(255, self.alpha))
        self.fade_surface.set_alpha(self.alpha)
        self.screen.blit(self.fade_surface, (0, 0))

    def update(self):
        self.alpha += self.fade_direction * self.fade_speed
        if self.alpha <= 0:
            self.alpha = 0
            self.finished = True
        elif self.alpha >= 255:
            self.alpha = 255
            self.fade_direction = -1 * self.fade_direction

        self.transition_surface.set_alpha(self.alpha)

    def draw(self):
        self.screen.blit(self.transition_surface, (0, 0))