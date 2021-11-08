import pygame

from settings import *


class ShopUpgrade:

    def __init__(self, num):

        self.num = num

        self.image = pygame.image.load(f"assets/upgrade{num + 1}.png")
        self.image = pygame.transform.scale((65, 65))

        if num == 0:
            self.x = 125

        if num == 1:
            self.x = WIDTH // 2

        if num == 2:
            self.x = WIDTH // 2 + 125

        self.y = HEIGHT // 2 + 60
    
    def draw(self, screen):

        screen.blit(self.image, (self.x - self.image.get_size()[0] // 2, self.y - self.image.get_size()[1] // 2))