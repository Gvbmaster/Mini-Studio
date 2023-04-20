import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, name, **kwargs):
        super(Text, self).__init__()
        self.color = color
        self.font = pygame.font.SysFont(name, size)
        self.kwargs = kwargs
        self.set(text)

    def set(self, text):
        self.image = self.font.render(str(text), 1, self.color)
        self.rect = self.image.get_rect(**self.kwargs)