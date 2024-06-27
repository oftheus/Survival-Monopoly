import pygame
import sys
import random

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
        return False

       
    def awaitsInput(self):
        #print('IA')
        return False