import pygame, sys
from utilitario import get_fonte

#Função para exibir a tela de opções do jogo.

#implentar algo aqui, talvez colocar regras, mutar volume ...

def opcoes(SCREEN):
    while True:
        SCREEN.fill("white")

        TEXTO = get_fonte(45).render("COLOCAR OPÇÕES AQUI", True, "Black")
        TEXTO_RECT = TEXTO.get_rect(center=(640, 260))
        SCREEN.blit(TEXTO, TEXTO_RECT)

        pygame.display.update()