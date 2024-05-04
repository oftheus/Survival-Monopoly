import pygame, sys
from utilitario import *
from dado import *
from peao import *

#Imagem de fundo aqui
BGTABULEIRO = get_tabuleiro()

#funcão principal para a tela do jogo
def jogar(screen, qtd_jogadores):
    peoes = iniciar_peoes(qtd_jogadores)  # inciar peoes dos jogadores
    while True:
        screen.blit(BGTABULEIRO, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Quando clicar com o botão esquerdo do mouse
                    if sprite_dado.rect.collidepoint(event.pos): # verifica se colidiu com o retângulo do dado, limitando praquele determinado espaço
                        sprite_dado.rolar()
                if event.button == 3:  # Se clicar com botão direito -> Fecha o jogo (TEMPORÁRIO) !!
                    pygame.quit()
                    sys.exit()

        # Desenhando peao na tela
        for peao in peoes:
            screen.blit(peao.image, peao.rect)

        # desenhando a sprite do dado
        sprite_dado.draw(screen)
        pygame.display.update()


