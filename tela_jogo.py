import pygame, sys
from utilitario import get_fonte, get_tabuleiro

#Imagem de fundo aqui
BGTABULEIRO = get_tabuleiro()

#funcão principal para a tela do jogo
def jogar(screen):
    while True:

        screen.blit(BGTABULEIRO, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        pygame.display.update()


