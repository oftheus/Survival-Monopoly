import sys
import pygame
from displaylog import *

class Humano:
    def __init__(self, jogo):
        # Inicializa a classe base e armazena a referência ao jogo
        super().__init__()
        self.jogo = jogo
        return

    def controlar(self, input):
        # Função para controlar ações baseadas na entrada do usuário
        if input == "Comprar Casa":
            # Exibe a mensagem no log pedindo confirmação para comprar casa
            self.display_on_log(''.join([char*30 for char in ' '])  +"Colonizar? (Y) ou (N)               ")
            while True:
                # Trava o jogo e aguarda a resposta do usuário
                self.jogo.lock()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.end_display()  # Encerra a exibição da mensagem
                            self.jogo.unlock()  # Destrava o jogo
                            return True
                        if event.key == pygame.K_n:
                            self.end_display()
                            self.jogo.unlock()
                            return False
        if input == "Espera Click":
            # Exibe a mensagem no log esperando um clique
            self.display_on_log("Um evento ocorreu! Pressione SPACEBAR para continuar.")
            while True:
                # Trava o jogo e aguarda a interação do usuário
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
        if input == "Pilhar Base":
            # Exibe a mensagem no log pedindo confirmação para comprar casa
            self.display_on_log(''.join([char*30 for char in ' '])  +"Pilhar Base? (Y) ou (N)               ")
            while True:
                # Trava o jogo e aguarda a resposta do usuário
                self.jogo.lock()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            self.end_display()  # Encerra a exibição da mensagem
                            self.jogo.unlock()  # Destrava o jogo
                            return True
                        if event.key == pygame.K_n:
                            self.end_display()
                            self.jogo.unlock()
                            return False

    def awaitsInput(self):
        # Função que indica que o controlador humano aguarda uma entrada do usuário
        return True
       
    def display_on_log(self, w):
        # Função para exibir uma mensagem no log do jogo
        inst = DisplayLog.instance()
        inst.addToLog(w)
        pygame.display.update()

    def end_display(self):
        # Função para remover a última mensagem do log
        inst = DisplayLog.instance()
        inst.removeFromLog()
