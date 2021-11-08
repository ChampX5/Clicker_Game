import math

import pygame

from settings import *
from coin_class import *


class App:
    
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(pygame.image.load("assets/icon.ico"))
        pygame.display.set_caption("Coin Clicker")

        self.coin = Coin()
        self.money = 0
        self.state = "START"

        self.running = True
    
    def start_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.state = "PLAYING"
    
    def start_draw(self):

        self.screen.fill((0, 0, 0))
    
    def playing_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.get_distance((WIDTH // 2, HEIGHT // 2), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) <= self.coin.image.get_size()[0] // 2:

                    self.money += 1
                    print(self.money)
    
    def playing_draw(self):

        self.screen.blit(self.coin.image, (self.coin.x - self.coin.image.get_size()[0] // 2, self.coin.y - self.coin.image.get_size()[1] // 2))
    
    def get_distance(self, pos_1, pos_2):
        return math.sqrt(((pos_2[0] - pos_1[0]) ** 2) + ((pos_2[1] - pos_1[1]) ** 2))
    
    def run(self):

        while self.running:

            if self.state == "START":

                self.start_events()
                self.start_draw()
            
            if self.state == "PLAYING":

                self.playing_events()
                self.playing_draw()
            
            pygame.display.update()