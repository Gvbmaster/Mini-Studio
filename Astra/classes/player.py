import pygame

class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/ShipTest.png").convert_alpha()
        self.imageWidth = 101.25
        self.imageHeight = 105.5
        self.image = pygame.transform.scale(self.image,(int(self.imageWidth), int(self.imageHeight)))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]
        self._kill = False
        self.has_buff = False

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.has_buff:
            shield_image = pygame.image.load("img/Shield.png").convert_alpha()
            shield_rect = shield_image.get_rect(center=self.rect.center)
            screen.blit(shield_image, shield_rect)