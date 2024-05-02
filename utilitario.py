import pygame

def get_fonte(size): 
    return pygame.font.Font("assets/fonte.ttf", size)

def get_fonte_titulo(size): 
    return pygame.font.Font("assets/fonte2.ttf", size)

def get_bg():
    return pygame.image.load("assets/Background.jpg")

def get_icone():
    return pygame.image.load("assets/icone.ico")
