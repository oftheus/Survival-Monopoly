import pygame
from tela_menu_principal import menu_principal
from utilitario import *

# iniciando pygame
pygame.init()

# definindo dimensão da tela
SCREEN = pygame.display.set_mode((1200, 800))

# título da janela
pygame.display.set_caption("The Last Of Monopoly")

# define o icone da janela
icone = get_icone()
pygame.display.set_icon(icone)

# Chama a função menu_principal passando a tela do jogo como argumento
menu_principal(SCREEN)
