import pygame, sys
from tela_menu_principal import menu_principal
from utilitario import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Last Of Monopoly")

icone = get_icone()
pygame.display.set_icon(icone)


menu_principal(SCREEN)
