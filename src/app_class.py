import math

import pygame

from settings import *
from coin_class import *
from shop_class import *


class App:
    
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(pygame.image.load("assets/icon.ico"))
        pygame.display.set_caption("Coin Clicker")

        self.coin = Coin()
        self.money = 0
        self.state = "START"

        self.shop = Shop()

        self.click_value = 1

        self.running = True
    
    def write_text(self, words, size, pos, color, centered = False):

        font = pygame.font.SysFont(GAME_FONT, size)
        text = font.render(words, False, color)

        if centered:

            pos[0] = pos[0] - text.get_size()[0] // 2
            pos[1] = pos[1] - text.get_size()[1] // 2
        
        self.screen.blit(text, pos)
    
    def start_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.state = "PLAYING"
    
    def start_draw(self):
        self.write_text("Press SPACE BAR to start", 25, [WIDTH // 2, HEIGHT // 2], (255, 189, 8), centered = True)
    
    def playing_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.get_distance((WIDTH // 2, HEIGHT // 2), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])) <= self.coin.image.get_size()[0] // 2:
                    self.money += self.click_value
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    self.state = "SHOP"
    
    def playing_draw(self):

        self.write_text(f"Money: {self.money}", 16, [5, 0], RED)
        self.write_text("Press 'P' to open the SHOP", 16, [5, HEIGHT - 25], CYAN)
        self.write_text(f"Click Value: {self.click_value}", 16, [WIDTH // 2, 5], (255, 255, 255))

        self.screen.blit(self.coin.image, (self.coin.x - self.coin.image.get_size()[0] // 2, self.coin.y - self.coin.image.get_size()[1] // 2))
    
    def shop_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    self.state = "PLAYING"
            
            for upgrade in self.shop.upgrades:

                if upgrade.touching_mouse_pointer():

                    self.write_text(f"Cost: {upgrade.cost}", 16, [WIDTH // 2, HEIGHT // 2 + 120], BLACK, centered = True)

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if self.money >= upgrade.cost:

                            self.money -= upgrade.cost
                            self.click_value += upgrade.product
    
    def shop_draw(self):

        self.write_text(f"Money: {self.money}", 16, [5, 0], RED)
        self.write_text("Press 'P' to close the SHOP", 16, [5, HEIGHT - 25], CYAN)
        self.write_text(f"Click Value: {self.click_value}", 16, [WIDTH // 2, 5], (255, 255, 255))

        self.screen.blit(self.shop.image, (self.shop.x - self.shop.image.get_size()[0] // 2, self.shop.y - self.shop.image.get_size()[1] // 2))

        for i in self.shop.upgrades:
            i.draw(self.screen)
    
    def get_distance(self, pos_1, pos_2):
        return math.sqrt(((pos_2[0] - pos_1[0]) ** 2) + ((pos_2[1] - pos_1[1]) ** 2))
    
    def run(self):

        while self.running:

            self.screen.fill(BLACK)

            if self.state == "START":

                self.start_events()
                self.start_draw()
            
            if self.state == "PLAYING":

                self.playing_events()
                self.playing_draw()
            
            if self.state == "SHOP":

                self.shop_draw()
                self.shop_events()
            
            pygame.display.update()