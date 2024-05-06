import pygame, sys
from utilitario import *
from dado import *
from jogador import *
from carta import *

#Imagem de fundo aqui
BGTABULEIRO = get_tabuleiro()

#funcão principal para a tela do jogo
def jogar(screen, qtd_jogadores):
    # Inicializa os jogadores e suas posições iniciais
    jogadores, posicoes_iniciais = iniciar_jogadores(qtd_jogadores)

    # Cria os peões com base nos jogadores e suas posições iniciais
    peoes = [Peao(jogador, posicao) for jogador, posicao in zip(jogadores, posicoes_iniciais)]
    
     # Obtém a fonte para renderizar o dinheiro dos jogadores
    font = get_fonte_titulo(24)

    # Criar uma instância da carta
    carta = Carta()

    # GAME LOOP
    while True:
        
        screen.blit(BGTABULEIRO, (0, 0)) # Desenha o fundo do tabuleiro na tela
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: # Quando um botão do mouse é pressionado
                if event.button == 1: # Botão esquerdo do mouse
                    if sprite_dado.rect.collidepoint(event.pos): # Verifica se o botão do dado foi clicado
                        sprite_dado.rolar() # Rola o dado
                    if carta.rect.collidepoint(event.pos): # Verifica se o clique foi na área da carta
                        carta.trocar_carta() # Troca a imagem da carta
                if event.button == 3: # Botão direito do mouse ( TIRAR ISSO DEPOIS )
                    pygame.quit() # Fecha o pygame
                    sys.exit() 

        # desenha os peoes na tela do jogo
        for peao in peoes:
            screen.blit(peao.imagem, peao.rect)

        # desenhar o dinheiro dos jogadores
        for jogador in jogadores:
            jogador.renderizar_suprimento(font, screen)

        # Desenha o dado na tela
        sprite_dado.draw(screen)

        carta.draw(screen)

        # Atualiza a tela do jogo
        pygame.display.update()