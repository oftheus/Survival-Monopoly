import pygame
import sys
import random
from displaylog import *

class IA:
    def __init__(self, dificuldade, jogo):
        # Inicializa a classe base, define a dificuldade e armazena a referência ao jogo
        super().__init__()
        self.dificuldade = dificuldade
        self.jogo = jogo
        return

    def controlar(self, input):
        # Função para controlar ações baseadas na entrada do jogo
        if input == "Comprar Casa": 
            # A decisão de comprar uma casa é baseada na dificuldade da IA
            # A dificuldade aumenta a probabilidade de comprar casas
            return random.randint(0, 100) + 10 * self.dificuldade > 50
        
        if input == "Espera Click":
            # Exibe a mensagem no log esperando um clique
            self.display_on_log("Um evento ocorreu! Pressione SPACEBAR para continuar.")
            while True:
                # Trava o jogo e aguarda a interação do usuário
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
        # Função que indica que a IA não aguarda uma entrada do usuário
        return False
    
    def display_on_log(self, w):
        # Função para exibir uma mensagem no log do jogo
        inst = DisplayLog.instance()
        inst.addToLog(w)
        pygame.display.update()

    def end_display(self):
        # Função para remover a última mensagem do log
        inst = DisplayLog.instance()
        inst.removeFromLog()