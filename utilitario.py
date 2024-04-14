import pygame

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_bg():
    return pygame.image.load("assets/Background.png")