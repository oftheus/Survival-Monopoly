import pygame
import sys
import random
from displaylog import *

class IA:
    def __init__(self, dificuldade, jogo):
        super().__init__()
        self.dificuldade = dificuldade
        self.jogo = jogo
        return

    def controlar(self, input):
        if input == "Comprar Casa": 
            #dificuldade por emquanto apenas torna IA mais provável a comprar casas
            return random.randint(0,100)+10*self.dificuldade > 50
        if input == "Espera Click":
            self.display_on_log("Um evento ocorreu! Pressione SPACEBAR para continuar.")
            while True:
                self.jogo.lock()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        pygame.quit()
                        self.end_display()
                        sys.exit()
                     elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.end_display()
                            self.jogo.unlock()
                            return True
        return False

       
    def awaitsInput(self):
        #print('IA')
        return False
    
    def display_on_log(self, w):
        inst = DisplayLog.instance()
        inst.addToLog(w)
        pygame.display.update()

    def end_display(self,):
        inst = DisplayLog.instance()
        inst.removeFromLog()