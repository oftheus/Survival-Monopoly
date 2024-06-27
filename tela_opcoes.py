import pygame
import sys
from utilitario import *

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

BG = get_bg()

# Definir botões
posicao_dos_botoes = [(110, 300), (340, 300), (560, 300), (780, 300), (1005, 300)]
numjog_botao = ['0','1', '2', '3', '4', '5']
botao_selecionado = None #vai indicar a quantidade de jogadores selecionada

fonte = get_fonte(90)

def desenhar_botoes(screen):
    for i, (x, y) in enumerate(posicao_dos_botoes):
        if botao_selecionado == i:
            cor = VERDE
        else:
            cor = CINZA
        pygame.draw.rect(screen, cor, (x, y, 100, 100))
        text = fonte.render(numjog_botao[i], True, PRETO)
        text_rect = text.get_rect(center=(x + 50, y + 60))
        screen.blit(text, text_rect)

def desenhar_botao_jogar(screen):
    pygame.draw.rect(screen, VERMELHO, (400, 550, 400, 100))
    text = fonte.render("Selecionar", True, BRANCO)
    text_rect = text.get_rect(center=(600, 600))
    screen.blit(text, text_rect)

def opcoes(screen):
    dificuldade = 3
    global botao_selecionado
    while True:
        screen.blit(BG, (0,0))
        TEXTO = get_fonte_titulo(90).render("SELECICIONE  NUMERO  MAXIMO  DE  IAs", True, "#FFFFFF")
        TEXTO2 = get_fonte_titulo(32).render("Dificuldade: " + str(dificuldade) + "/5    (digite para mudar)", True, "#FFFFFF")
        
        TEXTO_RECT = TEXTO.get_rect(center=(610, 100))
        TEXTO_RECT2 = TEXTO2.get_rect(center=(610, 480))

        screen.blit(TEXTO, TEXTO_RECT)
        screen.blit(TEXTO2, TEXTO_RECT2)

        # Lidar com eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        dificuldade = 1
                    if event.key == pygame.K_2:
                        dificuldade = 2
                    if event.key == pygame.K_3:
                        dificuldade = 3
                    if event.key == pygame.K_4:
                        dificuldade = 4
                    if event.key == pygame.K_5:
                        dificuldade = 5
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar se algum botão foi clicado
                for i, (x, y) in enumerate(posicao_dos_botoes):
                    if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                        botao_selecionado = i
                    if 500 < event.pos[0] < 700 and 550 < event.pos[1] < 650 and botao_selecionado!=None:  # Verificar se o botão "Jogar" foi clicado
                        return [botao_selecionado, dificuldade]

        # Desenhar botões
        desenhar_botoes(screen)
        desenhar_botao_jogar(screen)

        # Atualizar a tela
        pygame.display.update()