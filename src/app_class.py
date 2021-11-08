import pygame

from settings import *


class App:
    
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.update((WIDTH, HEIGHT))
        self.running = True
    
    def run(self):

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    
                    self.running = False
            
            pygame.display.update()