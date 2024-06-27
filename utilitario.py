import pygame


def get_fonte(size):
    return pygame.font.Font("assets/fonte.ttf", size)


"""
    Carrega e retorna a fonte do arquivo 'fonte.ttf' com o tamanho especificado.

    Args:
        size (int): O tamanho da fonte.

    Returns:
        Font: O objeto de fonte carregado.
"""


def get_fonte_titulo(size):
    return pygame.font.Font("assets/fonte2.ttf", size)


# Carrega e retorna a imagem de fundo do arquivo 'Background.jpg'.
def get_bg():
    return pygame.image.load("assets/Background.jpg")

# Carrega imagem do tabuleiro


def get_tabuleiro():
    return pygame.image.load("assets/tabuleiro.png")


# Carrega e retorna o ícone do arquivo 'icone.ico'.
def get_icone():
    return pygame.image.load("assets/icone.ico")

# Carrega e retorna as imagens das faces dos dados


def get_imagem_dados():
    return [pygame.image.load(f"assets/dado{i}.png") for i in range(1, 7)]


def get_cartacapa():
    return pygame.image.load("assets/cartas/carta1.png")


def get_carta_sprite(numero):
    return pygame.image.load(f"assets/cartas/carta{numero}.png")
