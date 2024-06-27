import sys
import pygame
from jogo import *

class Humano:
    def __init__(self, jogo):
        super().__init__()
        self.jogo = jogo
        return

    def controlar(self, input):
        if input == "Comprar Casa":
            while True:
                self.jogo.lock()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                     elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.jogo.unlock()
                            return True
                        if event.key == pygame.K_n:
                            self.jogo.unlock()
                            return False
        if input == "Espera Click":
            while True:
                self.jogo.lock()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                     elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.jogo.unlock()
                            return True
    def awaitsInput(self):
        #print('Humano')
        return True
       