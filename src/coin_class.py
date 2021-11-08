import pygame

from settings import *


class Coin:
    
    def __init__(self):
        
        self.image = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale(self.image, (150, 150))

        self.x = WIDTH // 2
        self.y = HEIGHT // 2