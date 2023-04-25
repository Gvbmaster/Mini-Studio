import pygame

class Button():
    def init(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        pass

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkingInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Passed Successfully !")
            return True
        return False
        