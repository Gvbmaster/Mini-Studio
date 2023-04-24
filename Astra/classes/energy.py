import pygame

class Energy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, empty_image_path, filled_image_path):
        super().__init__()
        self.width = width
        self.height = height
        self.energy = 0
        self.max_energy = 100

        # Load the empty and filled images
        self.empty_image = pygame.image.load(empty_image_path).convert_alpha()
        self.filled_image = pygame.image.load(filled_image_path).convert_alpha()

        self.image = self.empty_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fill_rect = pygame.Surface((0, height))
        self.fill_rect.fill((0, 255, 0))
        self.fill_rect_rect = self.fill_rect.get_rect()
        self.fill_rect_rect.x = x
        self.fill_rect_rect.y = y

        self.fill_image = None
        self.fill_width = 0

    def update(self):
        fill_width = int(self.energy * self.width)
        self.fill_image = pygame.transform.scale(self.filled_image, (fill_width // 100, self.height))
        self.empty_image = pygame.transform.scale(self.empty_image, (self.width, self.height))
        self.image = self.empty_image.copy()
        self.image.blit(self.fill_image, (0, 0))

    def set_energy(self, energy):
        self.energy = energy
        self.update()