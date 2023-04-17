import pygame



class Player(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/ShipTest.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]
        self._kill = False

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)