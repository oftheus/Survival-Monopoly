import pygame, sys
from tela_jogo import play
from tela_opcoes import options
from tela_menu_principal import main_menu
from utilitario import get_font, get_bg

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

main_menu(SCREEN, play)
