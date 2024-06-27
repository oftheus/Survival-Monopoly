import sys
import pygame
from displaylog import *

class Humano:
    def __init__(self, jogo):
        super().__init__()
        self.jogo = jogo
        return

    def controlar(self, input):
        if input == "Comprar Casa":
            self.display_on_log(''.join([char*30 for char in ' '])  +"Comprar Casa? (Y) ou (N)               ")
            while True:
                self.jogo.lock()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                     elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.end_display()
                            self.jogo.unlock()
                            return True
                        if event.key == pygame.K_n:
                            self.end_display()
                            self.jogo.unlock()
                            return False
        if input == "Espera Click":
            self.display_on_log("Um evento ocorreu! Pressione SPACEBAR para continuar.")
            while True:
                self.jogo.lock()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        self.end_display()
                        pygame.quit()
                        sys.exit()
                     elif event.type == pygame.KEYDOWN:
                        self.end_display()
                        if event.key == pygame.K_SPACE:
                            self.jogo.unlock()
                            return True
    def awaitsInput(self):
        #print('Humano')
        return True
       
    def display_on_log(self, w):
        inst = DisplayLog.instance()
        inst.addToLog(w)
        pygame.display.update()

    def end_display(self,):
        inst = DisplayLog.instance()
        inst.removeFromLog()