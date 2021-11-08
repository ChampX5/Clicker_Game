import pygame

from settings import *
from shopUpgrade_class import *


class Shop:

    def __init__(self):

        self.image = pygame.image.load("assets/shop.png")
        self.image = pygame.transform.scale(self.image, (425, 300))

        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.upgrades = []

        for i in range(3):

            self.upgrades.append(ShopUpgrade(i))